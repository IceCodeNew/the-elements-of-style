"""Behavior tests of what the ablation harness measures and decides. They call no model.

Run from the repository root:

    python3 -m unittest discover -s tests -t . -v

tests/e2e.py builds the temporary repository with fake models. The contract test checks
that the real grader still answers in the form that the fakes assume; it calls the real
claude CLI, so it runs only when EVALS_CONTRACT_TEST=1.
"""

from __future__ import annotations

import json
import os
import shutil
import tempfile
import threading
import unittest
from pathlib import Path

from tests.e2e import CASES, EVALS, EndToEnd
from tests.helpers import load


class HarnessEndToEnd(EndToEnd):
    def test_user_screens_rules_on_each_model_with_a_grader_that_leaves_out_checks(
        self,
    ) -> None:
        """user screens a skill: Given a grader that leaves out one check in each reply,
        When the user screens the skill on a Claude model and on a Codex model,
        Then each model has its own results file and only the rules that change the output pass."""
        done = self.screen("fake-follow")
        self.assertIn(
            "summed change",
            done.stdout,
            "the screen must give the change over all checks",
        )
        self.screen("codex:fake:low")
        self.assertEqual(
            sorted(p.name for p in self.results().glob("screen-*.json")),
            [
                "screen-test-skill@codex-fake-low.json",
                "screen-test-skill@fake-follow.json",
            ],
            "each test model must write its own results file, otherwise one model overwrites the other",
        )
        screen = self.screen_pass("test-skill@*")
        self.assertEqual(
            [r for r, _ in screen.passing],
            ["test.alpha", "test.beta", "test.gamma"],
            "rules that change the output must pass",
        )
        self.assertEqual(
            screen.failing,
            ["test.dead"],
            "a rule without an effect must fail the screen",
        )

    def test_user_decides_a_language_rule_from_its_screens_with_each_genre_skill(
        self,
    ) -> None:
        """user screens a language skill: Given screens of the language skill against each of two genre skills,
        When the user applies the screen criterion to both screens, and then screens one genre pair on a second model,
        Then it decides only the language rule, from both screens, because a genre rule is in both variants of its
        screen; and it stops once the two genre pairs ran on different models."""
        for genre in ("test-skill", "test-other"):
            self.screen(
                "fake-follow",
                "--control-skills",
                genre,
                skills=f"{genre},test-lang",
                tag=f"{genre}-lang",
            )
        screen = self.screen_pass("*-lang@*")
        self.assertEqual(
            [(r, len(files)) for r, files in screen.passing],
            [("lang.epsilon", 2)],
            "the language rule must be decided from its screens with both genre skills",
        )
        self.assertEqual(
            screen.failing + screen.untested,
            [],
            "a rule of a genre skill must not be decided by a language screen",
        )
        self.screen(
            "fake-harm",
            "--control-skills",
            "test-skill",
            skills="test-skill,test-lang",
            tag="test-skill-lang",
        )
        with self.assertRaisesRegex(SystemExit, "different test models"):
            self.screen_pass("*-lang@*")

    def test_user_reruns_a_screen_from_the_cache(self) -> None:
        """user reruns a screen: Given a finished screen,
        When the user runs the same screen again,
        Then the harness calls no model."""
        self.screen("fake-follow")
        before = len(self.calls())
        self.screen("fake-follow")
        self.assertEqual(
            len(self.calls()),
            before,
            "a rerun must read the cache, otherwise it spends model calls again",
        )

    def test_user_keeps_a_rule_only_when_the_net_change_across_models_is_positive(
        self,
    ) -> None:
        """user decides on rules from two models: Given a model on which the BETA rule
        removes the words of two other rules, When the user ablates every rule on both
        models and applies the keep criterion, Then BETA is dropped with its side effects
        listed for review, and the rules with a net gain are kept."""
        for model in ("fake-follow", "fake-harm"):
            self.ablate(model)
        decisions = self.ablate_keep("test-skill@*")
        self.assertEqual(
            sorted(r for r, d in decisions.items() if d.keep),
            ["test.alpha", "test.gamma"],
            "rules with an effect and a net gain across models must stay",
        )
        self.assertEqual(
            sorted(r for r, d in decisions.items() if not d.keep),
            ["test.beta", "test.dead"],
            "a rule without a net gain must go, otherwise it ships a regression",
        )
        self.assertTrue(
            decisions["test.beta"].side,
            "a drop of 0.4 or more on another check must be listed for review",
        )

    def test_user_cannot_get_a_removed_rule_back_through_codex_tools(self) -> None:
        """user ablates on Codex: Given a Codex model that reads every SKILL.md when it has a
        tool that reads files, When the user ablates the ALPHA rule on that model,
        Then the variant without ALPHA lacks the word, so the rule keeps its measured effect."""
        self.ablate("codex:fake:low", "--rules", "test.alpha")
        decision = self.ablate_keep("test-skill@*")["test.alpha"]
        self.assertTrue(
            decision.keep,
            "a removed rule must stay removed, otherwise Codex results hide its effect",
        )

    def test_user_is_stopped_when_codex_would_read_a_global_agents_md(self) -> None:
        """user screens on Codex: Given an AGENTS.md in CODEX_HOME,
        When the user screens the skill on a Codex model,
        Then the harness stops before any model call and names the file."""
        (self.codex_home / "AGENTS.md").write_text(
            "Always write OMEGA.\n", encoding="utf-8"
        )
        done = self.screen("codex:fake:low", ok=False)
        self.assertIn(
            "AGENTS.md",
            done.stderr,
            "the error must name the file that would reach the model",
        )
        self.assertFalse(
            [c for c in self.calls() if c.startswith("codex")],
            "no Codex call may run with that file in place",
        )

    def test_user_gets_a_fallback_grade_when_the_judge_refuses(self) -> None:
        """user screens with a judge that refuses some outputs: Given a judge that refuses
        every output with GAMMA, When the user screens the skill,
        Then the fallback judge grades those outputs, each refusal is asked only once,
        and the results file lists the outputs that the fallback graded."""
        self.screen("fake-follow", env={"FAKE_REFUSE": "GAMMA"})
        refused = [c.split()[-1] for c in self.calls() if " refused " in c]
        self.assertTrue(refused, "the fixture must make the judge refuse")
        self.assertEqual(
            len(refused),
            len(set(refused)),
            "a refusal must not be retried, otherwise each one waits for minutes",
        )
        notes = self.report("screen-test-skill@fake-follow.json")["judge_fallbacks"]
        self.assertEqual(
            {n["judge"] for n in notes},
            {"opus"},
            "the results must show which outputs the fallback judge graded",
        )

    def test_user_counts_an_output_that_every_judge_refuses_as_failed(self) -> None:
        """user screens with judges that all refuse some outputs: Given judges that refuse
        every output with GAMMA, When the user screens the skill and screens it again,
        Then the judge checks of those outputs fail, the results list them as refused,
        the decision names the case, and the second screen calls no model."""
        self.screen("fake-follow", env={"FAKE_REFUSE": "GAMMA", "FAKE_REFUSE_ALL": "1"})
        report = self.report("screen-test-skill@fake-follow.json")
        self.assertEqual(
            report["checks"]["c1/has-alpha"]["full"],
            0.0,
            "a refused output must fail its judge checks",
        )
        self.assertEqual(
            report["checks"]["c1/says-alpha"]["full"],
            1.0,
            "a regex check of a refused output is still graded",
        )
        self.assertIn(
            "refused",
            {n["judge"] for n in report["judge_fallbacks"]},
            "the results must list the refused outputs",
        )
        refused = self.screen_pass("test-skill@*").refused
        self.assertIn(
            "c1",
            " ".join(refused["test.gamma"]),
            "the decision must name the case with refused outputs, so the user reads them first",
        )
        before = len(self.calls())
        self.screen("fake-follow", env={"FAKE_REFUSE": "GAMMA", "FAKE_REFUSE_ALL": "1"})
        self.assertEqual(
            len(self.calls()),
            before,
            "a refusal must be cached, otherwise each rerun asks again",
        )

    def test_user_counts_an_output_that_the_writer_refuses_as_failed(self) -> None:
        """user screens with a writer that refuses one task: Given a writer that refuses
        the task of case c2, When the user screens the skill,
        Then every check of c2 fails in both variants and the results list the refusals."""
        self.screen("fake-follow", env={"FAKE_WRITER_REFUSE": "Write another line."})
        report = self.report("screen-test-skill@fake-follow.json")
        self.assertEqual(
            report["checks"]["c2/has-alpha-2"]["full"],
            0.0,
            "a refused output must fail every check",
        )
        self.assertEqual(
            report["checks"]["c2/no-delta"]["full"],
            0.0,
            "a refused output must fail its regex checks too",
        )
        self.assertEqual(
            {n["judge"] for n in report["judge_fallbacks"]},
            {"writer-refused"},
            "the results must list the refusals",
        )

    def test_user_is_told_which_ablation_decisions_rest_on_refused_outputs(
        self,
    ) -> None:
        """user ablates with a writer that refuses one task: Given a writer that refuses the task of case c2,
        When the user ablates the ALPHA rule and applies the keep criterion,
        Then the decision names c2, so the user reads those outputs before recording it."""
        self.ablate(
            "fake-follow",
            "--rules",
            "test.alpha",
            env={"FAKE_WRITER_REFUSE": "Write another line."},
        )
        decision = self.ablate_keep("test-skill@*")["test.alpha"]
        self.assertIn(
            "c2",
            " ".join(decision.refused),
            "the decision must name the case with refused outputs",
        )

    def test_user_cannot_count_a_string_verdict_as_a_pass(self) -> None:
        """user screens with a grader that answers with strings: Given a grader that answers
        "false" instead of false, When the user screens the skill,
        Then the screen fails and names the case, instead of counting "false" as a pass."""
        done = self.screen("fake-follow", ok=False, env={"FAKE_STRING_VERDICTS": "1"})
        self.assertIn(
            "no true or false verdict",
            done.stderr,
            "the error must say why the grade failed",
        )

    def test_user_is_told_which_case_has_a_probe_in_the_old_form(self) -> None:
        """user adds a probe case in the old form: Given a case with "probe": true,
        When the user screens the skill, Then the harness stops and names the case."""
        old = {**CASES[2], "id": "p-old", "probe": True}
        (self.root / "evals" / "cases" / "old.json").write_text(
            json.dumps([old]), encoding="utf-8"
        )
        self.assertIn(
            "p-old",
            self.screen("fake-follow", ok=False).stderr,
            "the error must name the case to fix",
        )

    def test_user_sees_the_rules_that_no_case_tests(self) -> None:
        """user screens a skill without cases for one rule: Given a skill whose rule has no case,
        When the user applies the screen criterion, Then the output names that rule as untested."""
        self.screen("fake-follow", skills="test-other", tag="test-other")
        done = self.run_tool(
            "evals/decide.py", "screen-pass", "evals/results", "test-other@*"
        )
        self.assertIn(
            "NO CASES other.short",
            done.stdout,
            "a rule without cases needs cases, not a silent drop",
        )
        self.assertIn(
            "READ screen-test-other@fake-follow.json",
            done.stdout,
            "the output must name the files it decided from",
        )

    def test_user_cannot_name_an_unknown_rule_or_a_skipped_case(self) -> None:
        """user screens a reduced skill: Given a typo in --without or in --cases, or a case
        that the control skill makes the screen skip, When the user screens the skill,
        Then the harness stops and names the id."""
        self.assertIn(
            "test.alhpa",
            self.screen("fake-follow", "--without", "test.alhpa", ok=False).stderr,
            "a typo must not silently leave the rule in the skill",
        )
        self.assertIn(
            "nosuch",
            self.screen("fake-follow", "--cases", "nosuch", ok=False).stderr,
            "a typo must not silently test no case",
        )
        skipped = self.screen(
            "fake-follow", "--control-skills", "test-skill", "--cases", "c1", ok=False
        )
        self.assertIn(
            "c1",
            skipped.stderr,
            "a case that the run skips must not silently test nothing",
        )
        both = self.ablate(
            "fake-follow", "--rules", "test.beta", "--without", "test.beta", ok=False
        )
        self.assertIn(
            "test.beta",
            both.stderr,
            "a rule that both variants lack must not be ablated",
        )


class AtomicWrite(unittest.TestCase):
    def test_user_keeps_a_valid_cache_when_threads_write_the_same_file(self) -> None:
        """user grades two identical outputs at once: Given four threads that write the same
        cache file many times, When they finish, Then no write failed and the file is valid."""
        root = Path(tempfile.mkdtemp(prefix="evals-atomic-"))
        self.addCleanup(shutil.rmtree, root)
        (root / "evals").mkdir()
        shutil.copy(EVALS / "run.py", root / "evals" / "run.py")
        run = load("evals_run_atomic", root / "evals" / "run.py")
        target, errors = root / "evals" / ".cache" / "grade" / "x.json", []

        def write(n: int) -> None:
            for i in range(200):
                try:
                    run._write_atomic(
                        target, json.dumps({"writer": n, "i": i, "pad": "x" * 2000})
                    )
                except OSError as error:
                    errors.append(error)

        threads = [threading.Thread(target=write, args=(n,)) for n in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(
            errors, [], "concurrent writers of one cache file must not fail"
        )
        self.assertIn(
            "writer",
            json.loads(target.read_text(encoding="utf-8")),
            "the cache file must hold one complete write",
        )
        self.assertEqual(
            list(target.parent.glob(".*.tmp")), [], "no temporary file may stay behind"
        )
        with self.assertRaises(UnicodeEncodeError):
            run._write_atomic(target, "\ud800")
        self.assertEqual(
            list(target.parent.glob(".*.tmp")),
            [],
            "a failed write must not leave a temporary file",
        )


@unittest.skipUnless(
    os.environ.get("EVALS_CONTRACT_TEST") == "1",
    "set EVALS_CONTRACT_TEST=1 to call the real claude CLI",
)
class GraderContract(unittest.TestCase):
    def test_user_gets_a_verdict_for_every_check_from_the_real_grader(self) -> None:
        """user grades with the real CLI: Given a short output and three judge checks,
        When the harness grades the output with the real grader,
        Then every check gets a true or false verdict, which is what the fake grader assumes."""
        root = Path(tempfile.mkdtemp(prefix="evals-contract-"))
        self.addCleanup(shutil.rmtree, root)
        (root / "evals").mkdir()
        shutil.copy(EVALS / "run.py", root / "evals" / "run.py")
        run = load(
            "evals_run_contract", root / "evals" / "run.py"
        )  # its cache goes to the temporary copy
        checks = tuple(
            run.Check(f"c{i}", "test.any", "judge", text)
            for i, text in enumerate(
                (
                    "Does the output mention rain?",
                    "Does the output mention snow?",
                    "Is the output one sentence?",
                )
            )
        )
        case = run.Case(
            "contract",
            ("test-skill",),
            "Write one sentence about the weather.",
            checks,
            "new",
        )
        graded = run.grade(
            os.environ.get("EVALS_JUDGE", "sonnet"),
            case,
            "Rain fell all night on the tin roof.",
        )
        verdict = graded.passed
        self.assertEqual(
            sorted(verdict), ["c0", "c1", "c2"], "the grader must answer every check id"
        )
        self.assertTrue(
            all(isinstance(v, bool) for v in verdict.values()),
            "each verdict must be true or false",
        )
        self.assertEqual(
            (verdict["c0"], verdict["c1"]),
            (True, False),
            "the grader must answer the questions as asked",
        )


if __name__ == "__main__":
    unittest.main()
