# Writing rules and test cases

## A rule

- One rule is one bullet: one to three sentences, plus at most one short example. Name the behavior to produce. Use a prohibition only for something that writers do while they know better.
- State a real exception as its own conditional, keyed to something the writer can observe: "If the tool names the operation with a phrasal verb, use that verb." Do not append clauses such as "unless it matters"; they make the rule negotiable.
- Write rules for `writing-tech`, `writing-personal` and `writing-en` in English, `writing-ja` rules in Japanese, and `writing-zh` rules in Chinese.
- The rule text follows the rules it states: plain words, concrete, no filler.
- End the bullet with a marker that the ablation harness uses: `<!-- r:<prefix>.<slug> -->`. Prefixes: `both`, `tech`, `pers`, `en`, `ja`, `zh`. A rule shared by both genre skills has the same id in both files.

## A test case

Cases are JSON objects in a list in `evals/cases/<skill>.json`:

```json
{
  "id": "tech-postmortem-causes",
  "skills": ["writing-tech"],
  "source": "audit row ids, or 'new'",
  "prompt": "The full task, with all facts. End with an output instruction such as 'Output only the section.'",
  "checks": [
    {"id": "names-every-cause", "rule": "both.name-every-cause", "kind": "judge", "text": "Does the output name each of the three causes in the facts?"},
    {"id": "no-delve", "rule": "en.plain-words", "kind": "absent", "text": "(?i)\\bdelve"}
  ]
}
```

- `skills`: the skill set to load. A genre-rule case loads one genre skill. A language-rule case loads a genre skill and the language skill.
- `kind`: `judge` (a yes/no question for the grader model, true = good), `absent` (a Python regex that must not match), or `present` (a regex that must match).
- Each check tests one rule, named in `rule`. One case can hold checks for several rules.
- A judge question must be answerable from the task and the output alone. Name the exact thing to look for.
- Make the task tempt the failure, as a real request would: a hedge to drop, a figurative note to copy, a tool-named phrasal verb, several causes, a process that still runs.
- Add checks that catch over-application of a rule, for example "Does the output keep the uncertainty that the facts state?"
- Mix English, Japanese and Chinese prompts for genre rules, so that they are tested as language-independent.
