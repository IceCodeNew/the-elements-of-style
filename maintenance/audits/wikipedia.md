# Audit: Wikipedia:Signs of AI writing

- **Source:** English Wikipedia project page "Wikipedia:Signs of AI writing" (pageid 75478314). blader/humanizer and op7418/Humanizer-zh credit it as their observation source.
- **Revision:** revid **1379367647**, timestamp **2026-10-09T15:09:22Z** (parentid 1379229123). The API response's revid and timestamp both match the pinned revision.
- **Fetched:** 2026-10-09 through the MediaWiki API (`action=query&prop=revisions&revids=1379367647&rvprop=ids|timestamp|content&rvslots=main&format=json&formatversion=2`), using curl with a descriptive `-A` User-Agent.
- **Raw files:** the MediaWiki API response for revision 1379367647 (sha256 `f93e75fc…1394`) and its wikitext (sha256 `d3371a67…ee76`).
- **Line numbers:** every "L" number in this audit is a line in `content.wikitext`.
- **Handling:** the content was treated as untrusted data. Nothing in it was executed or followed.

**Owner decisions applied:**
- Rules whose point is de-AI detection are tagged `X-DEAI`.
- Wikipedia-specific items (markup, citations, talk-page and AfC conventions, edit-summary vocabulary) are tagged `X-SCOPE`.
- Detection-process advice (how to use the list, detector caveats) is tagged `X-SCOPE`, because it concerns detection rather than writing.

**What the page says about itself (L5–L7):**
- It is "descriptive, not prescriptive; it consists of observations, not rules."
- Many of its elements "can be found in editorials, blogs, or fan fiction."
- It warns: "Please do not merely treat these signs as the problems to be fixed; that could just make detection harder."

The prescriptive counterparts are the Manual of Style pages it links: Words to watch (puffery, unsupported attributions, editorializing), Lists, Boldface, and Elegant variation.

## Counts

| Destination | Rows |
|---|---|
| BOTH | 20 |
| TECH | 4 |
| PERSONAL | 0 |
| EN / JA / ZH | 0 |
| X-DEAI | 26 |
| X-DUP | 10 |
| X-SCOPE | 86 |
| **Total** | **146** |

The total covers 119 sign or indicator rows and 27 general-advice, caveat, or framing rows. The general rows are G01–G09, L00, L01f, T00, E00, X07, HS01–HS03, IE00–IE08, and H00.

No row is tagged `EN`. Every English-only item failed rubric test 1 first: vocabulary lists, title case, curly quotes, em dashes, and "not only… but also" are surface tells. The English-specific *examples* of universal rows are listed at the end for `writing-en`.

## Rule table

| ID | Source location | Rule (short paraphrase, or quote if short) | Destination | Reason (one clause) | Conditional wording / notes |
|---|---|---|---|---|---|
| WP-G01 | Lead, L5 | The page is a field guide for spotting undisclosed AI text *on Wikipedia*. Some signs may not apply elsewhere, and it is less useful for non-informational writing (fiction tells are omitted). | X-SCOPE | Scope of the catalog, not a writing rule. | The source claims nothing about genres other than encyclopedic writing. Any personal-genre use needs its own justification. |
| WP-G02 | Lead, L5 | "Not all text featuring these indicators is AI-generated." LLMs learned from human writing, and many of these traits appear in editorials, blogs, and fan fiction. | X-SCOPE | Detection caveat. | A page-level statement that humans write this way too. It supports keeping only substance rules and excluding surface tells. |
| WP-G03 | Lead, L7 | The list is "descriptive, not prescriptive… observations, not rules". Advice on language to avoid belongs in the policies, guidelines, and Manual of Style. | X-SCOPE | Meta-statement about the page. | Where a rule below is kept, the citable prescriptive source is the linked MOS page, not this page. |
| WP-G04 | Lead, L7 | Signs are not the problem itself. "Do not merely treat these signs as the problems to be fixed; that could just make detection harder." Fix the deeper issues instead. | X-SCOPE | Cleanup workflow, not writing. | Conflicts with the humanizer premise of rewriting surface tells (see Conflicts, item 1). Supports the owner's X-DEAI decision. |
| WP-G05 | Lead, L9 | Speedy-deletion criterion G15 uses only the most objective signs. The other signs are not sufficient on their own. | X-SCOPE | Wikipedia deletion policy. | |
| WP-G06 | Lead, L11 | The most common signs in October 2026: Markdown, AI edit summaries, hedging disclaimers about sources, vague connection or association, and canned attribution or media-coverage emphasis. | X-SCOPE | Frequency ranking for detection. | Three of the five also yield good-writing rules below: WP-C02, WP-C05, WP-U02. |
| WP-G07 | Caveats › AI detection tools, L14–17 | Do not rely solely on detectors such as GPTZero or Pangram. Their error rates are non-trivial, paraphrasing, markup, or unseen models fool them, and a detector score is not a G15 criterion. | X-SCOPE | Tooling. | |
| WP-G08 | Caveats › Your detection ability, L19–24 | Do not over-trust your own judgment. Humans detect AI text at near chance. Heavy LLM users do much better (90% hit rate, 3.3% false positives). | X-SCOPE | Detection process. | |
| WP-G09 | Caveats › Your detection ability, L26 | Human speech and writing are converging toward LLM word choice. LLM output is not converging toward human style. | X-SCOPE | Detection caveat. | Word-level tells will increasingly misfire on human text, which is another reason to keep vocabulary rows X-DEAI. |
| WP-C00 | Content (intro), L31–35 | LLMs regress to the mean. They replace specific, unusual facts with generic positive descriptions ("inventor of the first train-coupling device" becomes "a revolutionary titan of industry"), so the subject becomes "less specific and more exaggerated". | BOTH | Swapping a generic, inflated description for the specific fact improves any careful human's text. | **Conditional:** "If a description would fit many subjects, replace it with the fact that fits only this one."<br>**JA:** holds (具体的に書く).<br>**ZH:** holds (against 空话/套话).<br>**PERSONAL:** concrete detail is central to essays. |
| WP-C01 | Content › Undue emphasis on significance, legacy, and broader trends, L37–40 | Puffs up importance by saying an arbitrary detail "represents" or "contributes to" a broader topic ("marking a pivotal moment", "is a testament to", "reflects broader…", "setting the stage for"). | BOTH | Unsupported significance claims weaken any text (rubric test 1 names inflated significance). | **Conditional:** "If you claim significance, legacy, or a link to a broader trend, state the concrete consequence and its evidence; otherwise cut the claim."<br>**JA:** holds (〜を象徴する, 重要な役割を果たす, 転換点となった).<br>**ZH:** holds (具有重要意义, 标志着, 发挥了关键作用, 奠定了基础).<br>**Non-AI guideline:** MOS:PUFFERY.<br>**Examples:** to writing-en. |
| WP-C01a | Same section, L53 | Places the subject amid broader "debates", or says it "generated debate" or "prompted broader reflection", without naming who debated. | X-DUP | Same as WP-C01, plus the missing actor of WP-C06. | |
| WP-C01b | Same section, L67–73 | A hedging preamble concedes low importance ("Though it saw only limited application…") and then asserts importance anyway. | X-DUP | WP-C01 in concession form. | Same fix: support the claim or cut it. |
| WP-C01c | Same section, L76 | In biology topics, overstates ecosystem connections and dwells on conservation status or efforts, even when the status is unknown or no efforts exist. | X-DUP | Domain instance of WP-C01. The unknown-status padding is WP-U02. | |
| WP-C01d | Same section, L86 | (mid-2026) Pairs significance claims with hedging disclaimers and editorializes that a distinction or nuance "matters". | X-DUP | Announcing importance is WP-H02. | |
| WP-C02 | Content › Canned emphasis on notability, attribution, and media coverage, L88–94 (see also L1642) | Tries to prove notability by listing where the subject was covered and classifying the sources ("independent coverage", "regional media outlets", "trade publications", "featured in … and other prominent media outlets"). It alludes to coverage but does not say what the coverage says. | BOTH | Content-free name-dropping of sources weakens a careful human's prose too. | **Conditional:** "If you cite coverage as evidence, say what the coverage reports; do not substitute a list of outlets or source categories."<br>**Page caveat:** the narrow tell is the idiosyncratic phrasing and the echo of Wikipedia notability jargon. Human press releases have listed clippings for decades. Those phrasing and jargon tells are X-DEAI and X-SCOPE; only the substance rule is kept.<br>**JA:** holds (多数のメディアで紹介された).<br>**ZH:** holds (受到多家主流媒体广泛报道). |
| WP-C02a | Same section, L92; Superficial analyses, L134 | Attributes the writer's own analysis to a source that does not say it ("Roger Ebert highlighted the lasting influence…"). | BOTH | Accurate attribution is good writing anywhere. | **Conditional:** "Attribute a claim to a source only if that source makes it; mark your own interpretation as yours."<br>Language-independent. |
| WP-C02b | Same section, L96 | "maintains an active social media presence" | X-DEAI | Phrase-level tell (rare on Wikipedia before about 2024). | Any real problem is covered by WP-C04 and WP-C00. |
| WP-C03 | Content › Superficial analyses, L129–134 | Appends shallow interpretive tails, often trailing "-ing" clauses ("…, highlighting its significance", "…, contributing to the socio-economic development of the region"). These amount to synthesis or unattributed opinion. | BOTH | Unsupported interpretive add-ons weaken any text. | **Conditional:** "If an appended clause interprets a fact (impact, what it reflects or highlights), keep it only when it is specific and supported; otherwise cut it."<br>The "-ing participle" form is English grammar, so the examples go to writing-en.<br>**JA:** holds (〜しており、〜を示している; 〜を物語っている).<br>**ZH:** holds (……，彰显了……; ……，体现了……).<br>**PERSONAL:** earned, specific interpretation is welcome; generic tails are the target. |
| WP-C04 | Content › Promotional and advertisement-like language, L185–190 | Cannot keep a neutral tone and drifts into ad or travel-guide prose ("boasts", "vibrant", "rich", "nestled", "in the heart of", "groundbreaking", "renowned", "diverse array"). | BOTH | Stock praise improves no careful human's text (MOS:PUFFERY). | **Conditional:** "If an evaluative word is backed neither by a stated fact nor by the writer's own, explicitly personal judgment, replace it with the fact."<br>Strict neutrality is a TECH and encyclopedic norm. Personal writing may evaluate, but in the writer's own specific terms, not stock praise.<br>**Page caveat:** "Not all promotional or spammy writing is AI-generated." Newer LLMs are subtly positive.<br>**JA:** holds (〜を誇る, 風光明媚な).<br>**ZH:** holds (坐落于, 闻名遐迩, 历史悠久-style four-character praise). These idioms are conventional in tourism copy, a genre outside both skills. |
| WP-C04a | Same section › Subtypes, L194 | For "cultural heritage" topics, repeatedly reminds the reader of their importance. | X-DUP | WP-C01. | |
| WP-C04b | Same section › Subtypes, L207 | For people and companies, adopts a press-release tone ("emphasized the airline's commitment to sustainability…"). | X-DUP | WP-C04. | |
| WP-C05 | Content › Vague expression of connection or association, L221–225 | Says two things are "associated with", "connected to", or "in connection with" each other instead of stating the relation ("was the CEO of", "taught science at"). | BOTH | Naming the actual relation improves any text. | **Conditional:** "If you know the relationship (role, action, cause), state it; use 'associated with' only for a genuinely unknown link or a statistical association."<br>**TECH exception:** "associated with" is precise in statistics and in file or config associations.<br>**JA:** holds (〜に関連して, 〜と関わりのある).<br>**ZH:** holds (与……相关, 与……有关联, 涉及). |
| WP-C06 | Content › Vague attributions and overgeneralization of opinions, L263–267 | Attributes claims to vague authorities ("Industry reports", "Observers have cited", "Experts argue", "Some critics argue"). Presents one or two sources as widely held, or cites one person while mentioning "scholars". | BOTH | Weasel wording weakens any text (rubric test 1). | **Conditional:** "If you attribute a view, name who holds it; if you quantify support (many, several, widely), make the count match the sources."<br>**JA:** holds (〜と言われている, 〜とされる, 専門家は〜と指摘する).<br>**ZH:** holds (有专家指出, 业内人士认为, 普遍认为). Journalistic 据悉 and 据了解 are conventional for unnamed sources; even there, name the source or say why it is anonymous. |
| WP-C06a | Same section, L266–267 | Uses "such as", or otherwise implies a list is incomplete, when the list is exhaustive or the sources show no other examples. | BOTH | Implying items that do not exist misleads in any text. | **Conditional:** "If the list is complete, don't mark it as partial (such as, including, etc.)."<br>**ZH:** 等 plus a count closes a complete list (京、津、冀等三地), so it is not a violation. 等 without a count implies more items.<br>**JA:** など often softens even a complete list, and JA tech style guides advise dropping it then. Notes for writing-zh and writing-ja. |
| WP-C07 | Content › Outline-like conclusions about challenges and future prospects, L289–294 | A rigid "Despite its [praise], X faces several challenges…" paragraph or section. It ends with a vague positive verdict or with speculation about future initiatives ("Future Outlook"). | BOTH | Formulaic upbeat endings and speculation weaken human reports and essays too. | **Page caveat:** "This sign is about the rigid formula, not simply the mention of challenges."<br>**Conditional:** "If you include challenges or outlook, name specific, sourced problems and concrete plans; drop the closing reassurance ('Despite these challenges, X continues to thrive') and unsupported predictions."<br>**JA/ZH:** 今後の課題と展望 and 挑战与展望 are legitimate conventional closing sections. Do not ban the section, only the vague formula. |
| WP-C08 | Content › "Awards and recognition" section, L341–345 | "X and Y" headings, especially "Awards and recognition" or "Recognition", are near-ubiquitous in AI articles. | X-DEAI | Frequency tell based on heading wording. The page grants that humans also write legacy and impact sections. | The substance is covered by WP-C01 and WP-C02. |
| WP-L00 | Language and grammar (intro), L347–348 | AI text shows consistent syntactic and lexical patterns, an identifiable "voice". Models differ, and GPT-4o deviates most from human text. | X-SCOPE | Framing; no rule. | |
| WP-L01 | Language and grammar › High density of "AI vocabulary" words, L350–355 | LLMs overuse words from a research-backed list (Additionally, align with, boasts, bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight, interplay, intricate, key, landscape, meticulous, pivotal, robust, showcase, tapestry, testament, underscore, valuable, vibrant). One or two is coincidence; many is "one of the strongest tells". | X-DEAI | Frequency tell for English words. | Not tagged EN because rubric test 1 comes first.<br>Several of these words are legitimate technical terms (key, robust, landscape orientation, leverage, highlight as a UI action, underscore the character), so a ban would harm TECH text.<br>The promotional words (boasts, vibrant, tapestry) are already covered by WP-C04 and WP-C01. |
| WP-L01a | Same section, L359 | Word set for 2023 to mid-2024 (GPT-4). | X-DEAI | Era-specific tell. | |
| WP-L01b | Same section, L360 | Word set for mid-2024 to mid-2025 (GPT-4o). | X-DEAI | Era-specific tell. | |
| WP-L01c | Same section, L361 | Word set for mid-2025 to mid-2026 (GPT-5): emphasizing, enhance, highlighting, showcasing, plus the notability and attribution words. | X-DEAI | Era-specific tell. | |
| WP-L01d | Same section, L362 | Mid-2026 onward (GPT-6): challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally. Also more periods and commas, and sentences held to a strict 8–20 words. | X-DEAI | Era-specific statistical tell. | Conflicts with plain-language advice to write short sentences (Conflicts, item 2). The source for this bullet is a single review site. |
| WP-L01e | Same section, L364 | Word distribution differs by model. Grok overuses pseudo-scientific words (causal, empirical, correlate) and still overuses "underscore". | X-DEAI | Model-specific tell. | |
| WP-L01f | Same section, L366 | Read the list literally: a word's overuse does not imply its synonyms are overused. Mind context, such as a literal underscore or "underscore" in music. | X-SCOPE | Guidance on using the list. | The page itself warns against generalizing word lists. |
| WP-L02 | Language and grammar › Avoidance of basic copulatives, L400–406 | Replaces plain is, are, or has with "serves as", "stands as", "marks", "represents", or "boasts", "features", "offers". Also uses longer detours ("ventured into politics as a candidate" instead of "was a candidate"). | BOTH | Inflated substitutes for the plain verb weaken any text (a standard plain-language edit). | **Conditional:** "If 'serves as', 'functions as', or 'represents' means only 'is' (or 'features', 'offers', 'boasts' means only 'has'), use the plain verb; keep 'serves as' when the subject fills a role it does not inherently have."<br>The page notes that AI copyedits "improve" text in this direction.<br>**JA:** holds (〜として機能する, 〜の役割を担う, 〜を有する versus である, がある).<br>**ZH:** holds (作为……, 扮演……角色, 拥有, 具备 versus 是, 有). |
| WP-L02a | Same section, L408 | In lead sentences, uses "refers to" as though the article were about the word rather than the subject. | X-SCOPE | Wikipedia lead convention. | "X refers to Y" is legitimate in glossaries and term definitions. |
| WP-L03 | Language and grammar › Negative parallelisms (intro), L419–422 | Contrast framing that seems to correct a misconception the reader may not hold. Page: "common among human writers… it is stereotypically an 'AI sign.'" | BOTH | Refuting a view no reader holds wastes words and talks down; this is a content fault, not just a tell. | **Conditional:** "Use a 'not X but Y' contrast only when readers plausibly believe X; otherwise state Y directly."<br>**TECH:** "A container is not a VM" is fine when readers confuse the two.<br>**PERSONAL:** a single deliberate antithesis is a legitimate device; the fault is the reflexive one.<br>**JA:** holds (〜ではなく〜だ). **ZH:** holds (不是……而是……). |
| WP-L03a | Same section › Not just X, but also Y, L424–457 | Overuses "Not only … but …" and "It is not just …, it's …", including versions spread across sentences with "however". | X-DEAI | Construction-frequency tell; careful humans use these correlatives legitimately. | ZH 不仅……而且/更…… and JA 〜だけでなく〜も are standard connectives, so a ban would conflict with ZH and JA norms. The substance is in WP-L03. |
| WP-L03b | Same section › Not X, but Y, L459–483 | Overuses "It's not …, it's …" and "no …, no …, just …". | X-DEAI | Construction tell. | Substance in WP-L03. |
| WP-L03c | Same section › Y rather than X, L485–489 | The reversed form ("prioritizing X rather than Y"), common in recent output. | X-DEAI | Construction tell. | Substance in WP-L03. |
| WP-L04 | Language and grammar › Leads treating Wikipedia lists or broad article titles as proper nouns, L491–506 | The first sentence defines a list or a descriptive title as if it were a real-world entity ("The 'List of songs about Mexico' is a curated compilation…"). | X-SCOPE | Wikipedia lead and MOS convention. | |
| WP-L05 | Language and grammar › Rule of three, L508–512 | Overuses triads (three adjectives, three short phrases), often to make shallow analysis look comprehensive. The sign is stronger in terse contexts such as edit summaries. | X-DEAI | The owner names this as a frequency-tell example. | The padding residue ("don't add an item just to make three") is covered by WP-C03 and WP-C00, not by a triad ban. |
| WP-S01 | Style › Title case, L532–533 | Puts section headings in title case. | X-DEAI | A house-style choice careful humans make legitimately (Chicago headline style). | Applies to English only, since JA and ZH have no letter case. A sentence-case preference would be an EN house-style decision, not a rule from this page. |
| WP-S02 | Style › Overuse of boldface, L545–548 | Bolds mechanically, often every instance of a chosen phrase in "key takeaways" style. The page traces the habit to READMEs, fan wikis, how-tos, slide decks, and listicles. | BOTH | Over-bolding hurts any text, and the page itself traces it to human genres. | **Conditional:** "Bold only what a scanning reader must not miss (a warning, a term at its definition, UI labels where house style requires it); never every occurrence of a term."<br>**JA/ZH:** bold renders poorly in Mincho and Song faces, and traditional emphasis uses 傍点 (JA) or 着重号 (ZH). The principle of sparing emphasis still holds. |
| WP-S03 | Style › Inline-header vertical lists, L559–562 | Lists where each item starts with a bold inline header and a colon, followed by description, even for narrative content. | BOTH | Chopping connected reasoning into labeled fragments hurts any text (MOS: use prose where understood easily). | **Conditional:** "If items are parallel, independent, and looked up (options, parameters, glossary entries), an inline-header list is fine; if they form a narrative or argument, write paragraphs."<br>The TECH exception is essential.<br>**JA:** holds (**項目**：説明). **ZH:** holds (**标题**：说明). |
| WP-S03a | Same section, L564 | Uses bullet characters (•, -, –, #, emoji) or typed numbers instead of wikitext list markup; formatting is lost when copied. | X-SCOPE | Wikipedia markup. | |
| WP-S03b | Same section, L605 | Puts no punctuation between the inline header and the text. | X-DUP | A variant of WP-S03. | The page's XfD "!vote" bolding contrast is a Wikipedia convention. |
| WP-S04a | Style › Heading errors › Title heading, L650–651 | Puts a heading with the article name before the content. | X-SCOPE | Wikipedia page-title mechanics. | An H1 title is normal in Markdown documents. |
| WP-S04b | Style › Heading errors › Skipping heading levels, L659–660 | Starts sections at level 3, skipping level 2, against accessibility conventions. | BOTH | A skipped heading level breaks the document outline and screen-reader navigation in any structured text. | Auditor's generalization of a wikitext quirk.<br>**Conditional:** "If the text uses headings, nest them one level at a time."<br>Language-independent. Mostly relevant to TECH, and harmless for headed blog posts. |
| WP-S04c | Style › Heading errors › Overuse of level 1 headings, L665–668 | Uses level-1 headings, which Wikipedia reserves for the page title (probably translated from Markdown). | X-SCOPE | Wikipedia markup. | |
| WP-S04d | Style › Heading errors › Headings only containing other headings, L692–693 | A heading with no text of its own, followed directly by a subheading (a "stacked heading"). | TECH | Tech style guides discourage stacked headings; personal formats rarely have heading hierarchies. | **Conditional:** "If a heading has subheadings, put at least one sentence under it that introduces them."<br>Language-independent. |
| WP-S05 | Style › Emoji as formatting, L706–708 | Places emoji in front of headings or bullets, mostly in talk pages and edit summaries. Rarer now. | X-DEAI | The owner names emoji bans aimed at chatbot output as X-DEAI. | Social posts use emoji legitimately. |
| WP-S06 | Style › Unusual use of tables, L767–769 | Builds small, minimally formatted tables that would read better as prose (or as an infobox). | BOTH | A table for data that fits in one sentence slows any reader. | **Conditional:** "Use a table when readers compare several items across two or more attributes; if it has a few rows and one value column, write a sentence or list."<br>The infobox alternative is Wikipedia-only. One page example (the Xorai comparison, 4–5 rows × 3 columns) would pass this condition in tech docs.<br>Language-independent. |
| WP-S06a | Same section, L843 | Puts Markdown table syntax inside wikitables, which renders as garbage. | X-SCOPE | Markup. | |
| WP-S07 | Style › Curly quotation marks and apostrophes, L845–850 | ChatGPT and DeepSeek use curly quotes and apostrophes, sometimes inconsistently. | X-DEAI | The owner names curly quotes. The page says "Curly quotes alone do not prove LLM use" (Chicago, Word, and macOS/iOS smart quotes produce them). | ZH standard punctuation (GB/T 15834) uses “ ” and ‘ ’, and JA uses 「」, so a straight-quote rule would be wrong there. |
| WP-U01 | Communication intended for the user › Collaborative communication, L853–856 | Pasted chatbot correspondence, prewriting, or advice left in articles or comments ("I hope this helps", "Certainly!", "Would you like…", "let me know", "Here is a…"). | X-DEAI | The owner names "Certainly!" and "I hope this helps". | One example (L861, "In this section, we will discuss…") is an empty preview phrase, a good-writing fault under rubric test 1. The page does not state it as a rule, so take that rule from another source. |
| WP-U02 | Communication intended for the user › Hedging disclaimers about source availability and recommended usage, L923–927 | When it cannot find information, claims it is "not widely documented" or "limited in the provided sources", then speculates about what it "likely" is (for people: "maintains a low profile"). | BOTH | Guesses presented as content, and filler about missing information, hurt any text. | **Conditional:** "If a fact is unknown, omit it, or state the gap once when the gap matters to the reader (e.g., 'the vendor does not document the rate limit'); never follow it with speculation presented as fact."<br>**TECH:** stating that a behavior is undocumented is useful information.<br>**JA:** holds (詳細は明らかになっていないが、〜と考えられる). **ZH:** holds (目前公开资料有限，但……可能……). |
| WP-U02a | Same section, L929 | (mid-2026) Adds disclaimers about how to read sources ("should be treated as religious tradition rather than as an archaeological explanation"; "does not by itself establish…"). | X-DUP | WP-H02 (unsolicited caution to an imagined reader), plus the straw-man contrast of WP-L03. | In tech and science text, a limitation the reader would plausibly miss is legitimate (see the WP-H02 condition). |
| WP-U03 | Same part › Phrasal templates and placeholder text, L963–965 | Leaves Mad Libs-style placeholders unfilled ("[Your Name]", "[Describe the specific section…]", "(Add your channel URL here)"). | X-DEAI | A chatbot-template artifact, and reader-facing placeholders (`<your-api-key>`) are legitimate in tech docs. | The page notes that non-LLM article templates exist. |
| WP-U03a | Same section, L1000 | Puts placeholder dates ("2025-xx-xx") in citation access-date or date fields. | X-SCOPE | Citation template fields. | |
| WP-U03b | Same section, L1025 | Puts placeholders in other citation fields (`INSERT_SOURCE_URL_30`, `PASTE_SPOTIFY_TRACK_URL_HERE`). | X-SCOPE | Citation fields. | |
| WP-U03c | Same section, L1036 | Leaves infobox comments such as "Add if available with citation", or instructions to upload images to Commons. | X-SCOPE | Wikipedia infobox convention. | The page says to check whether the comment is the template's own boilerplate. |
| WP-M01 | Markup › Use of Markdown, L1043–1057 | Uses Markdown instead of wikitext. Markdown mixed with broken wikitext, or a ` ```wikitext ` fence, is a strong tell. | X-SCOPE | Wikipedia markup. | Page caveat: "Markdown alone is not such a strong indicator", since developers and writers use it widely. |
| WP-M01a | Same section › Misuse of asterisks, L1060–1062 | Uses `**text**` intending bold. | X-SCOPE | Markup. | |
| WP-M01b | Same section › Misuse of number signs, L1069–1071 | Uses `##` headings, which MediaWiki renders as a numbered list. | X-SCOPE | Markup. | |
| WP-M01c | Same section › Unusual link formatting, L1091–1092 | Formats links as `[text](url)`. | X-SCOPE | Markup. | |
| WP-M01d | Same section › Thematic breaks between sections, L1099–1100 | Puts `----` or `---` between every section. | X-SCOPE | Markup. | A general residue (separators redundant with headings) is too weak to propose. |
| WP-M02 | Markup › Broken wikitext, L1180–1181 | Produces faulty syntax, such as garbled AfC submission templates. | X-SCOPE | Markup. | |
| WP-M03 | Markup › Internal formatting and reference markup bugs, L1189–1191 | Leaked internal metadata is an "unambiguous indicator"; the exact bug varies by tool. | X-SCOPE | Tool artifacts. | |
| WP-M03a | Same section › ChatGPT, L1193–1194 | `:contentReference[oaicite:N]{index=N}`, `Example+1`, `oai_citation`. | X-SCOPE | Tool artifact. | |
| WP-M03b | Same section › ChatGPT, L1231–1233 | `citeturn0search0` (with Private Use Area characters), `turn0image…`, `citeturn0news0`, `citeturn1file0`, and the same strings as ref names. | X-SCOPE | Tool artifact. | |
| WP-M03c | Same section › ChatGPT, L1249 | `({"attribution":{"attributableIndex":"X-Y"}})` JSON at sentence ends. | X-SCOPE | Tool artifact. | |
| WP-M03d | Same section › Gemini, L1265–1267 | `[cite: 1]` and `[cite: 3, 12, 13]` markers. | X-SCOPE | Tool artifact. | |
| WP-M03e | Same section › Gemini, L1274 | `[span_1](start_span)` and `(end_span)`. | X-SCOPE | Tool artifact. | |
| WP-M03f | Same section › Grok, L1284–1286 | XML-style `grok_card` tags after citations. | X-SCOPE | Tool artifact. | |
| WP-M03g | Same section › Grok, L1293 | `grok_render_citation_card_json` in place of links. | X-SCOPE | Tool artifact. | |
| WP-M03h | Same section › DeepSeek, L1304–1305 | Lenticular brackets and daggers, such as `【85†L261-269】`. | X-SCOPE | Tool artifact. | |
| WP-M03i | Same section › Perplexity, L1324–1325 | `[attached_file:1]` and `[web:1]` at sentence ends. | X-SCOPE | Tool artifact. | |
| WP-M03j | Same section › Perplexity, L1331 | Citations pointing to S3 URLs that contain `ppl-ai-file-upload`. | X-SCOPE | Tool artifact. | |
| WP-M03k | Same section › Unclassified, L1336–1337 | `:::writing{variant="document" id="NNNNN"}` wrappers, seen since June 2026, also in localized form. | X-SCOPE | Tool artifact. | |
| WP-M04 | Markup › Non-existent or out-of-place categories, L1363–1367 | Adds hallucinated, renamed, or redirect categories, or broken forms such as "Category people". | X-SCOPE | Wikipedia categories. | Page caveat: humans make the same mistakes. Use only as corroborating evidence, except the "Category people" form. |
| WP-M05 | Markup › Non-existent templates, L1374–1375 | Uses hallucinated templates or parameters, or templates deleted after the model's cutoff. | X-SCOPE | Wikipedia templates. | Page: many broken templates are legitimate human mistakes. |
| WP-R01 | Citations › Broken external links, L1420–1423 | A new page has several dead links that were never archived. | X-SCOPE | Citation verification (owner: citations out of scope). | Caveats: paywalled or library-only links, bot-mangled URLs, and truncated pastes are human causes. |
| WP-R02 | Citations › Invalid DOI and ISBNs, L1425–1427 | Bad ISBN checksums or unresolvable DOIs suggest hallucinated references. | X-SCOPE | Citation verification. | |
| WP-R03 | Citations › DOIs that lead to unrelated articles, L1429–1442 | Valid-looking DOIs that resolve to unrelated papers. | X-SCOPE | Citation verification. | Caveat: a 2018–2023 VisualEditor bug produced irrelevant low-number PMIDs (a human cause). |
| WP-R04 | Citations › Book citations without page numbers or URLs, L1444–1462 | Cites books without page numbers, or with pages that do not verify the text. | X-SCOPE | Citation practice. | A universal residue for TECH and academic text ("cite precisely enough to verify") should come from a citation-focused source. |
| WP-R05 | Citations › Incorrect or unconventional use of references, L1464–1475 | Gets reference reuse syntax wrong, cites irrelevant sources, or repeats a reference after every full stop. | X-SCOPE | Wikipedia reference markup. | |
| WP-R05a | Same section, L1483 | `↩` back-reference characters around footnotes. | X-SCOPE | Copy artifact. | |
| WP-R06 | Citations › utm_source=, L1495–1499 | Cited URLs carry `utm_source=chatgpt.com`, `openai`, or `copilot.com`, or `referrer=grok.com`. | X-SCOPE | URL artifact. | Caveat: proves a tool found the source, not that it wrote the text. |
| WP-R07 | Citations › Named references declared in references section but unused, L1513–1514 | List-defined references that are never used inline, or named references that are never defined. | X-SCOPE | Wikipedia reference markup. | Human copy-paste can also cause this. |
| WP-T00 | Comment-specific indicators (intro), L1548–1553 | Suspected LLM comments may be collapsed with `{{collapse AI}}` or closed under the talk-page guidelines. | X-SCOPE | Wikipedia talk-page procedure. | |
| WP-T01 | Same section, L1554 | Misquotes policies and cites made-up shortcuts. | X-SCOPE | Wikipedia policy citation. | |
| WP-T02 | Same section, L1555 | Transcludes maintenance banners whenever it mentions them. | X-SCOPE | Wikipedia markup. | |
| WP-T03 | Same section, L1556 | Posts long comments split into titled sections (Markdown, plain text, or level-2 or level-3 subheadings). | X-SCOPE | Talk-page convention. | A residue ("a conversational reply is prose") is plausible for PERSONAL. But long code-review comments legitimately use headings, so it is not proposed from this source. |
| WP-T04 | Same section, L1557 | Downplays LLM use by claiming human effort, or that the comments reflect the editor's own thoughts. | X-SCOPE | Behavior, not writing. | |
| WP-T05 | Same section, L1558 | Asks critics or other editors to say exactly what needs improving. | X-SCOPE | Behavior. | |
| WP-T06 | Same section, L1559 | Dismisses concerns about origin as "unsubstantiated speculation" that lacks "concrete" evidence. | X-SCOPE | Behavior. | |
| WP-T07 | Same section, L1560 | Urges critics to focus on improving the content instead of on its AI origin. | X-SCOPE | Behavior. | |
| WP-T08 | Same section, L1562 | Uses a clerk or customer-service register: "carefully reviewed", apologizing for inconvenience it "may have" caused, "If there are specific issues…, please point them out". | X-DEAI | Register tell, which the page links to tools marketed for work. | A residue for error and incident text (replace a generic apology with what happened and what to do) belongs to error-message rules from other sources. |
| WP-T09 | Same section › Links to searches, L1565 | "I understand [the/your] concern(s) [about/regarding] AI-generated…" | X-SCOPE | A search query for Wikipedia replies to AI accusations. | |
| WP-T10 | Same section › Links to searches, L1566–1568 | "Dear Wikipedia Editorial Team", "I am writing to…", "I hope/trust this message finds you well." | X-DEAI | Letter formulas that humans legitimately use in letters. | |
| WP-E00 | Edit summaries (intro), L1570–1576 | AI edit summaries follow rigid templates. Summaries using common abbreviations ("ce") are unlikely to be AI. Older AI summaries are first-person with AI vocabulary, emoji, or Markdown; newer ones are exhaustively procedural. | X-SCOPE | Wikipedia edit-summary detection. | Edit summaries are Wikipedia's analog of commit messages; see WP-E01 and WP-E02. |
| WP-E01 | Edit summaries › Canned assurance of adherence to Wikipedia policies and guidelines, L1595–1602 | Makes verbose but unspecific claims of improvement ("improved clarity, flow, and readability", "ensure neutrality", "in compliance with the Manual of Style"). Humans write briefly and specifically ("removed excessive links per MOS:OVERLINK") and don't state the obvious. | TECH | For commit messages, PR descriptions, and changelogs, a specific summary beats a generic one in any language; personal writing has no change summaries. | **Conditional:** "In a change summary, name what changed and the specific reason or rule; cut generic improvement claims (clarity, readability, best practices, compliance) unless you say what was wrong."<br>The page says stacked assurances are a stronger sign.<br>**JA:** holds (可読性を向上 is equally vague). **ZH:** holds (优化代码，提升可读性 is equally vague). |
| WP-E02 | Edit summaries › Specific mentions of "preserved" or "retained" information, "avoided" mistakes, and other procedural statements, L1616–1621 | Mentions what was *not* changed ("while preserving the original meaning and technical details"), echoing the prompt. | TECH | Listing non-changes pads a change summary. | **Conditional:** "Mention what a change preserved only when a reviewer would otherwise assume it changed (e.g., 'no functional change' on a refactor)."<br>Stated absolutely, this would conflict with the NFC commit convention (Conflicts, item 6). |
| WP-E03 | Edit summaries › Overemphasis on presence/reliability of citations, L1639–1644 | Stresses that the content is "sourced" or comes "with independent sources" instead of saying what was added. | X-SCOPE | Wikipedia sourcing vocabulary. | The general "say what the change does" point is WP-E01. |
| WP-E04 | Edit summaries › Overemphasis on parameter/template names and markup idiosyncrasies, L1658–1659 | Itemizes infobox and reference parameters and template names, with markup. Humans rarely give this much detail. | X-SCOPE | Wikipedia-specific. | Conflict: in commit messages, naming the exact identifier is good practice (Conflicts, item 5). |
| WP-E05 | Edit summaries › Reference to AfC review, L1665–1666 | "Addressing reviewer feedback", which is too obvious for a human to state. | X-SCOPE | Wikipedia AfC workflow. | "Address review comments" commits are common on GitHub; the general fix is WP-E01. |
| WP-X01 | Miscellaneous › Pronounced shift in writing style, L1681–1684 | A sudden style change (e.g., flawless grammar unlike the editor's other writing), or a style that tracks LLM eras, suggests AI. A style consistent with pre-2022 edits suggests a human. | X-SCOPE | Detection method. | |
| WP-X02 | Miscellaneous › Sudden shift in English variety use, L1686–1688 | The English variety used does not match the author's location or the topic's national ties (LLMs default to American English). | X-SCOPE | Detection method. | Caveat: non-native speakers mix varieties, and code-switching is normal; only a dramatic shift counts. A "keep one variety" rule would be EN (MOS:ENGVAR), not from this page. |
| WP-X03 | Miscellaneous › "Submission statements" in AfC drafts, L1690–1691 | Drafts include notes to reviewers asserting that they meet the guidelines. | X-SCOPE | Wikipedia AfC. | |
| WP-X04 | Miscellaneous › Pre-placed maintenance templates, L1701–1703 | A draft is created with an AfC template already set to "declined" and no reasoning, which the page calls a "strong" indicator. | X-SCOPE | Wikipedia AfC. | |
| WP-X04a | Same section, L1705 | A new page carries implausible maintenance tags or protection templates. | X-SCOPE | Wikipedia templates. | |
| WP-X05 | Miscellaneous › Canned user pages, L1726–1729 | User pages follow a rigid format ("Welcome To My User Page!", "About Me", "Let's Connect!") with inline-header lists, emoji, and bold. | X-SCOPE | Wikipedia user pages. | Its components are covered by WP-S03, WP-S05, and WP-S02. |
| WP-X06 | Miscellaneous › Permissions gaming, L1753–1758 | Raises edit counts with throwaway AI edits to gain user rights. Use the sign in one direction only. | X-SCOPE | Wikipedia behavior. | |
| WP-X07 | Miscellaneous › Differences between LLMs, L1760–1767 | Each model has its own idiolect, and ChatGPT is historically the most used for Wikipedia edits. | X-SCOPE | Model attribution. | |
| WP-X07a | Same section, L1764 | Focusing on broader context is more typical of ChatGPT and Grok than of Gemini and Claude. | X-SCOPE | Model attribution. | |
| WP-X07b | Same section, L1765 | Gemini and Claude are more concise than ChatGPT and Grok. | X-SCOPE | Model attribution. | |
| WP-X08 | Miscellaneous › Biases in content › Pro-authoritarian bias, L1769–1772 | Frontier models show a pro-authoritarian bias on some prompts, more so in Chinese-language answers. | X-SCOPE | Content bias, not a writing rule. | |
| WP-HS01 | Signs of human writing › Age of text relative to ChatGPT launch, L1776–1781 | Text added before 30 November 2022 can be "safely" ruled out as AI; WhoWroteThat and WikiBlame find when text was inserted. | X-SCOPE | Detection method. | |
| WP-HS02 | Signs of human writing › Ability to explain one's own editorial choices, L1783–1784 | Ask the editor to explain a suspicious edit; a plausible explanation points to ordinary human error. | X-SCOPE | Process. | |
| WP-HS03 | Signs of human writing › Syntax (intro), L1786–1789 | LLMs aim for a "formal, neutral, encyclopedic tone" and avoid constructions that are common in human writing and accepted, sometimes preferred, by the MOS. | X-SCOPE | Framing for HS03a–e. | |
| WP-HS03a | Same section, L1791 | Humans use simple is and has phrases ("there is a", "it has a") more often. | X-DUP | WP-L02. | |
| WP-HS03b | Same section, L1792 | Humans prefer plain words over stiff or euphemistic synonyms (wrote/authored, moved/relocated, used/utilized, tried/attempted, died/passed away). | BOTH | Plain words improve any text (standard plain-language advice). | **Conditional:** "Prefer the plain word unless the longer one carries a needed distinction or the register requires it."<br>**PERSONAL:** "passed away" can be the kind choice when writing about one's own loss.<br>**JA:** kango verbs (使用する, 実施する) are the expected register in specs, so the target is padding such as 〜を行う, not register.<br>**ZH:** 书面语 (使用, 进行) is expected in formal text, and 逝世 is conventional for public figures; the target is empty dummy verbs (进行……工作).<br>The EN pairs go to writing-en. |
| WP-HS03c | Same section, L1793 | Humans make more superlative or definitive statements ("one of the best", "is the only", "was the first"). | X-DUP | WP-C00 (state the specific, checkable fact), under the WP-C04 condition. | Tension with anti-puffery rules; see Conflicts, item 4. |
| WP-HS03d | Same section, L1794 | Humans use more qualifiers and intensifiers ("very", "perhaps", "tends to"). | X-DEAI | As a rule, "add qualifiers" would only make text look human. | Conflicts with "omit needless words" (Conflicts, item 3). |
| WP-HS03e | Same section, L1795 | Humans use more isolated wordy constructions ("as a result of", "in order to", "all of the", "the fact that"). | X-DEAI | Adding wordiness to look human is de-AI, not good writing. | Conflicts with Strunk on "the fact that" (Conflicts, item 3). |
| WP-IE00 | Ineffective indicators (intro), L1797–1798 | False accusations drive away new editors. Watch for Dunning–Kruger and confirmation bias; style-only detection is hard. | X-SCOPE | Detection advice. | |
| WP-IE01 | Same section, L1800 | Perfect grammar is ineffective as an indicator, since many editors are skilled writers. | X-SCOPE | Detection. | Supports excluding any rule that adds errors to make text look human. |
| WP-IE02 | Same section, L1801 | A mix of casual and formal registers ("clinical" plus "emotional") is ineffective. It can reflect a technical writer, youth, playfulness, neurodivergence, or multiple editors. | X-SCOPE | Detection. | JA has a separate rule against mixing です・ます and だ・である; this page does not contradict it. |
| WP-IE03 | Same section, L1802 | "Bland" or "robotic" prose is ineffective. LLM text skews positive and verbose but may not read as robotic. | X-SCOPE | Detection. | |
| WP-IE04 | Same section, L1803 | "Fancy", academic, or formal prose is ineffective; the correlation holds only for specific words. | X-SCOPE | Detection. | Supports keeping word-list rows X-DEAI rather than banning formal register. |
| WP-IE05 | Same section, L1804 | Transition words in isolation (Additionally, Consequently, Notably) are a weak tell with human precedent, and many style guides accept them. | X-SCOPE | Detection. | Evidence against any source that bans these transitions outright (Conflicts, item 12). |
| WP-IE06 | Same section, L1805 | Unsourced content is ineffective: most uncited articles predate LLMs, and AI text now often has citations. | X-SCOPE | Detection. | |
| WP-IE07 | Same section, L1806 | Bizarre wikitext (a stray `<span>`, misplaced italics) points to browser extensions or VisualEditor, not LLMs. | X-SCOPE | Markup detection. | |
| WP-IE08 | Same section, L1807 | Correct wikitext is normal for humans who use the visual editor or preview. | X-SCOPE | Markup detection. | |
| WP-H00 | Historical indicators (intro), L1809–1810 | These signs come from older models and are now rare, but they help find old, undetected edits. | X-SCOPE | Framing. | "Historical" does not mean removed: the page keeps these entries. |
| WP-H01 | Historical › Statements about knowledge cutoffs (2022–2023), L1812–1817 | "As of my last knowledge update…" | X-DEAI | The owner names knowledge-cutoff disclaimers. | |
| WP-H02 | Historical › Didactic disclaimers (November 2022–2024), L1824–1828 | "It's important/critical/crucial to note/remember/consider", "worth noting", "may vary"; unsolicited safety advice to an imagined reader; disambiguation by locale. | BOTH | Announcing importance and generic cautions add nothing to a careful human's text (MOS:EDITORIAL). | **Conditional:** "Drop 'it is important to note' and state the point. Add a caution only for a concrete risk the reader faces, and name the condition (which versions, which jurisdictions) instead of 'may vary'."<br>Tech admonitions (Note and Warning blocks) are legitimate when the risk is concrete.<br>**JA:** holds (〜に注意が必要です, 〜ことが重要です). **ZH:** holds (值得注意的是, 需要指出的是, 因地区而异). |
| WP-H03 | Historical › Section summaries, L1837–1840 | "In summary", "In conclusion", "Overall"; "Conclusion" sections; ending paragraphs or sections by restating their core idea. | BOTH | Restating what the reader just read wastes words in any text. | **Conditional:** "Don't end a paragraph or short section by restating it; summarize only in long documents (a TL;DR first, or a closing summary), and make the summary add something, such as a decision or next step."<br>A "Conclusion" section in an encyclopedia article is a Wikipedia-specific issue.<br>JA tech blogs (Qiita, Zenn) conventionally end with まとめ, and ZH essays follow 总分总. Both fit the long-document exception (Conflicts, item 11). |
| WP-H04 | Historical › Prompt refusal, L1867–1869 | "As an AI language model…", apologies, and offers of alternatives. | X-DEAI | A pure machine-authorship tell. | |
| WP-H05 | Historical › Overuse of em dashes (2022–September 2026), L1876–1881 | Uses more em dashes than humans in the same genre, often spaced, where humans would use commas, parentheses, or colons. Best combined with other signs. | X-DEAI | The owner names em-dash counting; the page says humans use em dashes and the sign is weak alone. | An English typography matter: ZH —— (破折号) and JA ―― are standard punctuation. |
| WP-H05a | Same section, L1883 | Since September 2026 many models are hard-coded to avoid em dashes. The resulting low punctuation variety (more commas and periods than human text) is now a sign in itself; the page tags this `{{cn}}`. | X-DEAI | Statistical tell, unsourced on the page. | Conflicts with em-dash-removal rules in humanizer-type sources: removing dashes now creates a tell (Conflicts, item 2). |
| WP-H06 | Historical › Abrupt cut offs, L1914–1917 | Text stops mid-sentence because of a token limit. | X-DEAI | Generation artifact. | Caveat: a bad copy-paste or a copyright violation can cause the same thing. |
| WP-H07 | Historical › Outdated access-date parameters, L1919–1921 | Citation access dates are much older than the edit. | X-SCOPE | Citation fields. | Caveat: there are legitimate causes. |
| WP-H08 | Historical › Lexical diversity/elegant variation, L1923–1945 | A repetition penalty makes models rotate synonyms for one referent ("Soviet artistic constraints", "state-imposed artistic norms", "the constraints imposed by the Soviet regime"). | TECH | In technical text, one concept needs one term in every language; for personal prose the norm depends on the language. | **Conditional:** "Use the same term for the same thing; if you introduce a synonym, state the equivalence once."<br>**Page caveat:** non-native editors avoid repetition too; Italian schools teach it. JA and ZH school composition share that norm, while JA (用語の統一) and ZH (术语统一) technical writing require consistency.<br>EN/PERSONAL candidate: Fowler's "elegant variation".<br>The page also notes the tell fails across separately generated edits. |

## Conflicts found

1. **The page versus the humanizer approach (WP-G04).**
   - The page says: do not treat the signs as the problems to fix, because that "could just make detection harder". Fix the underlying issues instead: unsupported claims, sourcing, neutrality.
   - blader/humanizer cites this page but does the opposite: it rewrites surface signs.
   - Resolution: the owner's X-DEAI decision matches the page. Only rows whose substance improves human text (BOTH/TECH) go into the genre skills, and their conditional forms target the substance (evidence, specificity), not the marker words.

2. **Short sentences and punctuation (WP-L01d, WP-H05a) versus plain-language advice and em-dash removal.**
   - The page now lists uniformly short sentences (8–20 words) and heavy use of plain commas and periods as signs of GPT-6 and of dash-suppressed models.
   - Plain-language guides recommend short sentences, and humanizer-type sources tell writers to remove em dashes.
   - Resolution: the tell is uniformity, not shortness, so both rows are X-DEAI. Sentence-length guidance stays as a conditional rule from other sources ("vary length; keep a sentence short when it carries one point"). Em-dash rules stay X-DEAI and are language-specific in any case (ZH —— and JA ―― are standard).

3. **Wordiness and qualifiers (WP-HS03d, WP-HS03e) versus *The Elements of Style* ("omit needless words", avoid "rather, very, little, pretty", "the fact that").**
   - The page observes that humans use more qualifiers and wordy constructions than LLMs.
   - Resolution: this is descriptive, and "add them to look human" is X-DEAI. The rule to cut wordy constructions stays with its original source. Calibrated hedges ("tends to", "perhaps") remain correct where the uncertainty is real.

4. **Superlatives (WP-HS03c) versus the anti-puffery rule (WP-C04).**
   - Humans use "was the first" and "one of the best" more than newer LLMs, which the page calls "subtly positive".
   - Resolution: both reduce to WP-C00. State a definitive claim when it is checkable, and drop praise that no fact supports.

5. **Identifier detail in change summaries (WP-E04) versus tech commit-message norms.**
   - Wikipedia humans rarely itemize template or parameter names in edit summaries.
   - In commit messages and PRs, naming the exact function, flag, or parameter is good practice.
   - Resolution: WP-E04 is X-SCOPE (Wikipedia only). Do not import it into writing-tech.

6. **Stating what was preserved (WP-E02) versus "NFC / no functional change" commit conventions.**
   - Resolution: TECH with a condition. Mention a non-change only when a reviewer would otherwise assume the change happened.

7. **Elegant variation (WP-H08) versus school norms against repetition.**
   - The page itself cites Italian schools teaching writers to avoid repeated words. JA and ZH school composition share this norm, while technical style in both languages demands consistent terms.
   - Resolution: TECH (universal for technical text). Treat personal-prose variation as language-dependent; the EN/PERSONAL candidate is Fowler's "elegant variation".

8. **"such as" before a complete list (WP-C06a) versus ZH 等 and JA など.**
   - ZH 等 followed by a count legitimately closes a complete list. JA など is often a softener.
   - Resolution: the principle (don't imply items that don't exist) is universal. The ZH and JA nuances go into writing-zh and writing-ja.

9. **Banning "not only… but also" (WP-L03a–c) versus ZH 不仅……而且…… and JA 〜だけでなく〜も, standard connectives.**
   - Resolution: construction-level bans are X-DEAI. The conditional substance rule (WP-L03: contrast only against a view readers plausibly hold) is universal.

10. **Straight quotes (WP-S07) versus ZH and JA quotation norms.**
    - GB/T 15834 prescribes “ ” and ‘ ’ for Chinese; Japanese uses 「」.
    - Resolution: X-DEAI. Any quote-style rule belongs to a language skill.

11. **Section summaries (WP-H03) versus ZH 总分总 composition and the JA まとめ convention in tech blogs.**
    - Resolution: BOTH with a condition. Ban restating in short units; allow summaries in long documents when the summary adds a decision or next step.

12. **Transition words (WP-IE05) versus sources that ban "Additionally", "Moreover", and similar words.**
    - The page calls these a weak tell, with human precedent and style-guide acceptance.
    - Resolution: such bans are X-DEAI. This page is evidence for that classification.

13. **Challenges and outlook sections (WP-C07) versus conventional JA 今後の課題と展望 and ZH 挑战与展望 sections.**
    - The page itself says the sign is "about the rigid formula, not simply the mention of challenges".
    - Resolution: BOTH with a condition. Ban the vague formula, not the section.

14. **Literal technical meanings in the word lists (WP-L01).**
    - Several listed words are precise technical terms: key, robust, landscape, leverage, highlight, underscore.
    - Resolution: X-DEAI. Do not import the word list into writing-tech, and the page's own "take literally" note (WP-L01f) agrees.

## Rules whose absolute wording should become conditional

The page phrases its signs as observations, not commands. The risk is a downstream skill turning the "Words to watch" boxes into bans. Each kept row needs the predicate below.

| Row | Absolute form to avoid | Conditional form |
|---|---|---|
| WP-C00 | "Avoid generic descriptions." | If a description would fit many subjects, replace it with the fact that fits only this one. |
| WP-C01 | "Never claim significance or legacy." | If you claim significance, state the concrete consequence and its evidence; otherwise cut it. |
| WP-C02 | "Don't mention media coverage." | If you cite coverage as evidence, say what it reports; don't substitute a list of outlets or source types. |
| WP-C03 | "No trailing -ing clauses." | If an appended clause interprets a fact, keep it only when it is specific and supported. |
| WP-C04 | "Always use neutral tone." | If an evaluative word is backed neither by a stated fact nor by the writer's own explicit judgment, replace it with the fact. Neutrality as such is a TECH norm. |
| WP-C05 | "Never write 'associated with'." | If you know the relationship, name it; keep "associated with" for unknown links and statistical association. |
| WP-C06 | "Never use unnamed sources." | If you attribute a view, name its holder; if you quantify support, make the count match the sources. |
| WP-C06a | "Never write 'such as'." | If the list is complete, don't mark it as partial. ZH 等 plus a count is exempt. |
| WP-C07 | "No challenges or future sections." | If you include challenges or outlook, make them specific and sourced; drop the closing reassurance. |
| WP-L02 | "Never write 'serves as' or 'features'." | If the phrase means only "is" or "has", use the plain verb; keep "serves as" for a role the subject does not inherently have. |
| WP-L03 | "Never use 'not X but Y'." | Use the contrast only when readers plausibly believe X. |
| WP-S02 | "Don't use bold." | Bold only what a scanning reader must not miss; never every occurrence. |
| WP-S03 | "No bold-header lists." | Use them for parallel, looked-up items; write prose for a narrative or argument. |
| WP-S04b | — | If the text uses headings, nest them one level at a time. |
| WP-S04d | — | If a heading has subheadings, put an introductory sentence under it. |
| WP-S06 | "Don't use tables." | Use a table when readers compare several items across two or more attributes; otherwise write a sentence or list. |
| WP-U02 | "Never say information is unavailable." | If a fact is unknown, omit it or state the gap once when it matters; never follow it with speculation presented as fact. |
| WP-H02 | "Never warn the reader." | Drop "it is important to note"; caution only about a concrete risk, and name the condition instead of "may vary". |
| WP-H03 | "Never summarize." | Don't restate a short unit; summarize long documents only, and make the summary add something. |
| WP-H08 | "Never use synonyms." | Use one term per concept in technical text; if you introduce a synonym, state the equivalence once. |
| WP-HS03b | "Always use the shortest word." | Prefer the plain word unless the longer one carries a needed distinction or register. This includes tactful euphemism in personal writing, and register norms in JA and ZH formal text. |
| WP-E01 | — | In a change summary, name what changed and the specific reason; cut generic improvement claims unless you say what was wrong. |
| WP-E02 | "Never mention what you didn't change." | Mention a non-change only when a reviewer would otherwise assume it changed (e.g., "no functional change"). |

Several of the page's own statements are absolute, but all are X-SCOPE, so no action is needed:
- "AI use can be safely ruled out" before 30 November 2022 (WP-HS01).
- Leaked tool markup is an "unambiguous indicator" (WP-M03).

## Language-specific examples to move

**EN (to writing-en, attached to the universal rule IDs).** All of these come from the source:
- **WP-C01:** stands/serves as, is a testament/reminder, a crucial/pivotal/vital/significant/key role/moment, underscores/highlights its importance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, "distinction matters because"; "generated debate", "prompted broader reflection".
- **WP-C02:** independent coverage, local/regional/national media outlets, trade publications, cited/featured/profiled in, "and other prominent media outlets", written by a leading expert.
- **WP-C03:** trailing present-participle clauses (highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, cultivating, fostering, encompassing, enhancing); valuable insights; align/resonate with. The trailing "-ing" form is English-specific grammar.
- **WP-C04:** boasts a, vibrant, rich, profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, featuring, diverse array.
- **WP-C05:** in connection with/to, connected with/to, in association with, associated with, particularly/widely associated.
- **WP-C06:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications.
- **WP-C06a:** "such as" before a complete list.
- **WP-C07:** "Despite its… faces several challenges…", "Despite these challenges", "Challenges and Legacy", "Future Outlook".
- **WP-L02:** serves as / stands as / marks / functions as / operates as / represents [a]; boasts / features / maintains / offers [a]; ventured into politics as a candidate → was a candidate; began his career as → was.
- **WP-L03:** "It's not X, it's Y" used against a view no one holds. Keep the construction legal; only the straw-man use is the fault.
- **WP-H02:** it's important/critical/crucial to note/remember/consider; worth noting; may vary.
- **WP-H03:** In summary, In conclusion, Overall.
- **WP-HS03b:** wrote/authored, moved/relocated, used/utilized, tried/attempted, died/passed away.
- **WP-E01:** improved clarity/flow/readability, ensured… adheres to, in compliance with, refined, enhanced, streamlined.
- **WP-E02:** preserved/preserving, retained/retaining, avoided/avoiding, ensured/ensuring, aimed to.

Not moved: English-only items tagged X-DEAI (the AI-vocabulary lists in WP-L01–L01e, title case in WP-S01, curly quotes in WP-S07, em dashes in WP-H05). They are excluded, not reassigned to writing-en.

**JA.** The source has no Japanese examples. The analogs below are the auditor's own and need native review before use:
- **WP-C01:** 〜を象徴する, 重要な役割を果たす, 転換点となった.
- **WP-C03:** 〜しており、〜を示している / 〜を物語っている.
- **WP-C04:** 〜を誇る, 風光明媚な.
- **WP-C05:** 〜に関連して, 〜と関わりのある.
- **WP-C06:** 〜と言われている, 〜とされる, 専門家は〜と指摘する.
- **WP-C06a:** など used as a softener on a complete list.
- **WP-L02:** 〜として機能する, 〜の役割を担う, 〜を有する versus である, がある.
- **WP-L03:** 〜ではなく〜だ used against a view no one holds.
- **WP-U02:** 詳細は明らかになっていないが、〜と考えられる.
- **WP-H02:** 〜に注意が必要です, 〜ことが重要です.
- **WP-H03:** a まとめ section in a long document is fine; a restatement at the end of every paragraph is not.
- **WP-HS03b:** 〜を行う padding.
- **WP-E01:** 可読性を向上.
- **WP-H08:** 用語の統一 in technical text.

**ZH.** The source has no Chinese examples. The analogs below are the auditor's own and need native review before use:
- **WP-C01:** 具有重要意义, 标志着, 发挥了关键作用, 奠定了基础.
- **WP-C02:** 受到多家主流媒体广泛报道.
- **WP-C03:** ……，彰显了……; ……，体现了…….
- **WP-C04:** 坐落于, 闻名遐迩, 历史悠久.
- **WP-C05:** 与……相关, 与……有关联, 涉及.
- **WP-C06:** 有专家指出, 业内人士认为, 普遍认为 (and the 据悉 journalism note).
- **WP-C06a:** 等 without a count. 等 followed by a count, which closes a complete list, is fine.
- **WP-L02:** 作为……, 扮演……角色, 拥有, 具备 versus 是, 有.
- **WP-L03:** 不是……而是…… used against a view no one holds.
- **WP-U02:** 目前公开资料有限，但……可能…….
- **WP-H02:** 值得注意的是, 需要指出的是, 因地区而异.
- **WP-H03:** 总分总 summaries are fine in long documents.
- **WP-HS03b:** 进行……工作 dummy verbs. 逝世 is a register convention, not a violation.
- **WP-E01:** 优化代码，提升可读性.
- **WP-H08:** 术语统一 in technical text.
