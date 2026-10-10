# Results of the 2026-10 rebuild

This update rebuilt the candidate rules and the test cases from the pinned upstream sources, and ran the method of [`../README.md`](../README.md) on two test models. This file records each decision and each trade-off.

The 584 results files are archived as [`evals-results-2026-10.tar.xz`](https://github.com/IceCodeNew/the-elements-of-style/releases/download/evals-2026-10/evals-results-2026-10.tar.xz). To rerun `decide.py` or `run.py cases` on them, extract the archive into this directory:

```bash
tar -xJf evals-results-2026-10.tar.xz -C evals/results --strip-components=1
```

## Setup

- Test models: `claude-opus-5-5` (Claude Code CLI) and `codex:gpt-6.1-sol:xhigh` (Codex CLI). Judge: `claude-sonnet-5-5`; fallback judge: `claude-opus-5-5`.
- Repetitions: 5 per case. A rule whose mean change on a model was between 0.1 and 0.3 was run again with 10 repetitions under the same tag.
- Candidate rules: 114, one for each candidate id in `maintenance/coverage.md`. The genre skills held 57 (`writing-tech`) and 44 (`writing-personal`) candidates, the language skills 19 (`writing-en`), 16 (`writing-ja`) and 12 (`writing-zh`).
- Test cases: 173 before the case ablation: 31 from the previous update, 130 harvested from eight sources, and 12 written for rules that no source example tested. Global checks: 42, of which 12 came from the harvest. A proposed check for decorative emoji was rejected, because emoji are a sign of machine authorship, not a writing fault.

Tags name the steps: `s1` screen, `s2` leave one out, `s3*` final checks of the genre skills, `s3w` and `s3x` wording comparisons, `s4` and `s4f` add-back tests, `l1` to `l4` the same steps for the language skills, `l2w` a wording comparison, and `z` and `zl` the last final checks with the final cases and checks.

## How the method was applied

- **Genre rules in cases that load a language skill.** A genre screen runs only the cases whose skills are a subset of the genre skill, so the genre-rule checks in cases that also load a language skill were not measured. Each genre screen and leave-one-out run therefore also ran on those cases, with the language skill in both variants (tags ending in `-in-<lang>`). `decide.py` reads them as separate rows of evidence.
- **Refused outputs.** In three outputs of the personal leave-one-out, `claude-opus-5-5` printed its planning notes before the post, and every judge refused them. They occur only in the variants without a rule, because those variants are far more numerous, not because of a rule. Counted as failures, each moved a rule's net by about +8. Without them, `both.no-empty-previews` falls from +1.40 to -6.85 and is dropped from `writing-personal`; `both.plain-words` and `pers.first-person` stay dropped.
- **Wrong checks.** The reviews of the outputs behind each drop found 61 wrong checks, fixed in four rounds before the runs that followed them. Most global checks did not say how to judge a line kept from a draft being edited, so the judge graded the same kept line both ways.
- **Rewordings.** After the final check, a final rule was reworded when its harm was larger than its leave-one-out net, or when it conflicted with a language rule. Each new wording was compared with the old one on the final skill, with 10 repetitions, and the better one kept. This was done once; smaller harms are recorded below as trade-offs.
- **Add-backs together.** Each add-back rule was tested alone, so the skills with all add-backs had another final check. It showed two harms that the single tests could not see (see "Add back").

## Final check

The final skill against the control, with the final cases and checks: the summed change in pass rate over all checks of the cases, with 5 repetitions. The control is no skill for the genre skills, and the final genre skill alone for the language skills. In the `-in-<lang>` rows, the candidate language skill is loaded in both variants.

| Comparison | Checks | `claude-opus-5-5` | `codex:gpt-6.1-sol:xhigh` |
|---|---|---|---|
| `writing-tech` | 2080 | +65.8 | +59.8 |
| `writing-tech`, cases that load `writing-en` | 659 | +7.2 | +6.2 |
| `writing-tech`, cases that load `writing-ja` | 396 | +3.2 | +1.0 |
| `writing-tech`, cases that load `writing-zh` | 434 | +1.0 | +2.2 |
| `writing-personal` | 1655 | +97.0 | +79.6 |
| `writing-personal`, cases that load `writing-en` | 524 | +9.6 | +7.4 |
| `writing-personal`, cases that load `writing-ja` | 225 | +1.4 | +2.2 |
| `writing-personal`, cases that load `writing-zh` | 173 | +5.4 | +9.6 |
| `writing-en` on `writing-tech` | 659 | +3.2 | +1.0 |
| `writing-en` on `writing-personal` | 524 | +2.6 | -2.0 |
| `writing-ja` on `writing-tech` | 396 | +8.4 | +7.6 |
| `writing-ja` on `writing-personal` | 225 | +3.6 | +4.8 |
| `writing-zh` on `writing-tech` | 434 | +4.4 | +1.6 |
| `writing-zh` on `writing-personal` | 173 | +10.2 | +4.2 |

`writing-en` adds little on top of a genre skill, and on `codex:gpt-6.1-sol:xhigh` with `writing-personal` slightly less than nothing. Its drops are single -0.4 to -0.6 entries on genre-rule checks that do not recur across models.

## Final skills

`writing-tech` keeps 32 of 57 candidates, `writing-personal` 14 of 44, `writing-en` 7 of 19, `writing-ja` 10 of 16 and `writing-zh` 5 of 12.

Each rule's outcome and the step that decided it. "Net" is the summed change over all checks of the rule's cases on both models; "effect on" names the models on which the rule's own checks showed an effect.

### writing-tech

| Rule | Final | Evidence |
|---|---|---|
| `both.answer-first-in-replies` | kept | leave one out: keep (net +2.70, effect on Opus) |
| `both.attribute-claims` | dropped | leave one out: drop (net -2.00, effect on Codex); add-back drop (net +0.50, effect on none) |
| `both.be-specific` | kept | leave one out: keep (net +4.00, effect on Codex, Opus) |
| `both.claims-match-evidence` | kept | leave one out: drop (net -6.40, effect on Codex); add-back keep (net +2.40, effect on Codex, Opus) |
| `both.cut-needless-words` | kept | leave one out: keep (net +4.80, effect on Codex) |
| `both.define-and-keep-terms` | kept | leave one out: keep (net +1.40, effect on Opus) |
| `both.facts-not-praise` | kept | leave one out: drop (net -2.60, effect on none); add-back keep (net +6.00, effect on Codex) |
| `both.keep-certainty` | dropped | dropped at the screen: no effect on either model |
| `both.keep-literals` | dropped | dropped at the screen: no effect on either model; add-back drop (net -0.20, effect on none) |
| `both.list-what-is-there` | dropped | leave one out: drop (net -1.80, effect on none); add-back drop (net -1.40, effect on Codex) |
| `both.lists-vs-prose` | kept | leave one out: keep (net +8.50, effect on Codex, Opus) |
| `both.literal-claims` | kept | leave one out: drop (net +2.00, effect on none); add-back keep (net +1.40, effect on Opus) |
| `both.match-house-and-voice` | dropped | dropped at the screen: no effect on either model |
| `both.merge-repeated-referents` | dropped | dropped at the screen: no effect on either model; add-back drop (net -2.20, effect on none) |
| `both.name-every-cause` | dropped | leave one out: drop (net -3.00, effect on none); add-back keep (net +0.60, effect on Codex); not added back: ordinal paragraphs with lists-vs-prose and point-first |
| `both.name-the-actor` | kept | leave one out: drop (net -2.50, effect on Codex, Opus); add-back keep (net +2.10, effect on Codex, Opus) |
| `both.name-the-relation` | kept | leave one out: keep (net +2.80, effect on Codex, Opus); reworded after the final check |
| `both.no-empty-previews` | kept | leave one out: keep (net +4.00, effect on Codex) |
| `both.no-phantom-objections` | kept | leave one out: keep (net +0.80, effect on Codex, Opus) |
| `both.one-reading` | kept | leave one out: keep (net +0.60, effect on Codex) |
| `both.one-topic-per-paragraph` | dropped | dropped at the screen: no effect on either model |
| `both.parallel-form` | dropped | leave one out: drop (net -0.60, effect on none); add-back drop (net -0.60, effect on Codex) |
| `both.plain-words` | dropped | leave one out: drop (net -4.60, effect on none); add-back drop (net -1.80, effect on none) |
| `both.positive-form` | kept | leave one out: keep (net +2.70, effect on Opus) |
| `both.real-contrasts` | dropped | leave one out: drop (net -3.20, effect on Opus); add-back drop (net -1.00, effect on Codex, Opus) |
| `both.revise-without-loss` | dropped | dropped at the screen: no effect on either model |
| `both.say-it-once` | kept | leave one out: keep (net +7.50, effect on Codex, Opus) |
| `both.scope-claims` | kept | leave one out: drop (net -2.00, effect on Opus); add-back keep (net +5.70, effect on Codex, Opus) |
| `both.separate-non-causes` | dropped | dropped at the screen: no effect on either model |
| `both.show-not-label` | kept | leave one out: drop (net -3.00, effect on none); add-back keep (net +7.50, effect on Codex) |
| `both.sparing-bold` | kept | leave one out: keep (net +8.20, effect on Codex, Opus) |
| `both.state-dont-stage` | dropped | leave one out: drop (net -4.00, effect on none); add-back drop (net +2.40, effect on none) |
| `both.state-the-mechanism` | kept | leave one out: drop (net -1.20, effect on Opus); add-back keep (net +1.40, effect on Codex, Opus) |
| `both.write-for-the-reader` | dropped | dropped at the screen: no effect on either model; add-back drop (net -0.50, effect on none) |
| `tech.condition-before-action` | kept | leave one out: keep (net +1.30, effect on Codex) |
| `tech.describe-current-state` | kept | leave one out: keep (net +3.30, effect on Opus) |
| `tech.established-terms` | kept | leave one out: keep (net +3.30, effect on Codex, Opus) |
| `tech.first-mention` | dropped | leave one out: drop (net -0.20, effect on none); add-back drop (net +1.20, effect on none) |
| `tech.format-conventions` | dropped | dropped at the screen: no effect on either model |
| `tech.heading-anchors` | dropped | leave one out: drop (net +0.20, effect on none); add-back keep (net +0.80, effect on Opus); removed after the add-back final check: it kept teaser headings |
| `tech.headings-name-content` | dropped | dropped at the screen: no effect on either model; add-back drop (net +1.50, effect on none) |
| `tech.identifiers-when-used` | kept | leave one out: keep (net +2.60, effect on Codex, Opus) |
| `tech.media-roles` | dropped | dropped at the screen: no effect on either model |
| `tech.neutral-register` | kept | leave one out: keep (net +1.20, effect on Codex, Opus); reworded after the final check |
| `tech.no-production-narration` | kept | leave one out: keep (net +1.30, effect on Opus) |
| `tech.no-stacked-headings` | dropped | leave one out: keep (net +1.60, effect on Codex, Opus); add-back drop (net +0.00, effect on none); neither wording passed on the final skill (old net -0.10, new +0.30 with no effect) |
| `tech.one-action-per-step` | kept | leave one out: keep (net +4.40, effect on Codex, Opus) |
| `tech.operation-state` | kept | leave one out: keep (net +0.20, effect on Codex) |
| `tech.plain-effect` | kept | leave one out: keep (net +0.60, effect on Opus) |
| `tech.point-first` | kept | leave one out: keep (net +3.30, effect on Codex, Opus); reworded after the final check |
| `tech.requirement-keywords` | kept | leave one out: keep (net +1.20, effect on Codex, Opus); reworded after the final check |
| `tech.scope-statement` | dropped | dropped at the screen: no effect on either model |
| `tech.short-sentences` | kept | dropped at the screen: no effect on either model; add-back keep (net +1.80, effect on Opus) |
| `tech.specific-change-summary` | dropped | dropped at the screen: no effect on either model |
| `tech.tool-limits` | dropped | leave one out: drop (net -3.20, effect on none) |
| `tech.vertical-lists` | dropped | dropped at the screen: no effect on either model |
| `tech.warning-placement` | kept | leave one out: keep (net +3.80, effect on Codex, Opus) |

### writing-personal

| Rule | Final | Evidence |
|---|---|---|
| `both.answer-first-in-replies` | kept | leave one out: keep (net +1.20, effect on Codex) |
| `both.attribute-claims` | dropped | leave one out: drop (net -1.50, effect on Codex); add-back drop (net +0.60, effect on none) |
| `both.be-specific` | dropped | dropped at the screen: no effect on either model; add-back drop (net +0.40, effect on none) |
| `both.claims-match-evidence` | dropped | dropped at the screen: no effect on either model |
| `both.cut-needless-words` | dropped | leave one out: drop (net -3.30, effect on Codex); add-back drop (net -0.70, effect on none) |
| `both.define-and-keep-terms` | kept | leave one out: keep (net +0.20, effect on Codex) |
| `both.facts-not-praise` | kept | leave one out: keep (net +0.40, effect on Codex) |
| `both.keep-certainty` | kept | leave one out: keep (net +3.00, effect on Opus) |
| `both.keep-literals` | dropped | dropped at the screen: no effect on either model |
| `both.list-what-is-there` | dropped | leave one out: drop (net +0.60, effect on none); add-back drop (net +2.40, effect on none) |
| `both.lists-vs-prose` | dropped | leave one out: drop (net +0.70, effect on none); add-back drop (net +0.60, effect on none) |
| `both.literal-claims` | dropped | leave one out: drop (net +3.60, effect on none); add-back drop (net +2.80, effect on none) |
| `both.match-house-and-voice` | dropped | dropped at the screen: no effect on either model; add-back keep (net +0.10, effect on Codex); add-backs not kept: no aggregate gain, staged emphasis kept |
| `both.merge-repeated-referents` | dropped | leave one out: drop (net -3.40, effect on none); add-back drop (net -0.40, effect on Codex) |
| `both.name-every-cause` | kept | leave one out: keep (net +1.60, effect on Codex, Opus) |
| `both.name-the-actor` | dropped | leave one out: drop (net +1.00, effect on none); add-back drop (net +0.80, effect on none) |
| `both.name-the-relation` | dropped | dropped at the screen: no effect on either model |
| `both.no-empty-previews` | dropped | leave one out: keep (net +1.40, effect on Codex); add-back drop (net -1.80, effect on Codex); the step-2 keep rested on outputs that printed planning notes; dropped |
| `both.no-phantom-objections` | kept | leave one out: keep (net +2.10, effect on Codex, Opus) |
| `both.one-reading` | dropped | dropped at the screen: no effect on either model |
| `both.one-topic-per-paragraph` | kept | leave one out: keep (net +1.10, effect on Codex) |
| `both.parallel-form` | dropped | leave one out: drop (net -1.20, effect on Opus); add-back drop (net -0.10, effect on Opus) |
| `both.plain-words` | dropped | leave one out: drop (net +8.80, effect on none); add-back drop (net -3.40, effect on none) |
| `both.positive-form` | kept | leave one out: keep (net +0.80, effect on Codex, Opus) |
| `both.real-contrasts` | dropped | leave one out: drop (net -9.80, effect on none); add-back drop (net -5.80, effect on Codex) |
| `both.revise-without-loss` | dropped | dropped at the screen: no effect on either model |
| `both.say-it-once` | dropped | leave one out: drop (net -0.60, effect on Codex); add-back drop (net -4.60, effect on Codex) |
| `both.scope-claims` | dropped | leave one out: drop (net -1.60, effect on Opus); add-back keep (net +0.60, effect on Opus); add-backs not kept: no aggregate gain, staged emphasis kept |
| `both.separate-non-causes` | dropped | leave one out: drop (net +0.50, effect on none); add-back drop (net -0.60, effect on none) |
| `both.show-not-label` | kept | leave one out: keep (net +0.40, effect on Codex, Opus) |
| `both.sparing-bold` | dropped | leave one out: drop (net +1.20, effect on none); add-back drop (net -1.60, effect on none) |
| `both.state-dont-stage` | kept | leave one out: keep (net +16.20, effect on Codex, Opus); reworded twice |
| `both.state-the-mechanism` | dropped | leave one out: drop (net -3.00, effect on none); add-back drop (net +0.40, effect on none) |
| `both.write-for-the-reader` | dropped | leave one out: drop (net -1.10, effect on Codex); add-back keep (net +0.70, effect on Codex, Opus); add-backs not kept: no aggregate gain, staged emphasis kept |
| `pers.end-on-the-point` | kept | leave one out: keep (net +2.60, effect on Opus); reworded |
| `pers.first-person` | dropped | leave one out: drop (net +10.20, effect on none); add-back drop (net +0.80, effect on none) |
| `pers.keep-author-voice` | dropped | leave one out: drop (net -12.80, effect on Codex, Opus); add-back drop (net -12.40, effect on Codex, Opus) |
| `pers.keep-mixed-feelings` | dropped | dropped at the screen: no effect on either model |
| `pers.no-invented-reactions` | kept | leave one out: keep (net +2.20, effect on Codex, Opus) |
| `pers.no-signposts` | dropped | leave one out: drop (net -0.60, effect on none); add-back drop (net -1.60, effect on Codex) |
| `pers.reader-in-scene` | kept | leave one out: keep (net +1.30, effect on Codex, Opus) |
| `pers.rhythm-follows-content` | dropped | leave one out: keep (net +1.70, effect on Codex); add-back drop (net -0.20, effect on none); failed on the final skill with fixed checks (old -1.3, new -0.7) |
| `pers.specific-admission` | kept | leave one out: keep (net +11.10, effect on Codex, Opus) |
| `pers.state-the-view` | dropped | leave one out: drop (net +2.20, effect on none); add-back drop (net -3.60, effect on none) |

### writing-en

| Rule | Final | Evidence |
|---|---|---|
| `en.caps-emphasis` | dropped | dropped at the screen: no effect on either model |
| `en.complete-sentences` | kept | leave one out: drop (net -0.00, effect on Opus); add-back keep (net +4.60, effect on Opus) |
| `en.copula-verbs` | dropped | leave one out: drop (net -1.10, effect on none); add-back drop (net -1.00, effect on none) |
| `en.empty-emphasis` | dropped | leave one out: drop (net -1.60, effect on Codex, Opus); add-back keep (net +0.20, effect on Codex); not added back: six side drops of -0.4 to -0.8 |
| `en.heading-case` | kept | leave one out: keep (net +2.40, effect on Codex, Opus) |
| `en.hyphenation` | kept | leave one out: keep (net +2.00, effect on Codex, Opus) |
| `en.ing-clauses` | dropped | dropped at the screen: no effect on either model |
| `en.ing-rider` | dropped | dropped at the screen: no effect on either model |
| `en.literal-verbs` | dropped | dropped at the screen: no effect on either model |
| `en.noun-clusters` | kept | leave one out: keep (net +0.90, effect on Opus) |
| `en.paragraph-length` | dropped | dropped at the screen: no effect on either model |
| `en.plain-words` | kept | leave one out: keep (net +1.50, effect on Opus) |
| `en.real-actor` | dropped | dropped at the screen: no effect on either model |
| `en.sentence-length` | kept | leave one out: drop (net -0.60, effect on none); add-back keep (net +0.80, effect on Codex) |
| `en.spec-modals` | dropped | leave one out: drop (net +0.00, effect on none) |
| `en.tense-by-event` | dropped | dropped at the screen: no effect on either model; add-back drop (net +0.80, effect on none) |
| `en.tool-phrasal-verbs` | dropped | dropped at the screen: no effect on either model |
| `en.unambiguous-conjunctions` | dropped | dropped at the screen: no effect on either model |
| `en.usage-reference` | kept | leave one out: keep (net +0.80, effect on Codex, Opus) |

### writing-ja

| Rule | Final | Evidence |
|---|---|---|
| `ja.calque-verbs` | kept | leave one out: keep (net +0.50, effect on Opus) |
| `ja.empty-phrase-forms` | dropped | leave one out: drop (net -0.80, effect on Codex, Opus); add-back drop (net -1.20, effect on Codex, Opus) |
| `ja.i-adjective-desu` | kept | leave one out: keep (net +2.80, effect on Codex) |
| `ja.inanimate-subject` | dropped | dropped at the screen: no effect on either model |
| `ja.judgment-form` | kept | leave one out: keep (net +5.20, effect on Codex, Opus) |
| `ja.kagi-quotes` | kept | leave one out: keep (net +3.80, effect on Codex, Opus) |
| `ja.name-the-thinker` | kept | leave one out: keep (net +5.40, effect on Codex, Opus) |
| `ja.no-anata` | kept | leave one out: keep (net +1.00, effect on Opus) |
| `ja.one-hedge` | kept | leave one out: keep (net +1.60, effect on Codex, Opus) |
| `ja.person-names` | kept | leave one out: keep (net +2.20, effect on Codex, Opus) |
| `ja.plain-predicates` | kept | leave one out: keep (net +3.10, effect on Codex, Opus) |
| `ja.spoken-jargon` | dropped | dropped at the screen: no effect on either model |
| `ja.subject-inheritance` | dropped | dropped at the screen: no effect on either model |
| `ja.taigen-dome` | dropped | dropped at the screen: no effect on either model |
| `ja.type-before-modifiers` | kept | leave one out: keep (net +2.00, effect on Codex) |
| `ja.weak-ga` | dropped | dropped at the screen: no effect on either model |

### writing-zh

| Rule | Final | Evidence |
|---|---|---|
| `zh.background-opener` | kept | leave one out: keep (net +2.30, effect on Codex); new example: it no longer models a preview |
| `zh.bei-passive` | kept | leave one out: keep (net +0.90, effect on Codex, Opus) |
| `zh.dash-form` | dropped | dropped at the screen: no effect on either model |
| `zh.de-chain` | kept | leave one out: keep (net +0.20, effect on Opus) |
| `zh.four-char` | dropped | dropped at the screen: no effect on either model |
| `zh.full-width-punct` | kept | leave one out: keep (net +1.70, effect on Opus) |
| `zh.jinxing-verb` | kept | leave one out: keep (net +2.80, effect on Codex, Opus) |
| `zh.plain-words` | dropped | dropped at the screen: no effect on either model |
| `zh.significance-tail` | dropped | dropped at the screen: no effect on either model |
| `zh.state-markers` | dropped | leave one out: drop (net +2.00, effect on none); add-back drop (net +0.40, effect on none) |
| `zh.stock-closing` | dropped | leave one out: drop (net +1.00, effect on none); add-back drop (net -0.20, effect on none) |
| `zh.subject-omission` | dropped | dropped at the screen: no effect on either model |

## Rewordings

Net change and the models with an effect, on the final skill, with 10 repetitions.

| Rule | Harm of the old wording | Old | New | Kept |
|---|---|---|---|---|
| `tech.no-stacked-headings` | A sentence that only previews the subsections | -0.10 (Opus) | +0.30 (none) | neither; dropped |
| `both.state-dont-stage` (personal) | Flattened a climax fragment; cut the author's joke run | +10.9 | +16.1 | new |
| `pers.end-on-the-point` | Kept a closing moral as the verdict | +16.0 (Opus) | +16.6 (both) | new |
| `tech.point-first` | A summary lead that the body repeats | +2.3 | +4.7 | new |
| `tech.requirement-keywords` | Codex avoided lowercase "may" and "must" in a spec without RFC 2119 | +1.2 | +0.6 (Opus) | new: the conflict with `en.spec-modals` went from -1.0 to -0.2 and -0.4 |
| `both.name-the-relation` | Replaced an explaining dash; recast significance riders | +4.0 | +6.2 | new |
| `tech.neutral-register` | Kept intensifiers in academic edits | +1.2 | +1.5 | new |
| `tech.no-production-narration` | Cut a source credit | +3.8 (Opus) | +2.6 (Opus) | old: Codex drops the credit with both |
| `both.show-not-label` (personal) | Replaced labels with popularity claims | +6.8 | +2.3 | old |
| `pers.specific-admission` | Added a consequence that the material does not give | +4.7 | +2.5 | old: the harm remained |
| `pers.rhythm-follows-content` | Broke a deliberate Chinese parallel | -1.3 | -0.7 | neither; dropped |
| `zh.background-opener` | Its example ended in a preview ("本文介绍…") | +3.5 | +3.5 | new: fewer previews on Opus, more empty openers cut on Codex |

## Add back

Candidates were the dropped rules with a check at -0.4 or worse in the final check or at +0.4 or better in the screen: 22 in `writing-tech`, 24 in `writing-personal`, and 8 in the language skills. The fixes of the add-back reviews changed the grades of some kept rules, so those were graded again (tags `s4f`).

- `writing-tech` added back 9 rules: `both.claims-match-evidence`, `both.facts-not-praise`, `both.literal-claims`, `both.name-the-actor`, `both.scope-claims`, `both.show-not-label`, `both.state-the-mechanism`, `tech.short-sentences` and, for one round, `tech.heading-anchors`. The final check with all add-backs showed that `tech.heading-anchors` makes models keep a draft's teaser headings to avoid breaking links (10 checks fell, 1 rose). Its gain was +0.8 on one model, so it was removed. `both.name-every-cause` passed (+0.6) but, with `both.lists-vs-prose` and `tech.point-first`, made models write ordinal paragraphs in 7 of 10 outputs against 0 of 10; it was not added back.
- `writing-personal` added back none. Three rules passed alone (+0.1, +0.6 and +0.7), but together they gave no gain in the final check, and staged emphasis rose in 8 checks on both models.
- `writing-en` added back `en.complete-sentences` (+4.6) and `en.sentence-length` (+0.8). `en.empty-emphasis` passed at +0.2 with six side drops of -0.4 to -0.8, and dropped at -1.6 in leave-one-out; it was not added back.

## Accepted trade-offs

Each of these rules keeps a net gain with a smaller harm that the reviews confirmed in the outputs:

- `both.no-empty-previews`, `both.sparing-bold`, `both.define-and-keep-terms` and `both.cut-needless-words` (tech): occasional lost lead-ins, counts or bold labels.
- `tech.no-production-narration`: `codex:gpt-6.1-sol:xhigh` drops a price-source credit (-0.8).
- `pers.end-on-the-point`, `both.keep-certainty`, `both.no-phantom-objections` (personal): weak, single-case harms.
- `en.complete-sentences`: on one case, `claude-opus-5-5` turns "not much confidence" into "distrusted" in 3 of 5 outputs.
- `ja.plain-predicates`: keeps an empty 「を行う」 in one case.
- On `claude-opus-5-5`, Japanese technical cases show more repetition with `writing-tech` (`trope-repetition` -0.2 to -0.6 in six cases), and a Chinese deliberate parallel is broken in one case (-0.8).
- `en.spec-modals` is masked by `tech.requirement-keywords` on `claude-opus-5-5` and overridden by `writing-tech` on `codex:gpt-6.1-sol:xhigh`; it was dropped.

## Test cases

`run.py cases --results '2026-10-*'` against the final skills deleted 698 case checks and 32 cases. 397 of the deleted checks tested rules that the final skills do not hold; 301 never moved by 0.4. Six checks that caught a harm of a final rule were kept and tagged with that rule. 141 cases remain, with 224 case checks; 18 of them are kept only by the global checks that they probe. Every final rule has at least one case check.

## Not measured

- One judge family grades both test models.
- Each comparison has 5 repetitions, or 10 for a mean between 0.1 and 0.3; single-repetition differences (0.2) were not read.
- Harms on cases that do not test a rule show only in a final check, which does not attribute them to one rule.
