---
name: updating-upstream-rules
description: "Use when updating the writing skills or their test cases in this repository from third-party sources (obra/the-elements-of-style, op7418/Humanizer-zh, blader/humanizer, stop-slop, tropes.fyi, ninehills/skills deslop, Wikipedia \"Signs of AI writing\", japanese-tech-writing, ASD-STE100), when a source has a new commit, release, revision or version, when a new source of rules or counter-examples is proposed, or when someone asks whether an external writing skill would improve these skills."
---

# Updating upstream rules

## Overview

The skills in `skills/` adapt rules from third-party sources, and the tests in `evals/` use examples from more sources. Two records keep them honest: every upstream rule has an audit row that says where it went and why, and every rule in a skill passed an ablation test. An update keeps both records true and names the exact upstream versions in each skill.

`used_by` in `maintenance/upstreams.json` marks each source as one of two kinds:

- A **rule source** (`used_by` names skills): its rules can enter the skills.
- A **test source** (`used_by: ["evals"]`): an anti-pattern catalog or a skill that removes signs of AI writing. Its rules are `X-DEAI` and never enter the skills. Its examples become test cases and global checks.

**Do every step, even when the request says "keep it quick".** An update without the audit or the ablation ships unmeasured rules. If time is short, update fewer sources completely, and say which ones wait.

## Files

| File | Role |
|---|---|
| `maintenance/upstreams.json` | Every source: pinned version, license, `used_by`, and `via` (the source that led to it) |
| `maintenance/check_upstreams.py` | Checks that the registry agrees with the skills, audits and coverage table (`--offline` for only this part), then compares each pin with the latest version |
| `maintenance/audits/<source>.md` | One row per upstream rule, with its destination and reason |
| `maintenance/coverage.md` | The final outcome of every audit row: the skill rule that kept it, the cases that test it, or why it was dropped |
| `evals/README.md` | The ablation method and the decision criterion |
| `evals/run.py`, `evals/decide.py` | Ablation harness, and the keep/drop decision across test models |
| `tests/` | Behavior tests of the harness and the registry; run them after a change to `evals/` code or `maintenance/` |
| `evals/cases/*.json`, `evals/global-checks.json`, `evals/results/` | Test cases, anti-pattern checks applied to every output, results |
| `rubric.md` (next to this file) | Destination tags and the tests for each audit row |
| `rule-writing.md` (next to this file) | How to word a rule and a test case |

## Procedure

Create a todo for each step.

1. **Branch.** Start from the updated default branch: `git switch -c chore/upstream-sync-<date>`. All work goes to a pull request; never commit to the default branch.
2. **Ask for the test models.** Ask the owner which models the tests run on (`--model` of `evals/run.py`). Recommend at least two models from different vendors: a rule that helps one model can show no effect on another. Start no test run before the owner names the models; do the steps that need no model meanwhile.
3. **Check every source.** Run `python3 maintenance/check_upstreams.py`. It first checks that the registry agrees with the skills, the audits and the coverage table; fix every `INVALID` line. Then it checks all registry entries, including sources of sources (`via`). For a `manual` entry, do the check in its note: download the file and compare its sha256 with the pin. A request that names one or two sources does not limit this step.
4. **Verify claims.** Confirm each claimed release, version or merge on the source itself (`gh release view`, `gh pr view --json state,mergedAt`, the downloaded file). An open PR is not part of the upstream.
5. **Find new sources and originals.** For each changed or proposed source, read its credits (README, SKILL.md frontmatter and source list, LICENSE) at the new version.
   - A credited source that is not in the registry gets an entry with `via`, a pin, and a full audit.
   - If a source says that it copies another skill, compare the copy with the original repository. If the original is newer, pin and use the original. Exclude each copied file that repeats content this repository does not use, such as an older version of a registered source, and say so in the entry's `note`.
   - Set `used_by: ["evals"]` for a test source.
   - Pin a web page that has no commits as a `manual` entry: the sha256 of the downloaded file, the date, and a `check` note that says how to download it.
   - Read the license before quoting examples. If it does not allow copying, paraphrase the example.
6. **Diff.** For each changed source, diff the pinned version against the new one (`git diff <pinned>..<new>`, the gist revisions, the Wikipedia diff URL that the script prints, `diff -u` of downloaded files). List every added, changed and removed rule and example.
7. **Remove what the new version dropped.** The audits, cases and skills follow only the pinned version of each source. When a new version drops a rule or an example, or replaces the whole source (a catalog's v3 replacing v2), delete what only the old version had: its audit rows and the coverage rows that cite them, its checks, global checks and cases, and each skill rule that no other source supports. Do not keep an item because it still looks useful: the source removed it on purpose. Then move the pin, the credits and the license notices to the new version (step 14).
8. **Audit.** Add or update one row per changed rule in `maintenance/audits/<source>.md`. Follow `rubric.md`:
   - A rule whose purpose is to hide signs of machine authorship gets `X-DEAI`. It never goes into `writing-tech` or `writing-personal`.
   - A rule that depends on one language's words, grammar, punctuation or conventions goes to that language's skill only.
   - A rule that holds in every language goes to a genre skill: `TECH`, `PERSONAL` or `BOTH`.
   - A conflict between two sources, or with an existing rule, means the rule is language- or genre-specific. Classify it that way.
   - Audit test sources too. Each row names the candidate rule that its counter-example tests.
9. **Write rules.** Merge a change into the existing rule that covers its principle. Write a new rule only for a new principle. Follow `rule-writing.md`: state a condition the writer can observe instead of an absolute, and give each rule a marker `<!-- r:<id> -->`. Also re-test a rule that an earlier ablation dropped if the change gives it new support.
10. **Write test cases.** Harvest every example in every new or changed source, test sources included: bad and good pairs, before-and-after rewrites, examples the source says to keep, and fixtures. Each example lands in a check, or in the source's coverage list with the reason it was skipped. Follow `rule-writing.md`:
    - Put bad examples into a realistic draft to edit, with every fact the draft needs.
    - Use the examples a source keeps, and any upstream rewrite that invents facts or drops a real contrast, as checks against over-application.
    - An anti-pattern that can appear in any text goes into `evals/global-checks.json`, tagged with the candidate rule that prevents it. Add a probe case that tempts it, with `"probe": ["<global check id>"]`.
    - Then add cases for failures that no source shows.
11. **Ablate rules.** Follow the four steps in `evals/README.md` on every test model: screen, leave one out, final check, add back. The genre skills are tested first; the language skills are then tested on top of the final genre skills. Run tests only through `evals/run.py`: it runs each model in a temporary session that loads no user settings, plugins, skills, hooks or MCP servers.
    - Name the runs with `--tag`: one tag for one step of the update on each model, such as `2026-10-s1-tech` for the screen of `writing-tech`, and one tag for each add-back rule. The harness adds `@<model>`. Give `decide.py` one tag per skill set, check that its `READ` line lists every test model, and decide the shared rules of each genre skill on their own.
    - Keep or drop each rule by the criterion in `evals/README.md`; `python3 evals/decide.py` applies it to the results of all test models. Repeat a result between 0.1 and 0.3 with `--reps 10`.
    - Commit the results files, and record each decision and trade-off in `evals/results/README.md`.
    - Drop a rule with no measured effect. Every rule costs context each time the skill loads, and an unmeasured rule can mask or undo a measured one.
    - Read the outputs (`python3 evals/run.py inspect ...`) behind every check that does worse than the control. Fix a wrong check, or reword or drop the rule that causes the drop.
    - For a changed rule, ablate the old wording against the new wording too, and keep the better one.
    - Do not edit any `SKILL.md` while an experiment runs: the harness reads the files again for every variant.
    - If a run stops on a usage limit, rerun the same command: the cache keeps the finished outputs. A refusal by the judge goes to the fallback judge. An output that the writer or every judge refuses fails its checks, and `decide.py` marks the decisions that it touches with `REVIEW refused`: read those outputs before you record the decision.
12. **Ablate test cases.** When every screen and ablation of this update has written its results, run `python3 evals/run.py cases --results '<glob>'...` with the globs of every run of this update, such as `'2026-10-*'`. Delete each check marked `DELETE`, and each case marked `DELETE CASE`. A check marked `UNTESTED` has no result yet: run the comparison that tests it, then run the report again. Global checks are scored on every case but never delete a case. A check that detects a harmful interaction between rules is kept: tag it with the rule whose behavior it tests.
13. **Update the coverage table.** Edit the rows of `maintenance/coverage.md` for every added, changed or removed upstream rule. A test source's rows name the cases that use its examples.
14. **Update credits and licenses.** Set the new version in the source list at the top of each affected `SKILL.md`, and set `pinned` and `pinned_date` in `upstreams.json`. Keep the license notice files (`NOTICE.md` in each skill directory and in `evals/`) complete for adapted or quoted content.
15. **Regenerate manifests.** Run `npx everyharness@1.0.0 generate`, then `npx everyharness@1.0.0 validate`. Never edit a file with the `GENERATED by everyharness` header by hand. `.claude-plugin/marketplace.json` is hand-written: update it when a skill is added or renamed, and bump the versions.
16. **Commit and open the PR.** Use signed commits (`git commit -S`) with Conventional Commits messages, one commit per source or per skill. Push the branch and open a draft PR. The PR body lists the test models, the old and new pin of each source, the audit rows added, the rules added, changed and dropped with their ablation numbers per model, the cases added and deleted, and anything not verified.

## Evaluating an external skill

When someone asks whether another writing skill would improve these skills:

1. Take its latest version from its original repository (step 5). Do not register it yet.
2. In a scratch copy of the repository, put the skill and the reference files it names in `skills/<name>/`. On every test model, run the cases of its language and genre with and without it: `python3 evals/run.py screen --skills <ours>,<name> --control-skills <ours> --all-cases --tag <name> --model <model>`, where `<ours>` is the genre skill plus the language skill.
3. If the summed change over all checks is not positive on any test model, record the numbers in `evals/results/README.md` and stop.
4. Otherwise register it as a rule source and audit its rules (step 8). Add each rule that no existing rule covers to the final skill on its own, and test it as in the add-back step. Never add the skill whole.

## Red flags

| Thought | Reality |
|---|---|
| "Just copy the new patterns in." | Each upstream rule needs an audit row and each kept rule an ablation result. |
| "Only the sources the owner named changed." | Run the check on every registry entry. Sources of sources change too. |
| "The owner said it was released or merged." | Verify it on the source. |
| "The old version had a useful item that the new one dropped." | Delete it. The source removed it on purpose. |
| "The rule is neutral, so keeping it is harmless." | Drop it. In this repository, removing rules without an effect also removed regressions that they caused. |
| "This upstream rule is a good AI tell." | Tells are `X-DEAI`. The genre skills hold rules that make any careful writer's text better. |
| "De-AI rules are excluded, so their examples do not matter." | Their examples are test material: cases, global checks and over-application guards. |
| "The copy in this collection is the source." | Compare it with the original repository and use the newer one. |
| "One model is enough." | Recommend several. A rule can help one model and do nothing for another. |
| "The external skill looks good, so add it." | Compare the skills with and without it first, then test its rules one by one. |
| "The upstream says 'never', so the rule says 'never'." | Write the condition under which it holds. |
| "A small fix to plugin.json is faster than regenerating." | Generated files are overwritten and fail `validate`. Edit `everyharness.yaml`. |
| "It is a quick update, so push to the default branch." | Every update goes through a PR. |
