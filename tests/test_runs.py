"""Behavior tests of how runs are named, locked, rerun and decided from their results files.

Run from the repository root:

    python3 -m unittest discover -s tests -t . -v
"""

from __future__ import annotations

import json
import subprocess
import sys
import time

from tests.e2e import SKILL, EndToEnd


class RunsEndToEnd(EndToEnd):
    def test_user_cannot_add_up_two_steps_or_two_settings_of_the_same_skills(
        self,
    ) -> None:
        """user runs and decides add-back runs: Given a full ablation and an add-back run without ALPHA,
        When the user runs the add-back tag on a second model without --without, and applies the
        keep criterion to globs that mix steps or settings,
        Then the run stops before any model call, the criterion refuses, and a mistyped glob stops it too."""
        self.ablate("fake-follow")
        self.ablate(
            "fake-follow",
            "--rules",
            "test.beta",
            "--without",
            "test.alpha",
            tag="addback",
        )
        before = len(self.calls())
        mixed = self.ablate(
            "fake-harm", "--rules", "test.beta", tag="addback", ok=False
        )
        self.assertIn(
            "addback", mixed.stderr, "the error must name the tag whose runs differ"
        )
        self.assertEqual(
            len(self.calls()),
            before,
            "a run of one tag with other settings must stop before any model call",
        )
        self.ablate("fake-harm", "--rules", "test.beta", tag="other")
        with self.assertRaisesRegex(SystemExit, "same model"):
            self.ablate_keep("*@fake-follow")
        with self.assertRaisesRegex(SystemExit, "other settings"):
            self.ablate_keep("addback@*", "other@*")
        with self.assertRaisesRegex(SystemExit, "match nosuch"):
            self.ablate_keep("test-skill@*", "nosuch@*")

    def test_user_is_stopped_while_a_model_has_not_run_every_rule(self) -> None:
        """user decides while one model still runs: Given an ablation of two rules on one model
        and of one of them on a second model, When the user applies the keep criterion,
        Then it stops, and it decides both rules once the second model has run them."""
        self.ablate("fake-follow", "--rules", "test.alpha,test.beta", tag="s2")
        self.ablate("fake-harm", "--rules", "test.alpha", tag="s2")
        with self.assertRaisesRegex(SystemExit, "different rules"):
            self.ablate_keep("s2@*")
        self.ablate("fake-harm", "--rules", "test.beta", tag="s2")
        self.assertEqual(
            sorted(self.ablate_keep("s2@*")),
            ["test.alpha", "test.beta"],
            "once every model has run every rule, the criterion decides them",
        )

    def test_user_is_stopped_when_a_model_stopped_before_its_first_result(self) -> None:
        """user decides after a screen failed on one model: Given a finished screen on one model
        and a screen of the same tag that failed on a second model before its first result,
        When the user applies the screen criterion, Then it stops instead of deciding from one model,
        and a rerun of the failed screen with a corrected judge completes the step."""
        self.screen("fake-follow", tag="s1")
        self.screen(
            "fake-harm",
            "--judge",
            "other",
            tag="s1",
            ok=False,
            env={"FAKE_STRING_VERDICTS": "1"},
        )
        with self.assertRaisesRegex(SystemExit, "no result yet"):
            self.screen_pass("s1@*")
        pending = self.run_tool("evals/run.py", "cases", "--results", "s1@*", ok=False)
        self.assertIn(
            "no result yet",
            pending.stderr,
            "the case report must not prune checks from part of the models",
        )
        self.screen("fake-harm", tag="s1")
        self.assertEqual(
            [r for r, _ in self.screen_pass("s1@*").passing],
            ["test.alpha", "test.beta", "test.gamma"],
            "the corrected rerun must replace the empty file",
        )

    def test_user_reruns_a_step_that_stopped_on_every_model(self) -> None:
        """user corrects a step that failed on every model: Given screens of one tag with a wrong
        --cases that stopped before their first result on two models,
        When the user reruns both with the corrected setting,
        Then both reruns go through and the step can be decided."""
        for model in ("fake-follow", "fake-harm"):
            self.screen(
                model,
                "--cases",
                "c1",
                tag="s1",
                ok=False,
                env={"FAKE_STRING_VERDICTS": "1"},
            )
        for model in ("fake-follow", "fake-harm"):
            self.screen(model, tag="s1")
        self.assertEqual(
            [r for r, _ in self.screen_pass("s1@*").passing],
            ["test.alpha", "test.beta", "test.gamma"],
            "an ended run without results must not block the corrected runs of the step",
        )

    def test_user_decides_the_shared_rules_of_each_genre_skill_on_their_own(
        self,
    ) -> None:
        """user screens two genre skills that share a rule: Given a screen of each genre skill,
        When the user applies the screen criterion to both screens at once,
        Then it stops, because each genre skill keeps or drops its own copy of the rule."""
        self.screen("fake-follow")
        self.screen("fake-follow", skills="test-other", tag="test-other")
        with self.assertRaisesRegex(SystemExit, "belongs to"):
            self.screen_pass("test-skill@*", "test-other@*")

    def test_user_cannot_start_a_conflicting_run_while_a_run_writes(self) -> None:
        """user starts runs of one step at once: Given a slow model that ablates under one tag,
        When the user starts a second ablation of that tag on the same model, and one with
        other settings on a second model, while the first runs,
        Then both stop before any model call, and the first writes its results."""
        args = [sys.executable, "-I", *self.command("ablate", "fake-follow", tag="s4")]
        env = {**self.env, "FAKE_DELAY": "0.2"}
        first = subprocess.Popen(
            [*args, "--rules", "test.alpha"],
            cwd=self.root,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.addCleanup(first.wait)
        self.addCleanup(first.kill)
        deadline = time.monotonic() + 60
        while not self.calls() and time.monotonic() < deadline:
            time.sleep(0.05)
        second = subprocess.run(
            [*args, "--rules", "test.beta"],
            cwd=self.root,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        other = self.ablate(
            "fake-harm",
            "--rules",
            "test.beta",
            "--without",
            "test.dead",
            tag="s4",
            ok=False,
        )
        self.assertIn(
            "ran --tag s4",
            other.stderr,
            "a run with other settings must see the run that is still going",
        )
        _, err = first.communicate(timeout=300)
        self.assertEqual(first.returncode, 0, f"the first run must finish:\n{err}")
        self.assertNotEqual(
            second.returncode,
            0,
            "a second run into the same file would overwrite the first",
        )
        self.assertIn(
            "another run writes",
            second.stderr,
            "the second run must stop because of the first, not for another reason",
        )
        self.assertEqual(
            sorted(self.report("ablate-s4@fake-follow.json")["rules"]),
            ["test.alpha"],
            "the file must hold the results of the run that wrote it",
        )

    def test_user_fills_the_cache_without_grading(self) -> None:
        """user generates the outputs first: Given a screen with --gen-only,
        When it runs, Then it writes outputs and no results file, and a later screen grades them."""
        self.screen("fake-follow", tag=None)
        self.assertFalse(
            [c for c in self.calls() if c.endswith(" grade")],
            "--gen-only must not grade",
        )
        self.assertEqual(
            list(self.results().glob("*.json")),
            [],
            "--gen-only must not write a results file",
        )
        writes = len([c for c in self.calls() if c.endswith(" write")])
        self.screen("fake-follow")
        self.assertEqual(
            len([c for c in self.calls() if c.endswith(" write")]),
            writes,
            "the later screen must read the outputs from the cache",
        )

    def test_user_names_each_run_with_a_plain_tag_and_model(self) -> None:
        """user screens a skill: Given no --tag, a tag with a path in it, and a Codex model
        name without a reasoning effort, When the user screens the skill,
        Then the harness stops before any model call and leaves no file."""
        done = self.run_tool(
            "evals/run.py",
            "screen",
            "--skills",
            "test-skill",
            "--model",
            "fake-follow",
            ok=False,
        )
        self.assertIn(
            "--tag", done.stderr, "a run without a name must say how to name it"
        )
        self.screen("fake-follow", tag="../outside", ok=False)
        malformed = self.screen("codex:fake", ok=False)
        self.assertIn(
            "codex:<model>:<reasoning effort>",
            malformed.stderr,
            "the error must show the form of a Codex model name",
        )
        self.assertEqual(
            self.calls(), [], "no model call may run before the run has a valid name"
        )
        self.assertEqual(
            list(self.results().glob("*.json")),
            [],
            "a run with a malformed name must leave no file",
        )

    def test_user_reruns_an_ablation_with_more_repetitions(self) -> None:
        """user repeats a close result: Given an ablation of two rules with 2 repetitions,
        When the user reruns one rule with 3 repetitions under the same tag,
        Then the run adds to the file, and the criterion still decides both rules."""
        self.ablate("fake-follow", "--rules", "test.alpha,test.beta")
        self.ablate("fake-follow", "--rules", "test.alpha", "--reps", "3")
        rules = self.report("ablate-test-skill@fake-follow.json")["rules"]
        self.assertEqual(
            (rules["test.alpha"]["reps"], rules["test.beta"]["reps"]),
            (3, 2),
            "the rerun must replace only the rule it ran",
        )
        self.assertEqual(
            sorted(self.ablate_keep("test-skill@*")),
            ["test.alpha", "test.beta"],
            "a rerun with more repetitions must not block the decision",
        )

    def test_user_keeps_a_finished_screen_without_rules(self) -> None:
        """user screens with every rule in the control, as for an external skill: Given a finished screen
        that measures no rule, When the user reruns it on the same model with --cases,
        Then the rerun stops, because the finished screen holds results."""
        both = "test-skill,test-lang"
        self.screen(
            "fake-follow",
            "--control-skills",
            both,
            "--all-cases",
            skills=both,
            tag="external",
        )
        self.assertTrue(
            self.report("screen-external@fake-follow.json")["checks"],
            "the fixture must measure checks",
        )
        rerun = self.screen(
            "fake-follow",
            "--control-skills",
            both,
            "--all-cases",
            "--cases",
            "c1",
            skills=both,
            tag="external",
            ok=False,
        )
        self.assertIn(
            "other settings",
            rerun.stderr,
            "a finished screen must bind its tag on its model",
        )

    def test_user_keeps_each_named_run_of_each_model_in_its_own_file(self) -> None:
        """user names the runs of a step: Given a full screen,
        When the user reuses its name for a screen of one case and names one step on two models,
        Then the reuse is refused, the full screen stays unchanged, and each model gets its own file."""
        self.screen("fake-follow")
        full = (self.results() / "screen-test-skill@fake-follow.json").read_text(
            encoding="utf-8"
        )
        for other in (("--cases", "c2"), ("--judge", "other")):
            refused = self.screen("fake-follow", *other, ok=False)
            self.assertIn(
                "other settings",
                refused.stderr,
                "the run must stop because of the first run's settings",
            )
        self.assertEqual(
            (self.results() / "screen-test-skill@fake-follow.json").read_text(
                encoding="utf-8"
            ),
            full,
            "a run with other settings must not overwrite the results of the first run",
        )
        for model in ("fake-follow", "fake-harm"):
            self.screen(model, tag="s1")
        self.assertEqual(
            sorted(p.name for p in self.results().glob("screen-s1@*.json")),
            ["screen-s1@fake-follow.json", "screen-s1@fake-harm.json"],
            "one name for a step must still give each model its own file",
        )

    def test_user_cannot_add_to_the_results_of_an_older_text(self) -> None:
        """user updates the skill: Given an ablation of the skill,
        When the user edits the skill and ablates under the same tag on the first and on a second model,
        Then both runs stop, and the criterion refuses to add up runs of the old and the new text
        under two tags."""
        self.ablate("fake-follow")
        skill = self.root / "skills" / "test-skill" / "SKILL.md"
        skill.write_text(
            SKILL.replace("- Write the word GAMMA. <!-- r:test.gamma -->\n", ""),
            encoding="utf-8",
        )
        for model in ("fake-follow", "fake-harm"):
            stale = self.ablate(model, "--rules", "test.alpha", ok=False)
            self.assertIn(
                "texts",
                stale.stderr,
                "the error must say that the skill or case texts changed",
            )
        self.ablate("fake-harm", tag="new")
        with self.assertRaisesRegex(SystemExit, "other settings or\\s+texts"):
            self.ablate_keep("test-skill@*", "new@*")

    def test_user_sees_untested_cases_instead_of_deletions(self) -> None:
        """user prunes the test cases: Given no results, and then a screen of only one case,
        When the user runs the case report with the glob that decide.py takes,
        Then it refuses to run without results or with a file of another format, and later
        marks the cases without results UNTESTED instead of DELETE."""
        done = self.run_tool(
            "evals/run.py", "cases", "--results", "test-skill@*", ok=False
        )
        self.assertIn(
            "no results",
            done.stderr,
            "without results the report must stop, otherwise it marks every case DELETE",
        )
        self.screen("fake-follow", "--cases", "c1")
        (self.results() / "screen-old@fake-follow.json").write_text(
            json.dumps({"format": 0, "checks": {}}), encoding="utf-8"
        )
        old = self.run_tool("evals/run.py", "cases", "--results", "old@*", ok=False)
        self.assertIn(
            "screen-old@fake-follow.json",
            old.stderr,
            "a file of another format must not keep or delete checks",
        )
        typo = self.run_tool(
            "evals/run.py", "cases", "--results", "test-skill@*", "tset@*", ok=False
        )
        self.assertIn(
            "tset@*", typo.stderr, "a mistyped glob must not let the report miss runs"
        )
        report = self.run_tool(
            "evals/run.py", "cases", "--results", "test-skill@*"
        ).stdout
        self.assertIn(
            "UNTESTED CASE",
            next(line for line in report.splitlines() if line.startswith("c2 ")),
            "a case without results must be UNTESTED",
        )
        self.assertNotIn(
            "DELETE CASE",
            report,
            "no case may be marked for deletion when its checks were not tested",
        )

    def test_user_never_deletes_a_global_check_through_a_probe_case(self) -> None:
        """user prunes the test cases: Given a probe case that tempts one pattern that the
        skill changes and one that it does not, When the user screens the skill and runs
        the case report, Then the probe case stays and no global check is marked DELETE."""
        self.screen("fake-follow")
        report = self.run_tool(
            "evals/run.py", "cases", "--results", "test-skill@*"
        ).stdout
        probe_rows = [line for line in report.splitlines() if line.startswith("p1/")]
        self.assertTrue(
            any("says-alpha" in line and "keep" in line for line in probe_rows),
            "a probed check that differs must keep the case",
        )
        self.assertFalse(
            [line for line in probe_rows if "no-delta" in line and "DELETE" in line],
            "a global check is shared by every case and must never be marked DELETE",
        )
        self.assertFalse(
            [
                line
                for line in report.splitlines()
                if line.startswith("p1 ") and "DELETE CASE" in line
            ],
            "the probe case must stay",
        )
