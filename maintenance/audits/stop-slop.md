# Rule audit: stop-slop

Source (an upstream of op7418/Humanizer-zh):

- `SS`: hardikpandya/stop-slop @ `8da1f030185bdfe8471220585162991eaeb970e9` (2026-03-18). Files: `SKILL.md`, `references/structures.md`, `references/phrases.md`, `references/examples.md`, `README.md`, `CHANGELOG.md`.

Conventions used in this audit:

- Granularity. `structures.md` gets one row per template where a section's table lists distinct templates (Binary Contrasts, Negative Listing, Dramatic Fragmentation, Rhetorical Setups, Formulaic Constructions, Narrator-from-a-Distance, Sentence Starters, Rhythm Patterns, Word Patterns). False Agency and Passive Voice get one row per section, because their tables list instances of one template. `phrases.md` gets one row per category; the words are listed in the notes. Compound SKILL.md core rules are split into a/b/c/d rows.
- Canonical rows for `X-DUP`. The most specific statement is canonical. SKILL.md core rules, Quick Checks, README and CHANGELOG restate `references/` rows, so they point there.
- JA/ZH words in the notes are auditor-supplied equivalents used to test universality. The sources contain only English examples.

## Counts

| Destination | SS |
|---|---|
| BOTH | 14 |
| TECH | 0 |
| PERSONAL | 5 |
| EN | 2 |
| JA | 0 |
| ZH | 0 |
| X-DEAI | 14 |
| X-DUP | 56 |
| X-SCOPE | 2 |
| Total | 93 |

Most SS `X-DUP` rows (39 of 56) come from SKILL.md summaries, Quick Checks, README, CHANGELOG and examples that restate `references/` rows.

## hardikpandya/stop-slop

| ID | Source location | Rule (short paraphrase, or quote if short) | Destination | Reason (one clause) | Conditional wording / notes |
|---|---|---|---|---|---|
| SS-C1 | SKILL.md §Core Rules 1 (L15) | "Cut filler phrases": throat-clearing openers, emphasis crutches, all adverbs | X-DUP | Summary of SS-P01, SS-P02, SS-P04 | — |
| SS-C2 | SKILL.md §Core Rules 2 (L17) | "Break formulaic structures": binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency | X-DUP | Pointer to SS-ST01–SS-ST23 | — |
| SS-C3a | SKILL.md §Core Rules 3 (L19) | "Use active voice. Every sentence needs a human subject doing something. No passive constructions." | X-DUP | Same as SS-ST28 | "Human subject" in every sentence is stricter than ST28. It conflicts with JA/ZH subject omission, imperative procedure steps, and system-as-actor in tech docs. Use ST28's conditional instead. |
| SS-C3b | SKILL.md §Core Rules 3 (L19) | "No inanimate objects performing human actions ('the complaint becomes a fix')" | X-DUP | Same as SS-ST23 | — |
| SS-C4a | SKILL.md §Core Rules 4 (L21) | "Be specific. No vague declaratives… Name the specific thing." | X-DUP | Same as SS-P09 | — |
| SS-C4b | SKILL.md §Core Rules 4 (L21) | No lazy extremes ("every," "always," "never") doing vague work | X-DUP | Same as SS-ST38 | — |
| SS-C5 | SKILL.md §Core Rules 5 (L23) | "Put the reader in the room." No narrator-from-a-distance voice; "'You' beats 'People.' Specifics beat abstractions." | X-DUP | Same as SS-ST24 | The "'You' beats 'People'" device fits EN and ZH personal prose. A generic 「あなた」 is unnatural in JA. |
| SS-C6a | SKILL.md §Core Rules 6 (L25) | "Vary rhythm. Mix sentence lengths." | PERSONAL | Monotonous rhythm weakens prose in every language, but procedures and reference text want uniformly short sentences | If three or more consecutive sentences of running prose share length and shape, rewrite one. Does not apply to procedure steps, lists or reference entries. JA: 一文一義 governs tech text; in essays the JA analogue is varying 文末 (です。です。です。), which belongs in the JA skill. ZH: 长短句交错 in essays holds. |
| SS-C6b | SKILL.md §Core Rules 6 (L25) | "Two items beat three." | X-DUP | Same as SS-ST32 | — |
| SS-C6c | SKILL.md §Core Rules 6 (L25) | "End paragraphs differently." | X-DUP | Same as SS-ST34 | — |
| SS-C6d | SKILL.md §Core Rules 6 (L25) | "No em dashes." | X-DUP | Same as SS-ST35 | — |
| SS-C7 | SKILL.md §Core Rules 7 (L27) | "Trust readers. State facts directly. Skip softening, justification, hand-holding." | BOTH | Needless softening and over-explanation waste the reader's time in any genre | If you are sure of a claim, state it without softeners. If the target reader already knows a step or concept, don't explain it. Keep hedges that encode real uncertainty, and keep the rationale (the "why") that commit messages, design docs and ADRs require. "Justification" should mean defensive self-justification only. JA: cushion phrases (クッション言葉) are expected in letters and email, but the certainty-based test still holds for essays and tech text. ZH: holds (过度铺垫/客套). |
| SS-C8 | SKILL.md §Core Rules 8 (L29) | "Cut quotables. If it sounds like a pull-quote, rewrite it." | X-DEAI | Careful essayists write memorable lines on purpose; the ban targets the LLM aphorism habit | The useful residue, a closing line that only restates the paragraph, is covered by SS-ST34. |
| SS-Q01 | SKILL.md §Quick Checks (L35) | "Any adverbs? Kill them." | X-DUP | Same as SS-P04 | — |
| SS-Q02 | SKILL.md §Quick Checks (L36) | "Any passive voice? Find the actor, make them the subject." | X-DUP | Same as SS-ST28 | — |
| SS-Q03 | SKILL.md §Quick Checks (L37) | "Inanimate thing doing a human verb? Name the person." | X-DUP | Same as SS-ST23 | — |
| SS-Q04 | SKILL.md §Quick Checks (L38) | "Sentence starts with a Wh- word? Restructure it." | X-DUP | Same as SS-ST29 | — |
| SS-Q05 | SKILL.md §Quick Checks (L39) | "Any 'here's what/this/that' throat-clearing? Cut to the point." | X-DUP | Same as SS-P01 | — |
| SS-Q06 | SKILL.md §Quick Checks (L40) | "Any 'not X, it's Y' contrasts? State Y directly." | X-DUP | Same as SS-ST06 | — |
| SS-Q07 | SKILL.md §Quick Checks (L41) | "Three consecutive sentences match length? Break one." | X-DUP | Same as SS-C6a | — |
| SS-Q08 | SKILL.md §Quick Checks (L42) | "Paragraph ends with punchy one-liner? Vary it." | X-DUP | Same as SS-ST34 | — |
| SS-Q09 | SKILL.md §Quick Checks (L43) | "Em-dash anywhere? Remove it." | X-DUP | Same as SS-ST35 | — |
| SS-Q10 | SKILL.md §Quick Checks (L44) | "Vague declarative? Name the specific implication." | X-DUP | Same as SS-P09 | — |
| SS-Q11 | SKILL.md §Quick Checks (L45) | "Narrator-from-a-distance? Put the reader in the scene." | X-DUP | Same as SS-ST24 | — |
| SS-Q12 | SKILL.md §Quick Checks (L46) | "Meta-joiners ('The rest of this essay...')? Delete. Let the essay move." | X-DUP | Same as SS-P06 | — |
| SS-S1 | SKILL.md §Scoring (L48–60) | Rate Directness, Rhythm, Trust, Authenticity, Density 1–10; revise below 35/50 | X-SCOPE | Self-scoring procedure, not a writing rule | "Authenticity: sounds human?" is a de-AI criterion. The other four dimensions restate SS-C6a, SS-C7 and SS-P01–P09. |
| SS-ST01 | references/structures.md §Binary Contrasts (L9) | "Not because X. Because Y." / "Not because X, but because Y." (telegraphed reversal) | X-DUP | Causal variant of SS-ST06 | Postmortems and debugging docs must rule out suspected causes ("not the deploy; the expired cert"). ST06's predicate (does a reader hold X?) keeps those. |
| SS-ST02 | references/structures.md §Binary Contrasts (L10) | "[X] isn't the problem. [Y] is." | X-DUP | Variant of SS-ST06 | — |
| SS-ST03 | references/structures.md §Binary Contrasts (L11) | "The answer isn't X. It's Y." | X-DUP | Variant of SS-ST06 | — |
| SS-ST04 | references/structures.md §Binary Contrasts (L12) | "It feels like X. It's actually Y." | X-DUP | Variant of SS-ST06 | Legitimate when it corrects an intuition the reader actually has, such as a performance myth. |
| SS-ST05 | references/structures.md §Binary Contrasts (L13) | "The question isn't X. It's Y." | X-DUP | Variant of SS-ST06 | — |
| SS-ST06 | references/structures.md §Binary Contrasts (L14, "Instead" L21) | "Not X. But Y." / "not X, it's Y" / "isn't X, it's Y". Instead: "State Y directly… Drop the negation entirely." | BOTH | Negating a position no reader holds is a strawman that delays the point in any genre | Canonical row for ST01–ST05, ST07, ST09, ST10, ST12 and ST13. Conditional: "If no plausible reader believes X, drop 'not X' and state Y. Keep the contrast when it corrects a belief the reader likely holds, or when it scopes a document ('This guide is not a reference; see …')." ZH 「不是……而是……」 and JA 「XではなくY」 are the same move, and the test holds for both. |
| SS-ST07 | references/structures.md §Binary Contrasts (L15) | "It's not this. It's that." | X-DUP | The source itself calls it the same formula as SS-ST06 | — |
| SS-ST08 | references/structures.md §Binary Contrasts (L16) | "stops being X and starts being Y" (false transformation arc) | X-DEAI | Literal when a real state change happens; flagged only as a cadence tell | Tech text uses it literally ("the cache stops being useful when …"). |
| SS-ST09 | references/structures.md §Binary Contrasts (L17) | "doesn't mean X, but actually Y" | X-DUP | Variant of SS-ST06 | — |
| SS-ST10 | references/structures.md §Binary Contrasts (L18) | "is about X but not Y" (false distinction) | X-DUP | Variant of SS-ST06 | — |
| SS-ST11 | references/structures.md §Binary Contrasts (L19) | "not just X but also Y" (additive hedge) | X-DEAI | "Not only … but also" is a standard correlative (JA だけでなく…も, ZH 不仅……而且……) | It is a problem only when "not just X" implies the reader thought "only X"; SS-ST06 then applies. |
| SS-ST12 | references/structures.md §Negative Listing (L29, "Instead" L32) | "Not a X... Not a Y... A Z." Instead: "State Z. The reader doesn't need the runway." | X-DUP | Multi-item form of SS-ST06 | — |
| SS-ST13 | references/structures.md §Negative Listing (L30) | "It wasn't X. It wasn't Y. It was Z." | X-DUP | Past-tense form of SS-ST12 | The tense difference is English grammar and does not change the rule. |
| SS-ST14 | references/structures.md §Dramatic Fragmentation (L40) | "[Noun]. That's it. That's the [thing]." (performative simplicity) | X-DEAI | A fragment cadence careful writers use by choice; the empty-emphasis part is SS-P02 | The section's fix, "Complete sentences" (L44), conflicts with tech norms: headings, UI labels, list items and commit subjects are fragments. |
| SS-ST15 | references/structures.md §Dramatic Fragmentation (L41) | "X. And Y. And Z." (staccato drama) | X-DEAI | A stylistic choice, not a defect in itself | The monotony residue is SS-C6a. |
| SS-ST16 | references/structures.md §Dramatic Fragmentation (L42) | "This unlocks something. [Word]." (artificial revelation) | X-DEAI | Pure LLM cadence tell | — |
| SS-ST17 | references/structures.md §Rhetorical Setups (L52) | "What if [reframe]?" (Socratic posturing) | X-DEAI | Hypotheticals are a legitimate device; "What if I told you" is a meme, not a rule | — |
| SS-ST18 | references/structures.md §Rhetorical Setups (L53) | "Here's what I mean:" (redundant preview) | X-DUP | Same as SS-P01 ("Here's what [X]") | — |
| SS-ST19 | references/structures.md §Rhetorical Setups (L54) | "Think about it:" (condescending prompt) | X-DUP | Same move as SS-P02 ("Let that sink in") | — |
| SS-ST20 | references/structures.md §Rhetorical Setups (L55) | "And that's okay." (unnecessary permission) | X-DUP | Covered by SS-C7 (skip softening and hand-holding) | — |
| SS-ST21 | references/structures.md §Formulaic Constructions (L63) | "By the time X, I was Y." (narrative template) | X-DEAI | Ordinary narrative construction | — |
| SS-ST22 | references/structures.md §Formulaic Constructions (L64) | "X that isn't Y": say "X is broken" | BOTH | Positive form is shorter and clearer in all three languages (JA 肯定形で書く・二重否定を避ける, ZH 少用否定和双重否定) | If a positive term states the same fact exactly, use it instead of negating its opposite ("the build that isn't passing" → "the failing build"). Keep the negative when it is the precise fact ("does not support Windows"). |
| SS-ST23 | references/structures.md §False Agency (L66–80) | Inanimate things given human verbs ("a complaint becomes a fix", "the decision emerges", "the culture shifts", "the conversation moves toward", "the data tells us", "the market rewards"). Name the human, or use "you". | BOTH | Hiding the person who decided or acted removes information in any genre; JA 無生物主語 and ZH 无灵主语 are also translationese markers | If a person or team decided or acted and the reader needs to know who, name them. Software performing its own operations may be the subject ("the server rejects the request", "the function returns"). Blameless postmortems name roles, not individuals. ZH 「数据表明」 and JA 「データは〜を示す」 are standard in scientific writing and stay. The "use 'you'" fallback is PERSONAL and not for JA. |
| SS-ST24 | references/structures.md §Narrator-from-a-Distance (L88, "Instead" L93) | "Nobody designed this." (disembodied observation). Instead: "Put the reader in the room." | PERSONAL | Concrete scenes beat detached abstraction in essays; reference docs and specs are impersonal by design | If an abstract observation about people can be shown as a situation the reader recognizes, show the situation. Second-person "you" scenes suit EN and ZH (generic 你 is natural). In JA, write the scene without 「あなた」. |
| SS-ST25 | references/structures.md §Narrator-from-a-Distance (L89) | "This happens because..." (lecturer voice) | X-DEAI | Causal explanation is the core of troubleshooting and design docs | — |
| SS-ST26 | references/structures.md §Narrator-from-a-Distance (L90) | "This is why..." | X-DUP | The source marks it "Same" as SS-ST25 | — |
| SS-ST27 | references/structures.md §Narrator-from-a-Distance (L91) | "People tend to..." (armchair sociologist) | BOTH | Unsupported generalizations about people weaken any argument, including UX and research docs | If a sentence generalizes about what people do, back it with data, a source or a concrete case, or narrow it to the group you observed. JA 「人は〜しがちだ」 and ZH 「人们往往……」 fail the same way. Overlaps SS-ST38. |
| SS-ST28 | references/structures.md §Passive Voice (L95–106) | "Every sentence needs a subject doing something." Passive hides the actor ("X was created", "It is believed that", "Mistakes were made", "The decision was reached"); front the actor. | BOTH | Hiding a known, relevant actor removes information in all three languages (JA 「〜とされる」「〜と考えられる」, ZH overuse of 被) | If the actor is known and the reader needs it, make the actor the subject. Keep the passive, or the JA/ZH subjectless or notional passive, when the actor is unknown, obvious or irrelevant (system behavior: "the file is written to /tmp") or when the object is the topic. Drop "every sentence needs a subject": JA and ZH omit subjects normally, and imperative steps have none. |
| SS-ST29 | references/structures.md §Sentence Starters (L112, L116) | Don't start sentences with What/When/Where/Which/Who/Why/How; "'What makes this hard is...' becomes 'The constraint is...'" | EN | Wh-words and the wh-cleft are English grammar | Narrow it: "If a sentence opens with a wh-cleft ('What X is …') and needs no contrastive focus, start with the subject." The absolute ban conflicts with the tech norm of stating the condition first ("When the build fails, check …"). JA 「〜なのは」 and ZH 「……的是」 clefts are covered by SS-P05. |
| SS-ST30 | references/structures.md §Sentence Starters (L113) | Paragraphs starting with "So": start with content | EN | English discourse marker | If "So" does not mark a consequence of the previous paragraph, delete it. |
| SS-ST31 | references/structures.md §Sentence Starters (L114) | Sentences starting with "Look,": remove | X-DUP | A throat-clearing opener; same as SS-P01 | English word; add it to the EN list. |
| SS-ST32 | references/structures.md §Rhythm Patterns (L122) | Three-item lists: use two items or one | X-DEAI | Rule of three as a frequency tell (rubric example); a list holds as many items as there are facts | — |
| SS-ST33 | references/structures.md §Rhythm Patterns (L123) | Questions answered immediately: let them breathe or cut them | X-DEAI | Hypophora is a legitimate device; FAQ and Q&A headings are a tech norm | — |
| SS-ST34 | references/structures.md §Rhythm Patterns (L124) | Every paragraph ends punchily: vary endings | PERSONAL | A kicker at the end of every paragraph is monotonous in essays (JA 体言止め overuse, ZH 段尾金句); tech paragraphs don't use kickers | If most paragraphs in a piece end on a short aphoristic line, rewrite some so they end on the content. |
| SS-ST35 | references/structures.md §Rhythm Patterns (L125) | Em-dashes: "Remove. Use commas or periods. No em dashes at all." | X-DEAI | Em-dash counting is a surface tell (rubric example) | Conflicts with SS's own examples.md L45. The ZH 破折号 "——" is standard punctuation (GB/T 15834). Broadened from "Em-dashes before reveals" in 1fdf64d. |
| SS-ST36 | references/structures.md §Rhythm Patterns (L126) | Staccato fragmentation: don't stack short punchy sentences | X-DUP | Same as SS-C6a (vary sentence length) | — |
| SS-ST37 | references/structures.md §Rhythm Patterns (L127) | "Not always. Not perfectly." (hedging disguised as reassurance) | X-DEAI | A specific English fragment cadence | The real-hedge residue is SS-C7. |
| SS-ST38 | references/structures.md §Word Patterns (L133) | Lazy extremes (every, always, never, everyone, everybody, nobody): "False authority. Use specifics instead of sweeping claims." | BOTH | Overgeneralization makes a claim false in any genre | If a universal quantifier is not literally true, replace it with the real scope or frequency. Keep "always", "never" and "must not" for invariants and requirements in tech text (RFC 2119 style). JA 「すべて」「必ず」「常に」「誰も」 and ZH 「所有」「总是」「从不」「每个人」 pass the same test. SS's own rules use absolutes ("all adverbs", "every sentence", "no em dashes at all"). |
| SS-ST39 | references/structures.md §Word Patterns (L134) | All adverbs (-ly words, really, just, literally, genuinely, honestly, simply, actually): empty emphasis | X-DUP | Same as SS-P04 | — |
| SS-P01 | references/phrases.md §Throat-Clearing Openers (L3–23) | Remove announcement phrases; "Any 'here's what/this/that' construction is throat-clearing before the point. Cut it." | BOTH | A phrase that announces a point instead of making it delays the reader in any genre and language | EN words: Here's the thing; Here's what/this/that/why [X]; The uncomfortable truth is; It turns out; The real [X] is; Let me be clear; The truth is; I'll say it again; I'm going to be honest; Can we talk about; Here's what I find interesting; Here's the problem though. Conditional: "If deleting the lead-in loses no information, delete it." Keep a lead-in that introduces a list, code block or command ("Here's the command:"). JA 「正直に言うと」「実は」 and ZH 「说实话」「事实上」 pass the same test. |
| SS-P02 | references/phrases.md §Emphasis Crutches (L25–33) | Phrases that only assert emphasis "add no meaning. Delete them." | BOTH | Emphasis should come from content, not from a label, in any genre | EN words: Full stop./Period.; Let that sink in.; This matters because; Make no mistake; Here's why that matters. Conditional: if the sentence keeps its meaning without the phrase, delete it. "This matters because" may stay when the reason that follows is not stated anywhere else. JA 「ここが重要です」 and ZH 「划重点」「敲黑板」 are equivalents. |
| SS-P03 | references/phrases.md §Business Jargon (L35–51) | Replace business jargon with plain language | BOTH | Plain words over buzzwords is a universal clarity rule (JA katakana jargon, ZH 互联网黑话) | EN table: navigate→handle, unpack→explain, lean into→accept, landscape→situation/field, game-changer→significant, double down→commit, deep dive→analysis, take a step back→reconsider, moving forward→next, circle back→revisit, on the same page→agreed. Some replacements are still vague ("game-changer"→"significant"); name the actual effect instead. |
| SS-P04 | references/phrases.md §Adverbs (L53–73) | "Kill all adverbs. No -ly words. No softeners, no intensifiers, no hedges." | BOTH | Empty intensifiers and sincerity markers add nothing in any language; the absolute form is wrong | Conditional: "Delete an intensifier or sincerity adverb if the claim reads the same without it. Keep adverbs of manner, scope, time and frequency ('only', 'locally', 'asynchronously', 'not') and hedges that encode real uncertainty." EN list: really, just, literally, genuinely, honestly, simply, actually, deeply, truly, fundamentally, inherently, inevitably, interestingly, importantly, crucially. "-ly words" is English morphology; drop it. JA 「本当に」「非常に」「まさに」 and ZH 「真正」「非常」「其实」「确实」 are equivalents. |
| SS-P05 | references/phrases.md §Adverbs, "Also cut these filler phrases" (L75–83) | Cut filler phrases | BOTH | Content-free framing phrases pad any text | EN words: At its core; In today's [X]; It's worth noting; At the end of the day; When it comes to; In a world where; The reality is. Conditional: delete if the sentence keeps its meaning. JA 「結局のところ」「〜に関して言えば」 and ZH 「归根结底」「说到……」「在当今……时代」 are equivalents. |
| SS-P06 | references/phrases.md §Meta-Commentary (L85–99) | Remove self-referential asides; "The essay should move, not announce its own structure." | PERSONAL | Signposting clutters short essays but is a norm in long tech docs, tutorials and books (EN "This section covers", JA 「本章では〜を説明する」, ZH 「本节介绍……」) | Conditional: in essays and posts, cut sentences that announce what the text will do or has done. Meta items: The rest of this essay explains; Let me walk you through; In this section, we'll; As we'll see; I want to explore. The other items are EN clichés, not meta-commentary: Hint:; Plot twist:/Spoiler:; You already know this, but; But that's another post; X is a feature, not a bug; Dressed up as. Do not migrate them (X-DEAI level). |
| SS-P07 | references/phrases.md §Performative Emphasis (L101–107) | "False intimacy or manufactured sincerity" | PERSONAL | Assurances in place of evidence are a personal-voice flaw; tech text doesn't use them | EN words: I promise; They exist, I promise. "creeps in" does not fit the category; drop it. Conditional: if you assure the reader ("I promise", "trust me"), replace the assurance with the evidence. ZH 「我保证」「相信我」 pass the same test. |
| SS-P08 | references/phrases.md §Telling Instead of Showing (L109–116) | Announcing difficulty or significance instead of demonstrating it | BOTH | Showing the hard part or the consequence beats labelling it in any genre and language | EN words: This is genuinely hard; This is what leadership actually looks like; This is what X actually looks like; actually matters. Conditional: if a sentence calls something hard, important or real, replace the label with the detail that makes it so, or cut it. JA 「これは本当に難しい」 and ZH 「这真的很难」 are equivalents. |
| SS-P09 | references/phrases.md §Vague Declaratives (L118–128) | Sentences announcing importance without naming the specific thing: name it or cut it | BOTH | Unnamed referents ("the reasons", "the implications") give the reader nothing in any genre and language | EN words: The reasons are structural; The implications are significant; This is the deepest problem; The stakes are high; The consequences are real. Conditional: if a sentence refers to reasons, implications or stakes without naming them, name them in that sentence or cut it. JA 「影響は大きい」 and ZH 「影响深远」「意义重大」 are equivalents. Overlaps SS-P08. |
| SS-E1 | references/examples.md Ex. 1 (L3–11) | Throat-clearing, binary contrast and emphasis crutch removed | X-DUP | Illustrates SS-P01, SS-ST01, SS-P02 | The "after" ("Technology is manageable. People aren't.") is itself a staccato contrast pair; don't reuse it as a model. |
| SS-E2a | references/examples.md Ex. 2 (L15–23) | Throat-clearing removed; permission-granting ending deleted | X-DUP | Illustrates SS-P01, SS-ST20 | — |
| SS-E2b | references/examples.md Ex. 2 "Changes" (L23) | "Cut hedging ('most')" | X-DEAI | Careful writers keep "most" when it is true, and the source's own rules no longer list it | The rule is also wrong. The "after" ("Nobody admits confusion") turns an accurate quantifier into a lazy extreme and contradicts SS-ST38. |
| SS-E3 | references/examples.md Ex. 3 (L27–35) | Business-jargon stack eliminated | X-DUP | Illustrates SS-P03, SS-P05, SS-P02 | The "after" ("Move faster. Your competition is.") drops content ("uncertainty"). It is also a quotable staccato pair that SS-C8 and SS-ST36 would flag. |
| SS-E4 | references/examples.md Ex. 4 (L39–47) | Dramatic fragmentation collapsed into one sentence | X-DUP | Illustrates SS-ST14, SS-ST15 | The "after" ("Speed, quality, cost—pick two.") uses an em dash, which contradicts SS-ST35. |
| SS-E5 | references/examples.md Ex. 5 (L51–59) | Rhetorical setup removed | X-DUP | Illustrates SS-ST17, SS-ST18, SS-ST19 | The "after" keeps an "X, not Y" contrast, which is fine under SS-ST06's conditional. |
| SS-R1 | README.md §What it catches (L36) | "Banned phrases": throat-clearing, emphasis crutches, business jargon, all adverbs, vague declaratives, meta-commentary | X-DUP | Summary of SS-P01–P04, SS-P06, SS-P09 | — |
| SS-R2 | README.md §What it catches (L38) | "Structural clichés": binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency, narrator-from-a-distance, passive voice | X-DUP | Summary of SS-ST01–SS-ST28 | — |
| SS-R3 | README.md §What it catches (L40) | "Sentence-level rules": no Wh- starters, no em dashes, no staccato, no lazy extremes, active voice required | X-DUP | Summary of SS-ST29, SS-ST35, SS-ST36, SS-ST38, SS-ST28 | — |
| SS-R4 | README.md §Scoring (L42–54) | The same five-dimension score | X-SCOPE | Scoring procedure; duplicates SS-S1 | — |
| SS-L1 | CHANGELOG.md 2026-01-13 Phrases (L8) | Throat-clearing additions ("Here's what I find interesting", "Here's the problem though") | X-DUP | Same as SS-P01 | The CHANGELOG stops at 2026-01-13; 1fdf64d and 8da1f03 (2026-03-18) are not logged. |
| SS-L2 | CHANGELOG.md 2026-01-13 Phrases (L9) | Performative emphasis | X-DUP | Same as SS-P07 | — |
| SS-L3 | CHANGELOG.md 2026-01-13 Phrases (L10) | Telling instead of showing | X-DUP | Same as SS-P08 | — |
| SS-L4 | CHANGELOG.md 2026-01-13 Structures (L13) | Binary contrasts: "Not X. But Y.", "It's not this. It's that.", "stops being X and starts being Y" | X-DUP | Same as SS-ST06, SS-ST07, SS-ST08 | — |
| SS-L5 | CHANGELOG.md 2026-01-13 Structures (L14) | Rhythm: staccato fragmentation | X-DUP | Same as SS-ST36 | — |
| SS-L6 | CHANGELOG.md 2026-01-13 Structures (L14) | Rhythm: dashes for dramatic pause | X-DUP | Same as SS-ST35 | Folded into the blanket em-dash ban in 1fdf64d. |
| SS-L7 | CHANGELOG.md 2026-01-13 Structures (L14) | Rhythm: hedging as reassurance | X-DUP | Same as SS-ST37 | — |
| SS-L8 | CHANGELOG.md 2026-01-13 Structures (L15) | Word patterns: absolute words | X-DUP | Same as SS-ST38 | Renamed "Lazy extremes" in 1fdf64d. |
| SS-L9 | CHANGELOG.md 2026-01-13 Structures (L15) | Word patterns: AI-overused intensifiers (deeply, truly, fundamentally, inherently, simply, literally, inevitably) | X-DUP | Same as SS-P04 and SS-ST39 | Folded into "All adverbs" in 1fdf64d. |

## Conflicts found

1. **How many em dashes.** SS-ST35, SS-C6d and SS-Q09 say "no em dashes at all". SS's own examples.md L45 ("Speed, quality, cost—pick two.") uses one. ZH punctuation standards (GB/T 15834) prescribe the 破折号 "——". Resolution: all of these rows are X-DEAI. Any dash rule is punctuation for the language skills, not a genre rule.
2. **Rule of three.** SS-ST32 and SS-C6b say to use two items or one, with no exceptions. Resolution: both are X-DEAI. In tech text a list has as many items as there are facts.
3. **Adverbs.** SS-P04 says to kill all adverbs. Tech text needs adverbs of manner and scope ("only", "locally", "asynchronously"). Resolution: SS-P04 becomes BOTH with an "empty intensifier" condition and the word list moves to EN.
4. **Passive voice and subjects.** SS-C3a and SS-ST28 say every sentence needs a (human) subject and forbid the passive. This conflicts with:
   - tech norms (system behavior, imperative steps, blameless postmortems);
   - JA/ZH, which drop subjects normally and use a notional passive.

   Resolution: BOTH, conditioned on the actor being known and relevant, without the "every sentence needs a subject" clause.
5. **False agency in tech text.** SS-ST23 forbids inanimate subjects with human verbs ("the data tells us"). Tech text uses system actors correctly ("the server rejects"), and ZH 「数据表明」 is standard scientific phrasing. Resolution: BOTH, conditioned on a person having decided or acted. Software actors and data-shows phrasing stay.
6. **"'You' beats 'People'".** SS-C5 and SS-ST24 conflict with JA norms, where generic 「あなた」 is unnatural, and with impersonal reference docs. Resolution: PERSONAL. The "you" device goes to EN/ZH examples only.
7. **Causal explanation.** SS-ST25 and SS-ST26 ban "This happens because…" and "This is why…". This conflicts with troubleshooting and design-doc norms. Resolution: X-DEAI.
8. **Wh- openers vs condition-first instructions.** SS-ST29 bans "When…" openers. Tech style guides put the condition first ("When the build fails, check …"). Resolution: EN only, narrowed to the wh-cleft.
9. **Signposts and summaries.** SS-P06 (meta-commentary) conflicts with tech, tutorial and book norms: EN "This section covers", JA 「本章では」 and 「まとめ」, ZH 「本节介绍」, 「本章小结」 and academic 「综上所述」. Resolution: SS-P06 is PERSONAL.
10. **Absolutes.** SS-ST38 bans "always/never/every". Tech requirements and invariants need them (RFC 2119), and SS's own rules are written in absolutes. Resolution: BOTH, conditioned on whether the quantifier is literally true.
11. **"Skip justification" vs "explain why".** SS-C7 conflicts with commit-message, design-doc and ADR norms that require the rationale. Resolution: BOTH, with the condition that only defensive self-justification goes.
12. **stop-slop contradicts itself.**
    - SS-E2b deletes "most" and produces a lazy extreme, which contradicts SS-ST38.
    - SS-E1 and SS-E3 produce staccato or quotable "after" text, which contradicts SS-C8 and SS-ST36.
    - SS-E4 uses an em dash, which contradicts SS-ST35.

    Resolution: don't import examples.md. Write new examples.

## Rules whose absolute wording should become conditional

Only rows that go into a skill (BOTH, PERSONAL, EN) are listed.

| ID | Source wording | Conditional form |
|---|---|---|
| SS-C6a | "Mix sentence lengths." | If three or more consecutive sentences of running prose share length and shape, rewrite one (not for steps, lists, reference entries). |
| SS-C7 | "Skip softening, justification, hand-holding." | If you are sure of a claim, state it without softeners; if the target reader already knows a step, don't explain it; keep real-uncertainty hedges and the rationale. |
| SS-ST06 | "State Y directly… Drop the negation entirely." | If no plausible reader believes X, drop "not X" and state Y; keep the contrast when it corrects a likely belief or scopes a document. |
| SS-ST22 | "X that isn't Y: say 'X is broken'." | If a positive term states the same fact exactly, use it; keep the negative when it is the precise fact. |
| SS-ST23 | "Name the human." (no inanimate actors) | If a person or team decided or acted and the reader needs to know who, name them; software and data may be subjects of their own operations. |
| SS-ST24 | "Put the reader in the room." | If an abstract observation about people can be shown as a recognizable situation, show it (no generic 「あなた」 in JA). |
| SS-ST27 | (implied ban on "People tend to…") | If a sentence generalizes about people, support it or narrow it to the observed group. |
| SS-ST28 | "Every sentence needs a subject doing something." / "No passive constructions." | If the actor is known and the reader needs it, make it the subject; otherwise passive or subjectless forms are fine. |
| SS-ST29 | Don't start sentences with What/When/…/How. | If a sentence opens with a wh-cleft and needs no contrastive focus, start with the subject (EN only). |
| SS-ST30 | Don't start paragraphs with "So". | If "So" does not mark a consequence, delete it (EN only). |
| SS-ST34 | "Every paragraph ends punchily: vary endings." | If most paragraphs end on a short aphoristic line, rewrite some to end on content. |
| SS-ST38 | "Use specifics instead of sweeping claims." (every/always/never/…) | If a universal quantifier is not literally true, replace it with the real scope; keep it for invariants and requirements. |
| SS-P01 | "Any 'here's what/this/that' construction is throat-clearing… Cut it." | If deleting the lead-in loses no information, delete it; keep lead-ins to lists, code blocks and commands. |
| SS-P02 | "These add no meaning. Delete them." | If the sentence keeps its meaning without the phrase, delete it. |
| SS-P04 | "Kill all adverbs. No -ly words. No softeners, no intensifiers, no hedges." | If an intensifier or sincerity adverb can go without changing the claim, delete it; keep manner/scope/time/frequency adverbs and real-uncertainty hedges. |
| SS-P05 | "Also cut these filler phrases." | If the sentence keeps its meaning without the phrase, delete it. |
| SS-P06 | "Remove self-referential asides." | In essays and posts, cut sentences that announce what the text will do or has done. |
| SS-P09 | "Kill these." | If a sentence refers to reasons/implications/stakes without naming them, name them or cut the sentence. |

Excluded rows that also had absolute wording (FYI): SS-ST35 "No em dashes at all", SS-ST32 "Use two items or one", SS-ST14–16 "Complete sentences", SS-C8 "If it sounds like a pull-quote, rewrite it".

## Language-specific examples to move

### EN (from the sources)

- **SS-P01 throat-clearing.**
  - From SS: Here's the thing; Here's what/this/that/why [X]; The uncomfortable truth is; It turns out; The real [X] is; Let me be clear; The truth is; I'll say it again; I'm going to be honest; Can we talk about; Here's what I find interesting; Here's the problem though; Look, (SS-ST31).
- **SS-P02 emphasis crutches:** Full stop./Period.; Let that sink in.; This matters because; Make no mistake; Here's why that matters; Think about it: (SS-ST19).
- **SS-P03 plain words.**
  - SS table: navigate, unpack, lean into, landscape, game-changer, double down, deep dive, take a step back, moving forward, circle back, on the same page.
- **SS-P04 empty intensifiers:** really, just, literally, genuinely, honestly, simply, actually, deeply, truly, fundamentally, inherently, inevitably, interestingly, importantly, crucially. Drop the "-ly words" criterion.
- **SS-P05 filler phrases:** At its core; In today's [X]; It's worth noting; At the end of the day; When it comes to; In a world where; The reality is.
- **SS-P06 meta-commentary (PERSONAL):** The rest of this essay explains; Let me walk you through; In this section, we'll; As we'll see; I want to explore. Don't migrate the clichés filed under this heading (Hint:, Plot twist:, Spoiler:, You already know this, but, But that's another post, X is a feature, not a bug, Dressed up as).
- **SS-P07:** I promise; They exist, I promise.
- **SS-P08:** This is genuinely hard; This is what X actually looks like; actually matters.
- **SS-P09:** The reasons are structural; The implications are significant; This is the deepest problem; The stakes are high; The consequences are real.
- **SS-ST06 family templates:** "Not because X. Because Y."; "[X] isn't the problem. [Y] is."; "The answer/question isn't X. It's Y."; "It feels like X. It's actually Y."; "It's not this. It's that."; "doesn't mean X, but actually Y"; "is about X but not Y"; "Not a X… Not a Y… A Z."; "It wasn't X. It wasn't Y. It was Z."
- **SS-ST22:** "the X that isn't working" → "the broken X".
- **SS-ST23:** a complaint becomes a fix; a bet lives or dies; the decision emerges; the culture shifts; the conversation moves toward; the data tells us; the market rewards.
- **SS-ST28:** X was created; It is believed that; Mistakes were made; The decision was reached.
- **SS-ST29 (EN rule):** wh-cleft "What makes this hard is …" → "The constraint is …".
- **SS-ST30 (EN rule):** paragraph-initial "So".
- **SS-ST38:** every, always, never, everyone, everybody, nobody.

### JA (none in the sources; auditor-supplied equivalents and overriding norms)

- **Equivalents for the universal rows:**
  - SS-P01: 「正直に言うと」「実は」
  - SS-P02: 「ここが重要です」
  - SS-P03: カタカナ業界語 「アジェンダ」「エビデンス」「シナジー」
  - SS-P04: 「本当に」「非常に」「まさに」
  - SS-P05: 「結局のところ」「〜に関して言えば」
  - SS-ST06: 「XではなくY」
  - SS-ST22: 二重否定
  - SS-ST23: 無生物主語
  - SS-ST28: 「〜とされる」「〜と考えられる」
  - SS-ST38: 「すべて」「必ず」「常に」
- **JA norms that limit the universal rows:**
  - No generic 「あなた」 (SS-C5, SS-ST24, SS-ST23 fallback).
  - Subject omission is normal (SS-C3a, SS-ST28).
  - 「本章では」 signposts and 「まとめ」 sections are conventional in tech books and Qiita/Zenn posts (SS-P06).
  - 文末 variety (です/ます monotony) is the JA form of SS-C6a, a JA-skill candidate.
  - 体言止め overuse is the JA form of SS-ST34.

### ZH (none in the sources; auditor-supplied equivalents and overriding norms)

- **Equivalents for the universal rows:**
  - SS-P01: 「说实话」「事实上」
  - SS-P02: 「划重点」「敲黑板」
  - SS-P03: 互联网黑话 「赋能」「抓手」「闭环」「对齐」「颗粒度」「底层逻辑」
  - SS-P04: 「真正」「非常」「其实」「确实」
  - SS-P05: 「归根结底」「在当今……时代」
  - SS-ST06: 「不是……而是……」
  - SS-ST23: 无灵主语
  - SS-ST28: 被字句 overuse
  - SS-ST38: 「所有」「总是」「从不」「每个人」
- **ZH norms that limit the universal rows:**
  - GB/T 15834 prescribes the 破折号 "——" (SS-ST35).
  - 「数据表明」 is standard scientific phrasing (SS-ST23).
  - Subject omission and notional passive are normal (SS-C3a, SS-ST28).
  - 「本节介绍」「本章小结」「综上所述」 are conventional in tech and academic writing (SS-P06).
  - Wh-word openers 「什么/为什么/如何」 are not an issue in ZH (SS-ST29 is EN-only).
