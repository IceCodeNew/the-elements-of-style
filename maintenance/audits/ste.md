# Audit: ASD-STE100 writing rules (Issue 9, 2025-01-15)

Evidence from micro-tests (Sonnet and Opus, 5 reps each, three task sets) is cited as "RED" (rule as written) and "GREEN" (conditional rewrite).

| ID | Source location | Rule | Destination | Reason | Conditional wording / notes |
|---|---|---|---|---|---|
| STE-0 | Intro | Follow ASD-STE100 Issue 9 so text is clear to non-native readers and easy to translate | EN/TECH | STE is a controlled-English standard for technical text | State that the skill adapts STE writing rules without the STE dictionary, so output is not certified STE |
| STE-S1 | Apply to | Procedures, runbooks, installation and troubleshooting steps | EN/TECH | Scope list | Merged into writing-tech scope |
| STE-S2 | Apply to | READMEs, API docs, code comments | EN/TECH | Scope list | Same |
| STE-S3 | Apply to | Commit messages, PR descriptions | EN/TECH | Scope list | Same |
| STE-S4 | Apply to | Error, log and UI help text | EN/TECH | Scope list | Same |
| STE-N1 | Do not apply to | Text in other languages | X-SCOPE | Handled by the language split | — |
| STE-N2 | Do not apply to | Chat replies, social posts, creative text, marketing copy | X-SCOPE | Handled by the genre split (writing-personal) | — |
| STE-N3 | Do not apply to | Code, commands, paths, identifiers, quotes stay verbatim | BOTH | Changing literal strings breaks them in any language | — |
| STE-N4 | Do not apply to | Documents with their own style guide | BOTH | A project style guide wins in any language | — |
| STE-N5 | Do not apply to | Text the user asks to write in a different style | BOTH | The user's explicit request wins | — |
| STE-1 | Requirements | Write procedures as commands, one instruction per sentence | TECH | Procedures in Japanese and Chinese also use one action per step | Japanese uses 「〜する」 or 「〜してください」 form per the document's style; keep in TECH, examples per language |
| STE-2 | Requirements | Procedural sentences ≤20 words, descriptive ≤25 words | EN/TECH | Word counts are English-specific; Japanese/Chinese do not segment words | RED: splits created repetition ("a channel that nobody watched. Nobody watched this channel…"). Conditional: do not count code; if a split repeats a noun phrase or drops because/while/so/unless, cut words instead |
| STE-3 | Requirements | Active voice; passive only in descriptions when the actor is unknown | BOTH (principle) + EN (STE condition) | Active voice with a real actor holds in all three languages; the STE condition is too narrow | RED: "Version 1.2 deprecated this field" (inanimate actor). Conditional: passive when the actor is unknown OR irrelevant to the reader; never promote a version/date/file to the actor of a human action |
| STE-4 | Requirements | Only infinitive, imperative, simple present/past/future, past participle as adjective | EN/TECH | Tense is English grammar; Chinese has no grammatical tense | RED: 9/10 runs wrote "did not finish" for a still-running sync (reads as failure); "is deprecated in v1.2". Conditional: choose the form from the time of the event (progressive for now, present perfect for not-yet/until-now, past perfect for before-another-past) |
| STE-5 | Requirements | No -ing forms as verbs | EN/TECH | English grammar | Conditional: allow progressive and -ing technical names; elsewhere write a clause ("before you delete") |
| STE-6 | Requirements | Short, common words; one meaning per word | TECH (principle) + EN (word examples) | Plain vocabulary and fixed meaning help non-native readers in any language | — |
| STE-7 | Requirements | One term for one thing in all of the text | BOTH | Universal; agrees with JTW (term consistency) and conflicts with nothing in personal writing that matters | X-DUP candidates: JTW 視点と語り (keep the introduced term), blader's dropped "synonym cycling" |
| STE-8 | Requirements | No phrasal verbs ("remove", not "take out") | EN/TECH | English grammar | RED: 6/10 runs avoided log in/roll back/back up/check out; circumlocutions "do a rollback of", "change your local repository to the tag". Conditional: if the tool/command/API/UI names the operation with a phrasal verb or its noun, use it; otherwise one-word verb. GREEN: 10/10 used tool-named phrasal verbs, 0/10 adopted team jargon "spin up" |
| STE-9 | Requirements | No noun clusters over three words | EN/TECH | English compounding; Japanese の-chains and Chinese 的-chains are separate language rules | — |
| STE-10 | Requirements | Do not omit articles, verbs or subjects to shorten a sentence | EN | Articles are English-only; subject omission is normal in Japanese (conflicts with JTW subject inheritance) | Conditional: follow format conventions (Go error strings, log messages, commit subjects, CLI lines, headings, table cells, labels) |
| STE-11 | Requirements | One topic per paragraph, six sentences or fewer | BOTH (one topic) + EN/TECH (six-sentence cap) | One topic per paragraph agrees with Strunk rule 8 and JTW; the numeric cap is STE's | X-DUP with EOS rule 8 and JTW-1.1 for the topic part |
| STE-12 | Requirements | Vertical lists for steps, conditions and options | TECH | Universal for procedures | — |
| STE-13 | Requirements | Warning: command first, then the risk ("Do not delete the volume. You will lose the data.") | TECH | Universal for procedures; placement before the step it protects | Conflict: JTW 演出の抑制 prefers 「〜するわけにはいかない」 over 「〜してはならない」 in argumentative prose. Resolution: different genre of text (procedure warning vs. book argument); the JTW tone rule is JA/TECH-prose |
| STE-14 | Requirements | Use technical names and verbs of the subject field ("pod", "commit", "deploy") | TECH | Universal; agrees with JTW (use field-standard terms) and op7418/Humanizer-zh (保留固定术语) | — |
