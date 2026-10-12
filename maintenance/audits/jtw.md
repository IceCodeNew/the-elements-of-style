# Audit: japanese-tech-writing (JTW)

- Source: gist `k16shikano/fd287c3133457c4fd8f5601d34aa817d`, revision `8f2d57610a73efc97d743c9b0b0ecb1002e09fa4`
- Pinned: gist k16shikano/fd287c3133457c4fd8f5601d34aa817d, revision 8f2d57610a73efc97d743c9b0b0ecb1002e09fa4 (2026-09-09), Unlicense
- Line numbers (`L`) refer to that file. Section numbers: §1 段落と論証の構成, §2 論証の厳密さ, §3 読み手の負荷の管理, §4 視点と語り, §5 演出の抑制, §6 LLM っぽい表現の禁止, §7 翻訳調の比喩と擬人化の禁止, §8 冗長の排除, §9 見出しの付け方, §10 読者への誠実さ.
- ID scheme: `JTW-<section>.<item>`. `.0` = a section-level framing statement that carries a rule. A letter suffix (`a`, `b`, ...) = one bullet that holds several separate rules, or a sub-bullet example.

## Destination counts

| Destination | Rows |
|---|---|
| BOTH | 76 |
| TECH | 15 |
| PERSONAL | 0 |
| JA | 15 |
| JA/TECH | 2 |
| EN / ZH | 0 |
| X-DEAI | 0 |
| X-DUP | 4 |
| X-SCOPE | 1 |
| **Total** | **113** |

No rule is X-DEAI. §6 and §7 start from LLM tells, but every rule there targets phrases that add no claim or that the reader takes literally. Those make a careful human's text worse too (rubric test 1).

## Rule table

| ID | Source location | Rule (short paraphrase, or quote if short) | Destination | Reason (one clause) | Conditional wording / notes |
|---|---|---|---|---|---|
| JTW-0.0 | frontmatter L3; intro L9 | Scope: follow these norms when writing or revising Japanese technical manuscripts (book chapters, articles, explanatory texts). | X-SCOPE | Trigger and scope statement, not a writing rule. | The description's topic list is a table of contents. |
| JTW-1.0 | §1 L13 | Use paragraph writing as the base: a paragraph is one step of the argument (「段落は論証の一歩」), and the reader must be able to follow the logic paragraph by paragraph. | BOTH | Paragraph-as-unit holds in EN/JA/ZH and in essays. | "In expository or argumentative passages, make each paragraph one step of the argument." In a narrative personal passage, a paragraph is one step of the story. |
| JTW-1.1 | §1 L15 | One topic per paragraph; split a long paragraph that mixes several stages of a scene (investigate, report, verify, evaluate). | BOTH | Paragraph unity is universal. | |
| JTW-1.2 | §1 L16 | A reader should know what a paragraph is about from its first sentence. | TECH | Topic-first paragraphs serve skimmed expository text; personal narrative often withholds the point on purpose. | "In expository text, let the first sentence name the paragraph's topic." |
| JTW-1.3 | §1 L17 | Open each paragraph with a connective that makes its logical relation to the previous paragraph explicit (「であれば」「実際」「しかし」「この例自体からも」). | BOTH | Explicit inter-paragraph logic holds in every language and genre. | Absolute "always open with a connective" conflicts with JTW-6.5 and with deslop transition-overuse rules. "If the relation to the previous paragraph is not evident from the content, open with a connective that names the relation (consequence, evidence, contrast); do not add purely additive connectives." Examples → JA. |
| JTW-1.4 | §1 L18 | Move the argument in one direction: do not conclude, then handle objections, then restate the conclusion; finish objections and doubts first, then state the conclusion once. | BOTH | Stating a conclusion once is universal. | Conflicts with BLUF / summary-first norms of design docs, PR descriptions and postmortems. "State the conclusion once. In an argument that builds to it, handle objections first; if the genre puts the conclusion first, lead with it and handle objections after without restating it." |
| JTW-1.5 | §1 L19 | Do not insert defenses of an example (e.g. pre-empting "this looks contrived") right after the scene's climax; handle them together at the start of the next section. | BOTH | Not breaking a scene's peak holds for any story-driven text. | "If a passage narrates a scene, put caveats about the example where the scene has ended (e.g. the next section's opening)." Content of the caveat: JTW-10.1. |
| JTW-1.6 | §1 L20 | When readers are likely to form a wrong interpretation, negate it explicitly, then give the real reason (「その理由は『〜だから』ではない。〜だからだ」). | BOTH | Pre-empting a likely misreading is universal. | "If a misreading is likely, ..." The predicate separates this from the "It's not X, it's Y" pattern that JTW-5.8 and deslop rules limit. Example frame → JA. |
| JTW-1.7 | §1 L21 | When you write "not A but B", add one sentence giving the ground for rejecting A; a counterfactual (「もしAなら、〜だっただろう」) often serves. | BOTH | Universal. | |
| JTW-1.8a | §1 L22 | When you define one concept by contrasting two objects, give both sentences predicates of the same form. | BOTH | Parallel structure is universal. | |
| JTW-1.8b | §1 L22 | Put the callback to an earlier explanation in a sentence-initial frame; do not bury the definition itself inside 「〜だと説明した」. | BOTH | Stating a definition as a direct claim rather than as reported speech is universal. | EN: "As Section 2 showed, X is Y", not "We explained that X is Y". Example → JA. |
| JTW-1.8c | §1 L22 | Cut out the characterizing phrase with 「」. | JA | Depends on the Japanese 「」 quotation convention. | EN would use quotes or italics, ZH “”; no universal rule here. |
| JTW-1.8d | §1 L22 | Make the contrast connective explicit. | BOTH | Universal. | Sentence-level counterpart of JTW-1.3. |
| JTW-1.8e | §1 L22 | For further attributes of the second pole, inherit the subject instead of naming it again (「主語を改めて名乗らず継承する」). | JA | Relies on Japanese subject omission and topic continuity. | Conflicts with STE ("do not omit subjects"); resolved because the rule is JA-only. |
| JTW-1.9 | §1 L23 | In a concession (「確かに〜」) only confirm facts; asserting in the author's voice, as cause, what you later correct is self-contradiction; to grant a surface diagnosis once, attribute it to the reader or received opinion (「〜と要約できてしまうかもしれない」). | BOTH | A concession that keeps the author's voice consistent is universal. | Example phrasing → JA. |
| JTW-1.10 | §1 L24 | Do not reveal, in the paragraph before the climax, information meant to land there (numbers, specific facts). | BOTH | Narrative pacing applies to stories in essays and in technical books alike. | Conflicts with front-loading in reference docs and summaries. "If a passage narrates a scene or worked example that builds to a result, do not state the result's key figure before the point where it lands; in summaries, reference docs and procedures, put key facts first." |
| JTW-1.11 | §1 L25 | When negating or limiting, write out the exact proposition you negate (「『明文化されていればすべてを任せられる』を意味しない」), not a vague negation such as 「何もかもが解決するわけではない」. | BOTH | Naming the exact negated proposition is universal. | 「」 marking → JA example; EN "does not mean that X". |
| JTW-1.12 | §1 L26 | Put forward references (「後の章で扱う」) where an argument step ends (paragraph end, section end), not mid-argument. | BOTH | Universal for long-form text. | Pairs with JTW-2.8. |
| JTW-2.0 | §2 L30 | Leave no openings for objections (「ツッコミどころ」); after drafting, anticipate the reader's rebuttals and check the points below. | BOTH | Universal. | The after-drafting check is process; the standard itself is the rule. |
| JTW-2.1 | §2 L32–37 | Do not mechanically turn conjecture, possibility, reader doubt or counterfactuals into assertions. Delete 「かもしれない」「だろう」「ようだ」「らしい」 only when they weaken a claim without grounds; keep the uncertainty for unverified possibilities, characters' perceptions, inferences from logs, likely reader doubts and counterfactuals; assert only when evidence in the text settles the proposition. | BOTH | Calibrated certainty is universal; this rule guards against over-applied hedge-removal. | Already conditional; use it as the model wording for hedge rules in deslop-en/zh. Hedge words → JA examples. |
| JTW-2.2 | §2 L38 | Do not lump different things together as "the same"; do not cover distinct objects (separate decisions, causes, problem types) with one word (bad 「同じ決定を別々に下していた」, good 「どれも別々の決定であり、しかも互いに依存している」). | BOTH | Universal. | |
| JTW-2.3 | §2 L39 | Do not reduce a multi-cause event to a single cause; separate the problem types and map which tool explains which. | BOTH | Universal. | |
| JTW-2.4 | §2 L40 | Treat a concept the same way across chapters and sections: classification, definition and term status stay aligned (not 「人間が決める」 in one section and 「チームで合意する」 in another). | BOTH | Universal for long texts. | |
| JTW-2.5 | §2 L41 | When you claim causation, state the mechanism in one sentence; do not write only "A leads to B". | BOTH | Universal. | "If the mechanism is not obvious to the target reader, state it in one sentence." |
| JTW-2.6 | §2 L42 | Do not write as if detection, guarantees or fixes "always" succeed; state the conditions (「〜しやすい」「〜できることが多い」「〜が成り立つときに限り」). | TECH | Claims about what methods and tools guarantee are a technical-text concern; opinion writing tolerates rhetorical absolutes. | Already conditional. Tension with JTW-8.12 resolves on "does the text establish the condition?". |
| JTW-2.7 | §2 L43 | Check that the examples actually support the whole claim; if they support only part, narrow the claim to match. | BOTH | Universal. | |
| JTW-2.8 | §2 L44 | Check that a point deferred with 「次節で扱う」 is actually resolved there; do not plant setups you never pay off. | BOTH | Universal for long-form text. | |
| JTW-2.9 | §2 L45 | After a concession or qualification (「ただし」「とはいえ」), always move the argument on; do not end on the adversative and leave the reader suspended. | BOTH | Universal. | "After a concession, say what it changes for the claim, unless an open ending is the point (essays)." |
| JTW-2.10 | §2 L46 | Define a section's central term, with its scope, before you use it. | BOTH | Universal. | JTW-8.11 duplicates this with wider scope; widen to "any concept or document name". |
| JTW-2.11 | §2 L47–48 | When you group several concepts under one umbrella term, state in one sentence just before naming it that they reduce to the same thing. | BOTH | Universal. | Inverse of JTW-2.2. |
| JTW-3.0 | §3 L52 | Treat the reader's memory and attention as finite resources. | BOTH | Universal. | |
| JTW-3.1a | §3 L54 | Increase what the reader must hold during in-order reading by only one level at a time. | BOTH | Universal. | |
| JTW-3.1b | §3 L54 | After cutting passages, trace the remaining mentions and drop topics no longer used anywhere else in the document. | BOTH | Universal revision hygiene. | |
| JTW-3.1c | §3 L54 | When a permission or a way of reading follows from the preceding sentences in one step, state it directly. | BOTH | Universal. | Source wording is terse; read as "do not leave a one-step inference implicit". |
| JTW-3.2 | §3 L55 | Do not mention proper names (file names, function names, identifiers) the reader will not need later; use a generic description (「仕様書」「金額計算のユーティリティ」). | TECH | Identifiers occur almost only in technical text. | Conflicts with procedure and reference norms that name the exact file or command. "If the reader will not type, search for or refer back to the name, describe the thing generically." Overlaps JTW-3.8. |
| JTW-3.3 | §3 L56 | If context does not fix the referent of an abstract phrase, identify it on the spot with a parenthetical appositive, where possible, so the reader need not reread. | BOTH | Universal. | |
| JTW-3.4 | §3 L57 | In the sentence that first presents a concept, order it so the reader first learns what kind of thing it is (data structure, procedure, constraint); do not put properties that only an informed reader finds natural before that identification. | BOTH | The principle is universal. | Bites hardest with head-final noun phrases (long JA pre-nominal modifiers, ZH 的-chains); EN "X, a data structure that ..." does it naturally. Add JA and ZH examples. |
| JTW-3.5 | §3 L58 | When a new example or scene adds context to hold, first say how it differs from the previous one and why another one is needed. | BOTH | Universal. | |
| JTW-3.6a | §3 L59 | When a section has several presentations (figure, table, code), divide what each medium explains (layout, numbers, procedure). | TECH | Multi-media sections are a feature of technical text. | |
| JTW-3.6b | §3 L59 | The media need not share types or data; they may be separate examples. | TECH | Same. | A permission; many tech guides recommend one running example, so keep it as "may", not "should". |
| JTW-3.6c | §3 L59 | Place demonstratives (「この2つ」「上記の例」) so context alone fixes which medium's example they point to. | TECH | Same. | The general unique-referent principle is JTW-3.3. |
| JTW-3.6d | §3 L59 | Do not carry a property you verified on one medium's example over to another medium's example. | TECH | Same. | |
| JTW-3.6e | §3 L59 | When you contrast two methods as 「Aの代わりにB」, align the word order with the replacement so in-order reading shows that the later-written side is adopted. | JA | "Later-written = adopted" follows the Japanese 「Aの代わりにB」 pattern. | EN procedure style puts the adopted option first ("Use B instead of A"; STE puts the command first). The kernel, "make the adopted option unambiguous", could go to TECH. |
| JTW-3.7 | §3 L60 | Do not stuff chapter openings or section intros with detail unrelated to the examples ahead. | BOTH | Universal. | |
| JTW-3.8 | §3 L61 | In example sections, omit only the detail irrelevant to the section's question or outcome, and keep the specifics the argument needs; typical omissions are decorative precision in agent reports (timestamps, HTTP status, coverage) and proper names never referred to again. | BOTH | A relevance filter is universal. | A postmortem needs its timestamps; the predicate "irrelevant to the section's question" already covers that. Overlaps JTW-3.2. |
| JTW-4.1 | §4 L65 | In examples, write a chain of actions with the actor as subject (「リポジトリを調査して特定し、見つけてくれた」), not a list of results or passives (「特定され、判明した」). | BOTH | Actor-first narration is universal; agrees with STE's active voice. | "If the actor is known and matters, make it the subject." The benefactive 「〜てくれた」 is JA-only → JA example. |
| JTW-4.2 | §4 L66 | Do not attach pointless fictional personas (「入社2年目のエンジニアが」). | BOTH | Universal. | "If the persona's attributes do not affect the example, drop them." |
| JTW-4.3 | §4 L67 | In the argument, do not address the reader as 「あなた」; use role names (「開発者」「読者」); keep second-person address to a few key points such as scene setup (「〜としよう」) and chapter or book endings. | JA | 「あなた」 is marked and distancing in Japanese. | Conflicts with EN tech style guides that use "you"; resolved because the rule is JA-only. |
| JTW-4.4 | §4 L68 | Pick specific words for referents; do not blur them with broad words such as 「AI」「ツール」. | BOTH | Universal. | |
| JTW-4.5 | §4 L69 | Once you introduce a formalization or term (K, contract, invariant), use it throughout; do not slide back to vague words (「文脈」「ツール」「AI」); such words are fine as lead-ins before the formalization. | BOTH | Holds for any defined term in any language. | "Once you define a term, ..." Elegant variation (encouraged in ZH school writing) yields only for defined terms. |
| JTW-4.6 | §4 L70 | Use the terms and translations conventional in the field (push notifications are 「配信」, not 「配送」); do not pick a near-synonym kango by everyday feel. | TECH | Field terminology is a technical-text concern; the principle holds in EN and ZH. | Example → JA. ZH analog: 推送, not 投递. |
| JTW-4.7 | §4 L71 | Write a person's name in the original spelling (Lehman, Bainbridge); for historical figures and eponymous concepts with an established name, use the established katakana form. | JA | Depends on katakana transliteration conventions. | ZH needs its own rule (established Chinese names such as 图灵, otherwise original spelling). |
| JTW-4.8 | §4 L72 | Do not reuse words that sound like technical terms where no term is meant (calling the chain from system to people 「経路」); use plain phrasing (「届くまでの流れ」「あいだに何があるか」). | TECH | Technical readers take term-like words as defined terms. | Example → JA. |
| JTW-4.9 | §4 L73 | Do not write i-adjective + です (「難しいです」); it signals a sentence cut off from its neighbors, so rewrite the surrounding flow, not just the ending; na-adjective + です (「重要です」) is exempt. | JA | Japanese grammar and register. | |
| JTW-5.0 | §5 L77 | 「演出の規範は全面禁止ではなく、節度の規範である」: use rhetoric only where it has an effect. | BOTH | Universal. | Already conditional; it governs JTW-5.1 to 5.9. |
| JTW-5.1 | §5 L79 | Use suspense (「ここには〜が潜んでいる」) or rhetorical questions to stage a derivation only where the tension serves the argument; where explanation suffices, just state it. | BOTH | Universal under its own condition. | Personal writing has more such points; the predicate scales. Example → JA. |
| JTW-5.2a | §5 L80 | Do not overuse short punchlines set as standalone paragraphs to create tension. | BOTH | Overuse weakens any text. | A frequency rule about effect, not a tell, so not X-DEAI. |
| JTW-5.2b | §5 L80 | A short 体言止め inside a paragraph (「ここまでわずか数十秒。」) is allowed, but only at a scene's climax. | JA | 体言止め is a Japanese device. | Universal analog: verbless fragments only at a climax (EN "Thirty seconds, start to finish."); could become a separate BOTH rule. |
| JTW-5.3 | §5 L81 | Do not overuse bold in body text; use it only at logical key points (a negation that prevents misreading, a section's conclusion), one or two per section at most, intros included; otherwise make things stand out through order and structure. | BOTH | Universal. | Covers emphasis only, not conventions such as bold UI labels in procedures. Treat the quota as a guideline. |
| JTW-5.4 | §5 L82 | Prefer the practitioner's-judgment form 「〜するわけにはいかない」 over the imperative 「〜してはならない」. | JA | Tone contrast between two Japanese forms. | Conflicts with STE (warnings start with "Do not ..."). Even in JA, limit it to explanatory prose; warnings and procedure steps keep the command form. |
| JTW-5.5 | §5 L83 | Do not over-dramatize turning points; one sentence stating the fact usually suffices; at the argument's climax, a short sentence with an exclamation mark is tolerated. | BOTH | Universal. | The exclamation allowance conflicts with tech style guides that ban "!"; "only in narrative article or book prose, never in reference docs, UI or error text". |
| JTW-5.6 | §5 L84 | Do not stoke fear of accidents or danger by listing consequences. | BOTH | Universal. | Conflicts with the STE / safety-warning format, which must state hazard and consequence. "Do not stack consequences for effect; in a warning, state the hazard, its consequence and how to avoid it, once." |
| JTW-5.7 | §5 L85 | Do not announce a claim with 「重要なのは〜である」; state it. A preface that declares the claim's mode (「標語として言い換えれば」) is fine. | X-DUP | JTW-6.1 lists 「重要なのは〜である」 too. | Move the mode-declaring-preface exception into JTW-6.1. |
| JTW-5.8 | §5 L86 | Do not overuse the antithetical punchline 「AではなくBだった」; light asides and evaluations may go in parentheses. | BOTH | Overuse is bad writing, not only an AI tell. | Bounded by JTW-1.6 and 1.7, which allow the form for a likely misreading. |
| JTW-5.9a | §5 L87 | Do not twist idioms (「知識を体に入れる」); say it with a plain verb (「身につく」). | TECH | Personal writing legitimately plays with idioms for voice. | "In technical text, ..." Example → JA. |
| JTW-5.9b | §5 L87 | Do not use a metaphor whose referent cannot be pinned down (「報告の外側に世界が広がっている」); say it plainly (「気付く機会が減る」). | BOTH | A metaphor the reader cannot resolve fails in any genre. | Same test as JTW-7.4b. |
| JTW-6.0a | §6 L91 | Do not give in to the contentless patterns LLMs mass-produce; check the draft against this section. | X-DUP | JTW-6.0c states the same rule with its test; the rest is process. | Drop the "LLM" framing in the target skill. |
| JTW-6.0b | §6 L92 | The book's own terms (本質的複雑さ, 回収, 判断の配置) are fine in argument; the problem is using them as empty decoration. | BOTH | A word is judged by whether it carries the argument; that holds everywhere. | Makes every §6 item conditional on "adds nothing here". |
| JTW-6.0c | §6 L94 | Phrases that add no point and only a feeling of "writing properly" (「ちゃんと書いている感」) are LLM tone; do not use them. | BOTH | Empty phrases make any text worse (rubric test 1). | "Cut a phrase if removing it loses no claim." |
| JTW-6.1 | §6 L96 | Previews and summaries: 「重要なのは〜である」「本章では〜を扱う／探求する」「ここでは〜について見ていく」「まとめると」「要するに」 (when they only rephrase what came before), 「〜に他ならない」. | BOTH | Empty previews and summaries are universal (rubric names them). | Internal conflict: the good example at L104 keeps 「本章では、〇〇の理論を扱う」. "Cut a preview that only names the topic the heading or next sentence already shows; keep a roadmap or scope statement that gives the order or what is excluded." Add JTW-5.7's exception. 「〜に他ならない」 is emphasis, not preview; judge it under JTW-6.3. |
| JTW-6.2 | §6 L97 | The 「正面から」 family (「正面から扱う／回収する／見る／書く／立てる」) declares a posture instead of content. | BOTH | Posture-only phrases are universal. | EN "tackle head-on"; ZH 正面回应. |
| JTW-6.3 | §6 L98 | Empty adjectives: 「不可欠」「核心的」「鍵となる」「根本的な」 (emphasis with no explanation), 「多角的」「包括的」「総合的」 (no account of what was examined and how). | BOTH | Universal. | "If the sentence does not say why it is essential or what was covered, replace the adjective with that content." |
| JTW-6.4 | §6 L99 | Empty verbs: 「掘り下げる」「深掘りする」「言語化する」 (no account of what was written and how), 「触れる」「言及する」 (when the treatment is one paragraph). | BOTH | Universal. | |
| JTW-6.5 | §6 L100 | Connective patterns: 「〜において」「〜という側面から」「〜の観点から」 when they add no information, and strings of 「さらに」「また」「加えて」. | BOTH | Universal. | 「において」 is standard formal Japanese; flag it only when deleting it loses nothing. |
| JTW-6.6 | §6 L101 | Weak hedges and intensifiers: 「〜と言えるだろう」「〜かもしれない」 (only when they weaken a claim without grounds; keep them for conjecture, assumption, reader doubt, characters' perceptions), 「非常に」「極めて」「大いに」 (empty emphasis). | BOTH | Universal. | Already conditional. Overlaps JTW-2.1 and 8.12. |
| JTW-7.0 | §7 L108–109 | LLMs produce expressions that do not exist in Japanese by three routes; unlike empty phrases, these slip in without the writer meaning a metaphor, so check sentences you did not intend as figurative too. | BOTH | Human translators and bilingual writers produce the same unintended calques. | Drop the LLM framing: "Check literal sentences for figurative verbs you did not choose." |
| JTW-7.1 | §7 L111 | Literal translation of English idioms: carry/open/expose/live/land are conventional figurative uses in English tech text; translated literally into Japanese, they become odd live metaphors that readers take literally. | BOTH | The principle (use a figurative verb only if it is conventional in the language you are writing) holds in every language. | The word list → JA. Direction matters: these verbs are fine in EN text, and ZH has adopted some (暴露接口, 开放问题), so the JA list does not transfer. |
| JTW-7.1a | §7 L112 | Bad 「ベクトルが選好を運ぶ」 (carry); good 「選好がベクトルとして表現される」「ベクトルに反映される」. | JA | Word-level Japanese example. | |
| JTW-7.1b | §7 L113 | Bad 「この問いは開かれている」 (open question); good 「この問いにはまだ答えが出ていない」「未解決である」. | JA | Word-level Japanese example. | ZH 开放问题 is an established term; EN "open question" is idiomatic. |
| JTW-7.1c | §7 L114 | Bad 「推敲の軸が露出する」 (expose); good 「推敲の軸が線形に取り出せる」. | JA | Word-level Japanese example. | ZH 暴露 is conventional for APIs. |
| JTW-7.1d | §7 L115 | Bad 「この情報は残差ストリームに住んでいる」 (live in); good 「残差ストリームに含まれる」. | JA | Word-level Japanese example. | |
| JTW-7.2 | §7 L116 | Imported inanimate-subject constructions: inanimate-subject transitive sentences are normal in English, but in Japanese they make models, data, vectors and losses act with intent; restore a person or process as agent, or use 「〜から分かる」「〜に含まれる」. | JA | Depends on how far Japanese tolerates inanimate agents. | Conflicts with STE (active voice, explicit subject; "The data shows" is standard); resolved because the rule is JA-only. The universal kernel is split out as JTW-7.2a. |
| JTW-7.2a | §7 L117 | Bad 「モデルは文体を知っている」; good: state the checkable fact (「モデルの出力には文体の一貫性がある」). | TECH | Not ascribing mental states (knows, understands, wants) to software, and stating observable behavior instead, holds in EN and ZH technical text. | Personal writing tolerates playful anthropomorphism. Operational verbs ("returns", "sends") are unaffected. |
| JTW-7.2b | §7 L118 | Bad 「データが語るのは〜である」; good 「データから分かるのは〜である」. | JA | EN "the data shows" and ZH 数据表明 are normal. | |
| JTW-7.3 | §7 L119 | Spoken researcher jargon (「効く」「刺さる」「筋がいい」) is slang in written technical text; write the concrete effect or prospect. | TECH | The principle holds in EN and ZH ("X works", "has legs"; 好使, 有戏); personal writing allows a colloquial register. | Word list → JA/TECH. |
| JTW-7.3a | §7 L120 | Bad 「規範スキルが効く」; good 「規範スキルを与えると生成が選好に近づく」. | JA/TECH | Japanese word, technical register. | |
| JTW-7.3b | §7 L121 | Bad 「この手法は筋がいい」; good 「この手法は〜という理由で有望である」. | JA/TECH | Japanese word, technical register. | |
| JTW-7.4a | §7 L123–124 | Judgment test, step 1: if a reader meeting the predicate for the first time could picture the literal action (運ぶ, 開く, 住む), suspect a calqued metaphor. | BOTH | The literal-reading test is universal. | |
| JTW-7.4b | §7 L125–127 | Step 2: try restating actor and object in concrete words. If you can, write the restatement; if you cannot, the sentence does not say what it refers to and makes no claim, so cut it or settle the content and rewrite. | BOTH | Universal. | "For a sentence meant to make a claim." A deliberate image in a personal essay that is not a claim falls outside the test. |
| JTW-8.0 | §8 L131 | Leave as little useless text as possible. | BOTH | Universal. | |
| JTW-8.1 | §8 L133 | Do not repeat a claim in paraphrase; write each claim once. A sentence on the same topic that adds a different proposition is not repetition; neither are frame words repeated to mark list items of equal status, nor a sentence that adds conditions or limits right after a definition. | BOTH | Universal. | Add exceptions: deliberate summaries and abstracts, a warning repeated at the step it applies to (STE, procedures), rhetorical repetition in personal writing. |
| JTW-8.2 | §8 L134 | If adjacent sections say the same thing from different angles, their roles overlap; merge them into one section. | BOTH | Universal. | |
| JTW-8.3 | §8 L135 | Do not re-summarize a scene right after describing it; add only a one-sentence significance (「このような作業は、ほぼ完全に任せられる」). | BOTH | Universal. | |
| JTW-8.4 | §8 L136 | Put parallel facts with the same logical role into one sentence instead of stacking sentences, and mark their logical status with a sentence-initial word (「当然、経理部の月次処理も顧客の支払いも〜」). | BOTH | Universal. | Conflicts with STE (one instruction per sentence, length caps) in procedures. "If the facts share a role and the merged sentence stays readable; in procedure steps keep one action per sentence." |
| JTW-8.5 | §8 L137 | Do not judge redundancy by character or sentence count. Shorten or merge only if motive, object, operation, its identity, cause and condition stay explicit in in-order reading; do not compress them into reader inference; keep the repetition and length they need. | BOTH | Universal. | Tension with STE word caps and generic "be concise" rules; this rule is the right guard on them. |
| JTW-8.6 | §8 L138 | Do not place sentences that only connect or evaluate (「それ自体はよいことである」). | BOTH | Universal. | |
| JTW-8.7a | §8 L139 | Do not use an imagined Q&A with the reader (a question answered in one word) as rhetoric; state the claim. | TECH | In personal writing the device is a legitimate voice choice when used sparingly. | Not X-DEAI: in technical prose it delays the claim. In personal writing, frequency falls under JTW-5.0/5.1. |
| JTW-8.7b | §8 L139 | Do not act out the reader's reaction and answer it (「〜と感じたかもしれない。そのとおりである」); make concessions briefly in the narrative voice (「もちろん、処置そのものは開発者が決める問題ではない」). | TECH | Blog voice uses this device legitimately. | Example → JA. |
| JTW-8.8 | §8 L140 | Do not introduce an idea the reader might have through meta-framing (「ここまでの話には自然な続きがある」「〜という発想である」); write the idea itself. A reader's question may stay a question (「その保守も任せればよいのではないだろうか」). | BOTH | Universal. | |
| JTW-8.9 | §8 L141 | Do not defend or excuse the author's position (「本書もそれを否定しない」); give only the factual description (「〜に書かせる場合が多い」). | TECH | In personal writing the author's stance is part of the content. | Distinguish from scope statements ("This guide does not cover X"), which tech docs need. |
| JTW-8.10 | §8 L142 | Write so the reader gets the context by the shortest route; if the reader understands without a step-by-step derivation, name the structure and state it outright. | BOTH | Universal. | Already conditional; novice tutorials may need the steps. Balanced by JTW-8.5. |
| JTW-8.11 | §8 L143 | Do not bring up concepts or document names before you introduce them. | X-DUP | Same as JTW-2.10 (define before use). | Widen JTW-2.10 to "any concept or document name". |
| JTW-8.12 | §8 L144 | Do not settle for hesitant, weak predicates (「有効な対策であり」); state what the text's evidence establishes strongly and concretely (「活用において必須であり」); keep weak predicates that express uncertainty, possibility, assumption or reader doubt; deliberate softening for tone (「必須だと言ってもいい」) is allowed. | BOTH | Universal. | Overlaps JTW-6.6 and 2.1; tension with JTW-2.6 resolves on the evidence predicate. |
| JTW-8.13 | §8 L145 | Connectives that make rhythm (「しかし一方で」) do not count as redundancy. | JA | A rhythm judgment about a Japanese collocation; EN editors would cut "but on the other hand". | Tension with JTW-6.5. |
| JTW-9.0 | §9 L149 | A heading must identify the content specifically: a phrase naming the question the section answers or the object it treats. | BOTH | Universal. | Imperative task headings in procedures ("Install the CLI") name the reader's task and qualify. |
| JTW-9.1 | §9 L151 | No heading that only describes the author's operation (「例に戻す」「〜を読み直す」) or carries no information. | BOTH | Universal. | Do not confuse with reader-task headings. |
| JTW-9.2 | §9 L152 | Do not make a heading a 「セリフ」 that states the section's conclusion; do not let the reader learn the punchline from the heading. | BOTH | Holds for argumentative and narrative sections in both genres. | Conflicts with BLUF / assertion-heading norms in reference docs, reports and postmortems. "If the section builds an argument toward its conclusion, do not state the conclusion in the heading; in reference, report or skim-oriented docs, a heading that states the answer is fine." |
| JTW-9.3 | §9 L153 | A noun phrase naming the object the section treats is also fine. | X-DUP | JTW-9.0 already allows it. | |
| JTW-9.4 | §9 L154 | Question form or declarative form does not matter; what matters is whether the heading points to the object or to the reader's question. | BOTH | Universal. | A declarative heading still must not state the conclusion (JTW-9.2). |
| JTW-9.5 | §9 L155 | Choose a question or a noun phrase to match the tone of the body. | BOTH | Universal. | Some tech house styles reserve question headings for FAQs; defer to the house style. |
| JTW-10.1 | §10 L159 | If an example may look contrived, do not hide it; acknowledge the reader's suspicion up front and briefly give grounds that it is realistic. | BOTH | Universal. | Placement: JTW-1.5. |
| JTW-10.2 | §10 L160 | Base those grounds not on the author's assertion (「十分あり得る状況だ」) but on general facts or common sayings that appeal to the reader's own experience (「この症状は珍しくないだろう」「〜という言い方もよく耳にする」). | BOTH | Universal. | Conflicts with vague-attribution rules (rubric test 1; deslop "people often say"). "Use this only to make a scenario's plausibility checkable against the reader's experience, never to support a factual claim." |
| JTW-10.3 | §10 L161 | Do not write unverified things smoothly, as if verified. | BOTH | Universal. | |

## Conflicts found

1. **Subject omission versus explicit subjects.** JTW-1.8e (inherit the subject, do not name it again) and JTW-7.2 (rewrite inanimate-subject sentences as 「〜から分かる」, which has no subject) conflict with STE ("do not omit subjects"; active voice with a stated agent, under which "The data shows ..." is fine). **Resolution:** both JTW rules are JA. Japanese topic continuity licenses the omission, and EN and ZH keep their own rules. JTW-4.1 (actor as subject, active chain) agrees with STE.
2. **Command-form warnings.** JTW-5.4 prefers 「〜するわけにはいかない」 over 「〜してはならない」; STE requires warnings to start with a command ("Do not ..."). **Resolution:** JA, and within JA limited to explanatory prose; warnings and procedure steps keep the command form.
3. **Consequences in warnings.** JTW-5.6 (do not list consequences to stoke fear) against the STE / safety-warning format, which states hazard and consequence. **Resolution:** conditional wording ("do not stack consequences for effect; in a warning, state hazard, consequence and avoidance once"); stays BOTH.
4. **Second person.** JTW-4.3 (no 「あなた」; use role names) against EN tech style guides that address the reader as "you". **Resolution:** JA. Japanese 「あなた」 is marked; ZH 你 and EN "you" are not.
5. **Sentence merging and brevity.** JTW-8.4 (merge parallel facts into one sentence) and JTW-8.5 (do not judge redundancy by length) against STE's one instruction per sentence and its word caps. **Resolution:** conditional; procedure steps keep one action per sentence. JTW-8.5 is the right guard on generic "be concise" rules.
6. **Substitution word order.** JTW-3.6e ("later-written = adopted", from 「Aの代わりにB」) against EN and STE command-first style ("Use B instead of A"). **Resolution:** JA.
7. **Internal: previews.** JTW-6.1 lists 「本章では〜を扱う」 as an empty preview, but the source's own good example (L104) is 「本章では、〇〇の理論を扱う」. **Resolution:** condition the rule on whether the preview adds anything (order, scope, exclusions) beyond the heading.
8. **Internal: certainty.** JTW-8.12 (assert strongly) against JTW-2.6 (never write "always") and JTW-2.1/6.6 (keep justified hedges). **Resolution:** all three key on the same predicate, "does evidence in the text settle the proposition?"; no reclassification needed.
9. **Internal: connectives.** JTW-1.3 (open paragraphs with connectives) and JTW-8.13 (rhythm connectives are not redundant) against JTW-6.5 (strings of 「さらに」「また」「加えて」) and deslop transition-overuse rules. **Resolution:** the connective must name a specific relation; JTW-8.13 stays JA.
10. **"Not A but B".** JTW-1.6/1.7 recommend explicit negation of a misreading; JTW-5.8 and deslop rules limit the "It's not X, it's Y" pattern. **Resolution:** frequency plus the predicate "a likely misreading, with the ground given".
11. **Vague attribution.** JTW-10.2 recommends 「〜という言い方もよく耳にする」 as grounds; the rubric and deslop rules treat vague attributions as bad writing. **Resolution:** allow it only to support a scenario's plausibility against the reader's own experience, never a factual claim.
12. **BLUF and front-loading.** JTW-1.4 (conclusion once, after objections), JTW-1.10 (do not pre-reveal climax figures) and JTW-9.2 (no conclusion headings) against summary-first norms in design docs, reports, postmortems and reference docs. **Resolution:** conditional on "a passage that builds an argument or narrates a scene"; kept BOTH rather than PERSONAL because technical books and articles contain such passages.
13. **Identifiers.** JTW-3.2 (omit names the reader will not need) against procedure and reference norms that name the exact file or command. **Resolution:** conditional on "reader will type, search for or refer back to it"; TECH.
14. **Exclamation marks.** JTW-5.5 tolerates 「！」 at a climax; most tech style guides ban "!" in docs. **Resolution:** limit to narrative article or book prose.
15. **Calque lists across languages.** JTW-7.1a–d assume English → Japanese. ZH has adopted 开放问题 and 暴露 (API), so the JA list must not be copied into writing-zh; only the literal-reading test (JTW-7.4) is shared.

## Rules whose absolute wording should become conditional

| ID | Conditional form |
|---|---|
| JTW-1.0 | In expository or argumentative passages, make each paragraph one step of the argument. |
| JTW-1.2 | In expository text, let the first sentence name the paragraph's topic. |
| JTW-1.3 | If the relation to the previous paragraph is not evident from the content, open with a connective that names it; do not add purely additive connectives. |
| JTW-1.4 | State the conclusion once. If the argument builds to it, handle objections first; if the genre puts the conclusion first, lead with it and handle objections after without restating it. |
| JTW-1.5 | If a passage narrates a scene, put caveats about the example after the scene ends. |
| JTW-1.6 | If a reader is likely to form a specific misreading, negate it explicitly, then give the real reason. |
| JTW-1.10 | If a passage builds to a result, do not reveal the result's key figure before it lands; in summaries, reference docs and procedures, put key facts first. |
| JTW-2.5 | If the mechanism is not obvious to the target reader, state it in one sentence. |
| JTW-2.9 | After a concession, say what it changes for the claim, unless the open ending is deliberate. |
| JTW-3.2 | If the reader will not type, search for or refer back to a name, describe the thing generically. |
| JTW-4.1 | If the actor is known and matters, make it the subject of an active verb chain. |
| JTW-4.2 | If a persona's attributes do not affect the example, drop the persona. |
| JTW-4.5 | Once you define a term, use that term throughout. |
| JTW-5.3 | Use bold for emphasis only at logical key points (guideline: one or two per section); typographic bold for UI labels is out of scope. |
| JTW-5.4 (JA) | In explanatory prose, prefer 「〜するわけにはいかない」; in warnings and procedure steps, keep the command form. |
| JTW-5.5 | Tolerate an exclamation mark only at the climax of narrative prose, never in reference docs, UI or error text. |
| JTW-5.6 | Do not stack consequences for effect; in a warning, state hazard, consequence and avoidance once. |
| JTW-5.9a | In technical text, do not twist idioms. |
| JTW-6.1 | Cut a preview or summary only if it adds nothing beyond the heading or the previous sentence; keep roadmaps and scope statements. |
| JTW-6.3 / 6.4 | If the sentence does not say why something is essential, or what was examined and how, replace the adjective or verb with that content. |
| JTW-6.5 | Flag 「において」 and similar frames only when deleting them loses nothing; flag additive connectives only when they repeat. |
| JTW-7.4b | Apply the restate-or-cut test to sentences meant to make a claim. |
| JTW-8.1 | Write each claim once, except deliberate summaries, warnings repeated at the step they apply to, and rhetorical repetition in personal writing. |
| JTW-8.4 | Merge parallel facts only if they share a role and the result stays readable; keep one action per procedure step. |
| JTW-8.7a | In technical prose, do not stage a question you answer in a word. |
| JTW-8.9 | Do not defend the author's position; scope statements are not defenses. |
| JTW-9.2 | If the section builds toward its conclusion, keep the conclusion out of the heading; in skim-oriented docs, a heading that states the answer is fine. |
| JTW-9.5 | Choose between question and noun phrase by tone, unless the house style restricts question headings. |
| JTW-10.2 | Appeal to the reader's experience only to support a scenario's plausibility, never a factual claim. |

## Language-specific examples to move

### JA (into writing-ja, attached to the universal rule they illustrate)

- JTW-1.3 / 1.8d: connectives 「であれば」「実際」「しかし」「この例自体からも」.
- JTW-1.6: 「その理由は『〜だから』ではない。〜だからだ」. JTW-1.7: counterfactual 「もしAなら、〜だっただろう」.
- JTW-1.8b: do not embed a definition in 「〜だと説明した」. JTW-1.8c: 「」 to cut out a phrase.
- JTW-1.9: 「確かに〜」; attribution 「〜と要約できてしまうかもしれない」.
- JTW-1.11: 「『明文化されていればすべてを任せられる』を意味しない」 versus 「何もかもが解決するわけではない」.
- JTW-2.1 / 6.6: hedges 「かもしれない」「だろう」「ようだ」「らしい」「〜と言えるだろう」; intensifiers 「非常に」「極めて」「大いに」; good example 「提示し続けている可能性がある」.
- JTW-2.2: 「同じ決定を別々に下していた」 → 「どれも別々の決定であり、しかも互いに依存している」.
- JTW-2.5: 「手順で分けると変更が全体に波及する」 → 「各工程がデータを受け渡すための表現を共有してしまい、…」.
- JTW-2.6: 「〜しやすい」「〜できることが多い」「〜が成り立つときに限り」. JTW-2.9: 「ただし」「とはいえ」.
- JTW-3.4: long pre-nominal modifier placed before the head noun (needs an example).
- JTW-4.1: 「特定され、判明した」 → 「リポジトリを調査して特定し、見つけてくれた」 (benefactive 〜てくれる).
- JTW-4.6: 「配信」 not 「配送」. JTW-4.8: 「経路」 → 「届くまでの流れ」.
- JTW-5.1: 「ここには〜が潜んでいる」. JTW-5.7 / 6.1: 「重要なのは〜である」, exception 「標語として言い換えれば」.
- JTW-5.9a/b: 「知識を体に入れる」→「身につく」; 「報告の外側に世界が広がっている」→「気付く機会が減る」.
- JTW-6.1–6.5: full phrase lists (「本章では〜を扱う／探求する」「ここでは〜について見ていく」「まとめると」「要するに」「〜に他ならない」「正面から〜」「不可欠」「核心的」「鍵となる」「根本的な」「多角的」「包括的」「総合的」「掘り下げる」「深掘りする」「言語化する」「触れる」「言及する」「〜において」「〜という側面から」「〜の観点から」「さらに」「また」「加えて」) and the bad/good pairs at L103–104.
- JTW-7.1a–d, 7.2b, 7.3a–b: the calque and jargon pairs (運ぶ, 開かれている, 露出する, 住んでいる, データが語る, 効く, 刺さる, 筋がいい).
- JTW-8.3: 「このような作業は、ほぼ完全に任せられる」. JTW-8.4: 「当然、経理部の月次処理も顧客の支払いも〜」. JTW-8.6: 「それ自体はよいことである」.
- JTW-8.7b: 「〜と感じたかもしれない。そのとおりである」 versus 「もちろん、処置そのものは開発者が決める問題ではない」.
- JTW-8.8: 「ここまでの話には自然な続きがある」「〜という発想である」; 「その保守も任せればよいのではないだろうか」.
- JTW-8.9: 「本書もそれを否定しない」. JTW-8.12: 「有効な対策であり」→「活用において必須であり」; 「必須だと言ってもいい」.
- JTW-9.1: 「例に戻す」「〜を読み直す」. JTW-10.2: 「十分あり得る状況だ」 versus 「この症状は珍しくないだろう」「〜という言い方もよく耳にする」.

### EN (none in the source; suggested analogs for the universal rules)

The English verbs carry/open/expose/live/land in JTW-7.1 are source-language notes for the JA calque list, not EN rules. Suggested EN examples:

- JTW-6.1: "It's important to note that", "In this section, we will explore", "In summary" (when it only restates).
- JTW-6.2: "tackle head-on", "squarely address". JTW-6.3: crucial, key, fundamental, comprehensive, holistic. JTW-6.4: delve into, unpack, touch on.
- JTW-6.5: "in terms of", "from the perspective of", chained Moreover/Furthermore/Additionally. JTW-6.6: arguably, very, extremely.
- JTW-7.3: "X works", "has legs". JTW-7.2a: "the model knows/understands/wants".
- JTW-1.8b: "As Section 2 showed, X is Y" versus "We explained that X is Y". JTW-5.2b analog: verbless fragment at a climax.

### ZH (none in the source; suggested analogs)

- JTW-6.1: 值得注意的是, 本文将探讨, 总而言之. JTW-6.2: 正面回应, 直面. JTW-6.3: 至关重要, 核心, 全面, 多维度. JTW-6.4: 深入探讨, 浅谈.
- JTW-6.5: 在……方面, 从……角度来看, chained 此外/另外. JTW-6.6: 可以说, 非常, 极其.
- JTW-7.3: 好使, 有戏. JTW-4.6: 推送, not 投递.
- JTW-3.4: long 的-chains before the head noun.
- Do not port JTW-7.1a–d: 开放问题 and 暴露 (API) are established in Chinese technical text.
