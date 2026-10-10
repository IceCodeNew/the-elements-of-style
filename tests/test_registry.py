"""Tests of the offline consistency check of the upstream registry.

Run from the repository root:

    python3 -m unittest discover -s tests -t . -v
"""

from __future__ import annotations

import unittest

from tests.helpers import REPO, load

check = load("check_upstreams", REPO / "maintenance" / "check_upstreams.py")

PIN = "a" * 40
FIXTURE = check.Repository(
    registry=[{"id": "src", "pinned": PIN, "used_by": ["writing-tech"]}],
    skills={
        "writing-tech": f"- [src](https://example.org) @ `{PIN}`\n- Keep it short. <!-- r:tech.short -->\n"
    },
    audits={
        "src.md": "| ID | Source | Rule | Destination |\n|---|---|---|---|\n| SR-01 | L1 | short | TECH |\n"
    },
    coverage="| Row | Audit destination | Outcome |\n|---|---|---|\n| SR-01 | TECH | kept as `tech.short` in `writing-tech` |\n",
)


class Registry(unittest.TestCase):
    def test_user_finds_the_registry_in_agreement_with_the_repository(self) -> None:
        """maintainer updates a source: Given the registry, the skills, the audits and coverage.md,
        When the offline consistency check runs, Then it finds no disagreement."""
        self.assertEqual(
            check.consistency_errors(check.load_repository()),
            [],
            "the registry must match the skills, audits and coverage",
        )

    def test_user_finds_no_error_in_a_consistent_fixture(self) -> None:
        """maintainer checks a small repository: Given a source cited by the one skill that uses it,
        When the check runs, Then it reports no error."""
        self.assertEqual(
            check.consistency_errors(FIXTURE),
            [],
            "the fixture must be consistent, otherwise the negative tests prove nothing",
        )

    def test_user_sees_a_used_by_that_misses_a_citing_skill(self) -> None:
        """maintainer adds a rule to another skill: Given a second skill that cites the pin,
        When the check runs, Then it reports that used_by misses that skill."""
        repo = FIXTURE._replace(skills={**FIXTURE.skills, "writing-en": f"@ `{PIN}`"})
        self.assertIn(
            "used_by",
            " ".join(check.consistency_errors(repo)),
            "a skill that cites a pin must be in used_by",
        )

    def test_user_sees_a_sha_that_is_not_a_pin(self) -> None:
        """maintainer forgets to update a source list: Given a skill that cites an old SHA,
        When the check runs, Then it reports the SHA."""
        old = "b" * 40
        repo = FIXTURE._replace(
            skills={
                "writing-tech": FIXTURE.skills["writing-tech"] + f"- old @ `{old}`\n"
            }
        )
        self.assertIn(
            old,
            " ".join(check.consistency_errors(repo)),
            "a cited SHA must be a pin in the registry",
        )

    def test_user_sees_a_missing_and_an_extra_coverage_row(self) -> None:
        """maintainer edits an audit: Given an audit row without a coverage row, and a coverage
        row without an audit row, When the check runs, Then it reports both with their row ids."""
        audits = {
            "src.md": FIXTURE.audits["src.md"] + "| SR-02 | L2 | plain | TECH |\n"
        }
        self.assertIn(
            "SR-02",
            " ".join(check.consistency_errors(FIXTURE._replace(audits=audits))),
            "an audit row needs a coverage row",
        )
        coverage = (
            FIXTURE.coverage
            + "| SR-09 | TECH | kept as `tech.short` in `writing-tech` |\n"
        )
        self.assertIn(
            "SR-09",
            " ".join(check.consistency_errors(FIXTURE._replace(coverage=coverage))),
            "a coverage row needs an audit row",
        )

    def test_user_sees_a_kept_rule_that_left_the_skills(self) -> None:
        """maintainer drops a rule: Given coverage.md that still says the rule was kept,
        When the check runs, Then it reports the rule."""
        repo = FIXTURE._replace(skills={"writing-tech": f"@ `{PIN}`\n"})
        self.assertIn(
            "tech.short",
            " ".join(check.consistency_errors(repo)),
            "a rule that coverage.md keeps must be in a skill",
        )


if __name__ == "__main__":
    unittest.main()
