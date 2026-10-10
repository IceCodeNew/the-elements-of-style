#!/usr/bin/env python3
"""Apply the keep/drop criterion of evals/README.md to results from one or more test models.

Run from the repository root:

    python3 evals/decide.py screen-pass evals/results '<tag-glob>'...
    python3 evals/decide.py ablate-keep evals/results '<tag-glob>'...

screen-pass prints the rules that show an effect in at least one listed screen result (PASS),
the rules that the screens measured without an effect (FAIL), and the rules that no listed
screen tested (NO CASES).
ablate-keep reads leave-one-out or add-back results and keeps a rule that shows an effect
for at least one model and whose summed change over all checks in its cases, across all
listed results, is positive. REVIEW lists other checks that dropped by 0.4 or more.
A results file is named <tag>@<model>, and a glob matches these names, such as
'2026-10-s2-tech@*' for one step on every model. Give one tag per skill set: its files must
share the settings and texts, and may differ only in the test model, the judges and the
repetitions; otherwise both commands stop. Each genre skill decides its own copy of the
shared rules, so decide the rules of each genre skill on their own.
Both commands first list the files they read (READ): check that every test model is there.
They stop when a file holds no result yet, or when the files of one skill set hold
different rules, as when a model stopped or still runs. They also list the decisions whose
cases hold an output that the writer or every judge refused (REVIEW refused); read those
outputs first.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import NamedTuple

EPS = 1e-9
RESULTS_FORMAT = 1  # the format of the results files that evals/run.py writes
# Settings that may differ between the files of one skill set: they belong to the test model.
PER_MODEL = ("model", "judge", "fallback_judge", "reps")


def shows_effect(deltas: list[float]) -> bool:
    """Apply the "shows an effect" definition of evals/README.md to one rule's own checks."""
    if not deltas:
        return False
    mean = sum(deltas) / len(deltas)
    return mean >= 0.2 - EPS or (max(deltas) >= 0.4 - EPS and min(deltas) > -0.4 + EPS)


def _step(settings: dict) -> dict:
    return {k: v for k, v in settings.items() if k not in PER_MODEL}


def result_files(rdir: Path, kind: str, globs: list[str]) -> list[tuple[Path, dict]]:
    """Read the matching results files; refuse evidence that must not be added up.

    The files form a grid: one row per skill set, one file per test model. The files of a
    row must share every setting and text apart from PER_MODEL, because two steps of the
    method or two updates of a skill would count a rule twice or mix texts. They must hold
    results, and the same rules, because a model that stopped or still runs would leave the
    decision to the others. Every row must cover the same models. Rows of different skill
    sets, such as the screens of a language skill with each genre skill, are separate
    evidence, as long as each rule belongs to one skill: each genre skill has its own copy
    of the shared rules.
    """
    paths: set[Path] = set()
    for g in globs:
        found = set(rdir.glob(f"{kind}-{g}.json"))
        if not found:
            raise SystemExit(f"no {kind} results in {rdir} match {g}")
        paths |= found
    files = [(p, json.loads(p.read_text(encoding="utf-8"))) for p in sorted(paths)]
    other = [p.name for p, data in files if data.get("format") != RESULTS_FORMAT]
    if other:
        raise SystemExit(
            f"another version of run.py wrote {', '.join(other)}; rerun each of those runs"
        )
    pending = [p.name for p, data in files if data.get("pending")]
    if pending:
        raise SystemExit(
            f"no result yet in {', '.join(pending)}: wait for each run, rerun it if it stopped,"
            " or delete its file if that run will not be repeated"
        )
    owners: dict[str, tuple[str, str]] = {}
    for path, data in files:
        for rule, info in data["rules"].items():
            skill, first = owners.setdefault(rule, (info["skill"], path.name))
            if skill != info["skill"]:
                raise SystemExit(
                    f"{rule} belongs to {skill} in {first} and to {info['skill']} in"
                    f" {path.name}; decide the rules of each genre skill on their own, and"
                    " ablate a language skill with --rules set to its own rules"
                )
    grid: dict[tuple[str, ...], dict[str, tuple[str, dict]]] = defaultdict(dict)
    for path, data in files:
        settings = data["settings"]
        row = grid[tuple(sorted(settings["skills"]))]
        if settings["model"] in row:
            raise SystemExit(
                f"{row[settings['model']][0]} and {path.name} test the same skills on the"
                " same model; give decide.py one tag per skill set"
            )
        row[settings["model"]] = (path.name, data)
    for row in grid.values():
        (name, first), *others = row.values()
        for other_name, data in others:
            if _step(data["settings"]) != _step(first["settings"]):
                raise SystemExit(
                    f"{name} and {other_name} test the same skills with other settings or"
                    " texts; give decide.py one tag per skill set"
                )
            differ = sorted(set(first["rules"]) ^ set(data["rules"]))
            if differ:
                raise SystemExit(
                    f"{name} and {other_name} hold different rules {differ};"
                    " rerun the model that stopped, or wait for the one that still runs"
                )
    models = {skills: sorted(row) for skills, row in grid.items()}
    if len({tuple(m) for m in models.values()}) > 1:
        listing = "; ".join(f"{'+'.join(k)}: {', '.join(m)}" for k, m in models.items())
        raise SystemExit(
            f"the skill sets ran on different test models ({listing}); run each on every model"
        )
    return files


def _refused(data: dict, variants: set[str]) -> tuple[set[str], set[str]]:
    """The cases with an output that the writer refused, and with one that every judge refused.

    A refused output fails its checks in one variant only, so it can move a rule's score by
    1/reps on its own. A judge refusal fails only the judge checks.
    """
    notes = [n for n in data["judge_fallbacks"] if n["variant"] in variants]
    return (
        {n["case"] for n in notes if n["judge"] == "writer-refused"},
        {n["case"] for n in notes if n["judge"] == "refused"},
    )


class Screen(NamedTuple):
    # Each rule, and the files in which it shows an effect.
    passing: list[tuple[str, list[str]]]
    # The rules that the screens measured without an effect.
    failing: list[str]
    # The rules that no listed screen had a case for.
    untested: list[str]
    # Rule -> "file: case" with a refused output in the rule's own checks.
    refused: dict[str, list[str]]


def screen_pass(files: list[tuple[Path, dict]]) -> Screen:
    own: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    refused: dict[str, set[str]] = defaultdict(set)
    rules_seen: set[str] = set()
    for path, data in files:
        rules_seen |= set(data["rules"])
        measured = {r for r, v in data["rules"].items() if "gain" in v}
        writer, judged = _refused(data, {"full", "control"})
        for key, check in data["checks"].items():
            # A check of a rule that this run did not measure (for example a rule in --without) does not count.
            if check["rule"] not in measured:
                continue
            own[check["rule"]][path.name].append(check["full"] - check["control"])
            case = key.split("/")[0]
            if case in writer or (check["kind"] == "judge" and case in judged):
                refused[check["rule"]].add(f"{path.name}: {case}")
    passing, failing, untested = [], [], []
    for rule in sorted(rules_seen):
        hit = [name for name, deltas in own[rule].items() if shows_effect(deltas)]
        if hit:
            passing.append((rule, hit))
        elif own[rule]:
            failing.append(rule)
        else:
            untested.append(rule)
    return Screen(
        passing, failing, untested, {r: sorted(v) for r, v in refused.items()}
    )


class Decision(NamedTuple):
    rule: str
    keep: bool
    # The result files in which the rule shows an effect.
    effect_in: list[str]
    # The mean change of the rule's own checks, per result file.
    means: dict[str, float]
    # The summed change of all checks in the rule's cases, across all files.
    net: float
    # Other checks that dropped by 0.4 or more.
    side: list[tuple[str, float, str]]
    # "file: case" with a refused output; the net sums every check of a case.
    refused: list[str]


def ablate_keep(files: list[tuple[Path, dict]]) -> list[Decision]:
    """A rule with no cases in any file is listed too, with no effect, so it is dropped."""
    seen: set[str] = set()
    own: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    net: dict[str, float] = defaultdict(float)
    side: dict[str, list[tuple[str, float, str]]] = defaultdict(list)
    refused: dict[str, set[str]] = defaultdict(set)
    for path, data in files:
        for rule, info in data["rules"].items():
            seen.add(rule)
            writer, judged = _refused(data, {"full", f"-{rule}"})
            for case in set(info.get("cases", {})) & (writer | judged):
                refused[rule].add(f"{path.name}: {case}")
            for key, check in info.get("checks", {}).items():
                delta = check["full"] - check["ablated"]
                net[rule] += delta
                if check["rule"] == rule:
                    own[rule][path.name].append(delta)
                elif delta <= -0.4 + EPS:
                    side[rule].append((key, round(delta, 2), path.name))
    out = []
    for rule in sorted(seen):
        effect_in = [name for name, deltas in own[rule].items() if shows_effect(deltas)]
        means = {
            name: round(sum(deltas) / len(deltas), 2)
            for name, deltas in own[rule].items()
        }
        keep = bool(effect_in) and net[rule] > EPS
        out.append(
            Decision(
                rule,
                keep,
                effect_in,
                means,
                round(net[rule], 2),
                side[rule],
                sorted(refused[rule]),
            )
        )
    return out


def main() -> int:
    if len(sys.argv) < 4 or sys.argv[1] not in ("screen-pass", "ablate-keep"):
        print(__doc__, file=sys.stderr)
        return 2
    cmd, rdir, globs = sys.argv[1], Path(sys.argv[2]), sys.argv[3:]
    files = result_files(rdir, "screen" if cmd == "screen-pass" else "ablate", globs)
    print("READ", ", ".join(path.name for path, _ in files))
    if cmd == "screen-pass":
        screen = screen_pass(files)
        print("PASS", ",".join(rule for rule, _ in screen.passing))
        print("FAIL", ",".join(screen.failing))
        print("NO CASES", ",".join(screen.untested))
        for rule, hit in screen.passing:
            print(f"  {rule:34s} {', '.join(hit)}")
        for rule, where in sorted(screen.refused.items()):
            print(f"REVIEW refused {rule:26s} {'; '.join(where)}")
    else:
        for d in ablate_keep(files):
            review = f" REVIEW {d.side}" if d.side else ""
            if d.refused:
                review += f" REVIEW refused {'; '.join(d.refused)}"
            cases = "" if d.means else " (no cases)"
            print(
                f"{'KEEP' if d.keep else 'drop'} {d.rule:32s} net={d.net:+.2f} means={d.means} effect_in={d.effect_in}{review}{cases}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
