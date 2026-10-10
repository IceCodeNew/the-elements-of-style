#!/usr/bin/env python3
"""Ablation harness for the writing skills in this repository.

Each rule in a SKILL.md carries a marker comment such as ``<!-- r:tech.hedge -->``.
A variant of a skill is the SKILL.md text with a set of rule blocks removed.
The harness asks a model to do each test case with a variant loaded, grades the
output against the case's checks, and compares pass rates between variants.

Subcommands:
  screen  Compare a skill set with a control skill set on all cases that apply.
  ablate  For each rule: compare the full skill set with the set minus that rule,
          on the cases that have checks for that rule.
  cases   Report, for each case, the rules for which it detected a difference.
  inspect Print the outputs and grades behind one case or check.
  show    Print a variant's system prompt, for inspection.

``--model`` names the model that writes the outputs: a ``claude`` CLI model name, or
``codex:<model>:<reasoning effort>`` for the Codex CLI. Each call runs in a temporary
session that loads no user settings, plugins, skills, hooks or MCP servers, and that has
no tools to read files or search the web. Outputs and grades are cached under
``evals/.cache`` (ignored by git), so a rerun only calls the model for new variants, cases
or repetitions. Requires Python 3.11 or newer.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import contextlib
import fcntl
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

import tomllib

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
CASES_DIR = ROOT / "evals" / "cases"
GLOBAL_CHECKS = ROOT / "evals" / "global-checks.json"
CACHE_DIR = ROOT / "evals" / ".cache"
RESULTS_DIR = ROOT / "evals" / "results"
# The format of a results file; evals/decide.py reads only this format.
RESULTS_FORMAT = 1
# Settings that may differ between the runs of one tag: they belong to the test model.
PER_MODEL = ("model", "judge", "fallback_judge", "reps")
MARKER = re.compile(r"<!--\s*r:([a-z0-9][a-z0-9._-]*)\s*-->")
HEADING = re.compile(r"^(#+)\s")
LIST_ITEM = re.compile(r"^(\s*)(?:[-*+]|\d+\.)\s")

CHECK_KINDS = ("judge", "absent", "present")

# Codex has no switch that turns off every tool, so each tool that could read files, search
# the web or add context is turned off by name; --strict-config rejects a key that Codex
# does not know. Codex still tells the model about sub-agents, which have the same limits.
# The list is part of the cache key of Codex outputs.
CODEX_ISOLATION = (
    "--strict-config",
    *("--disable", "hooks", "--disable", "plugins", "--disable", "apps"),
    *(
        arg
        for feature in (
            "shell_tool",
            "unified_exec",
            "code_mode_host",
            "multi_agent",
            "goals",
            "image_generation",
            "browser_use",
            "computer_use",
            "in_app_browser",
            "in_app_chat",
            "tool_suggest",
            "skill_search",
            "sleep_tool",
        )
        for arg in ("--disable", feature)
    ),
    *("-c", 'web_search="disabled"'),
    *("-c", "skills.include_instructions=false"),
    *("-c", "skills.bundled.enabled=false"),
)

# An output that the writer refused to produce. It fails every check.
REFUSED_OUTPUT = "\x00refused by the writer\x00"

PERSONA = "You are a careful writer."
GRADER_SYSTEM = (
    "You grade one piece of writing against yes/no checks. "
    "Read the task, the facts it gives, and the output. For each check, answer true "
    "only if the output satisfies the check as written. Judge only what each check asks. "
    "Reply with one JSON object that maps every check id to true or false, and nothing else."
)


# ---------------------------------------------------------------- skills ----


def rule_ids(text: str) -> list[str]:
    return MARKER.findall(text)


def _block_end(lines: list[str], start: int) -> int:
    """Return the index after the block that starts at ``lines[start]``."""
    line = lines[start]
    heading = HEADING.match(line)
    if heading:
        level = len(heading.group(1))
        end = start + 1
        while end < len(lines):
            other = HEADING.match(lines[end])
            if other and len(other.group(1)) <= level:
                break
            end += 1
        return end
    item = LIST_ITEM.match(line)
    if item or line.startswith("|"):
        indent = len(item.group(1)) if item else -1
        end = start + 1
        while end < len(lines):
            nxt = lines[end]
            if line.startswith("|"):
                break
            if not nxt.strip():
                # A blank line ends the item unless indented content follows.
                if (
                    end + 1 < len(lines)
                    and _indent(lines[end + 1]) > indent
                    and lines[end + 1].strip()
                ):
                    end += 1
                    continue
                break
            if _indent(nxt) <= indent:
                break
            end += 1
        return end
    end = start + 1
    while end < len(lines) and lines[end].strip():
        end += 1
    return end


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def remove_rules(text: str, removed: set[str]) -> str:
    """Remove the blocks whose marker id is in ``removed``."""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        ids = set(MARKER.findall(lines[i]))
        if ids & removed:
            i = _block_end(lines, i)
            # Drop one blank line left behind by a removed paragraph or section.
            if out and not out[-1].strip() and i < len(lines) and not lines[i].strip():
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def load_skill(name: str) -> str:
    path = SKILLS_DIR / name / "SKILL.md"
    return path.read_text(encoding="utf-8")


def all_rules(skill_names: list[str]) -> dict[str, str]:
    """Map every rule id to the skill that defines it."""
    owners: dict[str, str] = {}
    for name in skill_names:
        for rid in rule_ids(load_skill(name)):
            if rid in owners:
                raise SystemExit(
                    f"rule id {rid} is defined twice ({owners[rid]}, {name})"
                )
            owners[rid] = name
    return owners


def system_prompt(skill_names: list[str], removed: set[str]) -> str:
    if not skill_names:
        return PERSONA
    parts = [PERSONA, "", "You loaded the skills below. Follow them."]
    for name in skill_names:
        body = remove_rules(load_skill(name), removed)
        parts += ["", f'<skill name="{name}">', body.strip(), "</skill>"]
        # A supporting file that the remaining text names is inlined, as if the model read it.
        skill_dir = SKILLS_DIR / name
        for extra in sorted(skill_dir.rglob("*.md")):
            rel = extra.relative_to(skill_dir).as_posix()
            if rel in ("SKILL.md", "NOTICE.md", "README.md") or rel not in body:
                continue
            parts += [
                "",
                f'<skill-file skill="{name}" path="{rel}">',
                extra.read_text(encoding="utf-8").strip(),
                "</skill-file>",
            ]
    return "\n".join(parts)


# ----------------------------------------------------------------- cases ----


@dataclass(frozen=True)
class Check:
    id: str
    rule: str
    kind: str  # "judge", "absent" (regex must not match), "present" (regex must match)
    text: str  # the judge question, or the regex
    scope: str = "case"  # "global" for the checks in evals/global-checks.json


@dataclass(frozen=True)
class Case:
    id: str
    skills: tuple[str, ...]
    prompt: str
    checks: tuple[Check, ...]
    source: str
    # The ids of the global checks whose patterns the case tempts.
    probe: tuple[str, ...] = ()

    def rules(self) -> set[str]:
        """Rules that the case's own checks test (global checks do not select cases)."""
        return {c.rule for c in self.checks if c.scope == "case"}

    def all_rules(self) -> set[str]:
        return {c.rule for c in self.checks}


def _validate_checks(where: str, checks: tuple[Check, ...]) -> None:
    """Reject a check that would fail only after the model calls, or grade silently wrong."""
    ids = [c.id for c in checks]
    reserved = sorted(i for i in ids if i.startswith("_"))
    if reserved:
        raise SystemExit(f"{where}: check ids must not start with '_': {reserved}")
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        raise SystemExit(f"{where}: duplicate check ids {dupes}")
    for c in checks:
        if c.kind not in CHECK_KINDS:
            raise SystemExit(
                f"{where}/{c.id}: kind must be one of {CHECK_KINDS}, not {c.kind!r}"
            )
        if not c.rule:
            raise SystemExit(f"{where}/{c.id}: the check names no rule")
        if c.kind != "judge":
            try:
                re.compile(c.text)
            except re.error as error:
                raise SystemExit(f"{where}/{c.id}: invalid regex: {error}") from error


def load_cases() -> list[Case]:
    """Load the cases; every case also gets the global checks in evals/global-checks.json."""
    extra = tuple(
        Check(**c, scope="global")
        for c in json.loads(GLOBAL_CHECKS.read_text(encoding="utf-8"))
    )
    global_ids = [c.id for c in extra]
    cases: list[Case] = []
    for path in sorted(CASES_DIR.glob("*.json")):
        for raw in json.loads(path.read_text(encoding="utf-8")):
            checks = tuple(Check(**c) for c in raw["checks"]) + extra
            where = f"{path.name}:{raw['id']}"
            _validate_checks(where, checks)
            probe = raw.get("probe", [])
            if not isinstance(probe, list) or any(p not in global_ids for p in probe):
                raise SystemExit(
                    f"{where}: probe must be a list of global check ids, not {probe!r}"
                )
            cases.append(
                Case(
                    raw["id"],
                    tuple(raw["skills"]),
                    raw["prompt"],
                    checks,
                    raw.get("source", ""),
                    tuple(probe),
                )
            )
    ids = [c.id for c in cases]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"duplicate case ids: {sorted(dupes)}")
    return cases


# ------------------------------------------------------------- model I/O ----


def _key(*parts: str) -> str:
    return hashlib.sha256("\x00".join(parts).encode()).hexdigest()[:24]


def _write_atomic(path: Path, text: str) -> None:
    """Write a file in one step, so an interrupted run never leaves a partial file.

    Each writer gets its own temporary file, so threads that write the same path do not clash.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            out.write(text)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


class ModelRefused(RuntimeError):
    """The model service refused the request; a retry gets the same answer."""


class ModelUnavailable(RuntimeError):
    """The model name or the setup is wrong; a retry gets the same answer."""


REFUSED = ("safeguards flagged",)
UNAVAILABLE = ("issue with the selected model", "unrecognized_model")


def _claude_once(model: str, system: str, prompt: str, timeout: int) -> tuple[str, str]:
    cmd = [
        "claude",
        "-p",
        "--model",
        model,
        "--system-prompt",
        system,
        "--tools",
        "",
        "--setting-sources",
        "",
        "--strict-mcp-config",
        "--no-session-persistence",
        prompt,
    ]
    done = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=CACHE_DIR,
        check=False,
        stdin=subprocess.DEVNULL,
    )
    if done.returncode == 0 and done.stdout.strip():
        return done.stdout, ""
    return "", f"exit {done.returncode}: {_failure(done)}"


def _codex_parts(model: str) -> tuple[str, str]:
    """The model slug and the reasoning effort of a codex:<model>:<reasoning effort> name."""
    parts = model.split(":")
    if len(parts) != 3 or not all(parts):
        raise ValueError(
            f"use codex:<model>:<reasoning effort> for a Codex model, not {model!r}"
        )
    return parts[1], parts[2]


def _codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))


def _codex_once(model: str, system: str, prompt: str, timeout: int) -> tuple[str, str]:
    """Run one isolated Codex session (see CODEX_ISOLATION).

    ``model`` is ``codex:<slug>:<reasoning effort>``. The system prompt goes in as developer
    instructions. The session runs in a temporary directory outside the repository, with an
    empty HOME. CODEX_HOME stays the real one, so the existing login is used and never copied.
    """
    slug, effort = _codex_parts(model)
    for name in ("AGENTS.md", "AGENTS.override.md"):
        if (_codex_home() / name).exists():
            raise ModelUnavailable(
                f"Codex adds {_codex_home() / name} to every prompt; move it away while the tests run"
            )
    instructions = json.dumps(system, ensure_ascii=False)
    tomllib.loads(
        "developer_instructions = " + instructions
    )  # fail loudly if Codex would not parse it
    with tempfile.TemporaryDirectory(prefix="evals-codex-") as tmp:
        home, work, out = Path(tmp, "home"), Path(tmp, "work"), Path(tmp, "last.md")
        home.mkdir()
        work.mkdir()
        cmd = [
            "codex",
            "exec",
            "--ignore-user-config",
            "--ephemeral",
            "--skip-git-repo-check",
            *("-s", "read-only", "--color", "never", "-m", slug),
            *CODEX_ISOLATION,
            *("-c", f'model_reasoning_effort="{effort}"'),
            *("-c", "developer_instructions=" + instructions),
            *("-o", str(out), prompt),
        ]
        done = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=work,
            check=False,
            stdin=subprocess.DEVNULL,
            env=dict(os.environ, HOME=str(home), CODEX_HOME=str(_codex_home())),
        )
        text = out.read_text(encoding="utf-8") if out.exists() else ""
    if done.returncode == 0 and text.strip():
        return text, ""
    return "", f"exit {done.returncode}: {_failure(done)}"


def call_model(
    model: str, system: str, prompt: str, timeout: int = 900, attempts: int = 6
) -> str:
    """Call a model; retry with backoff when a call fails for a reason that can pass.

    ``model`` is a Claude model name for the claude CLI, or ``codex:<slug>:<effort>`` for Codex.
    A refusal or an unknown model fails at once, because a retry gets the same answer.
    """
    once = _codex_once if model.startswith("codex:") else _claude_once
    CACHE_DIR.mkdir(
        parents=True, exist_ok=True
    )  # the claude CLI runs with the cache as its working directory
    error = ""
    for attempt in range(attempts):
        try:
            text, error = once(model, system, prompt, timeout)
        except subprocess.TimeoutExpired:
            text, error = "", f"timed out after {timeout} s"
        if text:
            return text
        # Match on the full error text; only the message is shortened.
        if any(marker in error for marker in REFUSED):
            raise ModelRefused(f"{model} refused the request ({_short(error)})")
        if any(marker in error for marker in UNAVAILABLE):
            raise ModelUnavailable(f"{model} cannot run ({_short(error)})")
        if attempt + 1 < attempts:
            time.sleep(min(30 * 2**attempt, 900))
    raise RuntimeError(f"{model} failed after {attempts} attempts ({_short(error)})")


def _failure(done: subprocess.CompletedProcess) -> str:
    """The error text of a failed call; a CLI can print its error on either stream."""
    return "\n".join(t for t in (done.stderr.strip(), done.stdout.strip()) if t)


def _short(error: str, size: int = 300) -> str:
    return error if len(error) <= 2 * size else f"{error[:size]} [...] {error[-size:]}"


def output_path(model: str, system: str, case: Case, rep: int) -> Path:
    """Cache file of one output. A Codex output also depends on the isolation settings."""
    model_key = (
        " ".join((model, *CODEX_ISOLATION)) if model.startswith("codex:") else model
    )
    return CACHE_DIR / "gen" / f"{_key(model_key, system, case.prompt, str(rep))}.md"


def generate(model: str, system: str, case: Case, rep: int) -> str:
    """Return the cached or new output. A refusal is cached as REFUSED_OUTPUT."""
    path = output_path(model, system, case, rep)
    if path.exists():
        return path.read_text(encoding="utf-8")
    try:
        text = call_model(model, system, case.prompt)
    except ModelRefused as error:
        print(f"case {case.id} rep {rep}: {error}", file=sys.stderr)
        text = REFUSED_OUTPUT
    _write_atomic(path, text)
    return text


def _first_json_object(reply: str) -> dict | None:
    """Decode the first JSON object in the reply, ignoring any text around it."""
    start = reply.find("{")
    while start != -1:
        try:
            value, _end = json.JSONDecoder().raw_decode(reply, start)
        except json.JSONDecodeError:
            start = reply.find("{", start + 1)
            continue
        return value if isinstance(value, dict) else None
    return None


def _grade_prompt(case: Case, output: str, checks: list[Check]) -> str:
    questions = "\n".join(f"- {c.id}: {c.text}" for c in checks)
    return f"<task>\n{case.prompt}\n</task>\n\n<output>\n{output}\n</output>\n\n<checks>\n{questions}\n</checks>"


@dataclass(frozen=True)
class Graded:
    passed: dict[str, bool]
    judge: str  # the model that answered, "refused" (every judge refused) or "writer-refused"


def grade(judge: str, case: Case, output: str, fallback: str | None = None) -> Graded:
    """Grade one output.

    If the judge refuses the request, the fallback judge grades it. If every judge refuses,
    or the writer refused to write, every judge check fails. The cache key is that of the
    judge, and the cached verdict records who answered, so a rerun calls no model.
    """
    if output == REFUSED_OUTPUT:
        return Graded({c.id: False for c in case.checks}, "writer-refused")
    result: dict[str, bool] = {}
    judged = [c for c in case.checks if c.kind == "judge"]
    for c in case.checks:
        if c.kind == "absent":
            result[c.id] = re.search(c.text, output, re.MULTILINE) is None
        elif c.kind == "present":
            result[c.id] = re.search(c.text, output, re.MULTILINE) is not None
    if not judged:
        return Graded(result, judge)
    prompt = _grade_prompt(case, output, judged)
    path = CACHE_DIR / "grade" / f"{_key(judge, GRADER_SYSTEM, prompt)}.json"
    if path.exists():
        verdict = json.loads(path.read_text(encoding="utf-8"))
    else:
        verdict = {"_judge": "refused", **{c.id: False for c in judged}}
        for answering in dict.fromkeys(m for m in (judge, fallback) if m):
            try:
                verdict = {
                    "_judge": answering,
                    **_ask_judge(answering, case, output, judged),
                }
                break
            except ModelRefused as error:
                print(f"case {case.id}: {error}", file=sys.stderr)
        _write_atomic(path, json.dumps(verdict, ensure_ascii=False, indent=1))
    for c in judged:
        result[c.id] = verdict[c.id]
    return Graded(result, verdict.get("_judge", judge))


def _ask_judge(
    model: str, case: Case, output: str, judged: list[Check]
) -> dict[str, bool]:
    """Ask one judge. A reply can leave out some check ids or answer with something other
    than true or false; the next attempt asks only for those checks."""
    verdict: dict[str, bool] = {}
    missing = judged
    for _attempt in range(3):
        reply = call_model(model, GRADER_SYSTEM, _grade_prompt(case, output, missing))
        answered = _first_json_object(reply) or {}
        verdict.update(
            {
                c.id: answered[c.id]
                for c in missing
                if isinstance(answered.get(c.id), bool)
            }
        )
        missing = [c for c in missing if c.id not in verdict]
        if not missing:
            return verdict
    ids = ", ".join(c.id for c in missing)
    raise RuntimeError(
        f"case {case.id}: the grader gave no true or false verdict for {ids} in 3 attempts"
    )


# -------------------------------------------------------------- ablation ----


@dataclass(frozen=True)
class Variant:
    name: str
    skills: tuple[str, ...]
    removed: frozenset[str]


@dataclass(frozen=True)
class Judges:
    judge: str
    fallback: str | None


def fill_cache(
    variants: tuple[Variant, ...],
    cases: list[Case],
    reps: int,
    model: str,
    workers: int,
) -> None:
    """Generate the outputs of every variant into the cache, without grading them."""
    jobs = [
        (system_prompt(list(v.skills), set(v.removed)), case, rep)
        for v in variants
        for case in cases
        for rep in range(reps)
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(lambda job: generate(model, *job), jobs))


def run_variant(
    variant: Variant,
    cases: list[Case],
    reps: int,
    model: str,
    judges: Judges,
    workers: int,
) -> tuple[dict, list[dict]]:
    """Return ({case_id: {check_id: pass_rate}}, notes).

    The notes list each output that the judge did not grade itself: the fallback graded it,
    every judge refused it, or the writer refused to write it.
    """
    system = system_prompt(list(variant.skills), set(variant.removed))
    jobs = [(case, rep) for case in cases for rep in range(reps)]

    def one(job: tuple[Case, int]) -> tuple[str, int, Graded]:
        case, rep = job
        output = generate(model, system, case, rep)
        return case.id, rep, grade(judges.judge, case, output, judges.fallback)

    grades: dict[str, list[dict[str, bool]]] = {c.id: [] for c in cases}
    notes: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for case_id, rep, graded in pool.map(one, jobs):
            grades[case_id].append(graded.passed)
            if graded.judge != judges.judge:
                notes.append(
                    {
                        "variant": variant.name,
                        "case": case_id,
                        "rep": rep,
                        "judge": graded.judge,
                    }
                )
    rates = {}
    for case in cases:
        rows = grades[case.id]
        rates[case.id] = {
            c.id: sum(r[c.id] for r in rows) / len(rows) for c in case.checks
        }
    return rates, notes


def rule_score(rates: dict, cases: list[Case], rule: str) -> float:
    values = [
        rates[case.id][c.id]
        for case in cases
        if case.id in rates
        for c in case.checks
        if c.rule == rule
    ]
    if not values:
        raise ValueError(f"no checks for rule {rule}")
    return sum(values) / len(values)


def other_score(rates: dict, cases: list[Case], rule: str) -> float | None:
    values = [
        rates[case.id][c.id]
        for case in cases
        if case.id in rates
        for c in case.checks
        if c.rule != rule
    ]
    return sum(values) / len(values) if values else None


def _removed(args: argparse.Namespace, owners: dict[str, str]) -> frozenset[str]:
    """The rule ids of --without; a typo would silently leave a rule in the skill."""
    removed = frozenset(args.without.split(",")) if args.without else frozenset()
    unknown = sorted(removed - set(owners))
    if unknown:
        raise SystemExit(f"--without names unknown rule ids: {unknown}")
    return removed


def _selected(args: argparse.Namespace, cases: list[Case]) -> list[Case]:
    """The cases of --cases; a typo, or a case that this run skips, would silently test nothing."""
    if not args.cases:
        return cases
    wanted = args.cases.split(",")
    missing = sorted(set(wanted) - {c.id for c in cases})
    if missing:
        raise SystemExit(
            f"--cases names cases that are unknown or not run with these skills: {missing}"
        )
    return [c for c in cases if c.id in wanted]


def _inputs(skill_sets: list[list[str]], cases: list[Case]) -> str:
    """Fingerprint of the texts that the models read: the system prompts and the cases."""
    prompts = [system_prompt(skills, set()) for skills in skill_sets]
    texts = [repr((c.id, c.skills, c.prompt, c.checks, c.probe)) for c in cases]
    return _key(*prompts, *texts)[:12]


def _tag_name(value: str) -> str:
    """The --tag type: a run name that is safe in a file name and in a glob."""
    if not re.fullmatch(r"[A-Za-z0-9._-]+", value):
        raise argparse.ArgumentTypeError(
            f"use only letters, digits, '.', '_' and '-', not {value!r}"
        )
    return value


def _model_name(value: str) -> str:
    """The --model type: a claude CLI model name, or codex:<model>:<reasoning effort>."""
    if value.startswith("codex:"):
        try:
            _codex_parts(value)
        except ValueError as error:
            raise argparse.ArgumentTypeError(str(error)) from None
    return value


def _lock_path(path: Path) -> Path:
    return CACHE_DIR / "locks" / f"{path.name}.lock"


def _running(path: Path) -> bool:
    """Whether a run holds the lock of a results file now.

    The probe takes a shared lock, so two probes never block each other; a run that starts
    during a probe retries its own lock (see _hold_lock).
    """
    lock_path = _lock_path(path)
    if not lock_path.exists():
        return False
    with open(lock_path) as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_SH | fcntl.LOCK_NB)
        except BlockingIOError:
            return True
    return False


@contextlib.contextmanager
def _hold_lock(path: Path) -> Iterator[None]:
    """Hold the lock of a results file until the block ends.

    A probe (_running) holds the lock shared for a moment, so try for about 100 ms before
    deciding that another run holds it.
    """
    lock_path = _lock_path(path)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with open(lock_path, "w") as lock:
        for _ in range(10):
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                time.sleep(0.01)
        else:
            raise SystemExit(
                f"another run writes {path.relative_to(ROOT)}; wait for it, or name this run with another --tag"
            )
        yield


@contextlib.contextmanager
def _results_file(kind: str, tag: str, settings: dict) -> Iterator[tuple[Path, dict]]:
    """Hold the results file of this run, and give its previous content.

    A lock keeps every other run out of the file until this run ends. A new file exists from
    the start and stays pending until the run saves its first result, so a run that stops
    or still runs shows up. A run never adds to a file of other settings or texts, and the
    runs of one tag on different test models share every setting apart from PER_MODEL.
    """
    model = re.sub(r"[^A-Za-z0-9._-]+", "-", settings["model"])
    out = RESULTS_DIR / f"{kind}-{tag}@{model}.json"
    # On a case-insensitive file system, another spelling of the tag or the model names an
    # existing file that the glob of the tag misses, and the run would overwrite it.
    if out.exists() and out.name not in os.listdir(RESULTS_DIR):
        raise SystemExit(
            f"{out.relative_to(ROOT)} exists under another spelling of its tag or model;"
            " use the spelling of the existing file"
        )
    with _hold_lock(out):
        previous = _previous(kind, tag, out, settings)
        if not previous:
            _save(out, settings, pending=True)
        yield out, previous


def _without(settings: dict, free: tuple[str, ...]) -> dict:
    return {k: v for k, v in settings.items() if k not in free}


def _previous(kind: str, tag: str, out: Path, settings: dict) -> dict:
    """The earlier results of this run's file; refuse the files of the tag that differ.

    A rerun on the same model may change only the repetitions, and the runs on other models
    only the settings in PER_MODEL. A pending file binds nothing once its run has ended, so
    a corrected rerun replaces it; its lock shows whether that run still goes.
    """
    previous: dict = {}
    for path in sorted(RESULTS_DIR.glob(f"{kind}-{tag}@*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("format") != RESULTS_FORMAT:
            raise SystemExit(
                f"{path.relative_to(ROOT)} was written by another version of run.py;"
                " name this run with another --tag"
            )
        own = path == out
        if data.get("pending") and (own or not _running(path)):
            continue
        free = ("reps",) if own else PER_MODEL
        if _without(data["settings"], free) != _without(settings, free):
            raise SystemExit(
                f"{path.relative_to(ROOT)} ran --tag {tag} with other settings or other"
                " skill or case texts; name this run with another --tag"
            )
        if own:
            previous = data
    return previous


def _save(out: Path, settings: dict, **sections: object) -> None:
    report = {"format": RESULTS_FORMAT, "settings": settings, **sections}
    _write_atomic(out, json.dumps(report, ensure_ascii=False, indent=1) + "\n")


def _merge_notes(old: list[dict], new: list[dict]) -> list[dict]:
    """Merge grading notes; one note per variant, case and repetition."""
    merged = {(n["variant"], n["case"], n["rep"]): n for n in old + new}
    return list(merged.values())


def cmd_ablate(args: argparse.Namespace) -> None:
    skills = args.skills.split(",")
    owners = all_rules(skills)
    targets = args.rules.split(",") if args.rules else sorted(owners)
    unknown = [r for r in targets if r not in owners]
    if unknown:
        raise SystemExit(f"unknown rule ids: {unknown}")
    base_removed = _removed(args, owners)
    overlap = sorted(set(targets) & base_removed)
    if overlap:
        raise SystemExit(
            f"--rules and --without both name {overlap}; both variants would lack those rules"
        )
    cases = _selected(
        args,
        [c for c in load_cases() if set(c.skills) <= set(skills) or args.any_skills],
    )
    full = Variant("full", tuple(skills), base_removed)
    control = Variant("control", (), frozenset())
    judges = Judges(args.judge, args.fallback_judge)
    settings = {
        "skills": skills,
        "inputs": _inputs([skills], cases),
        "without": sorted(base_removed),
        "cases": sorted(args.cases.split(",")) if args.cases else "all",
        "any_skills": args.any_skills,
        "model": args.model,
        "judge": args.judge,
        "fallback_judge": args.fallback_judge,
        "reps": args.reps,
    }
    with _results_file("ablate", args.tag, settings) as (out, previous):
        rules: dict = previous.get("rules", {})
        notes: list[dict] = previous.get("judge_fallbacks", [])
        global_rule = {
            ch.id: ch.rule for c in cases for ch in c.checks if ch.scope == "global"
        }
        for rule in targets:
            relevant = [
                c
                for c in cases
                if rule in c.rules() or rule in {global_rule[g] for g in c.probe}
            ]
            if not relevant:
                rules[rule] = {
                    "status": "no-cases",
                    "skill": owners[rule],
                    "reps": args.reps,
                }
                print(f"{rule:28s} no cases")
            else:
                r_full, n_full = run_variant(
                    full, relevant, args.reps, args.model, judges, args.workers
                )
                r_abl, n_abl = run_variant(
                    Variant(f"-{rule}", tuple(skills), base_removed | {rule}),
                    relevant,
                    args.reps,
                    args.model,
                    judges,
                    args.workers,
                )
                r_ctl, n_ctl = run_variant(
                    control, relevant, args.reps, args.model, judges, args.workers
                )
                notes = _merge_notes(notes, n_full + n_abl + n_ctl)
                s_full, s_abl, s_ctl = (
                    rule_score(r, relevant, rule) for r in (r_full, r_abl, r_ctl)
                )
                o_full, o_abl = (
                    other_score(r_full, relevant, rule),
                    other_score(r_abl, relevant, rule),
                )
                effect = s_full - s_abl
                side = None if o_full is None or o_abl is None else o_full - o_abl
                rules[rule] = {
                    "skill": owners[rule],
                    "full": s_full,
                    "ablated": s_abl,
                    "control": s_ctl,
                    "effect": effect,
                    "side_effect": side,
                    "reps": args.reps,
                    "cases": {
                        c.id: {
                            "full": rule_score(r_full, [c], rule),
                            "ablated": rule_score(r_abl, [c], rule),
                            "control": rule_score(r_ctl, [c], rule),
                        }
                        for c in relevant
                    },
                    "checks": {
                        f"{c.id}/{ch.id}": {
                            "rule": ch.rule,
                            "full": r_full[c.id][ch.id],
                            "ablated": r_abl[c.id][ch.id],
                        }
                        for c in relevant
                        for ch in c.checks
                    },
                }
                side_txt = "" if side is None else f" other={side:+.2f}"
                print(
                    f"{rule:28s} full={s_full:.2f} ablated={s_abl:.2f} control={s_ctl:.2f} effect={effect:+.2f}{side_txt}"
                )
            # Save after each rule, so an interrupted run keeps the finished rules.
            _save(out, settings, rules=rules, judge_fallbacks=notes)
        print(f"wrote {out.relative_to(ROOT)}")


def cmd_screen(args: argparse.Namespace) -> None:
    """Run all cases with the full skill set and with the control set; report each rule's gain.

    If the full set does not beat the control on a rule's checks, removing that one rule
    cannot lower the score below the control either, so the rule shows no effect. A rule of
    a control skill is in both sets, so this screen does not measure it.
    """
    skills = args.skills.split(",")
    control_skills = args.control_skills.split(",") if args.control_skills else []
    owners = all_rules(skills)
    removed = _removed(args, owners)
    judges = Judges(args.judge, args.fallback_judge)
    cases = _selected(
        args,
        [
            c
            for c in load_cases()
            if set(c.skills) <= set(skills)
            and (args.all_cases or set(c.skills) - set(control_skills))
        ],
    )
    variants = (
        Variant("full", tuple(skills), removed),
        Variant("control", tuple(control_skills), removed),
    )
    if args.gen_only:
        fill_cache(variants, cases, args.reps, args.model, args.workers)
        print(f"generated {len(cases)} cases x {args.reps} reps x 2 variants")
        return
    settings = {
        "skills": skills,
        "control_skills": control_skills,
        "inputs": _inputs([skills, control_skills], cases),
        "without": sorted(removed),
        "cases": sorted(args.cases.split(",")) if args.cases else "all",
        "all_cases": args.all_cases,
        "model": args.model,
        "judge": args.judge,
        "fallback_judge": args.fallback_judge,
        "reps": args.reps,
    }
    with _results_file("screen", args.tag, settings) as (out, _):
        (full, n_full), (ctl, n_ctl) = (
            run_variant(v, cases, args.reps, args.model, judges, args.workers)
            for v in variants
        )
        report: dict = {"judge_fallbacks": n_full + n_ctl, "rules": {}, "checks": {}}
        for rule in sorted(owners):
            if rule in removed or owners[rule] in control_skills:
                continue
            relevant = [c for c in cases if rule in c.all_rules()]
            if not relevant:
                report["rules"][rule] = {"status": "no-cases", "skill": owners[rule]}
                print(f"{rule:34s} no cases")
                continue
            s_full, s_ctl = (
                rule_score(full, relevant, rule),
                rule_score(ctl, relevant, rule),
            )
            report["rules"][rule] = {
                "skill": owners[rule],
                "full": s_full,
                "control": s_ctl,
                "gain": s_full - s_ctl,
            }
            print(
                f"{rule:34s} full={s_full:.2f} control={s_ctl:.2f} gain={s_full - s_ctl:+.2f}"
            )
        for case in cases:
            for c in case.checks:
                report["checks"][f"{case.id}/{c.id}"] = {
                    "rule": c.rule,
                    "kind": c.kind,
                    "full": full[case.id][c.id],
                    "control": ctl[case.id][c.id],
                }
        deltas = [row["full"] - row["control"] for row in report["checks"].values()]
        print(f"all {len(deltas)} checks: summed change {sum(deltas):+.2f}")
        _save(out, settings, **report)
        print(f"wrote {out.relative_to(ROOT)}")


def check_deltas(globs: list[str]) -> dict[str, float]:
    """Largest pass-rate difference that each check showed in the matching results files.

    A glob matches result names without the screen- or ablate- prefix, as in decide.py.
    """
    best: dict[str, float] = {}

    def note(key: str, delta: float) -> None:
        best[key] = max(best.get(key, 0.0), abs(delta))

    paths: set[Path] = set()
    for g in globs:
        found = {
            p
            for kind in ("screen", "ablate")
            for p in RESULTS_DIR.glob(f"{kind}-{g}.json")
        }
        if not found:
            raise SystemExit(
                f"no results in {RESULTS_DIR.relative_to(ROOT)} match {g}: run the comparisons first"
            )
        paths |= found
    for path in sorted(paths):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("format") != RESULTS_FORMAT:
            raise SystemExit(
                f"{path.relative_to(ROOT)} was written by another version of run.py; rerun it"
            )
        if data.get("pending"):
            raise SystemExit(
                f"{path.relative_to(ROOT)} holds no result yet: wait for the run, rerun it if it"
                " stopped, or delete the file if that run will not be repeated"
            )
        for key, row in data.get("checks", {}).items():
            note(key, row["full"] - row["control"])
        for info in data.get("rules", {}).values():
            for key, row in info.get("checks", {}).items():
                note(key, row["full"] - row["ablated"])
    return best


def cmd_cases(args: argparse.Namespace) -> None:
    """List each check with its largest observed difference; mark checks and cases to delete.

    A case check is kept if the rule it tests is in a skill and the check showed a pass-rate
    difference of at least --threshold in a matching screen or ablation. A probe case is
    also kept by a probed global check that showed such a difference; a global check itself
    is never marked for deletion. A case with no kept check is deleted.
    """
    # A shared rule (both.*) appears in both genre skills, so collect ids per skill.
    owners = {
        rid
        for path in SKILLS_DIR.glob("*/SKILL.md")
        for rid in rule_ids(path.read_text(encoding="utf-8"))
    }
    best = check_deltas(args.results)
    for case in load_cases():
        kept = untested = 0
        for c in case.checks:
            if c.scope == "global" and c.id not in case.probe:
                continue
            key = f"{case.id}/{c.id}"
            delta = best.get(key)
            if c.scope == "case" and c.rule not in owners:
                status = "DELETE (rule removed)"
            elif delta is None:
                status = "UNTESTED (no result)"
                untested += 1
            elif delta + 1e-9 >= args.threshold:
                status = f"keep (max difference {delta:.2f})"
                kept += 1
            elif c.scope == "global":
                status = f"probe saw no difference (max {delta:.2f})"
            else:
                status = f"DELETE (max difference {delta:.2f})"
            print(f"{key:60s} {c.rule:32s} {status}")
        if kept:
            continue
        if untested:
            print(
                f"{case.id:60s} {'':32s} UNTESTED CASE ({untested} checks have no result)"
            )
        else:
            print(f"{case.id:60s} {'':32s} DELETE CASE (no kept check)")


def cmd_inspect(args: argparse.Namespace) -> None:
    """Print the cached outputs of one case for one variant, with each check's result."""
    skills = args.skills.split(",") if args.skills else []
    removed = set(_removed(args, all_rules(skills)))
    system = system_prompt(skills, removed)
    case = next((c for c in load_cases() if c.id == args.case), None)
    if case is None:
        raise SystemExit(f"unknown case {args.case}")
    for rep in range(args.reps):
        path = output_path(args.model, system, case, rep)
        if not path.exists():
            print(f"--- rep {rep}: not cached")
            continue
        output = path.read_text(encoding="utf-8")
        verdict = grade(args.judge, case, output, args.fallback_judge).passed
        shown = [c for c in case.checks if not args.check or c.id == args.check]
        marks = " ".join(f"{c.id}={'PASS' if verdict[c.id] else 'FAIL'}" for c in shown)
        print(f"--- rep {rep}: {marks}\n{output.strip()}\n")


def cmd_show(args: argparse.Namespace) -> None:
    skills = args.skills.split(",")
    print(system_prompt(skills, set(_removed(args, all_rules(skills)))))


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("ablate")
    p.add_argument(
        "--skills", required=True, help="comma-separated skill names loaded together"
    )
    p.add_argument(
        "--rules", help="comma-separated rule ids (default: every rule in the skills)"
    )
    p.add_argument(
        "--without",
        help="rule ids removed from every variant, such as rules already dropped",
    )
    p.add_argument("--reps", type=int, default=5)
    p.add_argument(
        "--model",
        type=_model_name,
        required=True,
        help="model that writes the outputs: a claude CLI model name, or codex:<model>:<reasoning effort>",
    )
    p.add_argument(
        "--judge", default="sonnet", help="claude CLI model that grades judge checks"
    )
    p.add_argument(
        "--fallback-judge",
        default="opus",
        help="claude CLI model that grades an output that the judge refuses (default: opus)",
    )
    p.add_argument(
        "--workers", type=int, default=int(os.environ.get("EVAL_WORKERS", "6"))
    )
    p.add_argument(
        "--any-skills",
        action="store_true",
        help="also use cases written for other skill sets",
    )
    p.add_argument(
        "--tag",
        type=_tag_name,
        required=True,
        help="name of the run: one step of one update, or one add-back rule, such as 2026-10-s2-tech; the results file is <tag>@<model>",
    )
    p.add_argument("--cases", help="comma-separated case ids (default: all that apply)")
    p.set_defaults(func=cmd_ablate)
    p = sub.add_parser("screen")
    p.add_argument(
        "--skills", required=True, help="comma-separated skill names loaded together"
    )
    p.add_argument(
        "--control-skills",
        default="",
        help="skills loaded in the control (default: none)",
    )
    p.add_argument("--without", help="rule ids removed from both variants")
    name = p.add_mutually_exclusive_group(required=True)
    name.add_argument(
        "--tag",
        type=_tag_name,
        help="name of the run: one step of one update, such as 2026-10-s1-tech; the results file is <tag>@<model>",
    )
    name.add_argument(
        "--gen-only",
        action="store_true",
        help="only generate the outputs into the cache, to grade them in a later run",
    )
    p.add_argument("--reps", type=int, default=5)
    p.add_argument(
        "--model",
        type=_model_name,
        required=True,
        help="model that writes the outputs: a claude CLI model name, or codex:<model>:<reasoning effort>",
    )
    p.add_argument(
        "--judge", default="sonnet", help="claude CLI model that grades judge checks"
    )
    p.add_argument(
        "--fallback-judge",
        default="opus",
        help="claude CLI model that grades an output that the judge refuses (default: opus)",
    )
    p.add_argument(
        "--workers", type=int, default=int(os.environ.get("EVAL_WORKERS", "6"))
    )
    p.add_argument("--cases", help="comma-separated case ids (default: all that apply)")
    p.add_argument(
        "--all-cases",
        action="store_true",
        help="also run cases that load only the control skills",
    )
    p.set_defaults(func=cmd_screen)
    p = sub.add_parser("cases")
    p.add_argument("--threshold", type=float, default=0.4)
    p.add_argument(
        "--results",
        nargs="+",
        required=True,
        help="globs of the runs of this update, as for decide.py, such as '2026-10-*'",
    )
    p.set_defaults(func=cmd_cases)
    p = sub.add_parser("inspect")
    p.add_argument(
        "--skills",
        default="",
        help="comma-separated skill names (empty for the control)",
    )
    p.add_argument("--without")
    p.add_argument("--case", required=True)
    p.add_argument("--check", help="show only this check's result")
    p.add_argument("--reps", type=int, default=5)
    p.add_argument(
        "--model",
        type=_model_name,
        required=True,
        help="model that writes the outputs: a claude CLI model name, or codex:<model>:<reasoning effort>",
    )
    p.add_argument(
        "--judge", default="sonnet", help="claude CLI model that grades judge checks"
    )
    p.add_argument(
        "--fallback-judge",
        default="opus",
        help="claude CLI model that grades an output that the judge refuses (default: opus)",
    )
    p.set_defaults(func=cmd_inspect)
    p = sub.add_parser("show")
    p.add_argument("--skills", required=True)
    p.add_argument("--without")
    p.set_defaults(func=cmd_show)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
