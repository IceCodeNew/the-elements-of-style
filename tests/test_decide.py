"""Unit tests of evals/decide.py: the keep criterion and what it reads from results files.

Run from the repository root:

    python3 -m unittest discover -s tests -t . -v
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tests.helpers import REPO, load

decide = load("evals_decide", REPO / "evals" / "decide.py")


class KeepCriterion(unittest.TestCase):
    def test_user_sees_an_effect_at_exactly_two_tenths_despite_float_error(
        self,
    ) -> None:
        """user reads a screen: Given pass rates of 0.6 with the rule and 0.4 without it,
        When the keep criterion runs, Then the rule shows an effect."""
        self.assertTrue(
            decide.shows_effect([0.6 - 0.4]),
            "a mean gain of 0.2 must count, otherwise float error drops the rule",
        )

    def test_user_sees_an_effect_from_one_strong_check(self) -> None:
        """user reads a screen: Given one own check that gains 0.4 and two that do not change,
        When the keep criterion runs, Then the rule shows an effect."""
        self.assertTrue(
            decide.shows_effect([0.4, 0.0, 0.0]),
            "one check that gains 0.4 must count when no own check drops",
        )

    def test_user_sees_no_effect_when_an_own_check_drops(self) -> None:
        """user reads a screen: Given one own check that gains 0.4 and one that drops 0.4,
        When the keep criterion runs, Then the rule shows no effect."""
        self.assertFalse(
            decide.shows_effect([0.4, -0.4]),
            "an own check that drops 0.4 must cancel the strong-check rule",
        )


class DecideInputs(unittest.TestCase):
    def results(self, kind: str, data: dict, *more: tuple[str, str, dict]) -> Path:
        """Write the results file s@m, and one file for each (skill, model, sections) in more."""
        rdir = Path(tempfile.mkdtemp(prefix="evals-decide-"))
        self.addCleanup(shutil.rmtree, rdir)
        files = [("s", "m", data), *more]
        for skill, model, sections in files:
            report = {
                "format": decide.RESULTS_FORMAT,
                "settings": {"model": model, "skills": [skill], "inputs": "x"},
                "judge_fallbacks": [],
                **sections,
            }
            (rdir / f"{kind}-{skill}@{model}.json").write_text(
                json.dumps(report), encoding="utf-8"
            )
        return rdir

    def test_user_is_stopped_until_every_model_has_run_every_rule(self) -> None:
        """user decides while a model still runs: Given two models of one skill set, one with a rule
        that the other has not run yet, When the user applies the keep criterion, Then it stops."""
        rules = {"r.a": {"skill": "s"}, "r.b": {"skill": "s"}}
        rdir = self.results(
            "ablate", {"rules": rules}, ("s", "n", {"rules": {"r.a": {"skill": "s"}}})
        )
        with self.assertRaisesRegex(SystemExit, r"different rules \['r.b'\]"):
            decide.result_files(rdir, "ablate", ["s@*"])

    def test_user_is_stopped_when_skill_sets_ran_on_different_models(self) -> None:
        """user decides a language rule: Given one skill set on two models and another on one,
        When the user applies the keep criterion to both, Then it stops and lists the models."""
        rules = {"r.a": {"skill": "lang"}}
        rdir = self.results(
            "ablate",
            {"rules": rules},
            ("s", "n", {"rules": rules}),
            ("t", "m", {"rules": rules}),
        )
        with self.assertRaisesRegex(SystemExit, "different test models"):
            decide.result_files(rdir, "ablate", ["*@*"])

    @staticmethod
    def comparison(variants: list[str], *checks: tuple[str, str, str, float]) -> dict:
        """A comparison of format 2 with (key, rule, kind, change) checks."""
        return {
            "variants": variants,
            "checks": {
                key: {"rule": rule, "kind": kind, "full": 0.4 + change, "reduced": 0.4}
                for key, rule, kind, change in checks
            },
        }

    def screen_flags(self, refusal: str) -> list[str]:
        rdir = self.results(
            "screen",
            {
                "rules": {
                    "r.judged": {"skill": "s", "comparison": "screen"},
                    "r.matched": {"skill": "s", "comparison": "screen"},
                },
                "comparisons": {
                    "screen": self.comparison(
                        ["full", "control"],
                        ("k1/asks", "r.judged", "judge", 0.2),
                        ("k1/finds", "r.matched", "absent", 0.2),
                    )
                },
                "judge_fallbacks": [
                    {"variant": "full", "case": "k1", "rep": 0, "judge": refusal}
                ],
            },
        )
        return sorted(
            decide.screen_pass(decide.result_files(rdir, "screen", ["s@*"])).refused
        )

    def test_user_is_stopped_by_a_results_file_of_another_harness_version(self) -> None:
        """user decides with a file of another harness version: Given a results file of another format,
        When the user applies the screen criterion, Then it stops and names the file."""
        rdir = self.results(
            "screen",
            {
                "format": decide.RESULTS_FORMAT + 1,
                "rules": {},
                "checks": {},
                "judge_fallbacks": [],
            },
        )
        with self.assertRaisesRegex(SystemExit, "another version") as stop:
            decide.screen_pass(decide.result_files(rdir, "screen", ["s@*"]))
        self.assertIn(
            "screen-s@m.json",
            str(stop.exception),
            "the error must name the file to rerun",
        )

    def test_user_reviews_only_the_screen_decisions_that_a_refusal_can_change(
        self,
    ) -> None:
        """user reads a screen with refused outputs: Given a case with a judge check of one rule
        and a regex check of another, When every judge refuses an output of that case,
        Then only the rule with the judge check is flagged; when the writer refuses, both are."""
        self.assertEqual(
            self.screen_flags("refused"),
            ["r.judged"],
            "a judge refusal does not change a regex check",
        )
        self.assertEqual(
            self.screen_flags("writer-refused"),
            ["r.judged", "r.matched"],
            "a writer refusal fails every check",
        )

    def test_user_reviews_only_the_ablation_decisions_that_a_refusal_can_change(
        self,
    ) -> None:
        """user reads an ablation with refused outputs: Given two rules with the same cases, and
        refusals in the control, in the variant without the second rule, and in the variant without the first rule,
        When the user applies the keep criterion, Then each rule is flagged only for the refusal in its own variants."""
        checks = (("k1/x", "r.a", "judge", 0.0), ("k2/x", "r.b", "judge", 0.0))
        rdir = self.results(
            "ablate",
            {
                "rules": {
                    "r.a": {"skill": "s", "comparison": "r.a"},
                    "r.b": {"skill": "s", "comparison": "r.b"},
                },
                "comparisons": {
                    "r.a": self.comparison(["full", "-r.a"], *checks),
                    "r.b": self.comparison(["full", "-r.b"], *checks),
                },
                "judge_fallbacks": [
                    {
                        "variant": "control",
                        "case": "k1",
                        "rep": 0,
                        "judge": "writer-refused",
                    },
                    {"variant": "-r.b", "case": "k1", "rep": 0, "judge": "refused"},
                    {"variant": "-r.a", "case": "k2", "rep": 0, "judge": "refused"},
                ],
            },
        )
        flags = {
            d.rule: d.refused
            for d in decide.ablate_keep(decide.result_files(rdir, "ablate", ["s@*"]))
        }
        self.assertEqual(
            flags,
            {"r.a": ["ablate-s@m.json: k2"], "r.b": ["ablate-s@m.json: k1"]},
            "a decision compares the full variant with its own reduced variant only",
        )

    def test_user_decides_again_from_the_archived_results_of_format_1(self) -> None:
        """user checks an archived decision: Given a screen and an ablation of format 1, each
        with a rule that has cases and one that has none, When the user applies both criteria,
        Then they decide as they did when the archive was written."""
        old = {"format": 1, "judge_fallbacks": []}
        no_cases = {"status": "no-cases", "skill": "s"}
        rdir = self.results(
            "screen",
            {
                **old,
                "rules": {"r.a": {"skill": "s", "gain": 0.6}, "r.none": no_cases},
                "checks": {
                    "k1/x": {
                        "rule": "r.a",
                        "kind": "judge",
                        "full": 0.8,
                        "control": 0.2,
                    }
                },
            },
        )
        screen = decide.screen_pass(decide.result_files(rdir, "screen", ["s@*"]))
        self.assertEqual(
            (screen.passing, screen.untested),
            ([("r.a", ["screen-s@m.json"])], ["r.none"]),
            "the screen of format 1 must pass the same rules",
        )
        rdir = self.results(
            "ablate",
            {
                **old,
                "rules": {
                    "r.a": {
                        "skill": "s",
                        "cases": {"k1": {}},
                        "checks": {
                            "k1/x": {"rule": "r.a", "full": 0.8, "ablated": 0.2},
                            "k1/y": {"rule": "r.b", "full": 0.6, "ablated": 1.0},
                        },
                    },
                    "r.none": no_cases,
                },
                "judge_fallbacks": [
                    {"variant": "-r.a", "case": "k1", "rep": 0, "judge": "refused"}
                ],
            },
        )
        kept = {
            d.rule: (d.keep, d.net, d.side, d.refused)
            for d in decide.ablate_keep(decide.result_files(rdir, "ablate", ["s@*"]))
        }
        self.assertEqual(
            kept,
            {
                "r.a": (
                    True,
                    0.2,
                    [("k1/y", -0.4, "ablate-s@m.json")],
                    ["ablate-s@m.json: k1"],
                ),
                "r.none": (False, 0, [], []),
            },
            "the ablation of format 1 must keep, drop and flag the same rules",
        )


if __name__ == "__main__":
    unittest.main()
