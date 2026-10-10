---
name: writing-tech
description: "Use when writing or editing technical text in any language, such as documentation, READMEs, runbooks, procedures, code comments, commit messages, pull request descriptions, error, log, CLI and UI text, postmortems, design docs, and technical articles or books."
---

# Writing technical text

These rules hold for technical text in every language. Load the skill for the text's language too: `writing-en`, `writing-ja` or `writing-zh`.

## Sources

- ASD-STE100 Simplified Technical English, Issue 9 (2025-01-15). The writing rules are paraphrased; the STE dictionary is not included, so text written with this skill is not certified STE.
- [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style) @ `05fc4f0d2b97b7c042dd9949ad658568e4a1324e`: William Strunk Jr., *The Elements of Style* (1918), Project Gutenberg #37134, public domain.
- [k16shikano/japanese-tech-writing](https://gist.github.com/k16shikano/fd287c3133457c4fd8f5601d34aa817d), gist revision `8f2d57610a73efc97d743c9b0b0ecb1002e09fa4`, Unlicense.
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) @ `f4518a8eab97b8bfebc66a89d34320a89bef6930`, MIT.
- [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 @ `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8`, MIT.
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) @ `8da1f030185bdfe8471220585162991eaeb970e9`, MIT.
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1379367647), revision 1379367647, CC BY-SA 4.0.

## Sentences

- Put a statement in positive form when a positive word states the same fact exactly: "the failing build", not "the build that isn't passing"; "common", not "not uncommon". Use "not" for instructions, warnings, limits and real negations: "does not support Windows". <!-- r:both.positive-form -->
- If the actor is known and the reader needs it, make the actor the subject: "The controller deletes the object." If the actor is unknown or does not matter to the reader, use the passive or a sentence without a subject, and do not invent an actor such as "the system" or "the team". Give a decision, intention or judgment to the person or group that made it, not to a version, a file, the data or "the market"; a program can still return, reject or show. <!-- r:both.name-the-actor -->
- Write each sentence so that it has one reading. Put a modifier next to the word that it modifies, and name the thing when "this", "it" or "the issue" could point to more than one thing. <!-- r:both.one-reading -->

## Structure

- Open each section and each expository paragraph with its main point: what the thing is and what it does, what was decided, or what caused the failure. Put background and history after it. If a passage tells events in time order or walks through an example, keep that order. <!-- r:tech.point-first -->
- If a heading has subheadings, put at least one sentence under it before the first subheading: what applies to all the subsections, or which one the reader needs first. <!-- r:tech.no-stacked-headings -->

## Words and names

- Use the term and translation that the field already uses (push notifications: 配信 in Japanese, 推送 in Chinese); do not coin a term or use a metaphor as a term when an established one exists. If the tool, command or UI names the operation, use that name instead of team slang: "create three temporary replicas" for `pgctl replicas create --count 3 --temporary`, not "spin up three throwaway replicas". <!-- r:tech.established-terms -->
- At first mention, expand an abbreviation, explain a technical term the stated audience may not know, and say what kind of thing a named command, file, table or setting is: "`pg_extension`, the system catalog that lists installed extensions". If the audience uses the term daily, skip the explanation. <!-- r:tech.first-mention -->
- Name a file, function, variable or other identifier only if the reader will type it, search for it, or meet it again in the text; otherwise describe it by its role ("the config loader"). Procedures and reference entries give the exact name. <!-- r:tech.identifiers-when-used -->

## Change documents

- In docs, code comments and reference text, describe what the code or system does now. Mention what it replaced or how it used to work only in changelogs, release notes, migration guides, deprecation notices, commit messages and PR descriptions. <!-- r:tech.describe-current-state -->
- Cut sentences about how the text was produced ("based on the maintainers' notes", "compiled from the logs", "unconfirmed items are flagged"). Keep a source the reader can follow, and keep the methods and test setup the reader needs to judge or repeat a result. <!-- r:tech.no-production-narration -->

## Procedures and specs

- Write a procedure as numbered steps in the imperative, with one action in each step. Put the command in a code block under the step that runs it. <!-- r:tech.one-action-per-step -->
- Put a condition before the action it controls: "If `pgctl check` reports an error, run `pgctl failover --to db-2`." A reader who acts while reading must not reach the command before the condition. <!-- r:tech.condition-before-action -->
- Put a warning directly before the step it protects, not after the step or in a notes section at the end. Start with what to do or not do, then give the consequence once: "Do not skip this step. Without the backup, a failed upgrade loses every write since the last backup." <!-- r:tech.warning-placement -->
- In specs, API contracts and procedures, mark each requirement level with one fixed keyword and keep it, for example must / should / may (RFC 2119), しなければならない / することが望ましい / してもよい (JIS Z 8301), 应 / 宜 / 可 (GB/T 1.1). Keep the level the source gives: a recommendation does not become "must". <!-- r:tech.requirement-keywords -->
