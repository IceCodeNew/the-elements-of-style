"""The end-to-end fixture of the harness tests: a temporary repository with fake models.

Each test copies evals/run.py and evals/decide.py into a temporary repository and puts
tests/fake_model.py, as fake `claude` and `codex` executables, first on PATH.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from functools import partialmethod
from pathlib import Path

from tests.helpers import REPO, load

EVALS = REPO / "evals"
FAKE_MODEL = Path(__file__).with_name("fake_model.py")

SKILL = """---
name: test-skill
description: "Use in the harness tests."
---

# Test skill

- Write the word ALPHA. <!-- r:test.alpha -->
- Write the word BETA. <!-- r:test.beta -->
- Write the word GAMMA. <!-- r:test.gamma -->
- Keep the text short. <!-- r:test.dead -->
"""

OTHER_SKILL = """---
name: test-other
description: "Use in the harness tests as a second genre skill."
---

# Other test skill

- Write the word ALPHA. <!-- r:test.alpha -->
- Keep the text short. <!-- r:other.short -->
"""

LANG_SKILL = """---
name: test-lang
description: "Use in the harness tests as a language skill."
---

# Test language skill

- Write the word EPSILON. <!-- r:lang.epsilon -->
"""


def check(word: str, rule: str, suffix: str = "") -> dict:
    return {
        "id": f"has-{word.lower()}{suffix}",
        "rule": rule,
        "kind": "judge",
        "text": f"Does the output contain {word}?",
    }


CASES = [
    {
        "id": "c1",
        "skills": ["test-skill"],
        "source": "new",
        "prompt": "Write one line.",
        "checks": [
            check("ALPHA", "test.alpha"),
            check("BETA", "test.beta"),
            check("GAMMA", "test.gamma"),
            check("OMEGA", "test.dead"),
        ],
    },
    {
        "id": "c2",
        "skills": ["test-skill"],
        "source": "new",
        "prompt": "Write another line.",
        "checks": [check("ALPHA", "test.alpha", "-2")],
    },
    {
        "id": "p1",
        "skills": ["test-skill"],
        "source": "new",
        "prompt": "Write a probe line.",
        "checks": [check("ALPHA", "test.alpha", "-p")],
        "probe": ["says-alpha", "no-delta"],
    },
    {
        "id": "c3",
        "skills": ["test-skill", "test-lang"],
        "source": "new",
        "prompt": "Write a line in the language.",
        "checks": [
            check("ALPHA", "test.alpha", "-3"),
            check("EPSILON", "lang.epsilon"),
        ],
    },
    {
        "id": "c4",
        "skills": ["test-other", "test-lang"],
        "source": "new",
        "prompt": "Write a short line in the language.",
        "checks": [check("EPSILON", "lang.epsilon", "-4")],
    },
]
GLOBAL_CHECKS = [
    {"id": "says-alpha", "rule": "test.alpha", "kind": "present", "text": "ALPHA"},
    {"id": "no-delta", "rule": "general", "kind": "absent", "text": "DELTA"},
]


class EndToEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="evals-test-"))
        self.addCleanup(shutil.rmtree, self.root)
        (self.root / "evals" / "cases").mkdir(parents=True)
        for name in ("run.py", "decide.py"):
            shutil.copy(EVALS / name, self.root / "evals" / name)
        (self.root / "evals" / "cases" / "c.json").write_text(
            json.dumps(CASES), encoding="utf-8"
        )
        (self.root / "evals" / "global-checks.json").write_text(
            json.dumps(GLOBAL_CHECKS), encoding="utf-8"
        )
        for name, text in (
            ("test-skill", SKILL),
            ("test-other", OTHER_SKILL),
            ("test-lang", LANG_SKILL),
        ):
            (self.root / "skills" / name).mkdir(parents=True)
            (self.root / "skills" / name / "SKILL.md").write_text(
                text, encoding="utf-8"
            )
        bin_dir = self.root / "bin"
        bin_dir.mkdir()
        for exe in ("claude", "codex"):
            fake = bin_dir / exe
            fake.write_text(
                f"#!{sys.executable}\n" + FAKE_MODEL.read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            fake.chmod(0o755)
        self.codex_home = self.root / "codex-home"
        self.codex_home.mkdir()
        self.log = self.root / "calls.log"
        self.env = dict(
            os.environ,
            PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
            FAKE_MODEL_LOG=str(self.log),
            FAKE_REPO_ROOT=str(self.root),
            CODEX_HOME=str(self.codex_home),
        )
        self.decide = load(f"decide_{id(self)}", self.root / "evals" / "decide.py")

    def run_tool(
        self, *args: str, ok: bool = True, env: dict[str, str] | None = None
    ) -> subprocess.CompletedProcess:
        done = subprocess.run(
            [sys.executable, "-I", *args],
            cwd=self.root,
            env={**self.env, **(env or {})},
            capture_output=True,
            text=True,
            check=False,
        )
        if ok:
            self.assertEqual(
                done.returncode,
                0,
                f"{' '.join(args)} must succeed, otherwise the user gets no result:\n{done.stderr}",
            )
        else:
            self.assertNotEqual(
                done.returncode,
                0,
                f"{' '.join(args)} must fail, otherwise the user trusts a wrong result",
            )
        return done

    def command(
        self,
        command: str,
        model: str,
        *extra: str,
        skills: str = "test-skill",
        tag: str | None = "test-skill",
    ) -> list[str]:
        """The command line of a run; tag=None fills the cache with --gen-only."""
        return [
            "evals/run.py",
            command,
            "--skills",
            skills,
            *(("--tag", tag) if tag else ("--gen-only",)),
            "--model",
            model,
            "--reps",
            "2",
            "--workers",
            "1",
            *extra,
        ]

    def compare(
        self,
        command: str,
        model: str,
        *extra: str,
        skills: str = "test-skill",
        tag: str | None = "test-skill",
        ok: bool = True,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess:
        return self.run_tool(
            *self.command(command, model, *extra, skills=skills, tag=tag),
            ok=ok,
            env=env,
        )

    screen = partialmethod(compare, "screen")
    ablate = partialmethod(compare, "ablate")

    def screen_pass(self, *globs: str):
        return self.decide.screen_pass(
            self.decide.result_files(self.results(), "screen", list(globs))
        )

    def ablate_keep(self, *globs: str) -> dict:
        files = self.decide.result_files(self.results(), "ablate", list(globs))
        return {d.rule: d for d in self.decide.ablate_keep(files)}

    def calls(self) -> list[str]:
        return (
            self.log.read_text(encoding="utf-8").splitlines()
            if self.log.exists()
            else []
        )

    def results(self) -> Path:
        return self.root / "evals" / "results"

    def report(self, name: str) -> dict:
        return json.loads((self.results() / name).read_text(encoding="utf-8"))
