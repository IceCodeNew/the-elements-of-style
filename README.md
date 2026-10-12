# Writing skills for coding agents

Five agent skills that make a coding agent write better technical and personal text in English, Japanese and Chinese. Every rule in them stayed only after an ablation test showed that it improves what the model writes.

This repository is a fork of [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style). It merges rules from Strunk's *The Elements of Style*, ASD-STE100 Simplified Technical English, op7418/Humanizer-zh and its upstreams, and k16shikano's Japanese technical-writing norms. The anti-pattern catalog of tropes.fyi serves as test material.

## Skills

| Skill | Use it for | Rules |
|---|---|---|
| `writing-tech` | Technical text in any language: documentation, READMEs, runbooks, code comments, commit messages, PR descriptions, error and log text, postmortems | 14 |
| `writing-personal` | Personal text in any language: blog posts, essays, newsletters, social posts, replies | 5 |
| `writing-en` | Rules that hold only for English | 3 |
| `writing-ja` | Rules that hold only for Japanese | 4 |
| `writing-zh` | Rules that hold only for Chinese | 1 |

Install one genre skill, `writing-tech` or `writing-personal`, and the language skills for the languages you write in. The genre skills hold the rules that apply in every language. The language skills hold only the rules that depend on their language.

## Install

### Claude Code

Add the marketplace, then install the plugins you need:

```
/plugin marketplace add IceCodeNew/the-elements-of-style
/plugin install writing-tech@elements-of-style
/plugin install writing-en@elements-of-style
```

### Codex

Add the marketplace, then install the plugin. It holds all five skills:

```
codex plugin marketplace add IceCodeNew/the-elements-of-style
codex plugin add elements-of-style@elements-of-style-dev
```

### One skill at a time, for any agent

[openskills](https://github.com/numman-ali/openskills) and the [skills CLI](https://github.com/vercel-labs/skills) install a single skill directory:

```
openskills install IceCodeNew/the-elements-of-style/skills/writing-tech -g -y
npx skills add IceCodeNew/the-elements-of-style --skill writing-tech
```

### All five skills, for other harnesses

The install docs below come from [everyharness](https://github.com/prime-radiant-inc/everyharness). They install all five skills as one plugin; each skill's description tells the agent when to use it.

<!-- everyharness:install:start -->

| Harness | Install |
|---|---|
| Cursor | see docs/install/cursor.md |
| Codex | see docs/install/codex.md |
| Devin CLI | see docs/install/devin.md |
| Kimi Code | see docs/install/kimi.md |
| Gemini CLI | see docs/install/gemini.md |
| OpenCode | see docs/install/opencode.md |
| Pi | see docs/install/pi.md |
| Hermes Agent | see docs/install/hermes.md |
| Agent Plugins 1.0 clients | see docs/install/agent-plugins-1.0.md |
| Factory Droid / Grok / Copilot (marketplace descriptor) | see docs/install/agents-marketplace.md |

<!-- everyharness:install:end -->

## How the rules were chosen

Each upstream rule went through three filters:

1. An audit placed each rule of each rule source in a genre skill, a language skill, or nowhere. Rules whose only purpose is to hide signs of machine authorship stayed out. `maintenance/coverage.md` gives the outcome of every rule and the totals, and `maintenance/audits/` gives the reasons.
2. The audited rules were merged into candidate rules, written as conditions the writer can observe instead of absolutes.
3. An ablation test ran each candidate: the model wrote test cases with and without the rule, and a grader checked the outputs. A candidate stayed only if it improved the checks it targets.

Some sources supply test material only. Their examples of bad writing, such as the anti-patterns in tropes.fyi, became test cases, and checks that the tests apply to every output.

`evals/` holds the test cases, the harness and the method.

## Updating from upstream

`maintenance/upstreams.json` lists every upstream source with the exact version that the skills and the tests use. To check for newer versions:

```
python3 maintenance/check_upstreams.py
```

The project skill `updating-upstream-rules` (in `.claude/skills/`, linked into `.agents/skills/` for Codex) gives the full procedure: audit every changed rule, test new and changed rules, update the credits, regenerate the manifests and open a pull request.

## Sources and licenses

Each `SKILL.md` names the sources and exact versions that its rules come from, and `maintenance/upstreams.json` lists the pinned version of every source. Each skill directory has a `NOTICE.md` with the license notices of the MIT-licensed sources that it adapts. `evals/NOTICE.md` covers the examples that the test cases quote.

| Source | License |
|---|---|
| [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style): Strunk, *The Elements of Style* (1918), Project Gutenberg #37134 | Public domain text |
| ASD-STE100 Simplified Technical English | Rules paraphrased; the dictionary is not included |
| [k16shikano/japanese-tech-writing](https://gist.github.com/k16shikano/fd287c3133457c4fd8f5601d34aa817d) | Unlicense |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | MIT |
| [blader/humanizer](https://github.com/blader/humanizer) | MIT |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | MIT |
| [tropes.fyi](https://tropes.fyi/tropes-md): tropes.md v2 and The Writing Whip 0.1.0 | None stated; used only as test material |
| [ninehills/skills](https://github.com/ninehills/skills): deslop, deslop-en, deslop-zh | deslop: MIT; deslop-en and deslop-zh: no license file; used only as test material, with paraphrased examples |
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | CC BY-SA 4.0; the skills paraphrase only principles, and the test cases quote examples with the attribution in `evals/NOTICE.md` |

The full 1918 text of *The Elements of Style* is in `maintenance/sources/elements-of-style.md` and `elements-of-style.html`.

## Development

everyharness generates the manifests for every harness except Claude Code from `everyharness.yaml`. Claude Code reads the hand-written `.claude-plugin/marketplace.json`, which installs each skill as its own plugin. After you change `everyharness.yaml` or add a skill, regenerate and check the manifests with the pinned version:

```
npx everyharness@1.0.0 generate
npx everyharness@1.0.0 validate
```

The tests in `tests/` cover the ablation harness and the upstream registry. They call no model:

```
python3 -m unittest discover -s tests -t . -v
```

Do not edit a file with the `GENERATED by everyharness` header by hand.
