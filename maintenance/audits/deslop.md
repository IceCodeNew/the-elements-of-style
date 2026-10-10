# Rule audit: deslop-zh, deslop-en, deslop

Sources (ninehills/skills @ `f3e82a7e2bfbed54fc2b4a715a1986f5f467e827`):

- `DZ`: `deslop-zh/SKILL.md` (Chinese; credits hexiecs/talk-normal and ninehills write / tech-doc-style-chinese).
- `DE`: `deslop-en/SKILL.md` (English; credits hardikpandya/stop-slop and stephenturner/skill-deslop).
- `DS`: `deslop/SKILL.md`, `deslop/references/structures.md`, `phrases.md`, `examples.md` (a copy of stephenturner/skill-deslop @ `a906154`, MIT).

`deslop/references/tropes.md` is not used as a source. Where `DS` SKILL.md points to it, only the words that SKILL.md itself prints are audited.

Rubric: `.claude/skills/updating-upstream-rules/rubric.md`. The extra last column names the candidate rule(s) whose behavior prevents the anti-pattern, or "none".

Conventions used in this audit:

- Granularity. One row per rule, in source order. Checklist and quick-check items, SKILL.md summaries and execution steps that restate a section are `X-DUP` of that section's row. Phrase catalogs get one row per category, with the words in the notes. Tables that list distinct templates get one row per template. Vocabulary tables get one row per table row. Worked examples get one row each; they illustrate rules, so they are `X-DUP`, and the notes record where an "after" version breaks another rule.
- Canonical rows. `SS-…` rows are in `maintenance/audits/stop-slop.md` (hardikpandya/stop-slop @ `8da1f03`). A `DS` or `DE` row that copies a stop-slop rule is `X-DUP` of the `SS` row, and the `SS` row's destination and conditional wording apply. When a rule appears first in `DZ` and again in `DE` or `DS`, the `DZ` row is canonical unless the `DE` or `DS` row carries the examples.
- Destinations follow the candidate set where it narrows an earlier `SS` decision: staged questions (`DE-P07`) and fragment runs (`DE-P10`) are `BOTH` under `both.state-dont-stage`, although `SS-ST33` and `SS-ST14` were tagged `X-DEAI`. The notes say so.

## Counts

| Destination | DZ | DE | DS | Total |
|---|---|---|---|---|
| BOTH | 24 | 13 | 6 | 43 |
| TECH | 12 |  | 1 | 13 |
| PERSONAL | 3 | 1 |  | 4 |
| EN |  | 23 | 1 | 24 |
| JA |  |  |  |  |
| ZH | 19 |  |  | 19 |
| ZH/TECH | 1 |  |  | 1 |
| X-DEAI | 8 | 2 | 3 | 13 |
| X-DUP | 69 | 59 | 126 | 254 |
| X-SCOPE | 16 | 6 | 3 | 25 |
| Total | 152 | 104 | 140 | 396 |

Most `X-DUP` rows restate another row of the same skill (checklists, quick checks, summaries, the 改写示例 and Examples) or copy a stop-slop rule: 82 of the 126 `DS` duplicates point to an `SS` row. Rows that name at least one candidate rule: 341 of 396.

## deslop-zh/SKILL.md

| ID | Source location | Rule (short paraphrase, or quote if short) | Destination | Reason (one clause) | Conditional wording / notes | Candidate rule(s) |
|---|---|---|---|---|---|---|
| DZ-1.1a | §一.1 (L21-22) | 读起来自然优先；不为去 AI 味硬塞口语词（说白了、居然、谁能想到、太太太） | BOTH | Forced colloquialisms make any text worse, in every language | If the source register is neutral, do not add slang, interjections or spoken fillers to make a text "sound human". | both.match-house-and-voice, tech.neutral-register |
| DZ-1.1b | §一.1 (L23) | 不为「更像人」把技术文改得像口播稿 | TECH | A spoken register breaks reference and procedure norms; personal posts may be chatty | — | tech.neutral-register |
| DZ-1.1c | §一.1 (L24) | 原句已经自然、准确、清楚，不改 | BOTH | Editing a clear sentence risks loss without gain | — | both.revise-without-loss |
| DZ-1.2a | §一.2 (L27-28) | 去 AI 味是做减法：先删解释腔、总结腔、多余转折、套话填充 | BOTH | Cutting empty words improves any text | Delete a phrase only if the sentence keeps its meaning without it. The skill's own examples (DZ-7.1, DZ-7.2, DZ-7.4) add content instead. | both.cut-needless-words, both.say-it-once |
| DZ-1.2b | §一.2 (L29) | 再调句式节奏、标点、用词口语化程度 | X-SCOPE | Editing order, not a writing rule | — | none |
| DZ-1.2c | §一.2 (L30) | 不改代码字面量、URL、API 路径、JSON 键名、数据库字段名 | BOTH | Literals must survive editing in any genre | — | both.keep-literals |
| DZ-1.3 | §一.3 (L33) | 保语义 > 去 AI 味；为「更口语」改坏原意 = 失败改写 | BOTH | Meaning preservation is universal | — | both.revise-without-loss |
| DZ-1.4a | §一.4 (L37) | 技术文档：克制、准确、可扫读，不用第二人称 | X-DUP | Same as DZ-4.1a and DZ-3.11a | — | tech.neutral-register |
| DZ-1.4b | §一.4 (L38) | 博客/技术长文：自然稳重的工程师口吻，不做报告腔也不做口播腔 | X-DUP | Same as DZ-4.2a | — | both.match-house-and-voice |
| DZ-1.4c | §一.4 (L39) | 社交媒体：有性格，有立场，不列功能清单 | X-DUP | Same as DZ-4.3b and DZ-4.3d | — | pers.state-the-view |
| DZ-1.4d | §一.4 (L40) | 发行说明：一句话说用户效果，条目密度匹配项目风格 | X-DUP | Same as DZ-4.4b and DZ-4.4c | — | tech.specific-change-summary, both.match-house-and-voice |
| DZ-1.4e | §一.4 (L41) | 科学论文：保持学术正式度但不用空洞套话 | X-DUP | Same as DZ-1.2a | — | both.cut-needless-words |
| DZ-2.01 | §二 (L47) | 段末「这说明」「可以看出」「到这里」收尾总结句 → 删 | X-DUP | Same as DZ-3.1 | — | both.say-it-once |
| DZ-2.02 | §二 (L48) | 「不是...而是...」 → 只说结论 | X-DUP | Same as DZ-3.3 | — | both.real-contrasts |
| DZ-2.03 | §二 (L49) | 「随着...的发展」「在当今...时代」开篇套话 → 删 | X-DUP | Same as DZ-3.6 | — | zh.background-opener |
| DZ-2.04 | §二 (L50) | 「赋能」「抓手」「闭环」「拉通」「沉淀」 → 替换 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-2.05 | §二 (L51) | 破折号（—） → 逗号或句号 | X-DUP | Same as DZ-3.9b | — | zh.dash-form |
| DZ-2.06 | §二 (L52) | 四五个短句连发像打电报 → 合并或变节奏 | X-DUP | Same as DZ-3.9e | — | zh.subject-omission, both.merge-repeated-referents |
| DZ-2.07 | §二 (L53) | 章节间「上面这些讲的是...下面我们看...」过渡句 → 删 | BOTH | A recap-and-preview between sections repeats what headings already show | If a heading already names the next section, cut the transition. Keep a scope statement at the top of a long document. ZH form moves to the ZH examples. | both.no-empty-previews, both.say-it-once |
| DZ-2.08 | §二 (L54) | 中文和英文/数字之间加空格 | X-DUP | Same as DZ-3.10a | — | none |
| DZ-2.09 | §二 (L55) | 「非常」「极其」「值得注意的是」「综上所述」「例如」 → 「很」「比如」 | X-DUP | Same as DZ-3.8a to DZ-3.8d | — | zh.stock-closing |
| DZ-2.10 | §二 (L56) | 升华句 → 删 | X-DUP | Same as DZ-3.2 | — | pers.end-on-the-point, both.facts-not-praise |
| DZ-2.11 | §二 (L57) | 第二人称「你」「您」：技术文档避免，博客酌情 | X-DUP | Same as DZ-3.11a and DZ-3.11b | — | none |
| DZ-2.12 | §二 (L58) | 「一句话总结」「简而言之」等总结标签 → 直接说结论 | X-DUP | Same as DZ-3.5 | — | pers.no-signposts |
| DZ-2.13 | §二 (L59) | 无生命事物做了人类动词（「决策浮现」「数据告诉我们」） → 命名真人 | X-DUP | Same as SS-ST23 | ZH form: 「数据表明」「结果显示」 are standard and stay; rewrite only thinking or intention verbs with a data or program subject. | both.name-the-actor |
| DZ-2.14 | §二 (L60) | 滥用三连排比 → 换二连或一连 | X-DUP | Same as DZ-3.14a | — | both.list-what-is-there |
| DZ-2.15 | §二 (L61) | 自问自答 → 直接陈述 | X-DUP | Same as DE-P07 | — | both.state-dont-stage |
| DZ-2.16 | §二 (L62) | 每个列表项都是 bold 关键词开头 → 换格式 | X-DUP | Same as DE-P24 | — | both.sparing-bold, both.lists-vs-prose |
| DZ-3.1 | §3.1 (L68-74) | 段末收尾总结句：一段解释完再重述一遍（这说明、到这里、可以看出、这本身就是、通过以上分析、由此可见） → 删 | BOTH | A closing sentence that restates its paragraph adds nothing in any genre | If the last sentence of a paragraph restates what the paragraph already said, delete it; keep one that draws a new conclusion. The signal words move to the ZH examples. | both.say-it-once |
| DZ-3.2 | §3.2 (L76-80) | 升华句：把具体工程观察上升到普适人生道理 → 给具体建议 | BOTH | An unearned moral adds no fact in any genre | If a closing line generalizes beyond what the text showed, cut it or replace it with the consequence the text supports. The ✅ adds advice that the ❌ lacks; an editor must not supply new advice. | pers.end-on-the-point, both.facts-not-praise, both.state-dont-stage |
| DZ-3.3 | §3.3 (L82-92) | 硬约束：禁止任何否定式对比（不是 X，而是 Y；X 已经不是瓶颈，Y 才是） | X-DUP | Same as SS-ST06 | The absolute ban is wrong. Example 3 (L91, 「性能瓶颈已经不是 I/O，而是锁竞争」) reports a real change whose halves both inform, and its ✅ loses that I/O was the bottleneck; example 2 (L88) answers a belief readers may hold. Use SS-ST06's condition. | both.real-contrasts |
| DZ-3.4 | §3.4 (L94-97) | 讲解腔/训人感起手（真拆开看、这背后是同一个变化、真正关键的问题是、先问问是不是、你要先明白） → 直接说 | BOTH | Lead-ins that announce or lecture delay the point in any genre | If deleting the lead-in loses no information, delete it. 「真正关键的问题是」 is a label (both.show-not-label). 「先问问是不是」→「先确认」 is a phrasing preference without a rule behind it. | both.no-empty-previews, both.show-not-label |
| DZ-3.5 | §3.5 (L99-104) | 不在结尾前加总结标签（一句话总结、简而言之、概括来说、总而言之、综上所述、总结一下、一句话落地） | PERSONAL | Summary labels clutter posts; technical and academic text uses labeled summaries (「综上」「本章小结」) | In posts and essays, drop a label that announces the summary. In technical and academic text, keep a labeled summary with content: zh.stock-closing keeps 「综上，两种方案都无法满足离线要求，暂不采用」. | pers.no-signposts, zh.stock-closing |
| DZ-3.6 | §3.6 (L106-110) | 文章开篇套话（随着 AI 技术的不断发展、在当今数字化浪潮中、近年来…受到了越来越多的关注） → 直接开头 | ZH | The 随着/在当今/近年来 opener is a Chinese formula; the universal residue is SS-P05 | If the opener only sets background and names no concrete change or cause, delete it; keep 「随着文件数量增加，检索时间也在增长」. Two ✅ openers (「先说结论」「这次想把 X 讲清楚」) are announcements that both.no-empty-previews cuts. | zh.background-opener |
| DZ-3.7a | §3.7 (L113-114, L117-118) | 黑话「绝对禁用」：赋能、抓手、闭环、沉淀、对齐、对标、拉通、打通、协同、联动、洞察、赛道、心智、调性、战役、链路、势能、兜底 | ZH | A list of Chinese business jargon | "Absolutely banned" is wrong for field terms: 闭环控制, 协同过滤, 链路追踪, 内存对齐, 兜底策略. Replace a word only when it names no exact action or object. | zh.plain-words |
| DZ-3.7b | §3.7 (L115) | 「谨慎使用」：场景、生态、体系、路径、触点、卡点、布局、矩阵、颗粒度、复盘、梳理、输出、提炼 | X-DEAI | Mostly ordinary Chinese words; "use carefully" gives no testable condition | The residue, a buzzword with no exact referent, is DZ-3.7a. | zh.plain-words |
| DZ-3.7c | §3.7 (L121) | 过度强调重要性（至关重要、意义重大、关键时刻、转折点） → 删 | BOTH | Unsupported significance claims weaken any text | If the text gives no evidence for the significance, drop the claim or replace it with the fact. | both.facts-not-praise, zh.plain-words |
| DZ-3.7d | §3.7 (L122) | 过度列举来源（依据多家媒体报道、显示其于产业中具一定能见度） → 删 | BOTH | A list of outlets stands in for a source | Name the source and what it said, or cut it. | both.attribute-claims |
| DZ-3.7e | §3.7 (L123) | 表面分析附加（反映了当代中国社会的变迁） → 删或给具体证据 | BOTH | A significance tail adds unsupported meaning in any language | Keep a trailing clause that states a cause, purpose or result from the facts. ZH forms: 「，反映了……」「，彰显了……」. | zh.significance-tail, en.ing-rider, both.facts-not-praise |
| DZ-3.7f | §3.7 (L124) | 推广语气（文化遗产、文化底蕴、自然之美） → 删 | BOTH | Praise without facts in any genre | An opinion the author holds and marks as theirs stays. | both.facts-not-praise |
| DZ-3.7g | §3.7 (L125) | 模糊归因（据业内人士指出、有评论认为） → 说清谁说的，或不说 | BOTH | Unnamed authorities give the reader nothing to check in any language | Name the source and what it said, or cut the claim; never invent a source. | both.attribute-claims |
| DZ-3.7h | §3.7 (L126) | 展望章节套话（尽管（主题）有其意义，但其面临的挑战有...） → 具体说问题 | BOTH | A dismiss-and-pivot formula hides the real problem | Name the specific problem with its evidence, and add no vague outlook. | both.facts-not-praise |
| DZ-3.8a | §3.8 (L131) | 非常 / 极其 → 很 | ZH | Chinese intensifiers | Delete the intensifier when the judgment stays the same; 很 is optional. | none |
| DZ-3.8b | §3.8 (L132) | 值得注意的是 → 直接说结论 | ZH | Chinese form of the universal filler rule SS-P05 | — | both.show-not-label |
| DZ-3.8c | §3.8 (L133) | 综上所述 → 直接收尾 | X-DUP | Same as DZ-3.5 | Keep 综上 with content in technical and academic text. | zh.stock-closing |
| DZ-3.8d | §3.8 (L134) | 例如 → 比如 | X-DEAI | A register preference; 例如 is standard written Chinese | — | none |
| DZ-3.8e | §3.8 (L135) | 购买 / 使用 → 买 / 用 | X-DEAI | 使用 and 购买 are the standard written register in technical Chinese | Conflicts with DZ-4.1a (克制). | none |
| DZ-3.8f | §3.8 (L136) | 很多同学 / 不少同学 → 很多人 / 不少人 | ZH | Generic 同学 is an in-group or condescending address in Chinese tech writing | If 同学 does not mean students, write 人 or the actual role. | none |
| DZ-3.8g | §3.8 (L137) | 这几个事 → 这几件事 | ZH | Measure-word choice (件 for 事) is Chinese grammar | — | none |
| DZ-3.9a | §3.9 (L140) | 使用直角引号「」，不用弯引号 | X-DEAI | GB/T 15834 prescribes “” for mainland Chinese; 「」 is a house style | Conflicts with zh.full-width-punct (“” by default, 「」 when the target format requires it). | zh.full-width-punct |
| DZ-3.9b | §3.9 (L141, L145) | 禁止破折号（—），用逗号或分号替代 | X-DEAI | 「——」 is standard Chinese punctuation (GB/T 15834); a ban is a surface tell | The useful residue: write the dash as 「——」, never 「—」, 「--」 or 「 — 」 (zh.dash-form). | zh.dash-form |
| DZ-3.9c | §3.9 (L142) | 不用感叹号（除非推文/社交场景且确有情绪） | TECH | Exclamation marks do not belong in reference and procedure text; personal posts may use them | In technical text, use no exclamation marks. | tech.neutral-register |
| DZ-3.9d | §3.9 (L143) | 中文标点：，。；：！？、「」『』【】 | ZH | The Chinese punctuation set | Matches zh.full-width-punct except for the quote marks (DZ-3.9a). | zh.full-width-punct |
| DZ-3.9e | §3.9 (L144) | 四五个句号连发 = 打电报 → 合成长句或用逗号连 | ZH | Chinese short-sentence chains usually repeat a subject that Chinese leaves out | If consecutive short sentences share a subject, merge them or drop the repeated 它; keep procedure steps separate. | zh.subject-omission, both.merge-repeated-referents |
| DZ-3.10a | §3.10 (L148) | 中文和英文之间加空格 | ZH | CJK–Latin spacing is a Chinese typographic convention | House style decides; style guides differ. | none |
| DZ-3.10b | §3.10 (L149) | 中文和数字之间加空格 | ZH | Same convention as DZ-3.10a | — | none |
| DZ-3.10c | §3.10 (L150) | 代码块、JSON 键名、URL、内联代码不加空格 | X-DUP | Same as DZ-1.2c | — | both.keep-literals |
| DZ-3.11a | §3.11 (L153) | 技术文档禁用「你」「您」，用「开发者」「技术负责人」等角色词，或不直接称呼读者 | ZH/TECH | Chinese reference text often leaves the reader unaddressed, but a ban conflicts with style guides that use 你 or 您 | Conditional: prefer sentences without address; when a step addresses the reader, use one form (你 or 您) throughout and do not turn the reader into 用户, 开发者 or 人们. | none |
| DZ-3.11b | §3.11 (L154) | 博客可以用「你」，但不要通篇「你会发现」「你需要」「你可以看到」 | BOTH | Reader-addressing fillers pad any text | If 「你会发现」「你可以看到」 can go without loss, cut it. | both.cut-needless-words |
| DZ-3.12a | §3.12 (L157-158) | 物理动作动词用在抽象认知上（接住、击穿、锋利、不崩、不爆、打穿、扛住） → 日常中文 | BOTH | Picture verbs for abstract operations blur the claim in any language (EN "surfaces", JA 「運ぶ」, ZH 「接住」) | Replace a picture verb with the literal operation; keep field terms such as 缓存击穿. In technical text, 扛住 and 不崩 become the measured effect. | both.literal-claims, tech.plain-effect |
| DZ-3.12b | §3.12 (L160-161) | 抽象名词做主语（工程上的现实比这些数字难看） → 人/动作做主语 | BOTH | An abstract subject with an evaluative predicate hides the literal claim | If an abstract noun is the subject of an evaluation, state the literal fact: what was measured, and by whom if the reader needs it. | both.literal-claims, both.name-the-actor |
| DZ-3.13 | §3.13 (L163-165) | 空泛形容词预判（更干净：xxx、逻辑很清晰：xxx） → 删掉，直接说 | BOTH | A pre-judging label stands in for the evidence | If an evaluative label precedes the content that should show it, drop the label. | both.show-not-label |
| DZ-3.14a | §3.14 (L168) | 三连排比用太多 → 换二连或一连；一个可以，背靠背的三连是失败 | X-DUP | Same as SS-ST32 | The useful residue is a padded series (an item that adds nothing). | both.list-what-is-there |
| DZ-3.14b | §3.14 (L169) | 「首先...其次...最后」 → 「一方面...另一方面...」 | X-DEAI | Ordinal connectives are standard Chinese (公文 「一是…二是…」); the replacement fits only two-sided arguments | The residue, ordinals for points that do not build on each other, is a list-or-prose question. | both.lists-vs-prose |
| DZ-3.14c | §3.14 (L170) | 段落结尾都是 punchy 短句 → 换节奏 | X-DUP | Same as SS-ST34 | — | pers.rhythm-follows-content, both.state-dont-stage |
| DZ-3.14d | §3.14 (L171) | bold 小标题 + 句号（`**xxx**。content`） → `**xxx**，content` | X-DEAI | A punctuation detail of bold run-in heads | The residue, bold labels on every item, is DE-P24. | both.sparing-bold |
| DZ-4.1a | §4.1 (L180) | 技术文档语气：克制、直接、可扫读 | TECH | A reference-text norm | — | tech.neutral-register, tech.short-sentences |
| DZ-4.1b | §4.1 (L181) | 不用第二人称（「你」「您」） | X-DUP | Same as DZ-3.11a | — | none |
| DZ-4.1c | §4.1 (L182) | 不用「领先」「强大」「重磅」「颠覆」「震惊」「炸裂」等宣传形容词 | BOTH | Marketing praise without facts fails in any genre | A measured claim may stay ("starts in 0.4 s"). | both.facts-not-praise |
| DZ-4.1d | §4.1 (L183) | 不用「赋能」「抓手」「闭环」等黑话 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-4.1e | §4.1 (L184) | 不用感叹号 | X-DUP | Same as DZ-3.9c | — | tech.neutral-register |
| DZ-4.1f | §4.1 (L185) | 直角引号「」 | X-DUP | Same as DZ-3.9a | — | zh.full-width-punct |
| DZ-4.1g | §4.1 (L186) | 中英留白 | X-DUP | Same as DZ-3.10a | — | none |
| DZ-4.1h | §4.1 (L187) | 不改代码字面量、JSON 键名、URL、API 路径 | X-DUP | Same as DZ-1.2c | — | both.keep-literals |
| DZ-4.1i | §4.1 (L188) | 术语首次出现标注，后续不重复解释 | TECH | First-mention definitions are a technical-documentation norm | Explain a term at first mention only if the audience may not know it. | tech.first-mention, both.define-and-keep-terms |
| DZ-4.1j | §4.1 (L189) | 不用「Hello」「Hi」等问候开篇 | TECH | Docs start with content; replies and letters expect a greeting | In docs, no greeting; in a reply, keep the greeting the medium expects. | tech.neutral-register, both.answer-first-in-replies |
| DZ-4.1k | §4.1 (L190) | 目标：说清楚「它是什么、用来做什么、下一步看哪里」 | TECH | A reference intro states what the thing is and does | — | tech.point-first |
| DZ-4.2a | §4.2 (L195) | 默认口吻：资深工程师给同事讲系统 | TECH | A register default for technical articles | Without a sample, take the register from the kind of text. | both.match-house-and-voice |
| DZ-4.2b | §4.2 (L196) | 可以口语，但不俚语化 | X-DUP | Same as DZ-1.1a | — | both.match-house-and-voice |
| DZ-4.2c | §4.2 (L197) | 减少情绪词、感叹词、口头禅 | TECH | Technical articles are read for content; personal writing may keep the author's habits | When editing personal writing, keep the author's own words (pers.keep-author-voice). | tech.neutral-register |
| DZ-4.2d | §4.2 (L198) | 少用「说白了 / 其实 / 你会发现 / 谁能想到」推进行文 | ZH | Chinese filler connectives | Cut one when the sentence keeps its meaning; keep 其实 that marks the author's doubt or correction. | both.cut-needless-words, both.match-house-and-voice |
| DZ-4.2e | §4.2 (L199) | 优先追求：清楚、稳、具体、节奏自然 | X-DUP | Restates DZ-1.1a and DZ-4.5e | — | both.be-specific |
| DZ-4.2f | §4.2 (L200) | 优先做减法：删解释腔、删总结腔、删多余转折 | X-DUP | Same as DZ-1.2a | — | both.cut-needless-words |
| DZ-4.2g | §4.2 (L201) | 把润色做成减法，不是重写 | X-DUP | Same as DZ-1.1c | — | both.revise-without-loss |
| DZ-4.2h | §4.2 (L202) | 如果原句已经自然，不改 | X-DUP | Same as DZ-1.1c | — | both.revise-without-loss |
| DZ-4.2i | §4.2 (L203) | 非工程师受众：去「不懂技术的同学」等居高临下词，去「你必须」等训人腔，去太深术语；走「我怎么用的，你试试」路径 | BOTH | Condescension and unexplained jargon fail a lay audience in any genre | For a lay audience, drop condescending labels and explain or drop terms they do not know. The "我怎么用的" path is a PERSONAL device. | both.write-for-the-reader, tech.first-mention |
| DZ-4.3a | §4.3 (L209) | 社区先行：开头用社区锚点（star 数、感谢用户），改动清单放后面 | X-SCOPE | Launch-post marketing strategy | — | none |
| DZ-4.3b | §4.3 (L210) | 亮点不全量：挑 2-4 个最有意思的 | PERSONAL | A social post carries a few points; the changelog carries the list | In a social post, pick the items the reader cares about; link the full list. | none |
| DZ-4.3c | §4.3 (L211) | 用户感受帧：「你用它的时候...」，不是「这个工具做了...」 | X-SCOPE | Marketing framing | — | none |
| DZ-4.3d | §4.3 (L212) | 一条立场：至少一句表明决策原因的意见句 | PERSONAL | A stated rationale gives a post its point | If the material gives the reason for a decision, state it as the author's view. | pers.state-the-view |
| DZ-4.3e | §4.3 (L213) | 中文节奏：用地道表达，避免翻译腔和正式词 | X-DUP | Same as DZ-3.12a and DZ-1.1a | — | both.literal-claims |
| DZ-4.3f | §4.3 (L215) | 结尾用邀请，不用 CTA | X-SCOPE | Marketing | — | none |
| DZ-4.3g | §4.3 (L216) | 身份和敏感信号脱敏 | X-SCOPE | A privacy review step | — | none |
| DZ-4.3h | §4.3 (L217) | 不踩竞品 | X-SCOPE | A communication policy | — | none |
| DZ-4.3i | §4.3 (L218) | 公开前扫三件事：脱敏、不踩竞品、用户感受先于功能清单 | X-SCOPE | A review checklist | — | none |
| DZ-4.4a | §4.4 (L223) | 结构：Breaking Changes → New Features → Fixes & Improvements → Deprecations | TECH | Release-note order is a technical convention; the exact order is house style | Follow the project's last release; if there is none, put breaking changes first. | both.match-house-and-voice |
| DZ-4.4b | §4.4 (L224) | 格式：优先匹配目标项目最近一次 release 风格 | TECH | House style governs release notes | — | both.match-house-and-voice |
| DZ-4.4c | §4.4 (L225) | 条目：5-8 条，每条约一句话，只说用户效果 | TECH | Release notes describe the effect on users | "5-8" is arbitrary: list every user-facing change. | tech.specific-change-summary, both.list-what-is-there |
| DZ-4.4d | §4.4 (L226) | title：版本号 + 最核心改动或主题，不超过 10 个词 | X-SCOPE | A template's title length | — | none |
| DZ-4.4e | §4.4 (L227) | 不要加 emoji（除非项目本身庆祝风格） | X-DEAI | Emoji bans aimed at chatbot output (rubric example) | House style decides. | both.match-house-and-voice |
| DZ-4.4f | §4.4 (L228) | 不加「不再更新」「final release」「停止维护」等终止信号（除非真实情况） | BOTH | A status the facts do not give is an invented claim in any genre | — | both.claims-match-evidence, tech.operation-state |
| DZ-4.4g | §4.4 (L229) | 中英双语：条目一一对应，不混写，英文在前 | X-SCOPE | Bilingual release layout | — | none |
| DZ-4.5a | §4.5 (L234) | 保持学术正式度，但删除空洞套话 | X-DUP | Same as DZ-1.2a | — | both.cut-needless-words |
| DZ-4.5b | §4.5 (L235) | 用「我们」指自己工作（不用被动躲闪） | X-DUP | Same as SS-ST28 | ZH: 被 and 据观察-type evasions (zh.bei-passive). | both.name-the-actor, zh.bei-passive |
| DZ-4.5c | §4.5 (L236) | 引用具体作者，不用「有研究者指出」 | X-DUP | Same as DZ-3.7g | — | both.attribute-claims |
| DZ-4.5d | §4.5 (L237) | 不用「长期以来人们认识到...」 | X-DUP | Same as DZ-3.7g | — | both.attribute-claims |
| DZ-4.5e | §4.5 (L238) | 给出具体数字而非空泛结论 | BOTH | The most specific available fact helps any reader | Use the numbers the source gives; do not invent them. | both.be-specific |
| DZ-4.5f | §4.5 (L239) | 不用「在当今日新月异的领域中」 | X-DUP | Same as DZ-3.6 | — | zh.background-opener |
| DZ-4.5g | §4.5 (L240) | 不用「这一范式转变具有深远意义」 | X-DUP | Same as DZ-3.7c | — | both.facts-not-praise |
| DZ-4.5h | §4.5 (L241) | 不用「结果表明」「据观察」 | X-DUP | 据观察 is DZ-4.5b | 「结果表明」 is standard in Chinese scientific text and stays; the ban on it is wrong. | both.name-the-actor |
| DZ-4.6a | §4.6 (L246) | 中英字符间加空格 | X-DUP | Same as DZ-3.10a | — | none |
| DZ-4.6b | §4.6 (L247) | 不混用标点：中文用中文标点，英文用英文标点 | ZH | Punctuation choice by script | — | zh.full-width-punct |
| DZ-4.6c | §4.6 (L248) | 术语跨全文一致 | BOTH | One term per referent helps any reader | — | both.define-and-keep-terms |
| DZ-4.6d | §4.6 (L249) | 术语首次出现：保留英文 + 中文注解（或中文前置 + 英文括注） | TECH | A first-mention convention for translated terms | — | tech.first-mention, tech.established-terms |
| DZ-4.6e | §4.6 (L250) | 后续只用中文，不要中英混用 | X-DUP | Same as DZ-4.6c | — | both.define-and-keep-terms |
| DZ-4.6f | §4.6 (L251) | 常见可替换：context→上下文、state→状态、cache→缓存、claim→断言、runtime→运行时 | ZH | Established Chinese terms | — | tech.established-terms |
| DZ-4.6g | §4.6 (L252) | 术语未收敛的（prompt、embedding、tokenizer）保留英文合理 | ZH | Chinese has no settled term for these yet | — | tech.established-terms |
| DZ-4.6h | §4.6 (L253) | 双语版：条目编号一一对应，确认 EN/CN 意思一致，标记翻译损失 | X-SCOPE | A translation review process | — | none |
| DZ-4.6i | §4.6 (L254) | 禁止破折号 | X-DUP | Same as DZ-3.9b | — | zh.dash-form |
| DZ-5.01 | §五 (L262) | 非常 / 极其 → 很 | X-DUP | Same as DZ-3.8a | — | none |
| DZ-5.02 | §五 (L263) | 值得注意的是 → 直接说结论 | X-DUP | Same as DZ-3.8b | — | none |
| DZ-5.03 | §五 (L264) | 综上所述 / 总之 → 直接收尾 | X-DUP | Same as DZ-3.8c | — | zh.stock-closing |
| DZ-5.04 | §五 (L265) | 例如 → 比如 | X-DUP | Same as DZ-3.8d | — | none |
| DZ-5.05 | §五 (L266) | 购买 → 买 | X-DUP | Same as DZ-3.8e | — | none |
| DZ-5.06 | §五 (L267) | 使用 → 用 | X-DUP | Same as DZ-3.8e | — | none |
| DZ-5.07 | §五 (L268) | 拥有 → 有 | ZH | A Chinese word pair; the principle is both.plain-words | — | both.plain-words |
| DZ-5.08 | §五 (L269) | 呈现 → 是 / 显得 | ZH | A Chinese word pair; the principle is both.plain-words | — | both.plain-words |
| DZ-5.09 | §五 (L270) | 进行（+动词） → 删掉「进行」，用动词本身 | ZH | The 进行 + verb construction is Chinese grammar | Keep 进行 as a main verb (「迁移还在进行」) and in set phrases (「进行表决」). | zh.jinxing-verb |
| DZ-5.10 | §五 (L271) | 赋能 → 提供 / 帮助 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-5.11 | §五 (L272) | 抓手 → 关键措施 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-5.12 | §五 (L273) | 闭环 → 完整流程 | X-DUP | Same as DZ-3.7a | Keep 闭环控制 and 闭环反馈. | zh.plain-words |
| DZ-5.13 | §五 (L274) | 沉淀 → 形成 / 积累 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-5.14 | §五 (L275) | 对齐 → 统一 | X-DUP | Same as DZ-3.7a | Keep 内存对齐 and 文本对齐. | zh.plain-words |
| DZ-5.15 | §五 (L276) | 拉通 / 打通 → 连接 / 贯通 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-5.16 | §五 (L277) | 洞察 → 分析结论 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-5.17 | §五 (L278) | 兜底 → 保障机制 | X-DUP | Same as DZ-3.7a | — | zh.plain-words |
| DZ-5.18 | §五 (L279) | 至关重要 / 意义重大 → 重要 | X-DUP | Same as DZ-3.7c | — | zh.plain-words, both.facts-not-praise |
| DZ-5.19 | §五 (L280) | 褒有 → 有 | X-DUP | Same as DZ-5.07 | 褒有 is not a Chinese word; probably a typo for 葆有 or 拥有. | both.plain-words |
| DZ-5.20 | §五 (L281) | 坐落于 → 在 | ZH | A Chinese word pair; the principle is both.plain-words | — | both.plain-words |
| DZ-5.21 | §五 (L282) | 致力于 → 努力 / 专注 | ZH | A Chinese word pair; the principle is both.plain-words | — | both.plain-words |
| DZ-6.1 | §六 (L288) | 先识别场景，确定语气标准 | X-SCOPE | Process step | — | none |
| DZ-6.2 | §六 (L289) | 先保语义 | X-DUP | Same as DZ-1.3 | — | both.revise-without-loss |
| DZ-6.3 | §六 (L290-295) | 做减法的顺序：段末总结句 → 对比句式 → 喉清开场、元评论、强调拐杖 → 副词、被动语态、假主体 → 黑话、空洞形容词 | X-SCOPE | Process order | It names categories that DZ never defines (喉清开场, 元评论, 强调拐杖, 副词, 被动语态, 假主体); they are SS-P01, SS-P06, SS-P02, SS-P04, SS-ST28 and SS-ST23. | none |
| DZ-6.4 | §六 (L296) | 再顺句子：节奏、标点、中英留白、破折号 | X-SCOPE | Process step | — | none |
| DZ-6.5 | §六 (L297) | 最后回读：优先修不自然处，不强改自然处 | X-DUP | Same as DZ-1.1c | — | both.revise-without-loss |
| DZ-6.6 | §六 (L298) | 只给改写后的文本，不加改动清单、解释、收尾话 | X-SCOPE | Output format | — | none |
| DZ-7.1 | §七 示例 1 (L304-312) | 中文技术博客开头改写 | X-DUP | Illustrates DZ-3.6, DZ-3.8b, DZ-3.3, DZ-3.2 | The 改写后 adds facts that the 改写前 lacks (三年生产环境, 五个坑, 止损方案). As an editing model it breaks both.claims-match-evidence and DZ-1.3. | both.claims-match-evidence |
| DZ-7.2 | §七 示例 2 (L314-322) | 技术文档开头改写 | X-DUP | Illustrates DZ-4.1j, DZ-3.9c, DZ-4.1c, DZ-3.7a, DZ-3.11a | The 改写后 invents a capability list (批量查询、实时推送、数据清洗) and a 「认证」章节. | both.claims-match-evidence |
| DZ-7.3 | §七 示例 3 (L324-330) | 对比句式修复 | X-DUP | Illustrates DZ-3.3 | The example writes "微" with half-width quotes, against DZ-3.9a and zh.full-width-punct. | both.real-contrasts, zh.full-width-punct |
| DZ-7.4 | §七 示例 4 (L332-338) | 空洞套话净化 | X-DUP | Illustrates DZ-3.7c | The 改写后 adds a benchmark (Redis QPS two orders of magnitude above MySQL) that the 改写前 lacks. | both.facts-not-praise, both.claims-match-evidence |
| DZ-8 | §八 (L342-352) | 质量评分：直接性、节奏、信任、真实度、密度，各 1-10 分，低于 35/50 需修订 | X-SCOPE | Self-scoring procedure | "真实度" is a de-AI criterion. | none |
| DZ-9 | §九 (L356-359) | 相关技能 | X-SCOPE | Pointer to other skills | — | none |

## deslop-en/SKILL.md

| ID | Source location | Rule (short paraphrase, or quote if short) | Destination | Reason (one clause) | Conditional wording / notes | Candidate rule(s) |
|---|---|---|---|---|---|---|
| DE-C1 | Core Principles 1 (L17) | "Naturalness first." Don't add slang or forced quirkiness; if it's already clean, don't touch it | X-DUP | Same as DZ-1.1a and DZ-1.1c | — | both.match-house-and-voice, both.revise-without-loss |
| DE-C2 | Core Principles 2 (L18) | "Subtraction over addition." Kill filler, adverbs and throat-clearing before adjusting rhythm | X-DUP | Same as DZ-1.2a | — | both.cut-needless-words |
| DE-C3 | Core Principles 3 (L19) | "Preserve meaning." If removing a pattern alters the author's intent, keep the original | X-DUP | Same as DZ-1.3 | — | both.revise-without-loss |
| DE-C4 | Core Principles 4 (L20) | "Match register to context." | BOTH | The kind of text sets the register in any language | If the project or user gives a style, follow it; otherwise take the register from the kind of text. | both.match-house-and-voice |
| DE-Q01 | Quick Checklist (L26) | Any adverbs (-ly words)? Delete them | X-DUP | Same as DE-P02a | — | en.empty-emphasis |
| DE-Q02 | Quick Checklist (L27) | Any passive voice? Find the actor | X-DUP | Same as DE-P03 | — | both.name-the-actor |
| DE-Q03 | Quick Checklist (L28) | Inanimate thing doing a human verb ("the decision emerges")? Name the person | X-DUP | Same as DE-P04 | — | both.name-the-actor |
| DE-Q04 | Quick Checklist (L29) | Any "here's what/this/that" throat-clearing? | X-DUP | Same as DE-P01 | — | both.no-empty-previews |
| DE-Q05 | Quick Checklist (L30) | Any "not X, it's Y" contrasts? | X-DUP | Same as DE-P05 | — | both.real-contrasts |
| DE-Q06 | Quick Checklist (L31) | Self-posed rhetorical question answered immediately? | X-DUP | Same as DE-P07 | — | both.state-dont-stage |
| DE-Q07 | Quick Checklist (L32) | Three consecutive sentences match length? Break one | X-DUP | Same as SS-C6a | — | pers.rhythm-follows-content |
| DE-Q08 | Quick Checklist (L33) | Paragraph ends with a punchy one-liner? Vary it | X-DUP | Same as SS-ST34 | — | pers.rhythm-follows-content |
| DE-Q09 | Quick Checklist (L34) | Em dash anywhere? Replace it | X-DUP | Same as DE-P25 | — | none |
| DE-Q10 | Quick Checklist (L35) | Vague declarative ("The implications are significant")? Name the implication | X-DUP | Same as SS-P09 | — | both.show-not-label |
| DE-Q11 | Quick Checklist (L36) | Meta-joiners ("The rest of this essay...")? Delete | X-DUP | Same as DE-P11 | — | pers.no-signposts |
| DE-Q12 | Quick Checklist (L37) | "Let's break this down" / "Let's dive in"? Delete | X-DUP | Same as DE-P14 | — | both.no-empty-previews |
| DE-Q13 | Quick Checklist (L38) | Tricolon stacking? Use two items or one | X-DUP | Same as DE-P08 | — | both.list-what-is-there |
| DE-Q14 | Quick Checklist (L39) | Every list item starts with a bold keyword? Reformulate | X-DUP | Same as DE-P24 | — | both.sparing-bold |
| DE-P01 | Throat-Clearing Openers (L45-49) | Remove announcement phrases: Here's the thing / The truth is / Let me be clear / It turns out / I'm going to be honest / Can we talk about / Here's the kicker / Here's where it gets interesting | X-DUP | Same as SS-P01 | Adds 'Here's the kicker' and 'Here's where it gets interesting', setup lines that promise a reveal (both.state-dont-stage). EN words go to the EN examples. | both.no-empty-previews, both.state-dont-stage |
| DE-P02a | Adverbs (L51-54) | "Kill all -ly words." List: really, just, literally, genuinely, honestly, simply, actually, deeply, truly, fundamentally, inherently, inevitably, interestingly, importantly, crucially, quietly, remarkably, arguably, certainly | X-DUP | Same as SS-P04 | Adds quietly, remarkably, arguably and certainly. 'arguably' is a hedge: deleting it raises the claim's certainty (both.keep-certainty, pers.state-the-view). "All -ly words" is English morphology and wrong for manner and scope adverbs. | en.empty-emphasis, both.cut-needless-words, both.show-not-label |
| DE-P02b | Adverbs, filler phrases (L56-57) | At its core / In today's [X] / It's worth noting / It bears mentioning / Notably / At the end of the day / When it comes to / In a world where / The reality is | X-DUP | Same as SS-P05 | Adds 'It bears mentioning' and 'Notably'. | both.show-not-label, both.cut-needless-words |
| DE-P03 | Passive Voice & False Agency (L59-60) | "Every sentence needs a human subject doing something." Find the actor | X-DUP | Same as SS-ST28 and SS-C3a | "Every sentence needs a human subject" is wrong for system behavior, imperative steps and JA/ZH subject omission; use SS-ST28's condition. | both.name-the-actor |
| DE-P04 | Passive Voice & False Agency (L62-69) | Inanimate objects don't perform human verbs ("the complaint becomes a fix", "the decision emerges", "the data tells us", "the market rewards"); name the actor, or use "you" or "we" | X-DUP | Same as SS-ST23 | — | both.name-the-actor, en.real-actor |
| DE-P05 | Binary Contrasts (L71-75) | "It's not X — it's Y." / "Not because X. Because Y." / "The question isn't X. It's Y." / "stops being X and starts being Y" → state Y | X-DUP | Same as SS-ST06 | — | both.real-contrasts |
| DE-P06 | Negative Listing (L77-81) | "Not a X. Not a Y. A Z." / "It wasn't X. It wasn't Y. It was Z." / "Not ten. Not fifty. Five hundred." → state Z | X-DUP | Same as SS-ST12 | Adds the numeric countdown. | both.real-contrasts |
| DE-P07 | Self-Posed Rhetorical Questions (L83-87) | "The result? Devastating." / "The worst part? Nobody saw it coming." / "What if I told you..." → state it | BOTH | A question that nobody asked, answered in its next words, stages a point that a sentence could state, in any language | If a question is answered in its next words and no reader asked it, state the answer. Keep FAQ headings, questions the reader asked and real open questions. SS-ST33 was tagged X-DEAI; the candidate set keeps this narrower form, and this row follows it. "What if I told you" is a meme (SS-ST17). | both.state-dont-stage |
| DE-P08 | Tricolon Abuse (L89-93) | Overuse of the rule of three; use two items or one; "A single tricolon is fine. Back-to-back tricola are pattern recognition failure." | X-DEAI | A frequency tell (rubric example); a list holds as many items as there are facts | The residue is a padded series or back-to-back antitheses whose items add nothing (both.list-what-is-there). | both.list-what-is-there |
| DE-P09 | Anaphora Abuse (L95-99) | "They assume that... They assume that... They assume that..." → vary openings, combine points | BOTH | Repeating an opener to carry one idea pads running prose in any language | In running prose, if three or more consecutive sentences open with the same words to carry one idea, merge them. Procedure steps, list items and headings may share an opening; Chinese 排比 used for one deliberate rhetorical effect stays in personal writing. | both.merge-repeated-referents |
| DE-P10 | Dramatic Fragmentation (L101-105) | "[Noun]. That's it. That's the [thing]." / "He published this. Openly. In a book. As a priest." / "Platforms do." → complete sentences | BOTH | A run of fragments that restates a point for effect stages it instead of stating it | If fragments or one-line paragraphs restate a point for effect, write the claim as a sentence. Keep a short sentence that carries a new fact; headings, list items and labels are fragments by design. SS-ST14 was tagged X-DEAI; the candidate set keeps this narrower form. | both.state-dont-stage, en.complete-sentences |
| DE-P11 | Meta-Commentary (L107-111) | "In this section, we'll explore..." / "As we'll see..." / "Let me walk you through..." / "The rest of this essay explains..." / "And so we return to where we began." → delete | X-DUP | Same as SS-P06 | Adds the circular close 'And so we return to where we began.' | pers.no-signposts, both.no-empty-previews |
| DE-P12 | The "Serves As" Dodge (L113-117) | serves as / stands as / marks / represents / constitutes / boasts / features (as 'has') → is / are / has | EN | English copula substitutes | Keep 'acts as' or 'functions as' for a stand-in, 'represents' for a literal model mapping (a node that represents a server), and the noun 'features'. The universal principle is both.plain-words. | en.copula-verbs, both.plain-words |
| DE-P13 | Emphasis Crutches (L119-123) | Full stop. / Period. / Let that sink in. / This matters because. / Make no mistake. / Here's why that matters. → delete | X-DUP | Same as SS-P02 | — | both.show-not-label, both.state-dont-stage |
| DE-P14 | Pedagogical Hand-Holding (L125-129) | Let's break this down. / Let's unpack this. / Let's dive in. / Think of it as... / Imagine a world where... → state the information | BOTH | Hand-holding lead-ins delay the content in any genre (ZH 「下面我们一起来看看」, JA 「では見ていきましょう」) | Delete a "Let's …" lead-in that only announces; keep an analogy that explains (DE-P23); "Imagine a world where" is stakes inflation (DZ-3.7c). A tutorial may keep a "let's" step voice where house style uses it. | both.no-empty-previews, both.write-for-the-reader, both.facts-not-praise |
| DE-P15 | Superficial Participle Analyses (L131-135) | "contributing to the region's rich cultural heritage" / "highlighting its importance" / "underscoring the need" → delete or give evidence | BOTH | A tacked-on significance clause adds unsupported meaning in any language (ZH 「，彰显了……」, JA 「〜を象徴している」) | Keep a trailing clause that states a cause, purpose or result from the facts. The -ing form is English grammar (en.ing-rider). | both.facts-not-praise, en.ing-rider, zh.significance-tail |
| DE-P16 | False Ranges (L137-141) | "From innovation to implementation to cultural transformation." → use "from X to Y" only on a real scale | BOTH | A range whose ends are not on one scale misstates a list in any language (ZH 「从……到……」) | Write "from X to Y" only for two ends of one scale; otherwise list the items. | both.list-what-is-there |
| DE-P17 | Listicle in a Trench Coat (L143-147) | "The first wall is... The second wall is..." → if a list is needed, use a list | BOTH | Ordinal prose for independent points hides a list in any language (ZH 「第一……第二……」) | If the points do not build on each other, use a list or weave them; ordinals inside a chain of reasoning, and JA/ZH ordinal conventions in formal reports, are fine. | both.lists-vs-prose |
| DE-P18 | Notability Overemphasis (L149-153) | "Her views have been featured in Forbes, TechCrunch, Wired, and The New York Times..." → mention sources only where they belong | BOTH | A press list stands in for a source in any genre | Name an outlet only with what it said that bears on the point. | both.attribute-claims |
| DE-P19 | Vague Attribution (L155-159) | "Experts argue..." / "Many believe..." / "Studies show..." / "It is widely regarded..." / "Observers note..." → name the source or don't invoke one | X-DUP | Same as DZ-3.7g | — | both.attribute-claims |
| DE-P20 | The "Despite Its... Faces Challenges" Formula (L161-165) | Formulaic challenges-and-prospects ending (Korattur) → name specific problems | X-DUP | Same as DZ-3.7h | — | both.facts-not-praise |
| DE-P21 | False Vulnerability / Performative Emphasis (L167-171) | "And yes, I'm openly..." / "This is not a rant; it's a diagnosis" / "I promise" / "They exist, I promise" / "creeps in" → delete | PERSONAL | Performed candor replaces the admission or evidence it pretends to give; tech text does not use it | If you admit a bias or limit, name it and say what it changes; replace "I promise" with the evidence. "creeps in" does not fit the category. Overlaps SS-P07. | pers.specific-admission |
| DE-P22 | Elegant Variation (L173-177) | Cycling synonyms to avoid repetition ("Soviet artistic constraints… non-conformist artists… state-imposed artistic norms…") → repeat the word | BOTH | Synonym cycling makes readers think a new thing is meant, in any language | Use one term per referent; pronouns and obvious short forms are fine. | both.define-and-keep-terms |
| DE-P23 | Patronizing Analogies (L179-183) | "Think of it as a Swiss Army knife." / "Think of it like a highway system for data." → explain directly unless the analogy carries real weight | BOTH | An analogy the reader does not need talks down and blurs the claim | Keep an analogy that explains a mechanism more clearly than the literal wording (a buffer "works like a write-ahead log"). | both.write-for-the-reader, both.literal-claims |
| DE-P24 | Bold-First Bullets (L185-189) | Every list item starts with a bolded keyword and colon → write as prose | BOTH | Bold labels that only repeat their item add noise in any genre | Remove a bold label that only repeats its item. Keep term–description lists (glossaries, parameters) and keep a list as a list: "write as prose" conflicts with both.lists-vs-prose for parallel items. | both.sparing-bold, both.lists-vs-prose |
| DE-P25 | Em Dash Overuse (L191-195) | "More than one em dash per 500 words is a tell." → periods, commas | X-DEAI | Em-dash counting is a surface tell (rubric example) | Dash form is a language-skill matter (zh.dash-form). | none |
| DE-G01 | Blog Posts & Newsletters (L202) | Put the reader in the room: "You" beats "People"; specifics beat abstractions | X-DUP | Same as SS-ST24 | — | pers.reader-in-scene |
| DE-G02 | Blog Posts & Newsletters (L203) | No narrator-from-a-distance ("Nobody designed this" → "You inherit a system that grew by accretion") | X-DUP | Same as SS-ST24 | — | pers.reader-in-scene |
| DE-G03 | Blog Posts & Newsletters (L204) | One point per section; don't restate the same argument ten ways | BOTH | Restating one claim in new words wastes the reader's time in any genre | Write each claim once; repeat a warning only at each step it applies to. | both.say-it-once |
| DE-G04 | Scientific Writing (L207) | Maintain formality while cutting hollow filler | X-DUP | Same as DZ-1.2a | — | both.cut-needless-words |
| DE-G05 | Scientific Writing (L208) | Use "we" for your own work (no passive evasion) | X-DUP | Same as DZ-4.5b | — | both.name-the-actor |
| DE-G06 | Scientific Writing (L209) | Cite specific authors, not "researchers have shown." | X-DUP | Same as DZ-3.7g | — | both.attribute-claims |
| DE-G07 | Scientific Writing (L210) | Give concrete numbers ("Each additional week added roughly 15% to the mean WIS.") | X-DUP | Same as DZ-4.5e | The example keeps "roughly": the hedge stays with the number (both.keep-certainty). | both.be-specific, both.keep-certainty |
| DE-G08 | Scientific Writing (L211) | No "In today's rapidly evolving landscape" / "This paradigm shift has far-reaching implications" / "It has long been recognized that" / "It was observed that" | X-DUP | Same as SS-P05, DZ-3.7c, DZ-3.7g and DZ-4.5b | — | both.cut-needless-words, both.facts-not-praise, both.attribute-claims, both.name-the-actor |
| DE-G09 | Release Notes (L214) | Breaking Changes → New Features → Fixes & Improvements → Deprecations | X-DUP | Same as DZ-4.4a | — | both.match-house-and-voice |
| DE-G10 | Release Notes (L215) | Match the target project's most recent release style | X-DUP | Same as DZ-4.4b | — | both.match-house-and-voice |
| DE-G11 | Release Notes (L216) | 5-8 items, one sentence each, user impact | X-DUP | Same as DZ-4.4c | — | tech.specific-change-summary |
| DE-G12 | Release Notes (L217) | No emoji unless the project is celebratory | X-DUP | Same as DZ-4.4e | — | both.match-house-and-voice |
| DE-G13 | Social Copy (L220) | Lead with community context (stars, user thanks) | X-DUP | Same as DZ-4.3a | — | none |
| DE-G14 | Social Copy (L221) | Pick 2-4 highlights, not the full changelog | X-DUP | Same as DZ-4.3b | — | none |
| DE-G15 | Social Copy (L222) | Write from user experience: "When you use it..." not "This tool does..." | X-DUP | Same as DZ-4.3c | — | none |
| DE-G16 | Social Copy (L223) | At least one sentence stating a decision rationale | X-DUP | Same as DZ-4.3d | — | pers.state-the-view |
| DE-G17 | Social Copy (L224) | End with an invitation, not a CTA | X-DUP | Same as DZ-4.3f | — | none |
| DE-V01 | Vocabulary table (L232) | serve as / stand as / marks / represents → is / are | X-DUP | Same as DE-P12 | — | en.copula-verbs |
| DE-V02 | Vocabulary table (L233) | boasts / features (as 'has') → has | X-DUP | Same as DE-P12 | — | en.copula-verbs |
| DE-V03 | Vocabulary table (L234) | leverage / utilize → use | EN | English vocabulary; the principle is both.plain-words | Keep 'leverage' as a finance term. | both.plain-words |
| DE-V04 | Vocabulary table (L235) | harness → use / apply | EN | English vocabulary | Keep 'test harness'. | both.plain-words |
| DE-V05 | Vocabulary table (L236) | streamline → simplify | EN | English vocabulary | — | both.plain-words |
| DE-V06 | Vocabulary table (L237) | navigate (challenges) → handle / address | X-DUP | Same as SS-P03 | — | both.plain-words |
| DE-V07 | Vocabulary table (L238) | unpack → explain / examine | X-DUP | Same as SS-P03 | — | both.plain-words |
| DE-V08 | Vocabulary table (L239) | deep dive → analysis / examination | X-DUP | Same as SS-P03 | — | both.plain-words |
| DE-V09 | Vocabulary table (L240) | delve → examine / look at / explore | EN | English vocabulary | — | both.plain-words |
| DE-V10 | Vocabulary table (L241) | robust → strong / solid / reliable | EN | English vocabulary | Better: name the property ("retries three times with backoff"). Keep technical 'robust regression' and 'robust statistics'. | en.empty-emphasis |
| DE-V11 | Vocabulary table (L242) | paradigm → model / system / approach | EN | English vocabulary | — | both.plain-words |
| DE-V12 | Vocabulary table (L243) | synergy → cooperation / combined effect | EN | English vocabulary | — | both.plain-words |
| DE-V13 | Vocabulary table (L244) | ecosystem → system / field / community | EN | English vocabulary | Keep literal ecosystems (biology) and package ecosystems (npm). | both.plain-words, tech.established-terms |
| DE-V14 | Vocabulary table (L245) | landscape → situation / field / area | X-DUP | Same as SS-P03 | — | both.plain-words |
| DE-V15 | Vocabulary table (L246) | tapestry → mix / combination / range | EN | English vocabulary | — | both.plain-words, both.literal-claims |
| DE-V16 | Vocabulary table (L247) | crucial / pivotal / vital → important / key | EN | English vocabulary | "important" is still a label; better, show why (both.show-not-label). | both.show-not-label |
| DE-V17 | Vocabulary table (L248) | profound / indelible / paramount → significant (or delete) | EN | English vocabulary | As DE-V16. | both.show-not-label, both.facts-not-praise |
| DE-V18 | Vocabulary table (L249) | showcase → show / display | EN | English vocabulary | — | both.plain-words |
| DE-V19 | Vocabulary table (L250) | underscore / highlight → point out / show | EN | English vocabulary | As sentence tails, DE-P15 applies. | both.plain-words, en.ing-rider |
| DE-V20 | Vocabulary table (L251) | foster / cultivate → encourage / build | EN | English vocabulary | Keep literal uses (foster care, cell culture). | both.plain-words |
| DE-V21 | Vocabulary table (L252) | garner → get / receive | EN | English vocabulary | — | both.plain-words |
| DE-V22 | Vocabulary table (L253) | bolster → support / boost | EN | English vocabulary | — | both.plain-words |
| DE-V23 | Vocabulary table (L254) | facilitate → help / enable | EN | English vocabulary | — | both.plain-words |
| DE-V24 | Vocabulary table (L255) | consequently / thus / hence → so | EN | English vocabulary | The causal relation must stay (both.name-the-relation); "thus" and "hence" are normal in mathematical and scientific prose. | both.name-the-relation, both.plain-words |
| DE-V25 | Vocabulary table (L256) | furthermore / moreover / additionally → also / and | EN | English vocabulary | — | both.plain-words |
| DE-V26 | Vocabulary table (L257) | nonetheless / nevertheless → still / but | EN | English vocabulary | Keep the contrast. | both.plain-words, both.name-the-relation |
| DE-H1 | Hard ban (L260) | Never use: delve, tapestry, nuanced, certainly, realm, nexus, interplay, cornerstone, beacon, pillar, catalyst, crucible, confluence, odyssey, multifaceted, holistic, compelling | EN | English words | "Never" is wrong for literal senses: catalyst (chemistry), pillar (construction), crucible (metallurgy), compelling (law), holistic (medicine). Replace a word when it is figurative or decorative. | both.plain-words, en.empty-emphasis |
| DE-H2 | Hard ban (L261) | quietly orchestrating / fundamentally reshape / navigate the landscape / rich cultural heritage / diverse array | EN | English phrases | Residues: magic adverbs (SS-P04), stakes inflation (DZ-3.7c), jargon (SS-P03), significance tails (DE-P15). | both.show-not-label, both.facts-not-praise, both.plain-words |
| DE-H3 | Hard ban (L262) | groundbreaking, transformative, indelible, paramount, indispensable, quintessential | X-DUP | Same as DZ-4.1c | EN words go to the EN examples. | both.facts-not-praise |
| DE-H4 | Hard ban (L263) | showcases, fosters, garners, bolsters, spearheads, galvanizes | X-DUP | Same as DE-V18, DE-V20 to DE-V22 | Adds spearheads (→ led) and galvanizes (→ prompted). | both.plain-words |
| DE-H5 | Hard ban (L264) | In today's fast-paced world / In the ever-evolving landscape / It's worth noting / Without further ado | X-DUP | Same as SS-P05 and DE-P14 | 'Without further ado' is a preamble. | both.no-empty-previews, both.show-not-label |
| DE-X1 | Execution Flow 1 (L270) | Identify the genre; lock in the register | X-SCOPE | Process step | — | none |
| DE-X2 | Execution Flow 2 (L271) | Preserve meaning | X-DUP | Same as DE-C3 | — | both.revise-without-loss |
| DE-X3 | Execution Flow 3 (L272-278) | Subtract first: openers, meta-commentary, crutches, all adverbs, binary contrasts, false agency, "serves as", vague declaratives | X-SCOPE | Process order; each item has its own row | "Kill all adverbs" repeats DE-P02a's absolute form. | none |
| DE-X4 | Execution Flow 4 (L279) | Then smooth: vary sentence length, break tricola, remove em dashes | X-SCOPE | Process step | — | none |
| DE-X5 | Execution Flow 5 (L280) | Final readthrough; don't force changes on already-clean sentences | X-DUP | Same as DE-C1 | — | both.revise-without-loss |
| DE-X6 | Execution Flow 6 (L281) | Output the rewritten text only | X-SCOPE | Output format | — | none |
| DE-E1 | Example 1, Blog Post (L287-293) | Distributed-systems opener rewritten | X-DUP | Illustrates DE-P01, DE-P02a, DE-P05, DE-P13 and DE-Q10 | The after invents facts the before lacks: three failure sources, a claim about unit tests, and three adopted patterns. As an editing model it breaks both.claims-match-evidence. | both.claims-match-evidence |
| DE-E2 | Example 2, Scientific Abstract (L295-301) | FluSight "serves as" sentence rewritten | X-DUP | Illustrates DE-P12 and DE-P15 | The after adds facts ("dozens of modeling groups", "Since 2013 …") that the before lacks. | both.claims-match-evidence |
| DE-E3 | Example 3, Cover Letter (L303-309) | Filler and "despite these challenges" rewritten into the specific implication | X-DUP | Illustrates SS-P05, DE-P20, DE-P15 and DE-V10 | The after keeps the conditional "If … may not": a model for both.keep-certainty. | both.show-not-label, both.keep-certainty |
| DE-E4 | Example 4, Vague → Specific (L311-317) | Genomic-landscape opener rewritten | X-DUP | Illustrates SS-P05, DE-V14, DE-V11 and DZ-3.7c | — | both.facts-not-praise |
| DE-S1 | Scoring (L321-331) | Five dimensions 1-10; revise below 35/50 | X-SCOPE | Self-scoring procedure | "Authenticity" is a de-AI criterion. | none |
| DE-R1 | Related Skills (L335-337) | Pointer to deslop-zh | X-SCOPE | Pointer | — | none |

## deslop (stephenturner/skill-deslop copy)

| ID | Source location | Rule (short paraphrase, or quote if short) | Destination | Reason (one clause) | Conditional wording / notes | Candidate rule(s) |
|---|---|---|---|---|---|---|
| DS-W1 | SKILL.md §When to Apply (L10-15) | When the skill applies | X-SCOPE | Trigger description | — | none |
| DS-C1 | SKILL.md §Core Rules 1 (L19-21) | Cut filler phrases: throat-clearing, emphasis crutches, business jargon, meta-commentary | X-DUP | Summary of DS-P01, DS-P02, DS-P04 and DS-P09 | — | both.no-empty-previews, both.plain-words |
| DS-C2 | SKILL.md §Core Rules 2 (L23-25) | Break formulaic structures: binary contrasts, negative listings, dramatic fragmentation, self-posed questions, anaphora and tricolon abuse | X-DUP | Summary of DS-ST01, DS-ST12, DS-ST16, DS-ST21, DS-ST27 and DS-ST30 | — | both.real-contrasts, both.state-dont-stage |
| DS-C3 | SKILL.md §Core Rules 3 (L27-29) | Eliminate AI tropes: "quietly", "delve", "serves as", false ranges, participle analyses, invented concept labels, grandiose stakes, patronizing analogies, false vulnerability | X-DUP | Each item has its own row: DS-P07, DS-P05, DS-P06, DS-ST41, DS-ST40, DS-ST62, DS-P16, DE-P23, DS-P11 | The pointer to references/tropes.md is not audited. | both.show-not-label, both.plain-words, both.facts-not-praise |
| DS-C4 | SKILL.md §Core Rules 4 (L31-33) | Active voice with human subjects; "we" in science, "you" in blogs | X-DUP | Same as SS-ST28 and SS-ST23 | — | both.name-the-actor |
| DS-C5a | SKILL.md §Core Rules 5 (L37) | No vague declaratives ("The reasons are structural") | X-DUP | Same as SS-P09 | — | both.show-not-label |
| DS-C5b | SKILL.md §Core Rules 5 (L37) | No lazy extremes ("every," "always," "never") doing vague work | X-DUP | Same as SS-ST38 | — | both.scope-claims |
| DS-C5c | SKILL.md §Core Rules 5 (L37) | No vague attributions; "If you cannot name the expert, you do not have a source." | X-DUP | Same as DZ-3.7g | — | both.attribute-claims |
| DS-C5d | SKILL.md §Core Rules 5 (L39) | In scientific writing, domain terminology is fine ("Weighted interval score" is precise language); the problem is business buzzwords and AI vocabulary | TECH | Precise field terms are required in technical and scientific text | Keep established field terms; replace decorative buzzwords. This guards against over-applying DS-P04 and DE-H1. | tech.established-terms, both.plain-words |
| DS-C6a | SKILL.md §Core Rules 6 (L43) | Blogs: put the reader in the room; "You" beats "People"; no narrator-from-a-distance | X-DUP | Same as SS-ST24 | — | pers.reader-in-scene |
| DS-C6b | SKILL.md §Core Rules 6 (L45) | Scientific: formal; "we" for own work; cite specific authors; no "It has long been recognized that..."; no casual blog voice | X-DUP | Same as DZ-4.5b, DZ-3.7g and DE-C4 | — | both.name-the-actor, both.attribute-claims, both.match-house-and-voice |
| DS-C7a | SKILL.md §Core Rules 7 (L49) | Mix sentence lengths | X-DUP | Same as SS-C6a | — | pers.rhythm-follows-content |
| DS-C7b | SKILL.md §Core Rules 7 (L49) | Two items beat three | X-DUP | Same as SS-ST32 | Conflicts with DE-P08's "A single tricolon is fine." | both.list-what-is-there |
| DS-C7c | SKILL.md §Core Rules 7 (L49) | End paragraphs differently | X-DUP | Same as SS-ST34 | — | pers.rhythm-follows-content |
| DS-C7d | SKILL.md §Core Rules 7 (L49) | No em dashes | X-DUP | Same as SS-ST35 | — | none |
| DS-C7e | SKILL.md §Core Rules 7 (L49) | Do not stack short punchy fragments for manufactured emphasis | X-DUP | Same as DE-P10 | — | both.state-dont-stage |
| DS-C7f | SKILL.md §Core Rules 7 (L49) | No listicles disguised as prose ("The first wall... The second wall...") | X-DUP | Same as DE-P17 | — | both.lists-vs-prose |
| DS-C8a | SKILL.md §Core Rules 8 (L53) | Trust readers: state facts directly; skip softening, justification, hand-holding | X-DUP | Same as SS-C7 | — | both.write-for-the-reader, both.keep-certainty |
| DS-C8b | SKILL.md §Core Rules 8 (L53) | No "Let's break this down", no "Think of it as...", no pedagogical voice unless the audience needs it | X-DUP | Same as DE-P14 | — | both.no-empty-previews, both.write-for-the-reader |
| DS-C8c | SKILL.md §Core Rules 8 (L53) | No fractal summaries | X-DUP | Same as DS-ST59 | — | both.say-it-once |
| DS-C9 | SKILL.md §Core Rules 9 (L57) | Formatting tells: no bold-first bullets, unicode arrows, em dashes, signposted conclusions or "Despite these challenges..." formulas | X-DUP | Same as DS-ST55, DS-ST56, SS-ST35, DS-ST58 and DE-P20 | — | both.sparing-bold, pers.no-signposts, both.facts-not-praise |
| DS-C10a | SKILL.md §Core Rules 10 (L61) | One point per section; don't restate the same argument ten ways | X-DUP | Same as DE-G03 | — | both.say-it-once |
| DS-C10b | SKILL.md §Core Rules 10 (L61) | Don't beat a single metaphor to death | X-DUP | Same as DS-ST61 | — | none |
| DS-C10c | SKILL.md §Core Rules 10 (L61) | Don't stack historical analogies for false authority ("Apple didn't build Uber…") | X-DUP | Same as DS-ST42 | — | both.attribute-claims, both.be-specific |
| DS-Q01 | SKILL.md §Quick Checks (L67) | Heavy use of adverbs or -ly words? Cut them | X-DUP | Same as SS-P04 | — | en.empty-emphasis |
| DS-Q02 | SKILL.md §Quick Checks (L68) | Any passive voice? Find the actor | X-DUP | Same as SS-ST28 | — | both.name-the-actor |
| DS-Q03 | SKILL.md §Quick Checks (L69) | Inanimate thing doing a human verb? Name the person | X-DUP | Same as SS-ST23 | — | both.name-the-actor |
| DS-Q04 | SKILL.md §Quick Checks (L70) | Any "here's what/this/that" throat-clearing? | X-DUP | Same as SS-P01 | — | both.no-empty-previews |
| DS-Q05 | SKILL.md §Quick Checks (L71) | Any "not X, it's Y" contrasts? | X-DUP | Same as SS-ST06 | — | both.real-contrasts |
| DS-Q06 | SKILL.md §Quick Checks (L72) | Self-posed rhetorical question answered immediately? | X-DUP | Same as DE-P07 | — | both.state-dont-stage |
| DS-Q07 | SKILL.md §Quick Checks (L73) | Three consecutive sentences match length? | X-DUP | Same as SS-C6a | — | pers.rhythm-follows-content |
| DS-Q08 | SKILL.md §Quick Checks (L74) | Paragraph ends with a punchy one-liner? | X-DUP | Same as SS-ST34 | — | pers.rhythm-follows-content |
| DS-Q09 | SKILL.md §Quick Checks (L75) | Em dash anywhere? Remove it | X-DUP | Same as SS-ST35 | — | none |
| DS-Q10 | SKILL.md §Quick Checks (L76) | Vague declarative? Name the implication | X-DUP | Same as SS-P09 | — | both.show-not-label |
| DS-Q11 | SKILL.md §Quick Checks (L77) | Sentence starting with What/When/Where/Which/Who/Why/How as a crutch? | X-DUP | Same as SS-ST29 | — | none |
| DS-Q12 | SKILL.md §Quick Checks (L78) | Meta-joiners ("The rest of this essay...")? | X-DUP | Same as SS-P06 | — | pers.no-signposts |
| DS-Q13 | SKILL.md §Quick Checks (L79) | "It's worth noting" or similar filler transitions? | X-DUP | Same as SS-P05 | — | both.show-not-label |
| DS-Q14 | SKILL.md §Quick Checks (L80) | Same metaphor used more than twice? | X-DUP | Same as DS-ST61 | — | none |
| DS-Q15 | SKILL.md §Quick Checks (L81) | "Despite these challenges..." formula? | X-DUP | Same as DE-P20 | — | both.facts-not-praise |
| DS-Q16 | SKILL.md §Quick Checks (L82) | Bold-first bullet pattern? | X-DUP | Same as DE-P24 | — | both.sparing-bold |
| DS-Q17 | SKILL.md §Quick Checks (L83) | Tricolon (three-item list)? Use two items or one | X-DUP | Same as SS-ST32 | — | both.list-what-is-there |
| DS-S1 | SKILL.md §Scoring (L85-97) | Five dimensions 1-10; revise below 35/50 | X-SCOPE | Self-scoring procedure | — | none |
| DS-R1 | SKILL.md §Reference Files (L99-106) | Catalog of reference files | X-SCOPE | Pointer list | The tropes.md entry is excluded. | none |
| DS-E0a | SKILL.md §Examples, scientific (L112-120) | Inline before/after of the cover-letter sentence | X-DUP | Same text as DS-EX02 | — | both.show-not-label |
| DS-E0b | SKILL.md §Examples, blog (L122-130) | "Here's the thing: most bioinformatics pipelines break in production. Not because the code is bad. Because the data is bad. Let that sink in." rewritten | X-DUP | Illustrates SS-P01, SS-ST01 and SS-P02 | The after keeps "most", unlike stop-slop Example 2 (SS-E2b): a model for both.scope-claims. | both.scope-claims |
| DS-ST01 | structures.md §Binary Contrasts (L9) | "Not because X. Because Y." / "Not because X, but because Y." | X-DUP | Same as SS-ST01 | — | both.real-contrasts |
| DS-ST02 | structures.md §Binary Contrasts (L10) | "[X] isn't the problem. [Y] is." | X-DUP | Same as SS-ST02 | — | both.real-contrasts |
| DS-ST03 | structures.md §Binary Contrasts (L11) | "The answer isn't X. It's Y." | X-DUP | Same as SS-ST03 | — | both.real-contrasts |
| DS-ST04 | structures.md §Binary Contrasts (L12) | "It feels like X. It's actually Y." | X-DUP | Same as SS-ST04 | — | both.real-contrasts |
| DS-ST05 | structures.md §Binary Contrasts (L13) | "The question isn't X. It's Y." | X-DUP | Same as SS-ST05 | — | both.real-contrasts |
| DS-ST06 | structures.md §Binary Contrasts (L14, fix L21) | "Not X. But Y." / "not X, it's Y" / "isn't X, it's Y" → state Y | X-DUP | Same as SS-ST06 | The section intro (L5) adds that one per piece can work; the candidate rule tests the condition, not the count. | both.real-contrasts |
| DS-ST07 | structures.md §Binary Contrasts (L15) | "It's not this. It's that." | X-DUP | Same as SS-ST07 | — | both.real-contrasts |
| DS-ST08 | structures.md §Binary Contrasts (L16) | "stops being X and starts being Y" | X-DUP | Same as SS-ST08 | — | none |
| DS-ST09 | structures.md §Binary Contrasts (L17) | "doesn't mean X, but actually Y" | X-DUP | Same as SS-ST09 | — | both.real-contrasts |
| DS-ST10 | structures.md §Binary Contrasts (L18) | "is about X but not Y" | X-DUP | Same as SS-ST10 | — | both.real-contrasts |
| DS-ST11 | structures.md §Binary Contrasts (L19) | "not just X but also Y" | X-DUP | Same as SS-ST11 | — | both.real-contrasts |
| DS-ST12 | structures.md §Negative Listing (L29, fix L34) | "Not a X... Not a Y... A Z." → state Z | X-DUP | Same as SS-ST12 | — | both.real-contrasts |
| DS-ST13 | structures.md §Negative Listing (L30) | "It wasn't X. It wasn't Y. It was Z." | X-DUP | Same as SS-ST13 | — | both.real-contrasts |
| DS-ST14 | structures.md §Negative Listing (L31) | "Not ten. Not fifty. Five hundred." | X-DUP | Same as DE-P06 | — | both.real-contrasts |
| DS-ST15 | structures.md §Negative Listing (L32) | "not recklessly, not completely, but enough" (hedging disguised as precision) | X-DEAI | An English cadence; the real limit is better stated as the limit | If a limit matters, state it ("read and write access only"); this is SS-ST37's family. | both.real-contrasts |
| DS-ST16 | structures.md §Dramatic Fragmentation (L42, fix L48) | "[Noun]. That's it. That's the [thing]." | X-DUP | Same as SS-ST14 | — | both.state-dont-stage |
| DS-ST17 | structures.md §Dramatic Fragmentation (L43) | "X. And Y. And Z." | X-DUP | Same as SS-ST15 | — | both.state-dont-stage |
| DS-ST18 | structures.md §Dramatic Fragmentation (L44) | "This unlocks something. [Word]." | X-DUP | Same as SS-ST16 | — | both.state-dont-stage |
| DS-ST19 | structures.md §Dramatic Fragmentation (L45) | "He published this. Openly. In a book." | X-DUP | Same as DE-P10 | — | both.state-dont-stage |
| DS-ST20 | structures.md §Dramatic Fragmentation (L46) | "Platforms do." (orphaned fragment as punchline) | X-DUP | Same as DE-P10 | — | both.state-dont-stage |
| DS-ST21 | structures.md §Self-Posed Rhetorical Questions (L56, fix L63) | "The result? Devastating." | X-DUP | Same as DE-P07 | — | both.state-dont-stage |
| DS-ST22 | structures.md §Self-Posed Rhetorical Questions (L57) | "The worst part? Nobody saw it coming." | X-DUP | Same as DE-P07 | — | both.state-dont-stage |
| DS-ST23 | structures.md §Self-Posed Rhetorical Questions (L58) | "What if [reframe]?" | X-DUP | Same as SS-ST17 | — | none |
| DS-ST24 | structures.md §Self-Posed Rhetorical Questions (L59) | "Here's what I mean:" | X-DUP | Same as SS-ST18 | — | both.no-empty-previews |
| DS-ST25 | structures.md §Self-Posed Rhetorical Questions (L60) | "Think about it:" | X-DUP | Same as SS-ST19 | — | both.show-not-label |
| DS-ST26 | structures.md §Self-Posed Rhetorical Questions (L61) | "And that's okay." | X-DUP | Same as SS-ST20 | — | both.write-for-the-reader |
| DS-ST27 | structures.md §Anaphora Abuse (L71, fix L75) | "They assume that... They assume that... They assume that..." | X-DUP | Same as DE-P09 | — | both.merge-repeated-referents |
| DS-ST28 | structures.md §Anaphora Abuse (L72) | "They could expose... They could offer... They could provide..." (list disguised as prose) | X-DUP | Same as DE-P09 | — | both.merge-repeated-referents, both.lists-vs-prose |
| DS-ST29 | structures.md §Anaphora Abuse (L73) | "They have built X, but not Y. They have built A, but not B." | X-DUP | Same as DE-P09 | — | both.merge-repeated-referents |
| DS-ST30 | structures.md §Tricolon Abuse (L83, fix L87) | "Products impress; platforms empower. Products solve; platforms create." | X-DUP | Same as DE-P08 | — | both.list-what-is-there |
| DS-ST31 | structures.md §Tricolon Abuse (L84) | "identity, payments, compute, distribution" (extended lists masquerading as analysis) | BOTH | A list of items the text never discusses stands in for analysis in any genre | If a list stands in for analysis, keep only the items the text discusses, or discuss each. | both.list-what-is-there |
| DS-ST32 | structures.md §Tricolon Abuse (L85) | "workflows, decisions, and interactions" (three-item groupings everywhere) | X-DUP | Same as SS-ST32 | — | both.list-what-is-there |
| DS-ST33 | structures.md §False Agency (L91-103) | Inanimate things given human verbs; name the human or use "you" | X-DUP | Same as SS-ST23 | Identical table. | both.name-the-actor, en.real-actor |
| DS-ST34 | structures.md §Narrator-from-a-Distance (L111, fix L116) | "Nobody designed this." | X-DUP | Same as SS-ST24 | — | pers.reader-in-scene |
| DS-ST35 | structures.md §Narrator-from-a-Distance (L112) | "This happens because..." | X-DUP | Same as SS-ST25 | — | none |
| DS-ST36 | structures.md §Narrator-from-a-Distance (L113) | "This is why..." | X-DUP | Same as SS-ST26 | — | none |
| DS-ST37 | structures.md §Narrator-from-a-Distance (L114) | "People tend to..." | X-DUP | Same as SS-ST27 | — | both.scope-claims, pers.reader-in-scene |
| DS-ST38 | structures.md §Passive Voice (L118-129) | "Every sentence needs a subject doing something"; "X was created", "It is believed that", "Mistakes were made", "The decision was reached" | X-DUP | Same as SS-ST28 | Identical table. | both.name-the-actor, zh.bei-passive |
| DS-ST39 | structures.md §Listicle in a Trench Coat (L131-140) | "The first wall is... The second wall is..." / "The second takeaway is..." | X-DUP | Same as DE-P17 | — | both.lists-vs-prose |
| DS-ST40 | structures.md §Superficial Participle Analyses (L142-153) | "contributing to the region's rich cultural heritage" / "highlighting its enduring legacy" / "underscoring its role as a dynamic hub" / "reflecting broader trends in..." | X-DUP | Same as DE-P15 | — | both.facts-not-praise, en.ing-rider |
| DS-ST41 | structures.md §False Ranges (L155-165) | "From innovation to implementation to cultural transformation." / Big Bang to cosmic web / problem-solving to artistic expression | X-DUP | Same as DE-P16 | — | both.list-what-is-there |
| DS-ST42 | structures.md §Historical Analogy Stacking (L167-177) | "Apple didn't build Uber. Facebook didn't build Spotify." / "Every major shift -- the web, mobile, social, cloud -- followed..." / "Take Spotify... Or consider Uber..." → one example examined in depth | BOTH | Name-dropping companies or eras as proof stands in for analysis in any genre | Use one example and say what it shows; a list of cases that each come with a stated fact is fine. | both.attribute-claims, both.be-specific |
| DS-ST43 | structures.md §"Despite Its Challenges..." (L179-188) | "Despite these challenges, the initiative continues to thrive." / "Despite its prosperity, [X] faces challenges typical of..." | X-DUP | Same as DE-P20 | — | both.facts-not-praise |
| DS-ST44 | structures.md §Sentence Starters (L194, L198) | Sentences starting with What/When/Where/Which/Who/Why/How | X-DUP | Same as SS-ST29 | — | none |
| DS-ST45 | structures.md §Sentence Starters (L195) | Paragraphs starting with "So" | X-DUP | Same as SS-ST30 | — | both.name-the-relation |
| DS-ST46 | structures.md §Sentence Starters (L196) | Sentences starting with "Look," | X-DUP | Same as SS-ST31 | — | both.no-empty-previews |
| DS-ST47 | structures.md §Formulaic Constructions (L204) | "By the time X, I was Y." | X-DUP | Same as SS-ST21 | — | none |
| DS-ST48 | structures.md §Formulaic Constructions (L205) | "X that isn't Y" → "X is broken" | X-DUP | Same as SS-ST22 | — | both.positive-form |
| DS-ST49 | structures.md §Rhythm Patterns (L211) | Three-item lists → two items or one | X-DUP | Same as SS-ST32 | — | both.list-what-is-there |
| DS-ST50 | structures.md §Rhythm Patterns (L212) | Questions answered immediately → let them breathe or cut them | X-DUP | Same as SS-ST33 | DE-P07 keeps the narrower staged-question form as BOTH. | both.state-dont-stage |
| DS-ST51 | structures.md §Rhythm Patterns (L213) | Every paragraph ends punchily → vary endings | X-DUP | Same as SS-ST34 | — | pers.rhythm-follows-content |
| DS-ST52 | structures.md §Rhythm Patterns (L214) | Em dashes → remove | X-DUP | Same as SS-ST35 | — | none |
| DS-ST53 | structures.md §Rhythm Patterns (L215) | Staccato fragmentation → don't stack short punchy sentences | X-DUP | Same as SS-ST36 | — | both.state-dont-stage |
| DS-ST54 | structures.md §Rhythm Patterns (L216) | "Not always. Not perfectly." | X-DUP | Same as SS-ST37 | — | both.keep-certainty |
| DS-ST55 | structures.md §Formatting Tells (L222) | Bold-first bullets | X-DUP | Same as DE-P24 | — | both.sparing-bold, both.lists-vs-prose |
| DS-ST56 | structures.md §Formatting Tells (L223) | Unicode arrows (→) → use -> or => or plain text | X-DEAI | The arrow glyph is a surface tell | The useful residue: in running prose, write the verb instead of an arrow; arrows in diagrams, code and UI paths are fine. | both.name-the-relation |
| DS-ST57 | structures.md §Formatting Tells (L224) | Smart/curly quotes → straight quotes | X-DEAI | Curly quotes are correct typography (rubric example), and required in Chinese | Conflicts with zh.full-width-punct. | none |
| DS-ST58 | structures.md §Formatting Tells (L225) | Signposted conclusions ("In conclusion...") | X-DUP | Same as DZ-3.5 | — | pers.no-signposts |
| DS-ST59 | structures.md §Formatting Tells (L226) | Fractal summaries: don't summarize what you'll say, say it, then summarize it | BOTH | A preview and a recap of a section the reader sees whole repeat every point | Put a summary only at the start or end of a long document; a short piece or section gets neither preview nor recap. | both.say-it-once |
| DS-ST60 | structures.md §One-Point Dilution (L228-232) | Restating one argument in ten ways → state it once, support it, move on | X-DUP | Same as DE-G03 | — | both.say-it-once |
| DS-ST61 | structures.md §The Dead Metaphor (L234-238) | One metaphor in every paragraph → use it once or twice | BOTH | A recurring figure that adds no meaning tires readers in any language | Write later uses of a recurring figure in literal words; a defined term is not a figure and repeats. | none |
| DS-ST62 | structures.md §Invented Concept Labels (L240-250) | "the supervision paradox", "the acceleration trap", "workload creep" → define it or describe it plainly | BOTH | An undefined coined label poses as an established term in any language (ZH 「××陷阱」, JA 「〜の罠」) | Define a coined label at first use, or describe the thing in plain words. | both.define-and-keep-terms |
| DS-ST63 | structures.md §Word Patterns (L256) | Lazy extremes (every, always, never, everyone, nobody) | X-DUP | Same as SS-ST38 | — | both.scope-claims |
| DS-ST64 | structures.md §Word Patterns (L257) | All adverbs | X-DUP | Same as SS-ST39 | — | en.empty-emphasis |
| DS-P01 | phrases.md §Throat-Clearing Openers (L3-27) | Remove announcement phrases; any "here's what/this/that" is throat-clearing | X-DUP | Same as SS-P01 | Adds 'Here's the kicker', 'Here's where it gets interesting', 'Here's what most people miss', 'Here's the deal'. | both.no-empty-previews, both.state-dont-stage |
| DS-P02 | phrases.md §Emphasis Crutches (L29-37) | Full stop. / Period. / Let that sink in. / This matters because / Make no mistake / Here's why that matters | X-DUP | Same as SS-P02 | — | both.show-not-label |
| DS-P03 | phrases.md §Pedagogical Hand-Holding (L39-48) | Let's break this down / Let's unpack this / Let's explore / Let's dive in / Let's delve into / Think of it as... / Think of it like... / Imagine a world where... | X-DUP | Same as DE-P14 | Adds 'Let's explore', 'Let's delve into' and 'Think of it like'. | both.no-empty-previews, both.write-for-the-reader |
| DS-P04 | phrases.md §Business Jargon (L52-77) | Replace jargon with plain language (navigate, unpack, lean into, landscape, game-changer, … leverage, utilize, robust, streamline, harness, paradigm, synergy, ecosystem, framework) | X-DUP | Same as SS-P03 | Adds leverage, utilize, robust, streamline, harness, paradigm, synergy, ecosystem and framework. "Framework → Structure, approach" and "Ecosystem → System" are wrong for literal terms (a web framework, Nextflow, the npm ecosystem); DS-C5d says so. | both.plain-words, tech.established-terms |
| DS-P05 | phrases.md §AI Vocabulary Tells (L79-87) | delve, tapestry, certainly, landscape (as "field"), nuanced | EN | English words overrepresented in model output; the principle is both.plain-words | 'certainly' is empty emphasis (en.empty-emphasis); for 'nuanced', name the nuance. Keep literal 'landscape' (geography, page orientation). | both.plain-words, en.empty-emphasis |
| DS-P06 | phrases.md §The "Serves As" Dodge (L89-98) | serves as / stands as / marks / represents → is | X-DUP | Same as DE-P12 | — | en.copula-verbs |
| DS-P07 | phrases.md §Adverbs (L100-123) | "Kill all adverbs. No -ly words." List adds quietly, remarkably, arguably | X-DUP | Same as SS-P04 | 'arguably' is a hedge to keep when the author is unsure (both.keep-certainty, pers.state-the-view). | en.empty-emphasis, both.cut-needless-words |
| DS-P08 | phrases.md §Adverbs, filler phrases (L125-135) | At its core / In today's [X] / It's worth noting / It bears mentioning / Notably / … | X-DUP | Same as SS-P05 | Adds 'It bears mentioning' and 'Notably'. | both.show-not-label, both.cut-needless-words |
| DS-P09 | phrases.md §Meta-Commentary (L137-154) | Remove self-referential asides; adds "In conclusion" / "To sum up" / "In summary", "As we've seen in this section...", "And so we return to where we began." | X-DUP | Same as SS-P06 | The added summary labels are DZ-3.5 (PERSONAL). | pers.no-signposts, both.say-it-once |
| DS-P10 | phrases.md §Performative Emphasis (L156-162) | "creeps in" / "I promise" / "They exist, I promise" | X-DUP | Same as SS-P07 | — | pers.specific-admission |
| DS-P11 | phrases.md §False Vulnerability (L164-170) | "And yes, I'm openly..." / "And yes, since we're being honest..." / "This is not a rant; it's a diagnosis" | X-DUP | Same as DE-P21 | Example 13's after shows the right move only in part: it replaces the admission with an invented detail. | pers.specific-admission |
| DS-P12 | phrases.md §Telling Instead of Showing (L172-179) | "This is genuinely hard" / "This is what X actually looks like" / "actually matters" | X-DUP | Same as SS-P08 | — | both.show-not-label |
| DS-P13 | phrases.md §"The Truth Is Simple" (L181-188) | Asserting clarity instead of demonstrating it: "The reality is simpler", "History is unambiguous on this point", "History is clear, the metrics are clear, the examples are clear", "none of them is the real story. The real story is..." | BOTH | Declaring a point clear, simple or real replaces the evidence in any language (ZH 「事实很清楚」, JA 「答えは明らかだ」) | If a sentence says the answer is clear, simple or the real story, give the evidence instead or cut the sentence. | both.show-not-label, both.attribute-claims |
| DS-P14 | phrases.md §Vague Declaratives (L190-198) | "The reasons are structural" / "The implications are significant" / "This is the deepest problem" / "The stakes are high" / "The consequences are real" | X-DUP | Same as SS-P09 | — | both.show-not-label |
| DS-P15 | phrases.md §Vague Attributions (L200-207) | "Experts argue that..." / "Industry reports suggest that..." / "Observers have cited..." / "Several publications have noted..." | X-DUP | Same as DZ-3.7g | — | both.attribute-claims |
| DS-P16 | phrases.md §Grandiose Stakes Inflation (L209-215) | "This will fundamentally reshape how we think about everything." / "will define the next era of computing" / "something entirely new" → scale claims to the stakes | X-DUP | Same as DZ-3.7c | — | both.facts-not-praise |
| DS-EX01 | examples.md Example 1 (L3-11) | Throat-clearing and binary contrast in a forecasting sentence | X-DUP | A re-skin of SS-E1; illustrates SS-P01, SS-ST01, SS-P02 | Unlike SS-E1, the after names the specific data problem (a model for both.be-specific). | both.be-specific |
| DS-EX02 | examples.md Example 2 (L15-23) | Filler and "despite these challenges" in a cover letter | X-DUP | Illustrates SS-P05, SS-P09, DE-P20, DE-P15 | The after keeps "If … may not" (both.keep-certainty). | both.show-not-label, both.keep-certainty |
| DS-EX03 | examples.md Example 3 (L27-35) | Grandiose stakes and "landscape" in a scientific opener | X-DUP | Illustrates SS-P05, SS-P03, DS-P16 | — | both.facts-not-praise |
| DS-EX04 | examples.md Example 4 (L39-47) | Passive voice and false agency in a Discussion section | X-DUP | Illustrates SS-ST28 and SS-ST23 | The after keeps "roughly 15%" with the number. | both.name-the-actor, both.keep-certainty |
| DS-EX05 | examples.md Example 5 (L51-59) | Self-posed rhetorical questions in a blog post | X-DUP | Illustrates DE-P07 and SS-P02 | The before's "Nobody checks the intermediate outputs" is a lazy extreme (SS-ST38); the after drops it. | both.state-dont-stage, both.scope-claims |
| DS-EX06 | examples.md Example 6 (L63-71) | "Serves as" and participle analyses in an abstract | X-DUP | Illustrates DE-P12 and DE-P15 | The after adds facts (dozens of groups, since 2013, what FluSight standardized) that the before lacks. | both.claims-match-evidence |
| DS-EX07 | examples.md Example 7 (L75-83) | Narrator distance and vague declaratives in a blog post | X-DUP | Illustrates SS-ST24, SS-P09, SS-P08 | The after adds a repository list the before lacks. | pers.reader-in-scene, both.show-not-label |
| DS-EX08 | examples.md Example 8 (L87-95) | Listicle in a trench coat in a Discussion section | X-DUP | Illustrates DE-P17 | The after keeps all three limitations (a model for both.revise-without-loss). | both.lists-vs-prose, both.revise-without-loss |
| DS-EX09 | examples.md Example 9 (L99-107) | One-point dilution in a blog post | X-DUP | Illustrates DE-G03 | The after cites a study and figures that the before lacks; as an editing model it breaks both.claims-match-evidence. | both.say-it-once, both.claims-match-evidence |
| DS-EX10 | examples.md Example 10 (L111-119) | Historical analogy stacking | X-DUP | Illustrates DS-ST42 | The after's AWS/Airbnb claim is new content. | both.attribute-claims |
| DS-EX11 | examples.md Example 11 (L123-131) | Anaphora in a grant narrative | X-DUP | Illustrates DE-P09 | The after supplies methods and datasets that the before lacks. | both.merge-repeated-referents, both.be-specific |
| DS-EX12 | examples.md Example 12 (L135-143) | "Speed. Quality. Cost. You can only pick two. That's it. That's the tradeoff." | X-DUP | Verbatim SS-E4 | This copy's after drops the em dash that SS-E4's after used. | both.state-dont-stage |
| DS-EX13 | examples.md Example 13 (L147-155) | False vulnerability and meta-commentary in a blog post | X-DUP | Illustrates DE-P21 and SS-P06 | The after replaces the author's admission with an invented detail ("trying one more covariate") and a claim about the reader ("You probably have too"). | pers.specific-admission, pers.no-invented-reactions, both.claims-match-evidence |
| DS-EX14 | examples.md Example 14 (L159-167) | "It's worth noting" and an invented concept label | X-DUP | Illustrates SS-P05, DS-ST62, DE-P15 | — | both.define-and-keep-terms, both.keep-certainty |
| DS-EX15 | examples.md Example 15 (L171-179) | "Imagine a world" and a patronizing analogy | X-DUP | Illustrates DE-P14 and DE-P23 | The after adds a statistic with a citation ("Atlassian, 2019") that the before lacks. | both.claims-match-evidence |

## Conflicts found

1. **Negative contrasts.** DZ-3.3 bans every 「不是 X，而是 Y」 as a hard constraint, but its own example 3 (L91) reports a real change whose halves both inform, and its ✅ drops that I/O was the bottleneck. Example 2 (L88) denies a reading that the book's marketing invites. Resolution: X-DUP of SS-ST06 with its condition (both.real-contrasts); tested by deslop-zh-tech-cache-article/both-halves-kept and deslop-zh-pers-book-note/contrast-kept.
2. **Quote marks.** DZ-3.9a and DZ-4.1f require 「」 and forbid curly quotes; GB/T 15834 and zh.full-width-punct use “” unless the format requires 「」. DS-ST57 requires straight quotes in English. Resolution: both X-DEAI; quote form is a language-skill matter.
3. **Dashes.** DZ-3.9b and DZ-4.6i ban the Chinese dash, DE-P25 counts em dashes, and DS-C7d and DS-ST52 ban them. 「——」 is standard Chinese punctuation. Resolution: X-DEAI; zh.dash-form governs the form, and the global check grades overuse.
4. **Addressing the reader.** DZ-3.11a and DZ-4.1b forbid 你 and 您 in technical docs and suggest role words. DE-G01 and DS-C6a recommend "you" in blogs. Resolution: DZ-3.11a becomes ZH/TECH with the conditional "prefer no address; if addressing, one form, never a role word for the reader".
5. **结果表明 and 据观察.** DZ-4.5h bans both, but Chinese scientific text treats 「结果表明」「数据表明」 as standard. Resolution: only the evasive 据观察 goes (both.name-the-actor); tested by deslop-zh-tech-paper-abstract/finding-kept.
6. **Summary labels.** DZ-3.5 and DZ-3.8c drop 综上所述 everywhere; zh.stock-closing keeps a summary with content, and technical and academic text uses labeled summaries. Resolution: PERSONAL.
7. **Register.** DZ-3.8d and DZ-3.8e push spoken words (比如, 用, 买) while DZ-4.1a asks technical docs to be 克制. Resolution: X-DEAI for the word swaps.
8. **Adverbs and hedges.** DE-P02a, DS-P07 and DE-X3 say to kill all adverbs including 'arguably'; both.keep-certainty and pers.state-the-view keep a hedge the author chose. Resolution: X-DUP of SS-P04's conditional; tested by deslop-pers-reproducibility-essay/hedge-kept.
9. **Human subjects.** DE-P03 requires a human subject in every sentence; technical text describes system behavior, steps are imperative, and Japanese and Chinese omit subjects. Resolution: SS-ST28's conditional.
10. **Lists.** DE-P24 rewrites bold-first lists as prose; both.lists-vs-prose keeps parallel items in a list. Resolution: BOTH with the condition "drop labels that only repeat; keep the list"; tested by deslop-en-tech-readme/list-kept.
11. **Literal terms in word bans.** DS-P04 maps Framework → Structure and Ecosystem → System, and DE-H1 bans catalyst, pillar, crucible, compelling and holistic "never"; DS-C5d says domain terms are fine; DZ-3.7a bans 协同, 链路 and 闭环 absolutely. Resolution: conditional on figurative use; tested by deslop-sci-grant-aims/framework-kept, deslop-zh-tech-api-quickstart/terms-kept and deslop-zh-tech-cache-article/term-kept.
12. **Three items.** DS-C7b, DS-Q17 and DS-ST49 say "two items or one"; DE-P08 says "A single tricolon is fine." Resolution: X-DEAI (frequency tell); padded series is the residue.
13. **Subtraction vs. examples that add.** DZ-1.2a, DE-C2 and DE-C3 say to subtract and preserve meaning, but the "after" versions of DZ-7.1, DZ-7.2, DZ-7.4, DE-E1, DE-E2, DS-EX06, DS-EX07, DS-EX09, DS-EX11, DS-EX13 and DS-EX15 add facts, statistics or citations that their "before" lacks. Resolution: the examples are X-DUP, and their afters are tested as over-applications (no-added-claims, no-invented-facts, no-additions, no-invented-details checks in the deslop test cases).
14. **Staged questions and fragments.** SS-ST33 and SS-ST14 were tagged X-DEAI; the candidate set has both.state-dont-stage. Resolution: DE-P07 and DE-P10 are BOTH, narrowed to a question answered in its next words and a fragment run that restates a point.
15. **Ordinal connectives.** DZ-3.14b replaces 首先…其次…最后 with 一方面…另一方面, which fits only two sides; Chinese formal writing uses ordinals. Resolution: X-DEAI; the list-or-prose test is both.lists-vs-prose.
16. **Exclamation marks.** DZ-4.1e bans them in technical docs; DZ-3.9c itself allows them in social posts with real emotion. Resolution: TECH.

## Rules whose absolute wording should become conditional

- DZ-1.2a "去 AI 味是做减法": delete a phrase only if the sentence keeps its meaning without it, and add no content when editing someone's text.
- DZ-3.3 "禁止否定式对比": if no plausible reader believes X, state Y; keep a contrast that corrects a held belief or reports a change whose halves both inform.
- DZ-3.6 "开篇套话 → 删": delete the opener only if it names no concrete change or cause.
- DZ-3.7a "绝对禁用": replace a jargon word only when it names no exact action or object; keep field terms (闭环控制, 协同过滤, 链路追踪, 内存对齐).
- DZ-3.8a "非常 / 极其 → 很": delete the intensifier when the judgment stays the same.
- DZ-3.9c "不用感叹号": in technical text.
- DZ-3.11a "技术文档禁用「你」「您」": prefer no address; if a step addresses the reader, use one form throughout and do not replace the reader with a role word.
- DZ-4.2d "少用其实": keep 其实 when it marks the author's doubt or correction.
- DZ-4.4c "5-8 条": list every user-facing change.
- DZ-4.5h "不用结果表明": keep 结果表明; rewrite only evasions that hide a known observer.
- DE-P02a and DS-P07 "Kill all -ly words": delete an intensifier or sincerity adverb if the claim reads the same without it; keep adverbs of manner, scope, time and frequency, and hedges that encode real uncertainty ('arguably', 'roughly').
- DE-P03 "Every sentence needs a human subject": if the actor is known and the reader needs it, make the actor the subject.
- DE-P10 "Use complete sentences": only for fragment runs that restate a point; headings, labels and list items stay fragments.
- DE-P24 "Write as prose": drop bold labels that only repeat their item; keep parallel items in a list.
- DE-V24 "consequently / thus / hence → so": keep the causal relation; any marker that states it is fine.
- DE-H1 "Hard ban (never use)": replace the word when it is figurative or decorative; keep literal senses (catalyst, pillar, crucible, compelling, holistic).
- DS-C7b and DS-ST49 "Two items beat three": a list holds as many items as there are facts; cut only items that add nothing.
- DS-P04 "Framework → Structure", "Ecosystem → System": only for figurative uses.
- DS-ST56 "Unicode arrows": in running prose, write the verb; arrows in diagrams, code and UI paths stay.

## Language-specific examples to move

### EN

- Copula substitutes (DE-P12, DE-V01, DE-V02, DS-P06): serves as, stands as, marks, represents, constitutes, boasts, features (as 'has'); keep 'acts as', 'functions as', literal 'represents' and the noun 'features'.
- Plain-word pairs (DE-V03 to DE-V26, DE-H4): leverage/utilize → use, harness → use, streamline → simplify, delve → examine, robust → the property, paradigm → model, synergy → cooperation, ecosystem → system, tapestry → mix, showcase → show, underscore/highlight → show, foster → encourage, garner → get, bolster → support, facilitate → help, spearhead → lead, galvanize → prompt, furthermore/moreover → also, nonetheless → still; consequently/thus/hence → so with the relation kept.
- Decorative words (DE-H1, DE-H2, DS-P05): nuanced, realm, nexus, interplay, cornerstone, beacon, pillar, catalyst, crucible, confluence, odyssey, multifaceted, holistic, compelling; 'quietly orchestrating', 'navigate the landscape', 'diverse array' (figurative uses only).
- Empty emphasis additions (DE-P02a, DS-P07): quietly, remarkably, certainly; 'arguably' is a hedge, not emphasis.
- Lead-ins and setups (DE-P01, DS-P01, DS-P03): 'Here's the kicker', 'Here's where it gets interesting', 'Here's what most people miss', 'Here's the deal', 'Let's explore', 'Let's delve into', 'Think of it like', 'Without further ado'.
- Clarity claims and attributions (DS-P13, DS-P15): 'The reality is simpler', 'History is unambiguous on this point', 'the real story is'; 'Industry reports suggest', 'Observers have cited', 'Several publications have noted'.

### JA

- The sources contain no Japanese. Auditor-supplied equivalents used to test universality: 「本当に重要なのは」 for 「真正关键的问题是」 (DZ-3.4), 「答えは明らかだ」 for "History is unambiguous" (DS-P13), 「〜の罠」 for invented labels (DS-ST62), 「では見ていきましょう」 for "Let's dive in" (DE-P14). Existing JA candidates (ja.empty-phrase-forms, ja.calque-verbs) already hold the first and the picture-verb family of DZ-3.12a.

### ZH

- Paragraph-closing recaps (DZ-3.1): 这说明、到这里、可以看出、这本身就是、通过以上分析、由此可见.
- Lecture lead-ins (DZ-3.4, DZ-2.07): 真拆开看、这背后是同一个变化、你要先明白、上面这些讲的是…下面我们看….
- Background openers (DZ-3.6, DZ-4.5f): 随着…的不断发展、在当今数字化浪潮中、在当今日新月异的领域中、近年来…受到了越来越多的关注; keep 「随着文件数量增加，检索时间也在增长」.
- Jargon (DZ-3.7a, §五): 赋能、抓手、闭环、沉淀、对齐、对标、拉通、打通、联动、洞察、赛道、心智、调性、战役、势能、兜底; keep 闭环控制、协同过滤、链路追踪、内存对齐.
- Plain-word pairs (DZ-5.07, DZ-5.08, DZ-5.20, DZ-5.21): 拥有 → 有、呈现 → 是、坐落于 → 在、致力于 → 专注; 进行 + verb (DZ-5.09, zh.jinxing-verb).
- Intensifiers and fillers (DZ-3.8a, DZ-3.8b, DZ-4.2d, DZ-3.11b): 非常、极其、值得注意的是、说白了、谁能想到、你会发现、你可以看到; keep 其实 that marks doubt.
- Picture verbs (DZ-3.12a): 接住、锋利、打穿、扛住、不崩、不爆; keep 缓存击穿.
- Pre-judging labels (DZ-3.13): 更干净：、逻辑很清晰：.
- Address and register (DZ-3.8f, DZ-4.2i): 很多同学、不懂技术的同学、你必须.
- Measure words (DZ-3.8g): 这几个事 → 这几件事.
- Punctuation and spacing (DZ-3.9d, DZ-3.9e, DZ-3.10a, DZ-3.10b, DZ-4.6b): full-width punctuation, no 打电报 chains of 它-sentences, CJK–Latin and CJK–digit spacing as house style.
- Bilingual terms (DZ-4.6f, DZ-4.6g): context → 上下文、state → 状态、cache → 缓存、claim → 断言、runtime → 运行时; prompt、embedding、tokenizer may stay in English.
