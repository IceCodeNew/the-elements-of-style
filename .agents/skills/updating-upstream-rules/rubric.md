# Audit rubric

Tag every upstream rule with exactly one destination, in the audit file of its source (`maintenance/audits/<source>.md`).

## Skills

| Skill | Holds |
|---|---|
| `writing-tech` | Rules for good technical text in every language: docs, READMEs, runbooks, procedures, code comments, commit messages, PR descriptions, error, log, CLI and UI text, postmortems, design docs, technical articles and books |
| `writing-personal` | Rules for good personal text in every language: blog posts, essays, newsletters, social posts |
| `writing-en`, `writing-ja`, `writing-zh` | Rules that hold only in that language |

A test source (`used_by: ["evals"]` in `maintenance/upstreams.json`) is audited with the same tags. Its rows also name the candidate rule that each counter-example tests.

## Destinations

- `BOTH`: good writing in both genres and every language. It goes into `writing-tech` and `writing-personal`.
- `TECH`: good writing in every language, for technical text only.
- `PERSONAL`: good writing in every language, for personal writing only.
- `EN`, `JA`, `ZH`: the rule depends on that language's words, punctuation, grammar (tense, articles, particles, measure words, word order), typography or conventions. Add `/TECH` or `/PERSONAL` if it also depends on the genre.
- `X-DEAI`: excluded. The rule's purpose is to hide signs of machine authorship. It would not improve a text that a careful human wrote, or careful writers use the flagged form legitimately (rule-of-three counts, dash counts, emoji, "Certainly!", curly quotes).
- `X-DUP`: excluded, because another rule says the same thing. Name it.
- `X-SCOPE`: excluded, because it is about the upstream's process, tooling, scoring or output format, not about writing.

## Tests, in order

1. **Good writing or de-AI?** Ask: "Would this rule improve a text that a careful human wrote?" If not, tag `X-DEAI`. A rule can start from an AI tell and still be good writing: empty preview phrases, vague attributions and inflated significance make any text worse.
2. **Language-independent?** Check the rule against English, Japanese and Chinese norms. If it names one language's words, punctuation or grammar, or conflicts with another language's norm, it is language-specific. A universal principle with language-specific examples is universal; move the examples to the language skill.
3. **Genre?** Check it against technical-documentation norms and against personal-writing norms.
4. **Absolute wording?** If the source says "never" or "always" and the rule has exceptions, write the conditional form, keyed to something the writer can observe.
5. **Conflict?** If two sources disagree, the rule is usually language- or genre-specific. Name both sides and the classification that resolves it.

## Row format

A row ID is the source's prefix of two or three capital letters, a hyphen, and a local number or name, such as `BH-P20a` or `SS-ST35`. `maintenance/check_upstreams.py` finds rows by this form.

| ID | Source location | Rule (short paraphrase) | Destination | Reason (one clause) | Conditional wording / notes |
|---|---|---|---|---|---|

One row per source rule of the pinned version, in source order; never merge rows. For an update, add rows for new rules, edit rows for changed rules, and delete the rows of rules that the new version removed.
