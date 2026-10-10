"""The fake `claude` and `codex` executables of the harness tests.

The tests copy this file as `claude` and `codex`. The writer follows rules of the form
"Write the word ALPHA."; the grader answers checks of the form "Does the output contain
ALPHA?" and always leaves out the last check of a reply that asks for more than one.

Environment switches:
  FAKE_MODEL_LOG       file that gets one line per call
  FAKE_REPO_ROOT       the test repository; Codex reads every SKILL.md there when it has a
                       tool that reads files, or when it runs inside the repository and so
                       loads its project context
  FAKE_REFUSE          a word; the judge "sonnet" refuses an output that contains it
  FAKE_REFUSE_ALL      with FAKE_REFUSE, every judge refuses such an output
  FAKE_WRITER_REFUSE   a task text that the writer refuses
  FAKE_STRING_VERDICTS the grader answers "true" and "false" as strings
  FAKE_DELAY           seconds that each call waits before it answers
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import NoReturn

WORDS = ("ALPHA", "BETA", "GAMMA", "EPSILON")
FILE_TOOLS = ("shell_tool", "unified_exec", "code_mode_host")


def write(model: str, system: str) -> str:
    words = [w for w in WORDS if f"Write the word {w}." in system]
    if model.endswith("harm") and "BETA" in words:
        words = [
            "BETA"
        ]  # this model drops the other words when it follows the BETA rule
    return " ".join(words) or "Nothing to say."


def grade(prompt: str) -> str:
    output = prompt.split("<output>\n", 1)[1].split("\n</output>", 1)[0].split()
    checks = re.findall(
        r"^- ([\w-]+): Does the output contain (\w+)\?$",
        prompt.split("<checks>", 1)[1],
        re.MULTILINE,
    )
    verdict: dict[str, bool | str] = {cid: word in output for cid, word in checks}
    if os.environ.get("FAKE_STRING_VERDICTS"):
        verdict = {cid: str(v).lower() for cid, v in verdict.items()}
    if len(checks) > 1:
        verdict.pop(checks[-1][0])
    return "Verdict:\n" + json.dumps(verdict)


def log(*parts: str) -> None:
    with open(os.environ["FAKE_MODEL_LOG"], "a", encoding="utf-8") as f:
        f.write(" ".join(parts) + "\n")


def refuse(model: str) -> NoReturn:
    # A warning on stderr, and the error in the middle of a long text on stdout: the harness
    # must read both streams and the full text.
    print("warning: " + "w" * 700, file=sys.stderr)
    print(
        f"API Error: {'x' * 400} {model}'s safeguards flagged this message. {'y' * 400}"
    )
    sys.exit(1)


def codex(args: list[str], root: Path) -> None:
    model = "codex:" + args[args.index("-m") + 1]
    prefix = "developer_instructions="
    system = json.loads(next(a for a in args if a.startswith(prefix))[len(prefix) :])
    disabled = {args[i + 1] for i, a in enumerate(args) if a == "--disable"}
    cwd = Path.cwd().resolve()
    if root == cwd or root in cwd.parents or not set(FILE_TOOLS) <= disabled:
        # Inside the repository Codex loads project context, and a model with a tool that
        # reads files reads the full skills; either way it sees the removed rules.
        for skill in sorted(root.glob("skills/*/SKILL.md")):
            system += "\n" + skill.read_text(encoding="utf-8")
    log("codex", model)
    Path(args[args.index("-o") + 1]).write_text(write(model, system), encoding="utf-8")


def claude(args: list[str]) -> None:
    system, prompt = args[args.index("--system-prompt") + 1], args[-1]
    model = args[args.index("--model") + 1]
    if system.startswith("You grade"):
        word = os.environ.get("FAKE_REFUSE")
        output = prompt.split("<output>\n", 1)[1].split("\n</output>", 1)[0]
        if (
            word
            and word in output.split()
            and (model == "sonnet" or os.environ.get("FAKE_REFUSE_ALL"))
        ):
            log(
                "claude",
                model,
                "refused",
                hashlib.sha256(prompt.encode()).hexdigest()[:12],
            )
            refuse(model)
        log("claude", model, "grade")
        print(grade(prompt))
    else:
        if prompt == os.environ.get("FAKE_WRITER_REFUSE"):
            log("claude", model, "writer-refused")
            refuse(model)
        log("claude", model, "write")
        print(write(model, system))


def main() -> None:
    time.sleep(float(os.environ.get("FAKE_DELAY", "0")))
    root = Path(os.environ["FAKE_REPO_ROOT"]).resolve()
    if Path(sys.argv[0]).name == "codex":
        codex(sys.argv[1:], root)
    else:
        claude(sys.argv[1:])


if __name__ == "__main__":
    main()
