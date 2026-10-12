# Coverage of upstream rules

Every rule of every upstream source has one row here with its final outcome. The audit files in `audits/` give the reason for each destination. A rule that reached a candidate skill rule was kept only if the ablation tests in `evals/` showed an effect.

Rows: 1214. Kept through a skill rule: 55. Reached a candidate rule that showed no effect: 245. Excluded at audit or synthesis: 403. Test material only: 511.

## ASD-STE100 writing rules

Audit: [`audits/ste.md`](audits/ste.md).

| Row | Audit destination | Outcome |
|---|---|---|
| STE-0 | EN/TECH | excluded at synthesis: EN/TECH |
| STE-S1 | EN/TECH | excluded at synthesis: scope list |
| STE-S2 | EN/TECH | excluded at synthesis: scope list (skill description) |
| STE-S3 | EN/TECH | excluded at synthesis: scope list (skill description) |
| STE-S4 | EN/TECH | excluded at synthesis: scope list (skill description) |
| STE-N1 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| STE-N2 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| STE-N3 | BOTH | candidate rule `both.keep-literals` showed no measured effect |
| STE-N4 | BOTH | candidate rule `both.match-house-and-voice` showed no measured effect |
| STE-N5 | BOTH | candidate rule `both.match-house-and-voice` showed no measured effect |
| STE-1 | TECH | kept as `tech.one-action-per-step` in `writing-tech` |
| STE-2 | EN/TECH | candidate rule `en.sentence-length`, `tech.short-sentences` showed no measured effect |
| STE-3 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| STE-4 | EN/TECH | candidate rule `en.tense-by-event`, `tech.operation-state`, `zh.state-markers` showed no measured effect |
| STE-5 | EN/TECH | candidate rule `en.ing-clauses` showed no measured effect |
| STE-6 | TECH | kept as `en.plain-words` in `writing-en` |
| STE-7 | BOTH | candidate rule `both.define-and-keep-terms` showed no measured effect |
| STE-8 | EN/TECH | kept as `tech.established-terms` in `writing-tech` |
| STE-9 | EN/TECH | candidate rule `en.noun-clusters` showed no measured effect |
| STE-10 | EN | candidate rule `en.complete-sentences`, `tech.format-conventions` showed no measured effect |
| STE-11 | BOTH | candidate rule `both.one-topic-per-paragraph`, `en.paragraph-length` showed no measured effect |
| STE-12 | TECH | candidate rule `tech.vertical-lists` showed no measured effect |
| STE-13 | TECH | kept as `tech.warning-placement` in `writing-tech` |
| STE-14 | TECH | kept as `tech.established-terms` in `writing-tech` |

## obra/the-elements-of-style

Audit: [`audits/eos.md`](audits/eos.md).

| Row | Audit destination | Outcome |
|---|---|---|
| EOS-I01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-R01 | EN | candidate rule `en.usage-reference` showed no measured effect |
| EOS-R02 | EN | excluded at synthesis: see the audit row |
| EOS-R03 | EN | excluded at synthesis: see the audit row |
| EOS-R04 | EN | excluded at synthesis: see the audit row |
| EOS-R04b | BOTH | candidate rule `both.name-the-relation`, `ja.weak-ga` showed no measured effect |
| EOS-R04c | EN | candidate rule `en.unambiguous-conjunctions` showed no measured effect |
| EOS-R05 | EN | excluded at synthesis: see the audit row |
| EOS-R06 | EN | candidate rule `en.complete-sentences` showed no measured effect |
| EOS-R07 | EN | candidate rule `en.ing-clauses` showed no measured effect |
| EOS-R08 | BOTH | candidate rule `both.one-topic-per-paragraph` showed no measured effect |
| EOS-R08b | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| EOS-R08c | BOTH | excluded at synthesis: too narrow (dialogue layout in fiction and transcripts) |
| EOS-R09 | TECH | kept as `tech.point-first` in `writing-tech` |
| EOS-R10 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| EOS-R10b | EN | excluded at synthesis: see the audit row |
| EOS-R10c | BOTH | candidate rule `both.plain-words`, `ja.plain-predicates` showed no measured effect |
| EOS-R10d | EN | candidate rule `en.real-actor`, `ja.inanimate-subject` showed no measured effect |
| EOS-R11 | BOTH | kept as `both.positive-form` in `writing-personal`, `writing-tech` |
| EOS-R11b | BOTH | kept as `both.positive-form` in `writing-personal`, `writing-tech` |
| EOS-R12 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| EOS-R13 | BOTH | candidate rule `both.cut-needless-words` showed no measured effect |
| EOS-R13b | EN | kept as `en.plain-words` in `writing-en` |
| EOS-R13c | EN | excluded at synthesis: see the audit row |
| EOS-R13d | BOTH | candidate rule `both.merge-repeated-referents` showed no measured effect |
| EOS-R14 | BOTH | candidate rule `both.name-the-relation`, `ja.weak-ga` showed no measured effect |
| EOS-R15 | BOTH | candidate rule `both.parallel-form` showed no measured effect |
| EOS-R15b | EN | excluded at synthesis: see the audit row |
| EOS-R15c | BOTH | candidate rule `both.lists-vs-prose` showed no measured effect |
| EOS-R16 | BOTH | kept as `both.one-reading` in `writing-tech` |
| EOS-R16b | EN | excluded at synthesis: see the audit row |
| EOS-R17 | EN | candidate rule `zh.state-markers` showed no measured effect |
| EOS-R17b | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| EOS-R17c | BOTH | excluded at synthesis: too narrow (structure of reviews and comparisons) |
| EOS-R18 | EN | excluded at synthesis: see the audit row |
| EOS-R18b | PERSONAL | kept as `pers.end-on-the-point` in `writing-personal` |
| EOS-V00 | BOTH | candidate rule `both.plain-words` showed no measured effect |
| EOS-V01 | EN | excluded at synthesis: see the audit row |
| EOS-V02 | EN | excluded at synthesis: see the audit row |
| EOS-V03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-V04 | EN | excluded at synthesis: dated (M-W lists both "bid" and "bade") |
| EOS-V05 | EN | excluded at synthesis: dated ("cannot help but" is standard, M-W) |
| EOS-V05b | BOTH | candidate rule `ja.weak-ga` showed no measured effect |
| EOS-V06 | EN/TECH | kept as `en.spec-modals` in `writing-en`; kept as `tech.requirement-keywords` in `writing-tech` |
| EOS-V07 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V08 | EN | candidate rule `en.empty-emphasis` showed no measured effect |
| EOS-V09 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V10 | EN | excluded at synthesis: dated (M-W accepts "claim" = assert) |
| EOS-V11 | EN | excluded at synthesis: dated, not checked, no testable behavior |
| EOS-V12 | EN | excluded at synthesis: see the audit row |
| EOS-V13 | EN | excluded at synthesis: see the audit row |
| EOS-V14 | EN | excluded at synthesis: dated ("data is" is standard in computing, M-W) |
| EOS-V15 | EN | excluded at synthesis: dated (M-W lists "dependable" with no label) |
| EOS-V16 | EN | excluded at synthesis: dated (M-W treats "different than" as standard) |
| EOS-V17 | EN | excluded at synthesis: see the audit row |
| EOS-V18 | EN | excluded at synthesis: see the audit row |
| EOS-V19 | EN | excluded at synthesis: dated (prepositional "due to" is standard, M-W) |
| EOS-V20 | EN | excluded at synthesis: dated ("folks" is standard) |
| EOS-V21 | EN | excluded at synthesis: see the audit row |
| EOS-V22 | EN | excluded at synthesis: see the audit row |
| EOS-V22b | BOTH | candidate rule `both.list-what-is-there` showed no measured effect |
| EOS-V23 | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| EOS-V24 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V25 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V26 | EN | excluded at synthesis: dated ("fix a bug" is standard) |
| EOS-V27 | EN | excluded at synthesis: regional and dated ("gotten" in US English) |
| EOS-V28 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-V29 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-V30 | EN | excluded at synthesis: dated (sentence-initial "However," is accepted, Chicago) |
| EOS-V31 | BOTH | candidate rule `both.show-not-label` showed no measured effect |
| EOS-V32 | EN | excluded at synthesis: see the audit row |
| EOS-V33 | EN | excluded at synthesis: see the audit row |
| EOS-V34 | EN | excluded at synthesis: see the audit row |
| EOS-V35 | EN | excluded at synthesis: EN example of the genre rule from EOS-V00 (ready-made phrases) |
| EOS-V36 | EN | candidate rule `en.empty-emphasis` showed no measured effect |
| EOS-V37 | EN | candidate rule `en.tool-phrasal-verbs` showed no measured effect |
| EOS-V38 | EN | excluded at synthesis: see the audit row |
| EOS-V39 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V40 | EN | excluded at synthesis: dated ("nearby" is standard) |
| EOS-V41 | EN | excluded at synthesis: not checked |
| EOS-V42 | EN | excluded at synthesis: regional |
| EOS-V43 | EN | excluded at synthesis: see the audit row |
| EOS-V44 | EN | candidate rule `en.ing-clauses` showed no measured effect |
| EOS-V45 | EN | excluded at synthesis: not checked |
| EOS-V46 | EN | excluded at synthesis: see the audit row |
| EOS-V47 | EN | candidate rule `en.copula-verbs` showed no measured effect |
| EOS-V48 | EN | excluded at synthesis: dated ("proven" is standard, M-W) |
| EOS-V49 | EN | excluded at synthesis: too narrow |
| EOS-V50 | EN | kept as `en.spec-modals` in `writing-en` |
| EOS-V51 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-V52 | EN | candidate rule `en.empty-emphasis` showed no measured effect |
| EOS-V53 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-V54 | EN | excluded at synthesis: dated (Chicago and M-W accept a split infinitive) |
| EOS-V55 | EN | excluded at synthesis: not checked |
| EOS-V56 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V57 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V58 | EN | excluded at synthesis: letter etiquette, not checked |
| EOS-V59 | EN | excluded at synthesis: see the audit row |
| EOS-V60 | BOTH | candidate rule `both.cut-needless-words`, `en.empty-emphasis` showed no measured effect |
| EOS-V61 | EN | excluded at synthesis: dated ("viewpoint" is standard) |
| EOS-V62 | EN | candidate rule `en.unambiguous-conjunctions` showed no measured effect |
| EOS-V63 | EN | excluded at synthesis: see the audit row |
| EOS-V64 | EN | excluded at synthesis: dated form ("worthwhile" before a noun is standard) |
| EOS-V65 | EN | excluded at synthesis: see the audit row |
| EOS-SK01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-SK02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-SK03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-SK04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-SK05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-SK06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-SK07 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-SK08 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-SK09 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |

## k16shikano/japanese-tech-writing

Audit: [`audits/jtw.md`](audits/jtw.md).

| Row | Audit destination | Outcome |
|---|---|---|
| JTW-0.0 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| JTW-1.0 | BOTH | candidate rule `both.one-topic-per-paragraph` showed no measured effect |
| JTW-1.1 | BOTH | candidate rule `both.one-topic-per-paragraph` showed no measured effect |
| JTW-1.2 | TECH | kept as `tech.point-first` in `writing-tech` |
| JTW-1.3 | BOTH | candidate rule `both.name-the-relation` showed no measured effect |
| JTW-1.4 | BOTH | candidate rule `both.say-it-once` showed no measured effect |
| JTW-1.5 | BOTH | excluded at synthesis: too narrow (where caveats about an example go in a narrated scene) |
| JTW-1.6 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| JTW-1.7 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| JTW-1.8a | BOTH | candidate rule `both.parallel-form` showed no measured effect |
| JTW-1.8b | BOTH | excluded at synthesis: too narrow (one callback construction) |
| JTW-1.8c | JA | kept as `ja.kagi-quotes` in `writing-ja` |
| JTW-1.8d | BOTH | candidate rule `both.name-the-relation` showed no measured effect |
| JTW-1.8e | JA | candidate rule `ja.subject-inheritance` showed no measured effect |
| JTW-1.9 | BOTH | excluded at synthesis: too narrow (voice of a concession in a book argument) |
| JTW-1.10 | BOTH | excluded at synthesis: see the audit row |
| JTW-1.11 | BOTH | kept as `ja.kagi-quotes` in `writing-ja` |
| JTW-1.12 | BOTH | excluded at synthesis: not testable at case length (placement of forward references in long text) |
| JTW-2.0 | BOTH | candidate rule `both.claims-match-evidence` showed no measured effect |
| JTW-2.1 | BOTH | candidate rule `both.keep-certainty`, `ja.one-hedge` showed no measured effect |
| JTW-2.2 | BOTH | candidate rule `both.name-every-cause` showed no measured effect |
| JTW-2.3 | BOTH | candidate rule `both.name-every-cause` showed no measured effect |
| JTW-2.4 | BOTH | candidate rule `both.define-and-keep-terms` showed no measured effect |
| JTW-2.5 | BOTH | candidate rule `both.state-the-mechanism` showed no measured effect |
| JTW-2.6 | TECH | candidate rule `tech.tool-limits` showed no measured effect |
| JTW-2.7 | BOTH | candidate rule `both.scope-claims` showed no measured effect |
| JTW-2.8 | BOTH | excluded at synthesis: not testable at case length (a deferred point resolved in a later section) |
| JTW-2.9 | BOTH | excluded at synthesis: too narrow (what follows a concession in long-form argument) |
| JTW-2.10 | BOTH | candidate rule `both.define-and-keep-terms` showed no measured effect |
| JTW-2.11 | BOTH | candidate rule `both.define-and-keep-terms` showed no measured effect |
| JTW-3.0 | BOTH | excluded at synthesis: framing statement with no behavior of its own |
| JTW-3.1a | BOTH | excluded at synthesis: not observable in a short text (reader load raised one level at a time) |
| JTW-3.1b | BOTH | excluded at synthesis: revision bookkeeping after cuts in a long document |
| JTW-3.1c | BOTH | candidate rule `both.write-for-the-reader` showed no measured effect |
| JTW-3.2 | TECH | kept as `tech.identifiers-when-used` in `writing-tech` |
| JTW-3.3 | BOTH | kept as `both.one-reading` in `writing-tech` |
| JTW-3.4 | BOTH | candidate rule `both.define-and-keep-terms`, `ja.type-before-modifiers` showed no measured effect |
| JTW-3.5 | BOTH | excluded at synthesis: too narrow (sequencing several worked examples in long-form text) |
| JTW-3.6a | TECH | candidate rule `tech.media-roles` showed no measured effect |
| JTW-3.6b | TECH | excluded at synthesis: a permission (examples in different media may differ) |
| JTW-3.6c | TECH | candidate rule `tech.media-roles` showed no measured effect |
| JTW-3.6d | TECH | candidate rule `tech.media-roles` showed no measured effect |
| JTW-3.6e | JA | excluded at synthesis: too narrow |
| JTW-3.7 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| JTW-3.8 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| JTW-4.1 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| JTW-4.2 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| JTW-4.3 | JA | candidate rule `ja.no-anata` showed no measured effect |
| JTW-4.4 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| JTW-4.5 | BOTH | candidate rule `both.define-and-keep-terms` showed no measured effect |
| JTW-4.6 | TECH | kept as `tech.established-terms` in `writing-tech` |
| JTW-4.7 | JA | candidate rule `ja.person-names` showed no measured effect |
| JTW-4.8 | TECH | candidate rule `both.define-and-keep-terms` showed no measured effect |
| JTW-4.9 | JA | kept as `ja.i-adjective-desu` in `writing-ja` |
| JTW-5.0 | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| JTW-5.1 | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| JTW-5.2a | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| JTW-5.2b | JA | candidate rule `ja.taigen-dome` showed no measured effect |
| JTW-5.3 | BOTH | candidate rule `both.sparing-bold` showed no measured effect |
| JTW-5.4 | JA | kept as `ja.judgment-form` in `writing-ja` |
| JTW-5.5 | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| JTW-5.6 | BOTH | candidate rule `both.facts-not-praise` showed no measured effect |
| JTW-5.7 | X-DUP | candidate rule `ja.empty-phrase-forms` showed no measured effect |
| JTW-5.8 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| JTW-5.9a | TECH | candidate rule `tech.plain-effect` showed no measured effect |
| JTW-5.9b | BOTH | candidate rule `both.literal-claims` showed no measured effect |
| JTW-6.0a | X-DUP | excluded at audit (X-DUP); see the audit row |
| JTW-6.0b | BOTH | candidate rule `both.show-not-label` showed no measured effect |
| JTW-6.0c | BOTH | candidate rule `both.cut-needless-words` showed no measured effect |
| JTW-6.1 | BOTH | candidate rule `both.no-empty-previews`, `ja.empty-phrase-forms` showed no measured effect |
| JTW-6.2 | BOTH | candidate rule `both.show-not-label` showed no measured effect |
| JTW-6.3 | BOTH | candidate rule `both.show-not-label`, `en.empty-emphasis` showed no measured effect |
| JTW-6.4 | BOTH | candidate rule `both.show-not-label` showed no measured effect |
| JTW-6.5 | BOTH | candidate rule `both.cut-needless-words`, `ja.empty-phrase-forms` showed no measured effect |
| JTW-6.6 | BOTH | candidate rule `both.cut-needless-words`, `both.keep-certainty`, `ja.one-hedge` showed no measured effect |
| JTW-7.0 | BOTH | candidate rule `both.literal-claims` showed no measured effect |
| JTW-7.1 | BOTH | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1a | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1b | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1c | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1d | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.2 | JA | candidate rule `ja.inanimate-subject` showed no measured effect |
| JTW-7.2a | TECH | candidate rule `both.literal-claims` showed no measured effect |
| JTW-7.2b | JA | candidate rule `ja.inanimate-subject` showed no measured effect |
| JTW-7.3 | TECH | candidate rule `ja.spoken-jargon`, `tech.plain-effect` showed no measured effect |
| JTW-7.3a | JA/TECH | candidate rule `ja.spoken-jargon`, `tech.plain-effect` showed no measured effect |
| JTW-7.3b | JA/TECH | candidate rule `ja.spoken-jargon` showed no measured effect |
| JTW-7.4a | BOTH | candidate rule `both.literal-claims` showed no measured effect |
| JTW-7.4b | BOTH | candidate rule `both.literal-claims`, `en.literal-verbs` showed no measured effect |
| JTW-8.0 | BOTH | candidate rule `both.cut-needless-words` showed no measured effect |
| JTW-8.1 | BOTH | candidate rule `both.say-it-once` showed no measured effect |
| JTW-8.2 | BOTH | candidate rule `both.say-it-once` showed no measured effect |
| JTW-8.3 | BOTH | candidate rule `both.say-it-once` showed no measured effect |
| JTW-8.4 | BOTH | candidate rule `both.merge-repeated-referents` showed no measured effect |
| JTW-8.5 | BOTH | candidate rule `both.cut-needless-words` showed no measured effect |
| JTW-8.6 | BOTH | candidate rule `both.cut-needless-words` showed no measured effect |
| JTW-8.7a | TECH | candidate rule `both.state-dont-stage` showed no measured effect |
| JTW-8.7b | TECH | candidate rule `both.state-dont-stage` showed no measured effect |
| JTW-8.8 | BOTH | candidate rule `both.no-empty-previews` showed no measured effect |
| JTW-8.9 | TECH | candidate rule `tech.scope-statement` showed no measured effect |
| JTW-8.10 | BOTH | candidate rule `both.write-for-the-reader` showed no measured effect |
| JTW-8.11 | X-DUP | excluded at audit (X-DUP); see the audit row |
| JTW-8.12 | BOTH | candidate rule `both.keep-certainty`, `ja.one-hedge` showed no measured effect |
| JTW-8.13 | JA | excluded at synthesis: not testable as an improvement |
| JTW-9.0 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.1 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.2 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.3 | X-DUP | excluded at audit (X-DUP); see the audit row |
| JTW-9.4 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.5 | BOTH | excluded at synthesis: a choice of tone with no fixed behavior to test |
| JTW-10.1 | BOTH | candidate rule `both.no-phantom-objections` showed no measured effect |
| JTW-10.2 | BOTH | excluded at synthesis: conflicts with both.attribute-claims (unattributed 'people often say' as grounds) |
| JTW-10.3 | BOTH | candidate rule `both.claims-match-evidence` showed no measured effect |

## op7418/Humanizer-zh

Audit: [`audits/op7418.md`](audits/op7418.md).

| Row | Audit destination | Outcome |
|---|---|---|
| OP-H01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-H02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P00 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| OP-P01 | BOTH | candidate rule `both.claims-match-evidence`, `both.keep-certainty`, `both.revise-without-loss`, `both.separate-non-causes`, `zh.state-markers` showed no measured effect |
| OP-P02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P03 | BOTH | candidate rule `both.match-house-and-voice` showed no measured effect |
| OP-P04 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| OP-P05 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| OP-P06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P08 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-P09 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-V01 | PERSONAL | kept as `pers.no-invented-reactions` in `writing-personal` |
| OP-V02 | TECH | candidate rule `tech.operation-state`, `tech.tool-limits` showed no measured effect |
| OP-V03 | TECH | candidate rule `tech.neutral-register`, `zh.four-char` showed no measured effect |
| OP-V04 | BOTH | candidate rule `both.name-the-relation` showed no measured effect |
| OP-V05 | BOTH | candidate rule `both.lists-vs-prose` showed no measured effect |
| OP-V06 | BOTH | candidate rule `pers.rhythm-follows-content` showed no measured effect |
| OP-W01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-W02 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-W03 | X-DUP | candidate rule `zh.state-markers` showed no measured effect |
| OP-W04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-O01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-O02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-O03 | BOTH | candidate rule `both.keep-literals` showed no measured effect |
| OP-O04 | TECH | candidate rule `tech.heading-anchors` showed no measured effect |
| OP-O05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-O06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-U01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-U02 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-U03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-C01 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| OP-C02 | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| OP-C03 | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| OP-C04 | BOTH | candidate rule `both.no-empty-previews`, `ja.empty-phrase-forms` showed no measured effect |
| OP-C05 | BOTH | candidate rule `both.no-phantom-objections` showed no measured effect |
| OP-C06 | BOTH | candidate rule `both.list-what-is-there` showed no measured effect |
| OP-C07 | BOTH | candidate rule `both.merge-repeated-referents`, `zh.subject-omission` showed no measured effect |
| OP-C08 | BOTH | candidate rule `both.name-the-relation`, `zh.dash-form` showed no measured effect |
| OP-C09 | BOTH | candidate rule `both.keep-certainty` showed no measured effect |
| OP-C10 | BOTH | kept as `en.hyphenation` in `writing-en` |
| OP-C11 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| OP-C12 | BOTH | candidate rule `both.plain-words`, `zh.plain-words` showed no measured effect |
| OP-C13 | BOTH | candidate rule `both.facts-not-praise`, `zh.significance-tail` showed no measured effect |
| OP-C14 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| OP-C15 | BOTH | candidate rule `both.facts-not-praise`, `en.ing-rider`, `zh.significance-tail` showed no measured effect |
| OP-C16 | BOTH | candidate rule `both.facts-not-praise` showed no measured effect |
| OP-C17 | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| OP-C18 | BOTH | candidate rule `both.plain-words` showed no measured effect |
| OP-C19 | BOTH | candidate rule `both.sparing-bold` showed no measured effect |
| OP-C20a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| OP-C20b | EN | candidate rule `en.heading-case` showed no measured effect |
| OP-C21 | ZH | kept as `ja.kagi-quotes` in `writing-ja`; kept as `zh.full-width-punct` in `writing-zh` |
| OP-C22 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| OP-C23 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| OP-C24 | BOTH | candidate rule `both.no-empty-previews` showed no measured effect |
| OP-C25 | BOTH | excluded at synthesis: see the audit row |
| OP-CF0 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-C26 | ZH | candidate rule `en.noun-clusters`, `zh.de-chain` showed no measured effect |
| OP-C27 | ZH | candidate rule `ja.plain-predicates`, `zh.jinxing-verb`, `zh.state-markers` showed no measured effect |
| OP-C28 | ZH | candidate rule `zh.bei-passive` showed no measured effect |
| OP-C29 | ZH | candidate rule `zh.four-char` showed no measured effect |
| OP-C30 | ZH | candidate rule `zh.background-opener` showed no measured effect |
| OP-C31 | ZH | candidate rule `zh.stock-closing` showed no measured effect |
| OP-K01 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-K02 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-K03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-K04 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-K05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-K06 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-K07 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-K08 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-E01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-S01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-R01 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-R02 | X-DUP | candidate rule `zh.state-markers` showed no measured effect |
| OP-R03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-R04 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-R05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-R06 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-R07 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-L01 | X-DUP | candidate rule `zh.state-markers` showed no measured effect |
| OP-L02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-L03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-L04 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-L05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-L06 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-L07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-T01 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-T02 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-T03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-T04 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-T05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-T06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-T07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |

## blader/humanizer

Audit: [`audits/blader.md`](audits/blader.md).

| Row | Audit destination | Outcome |
|---|---|---|
| BH-D01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-I01 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-A00 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-A01 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-A02 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-A03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-A04 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-A05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-A06 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-A07 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-C01 | BOTH | candidate rule `both.say-it-once` showed no measured effect |
| BH-C02 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-C03 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-W00 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-W1.1 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-W1.2 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-W2.1 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| BH-W2.2 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| BH-W2.3 | BOTH | candidate rule `both.claims-match-evidence` showed no measured effect |
| BH-W2.4 | BOTH | candidate rule `both.claims-match-evidence` showed no measured effect |
| BH-W2.5 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-S3.1 | BOTH | excluded at synthesis: process step (read aloud) |
| BH-S3.2 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-S3.3 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| BH-S3.4 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-S3.5 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-S3.6 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-W4.1 | BOTH | excluded at synthesis: revision process |
| BH-W4.2 | BOTH | excluded at synthesis: revision process, as BH-W4.1 |
| BH-W4.3 | PERSONAL | candidate rule `pers.rhythm-follows-content` showed no measured effect |
| BH-V01 | BOTH | candidate rule `both.match-house-and-voice` showed no measured effect |
| BH-V02 | PERSONAL | candidate rule `pers.keep-author-voice` showed no measured effect |
| BH-V03 | BOTH | candidate rule `both.match-house-and-voice` showed no measured effect |
| BH-V04 | PERSONAL | candidate rule `pers.keep-author-voice`, `pers.keep-mixed-feelings`, `pers.state-the-view` showed no measured effect |
| BH-V05 | PERSONAL | kept as `pers.no-invented-reactions` in `writing-personal` |
| BH-V06 | TECH | candidate rule `tech.neutral-register` showed no measured effect |
| BH-V07 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-R01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-R02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-R03 | BOTH | candidate rule `both.keep-literals` showed no measured effect |
| BH-R04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-R05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-SA0 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P01 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| BH-P02a | BOTH | candidate rule `both.say-it-once` showed no measured effect |
| BH-P02b | BOTH | candidate rule `both.state-dont-stage`, `ja.taigen-dome` showed no measured effect |
| BH-P02c | EN | candidate rule `en.caps-emphasis` showed no measured effect |
| BH-P03 | BOTH | candidate rule `both.state-dont-stage` showed no measured effect |
| BH-P04 | BOTH | candidate rule `both.no-empty-previews`, `ja.empty-phrase-forms` showed no measured effect |
| BH-P05 | BOTH | candidate rule `both.no-phantom-objections` showed no measured effect |
| BH-SB0 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-P06 | BOTH | candidate rule `both.list-what-is-there` showed no measured effect |
| BH-P07 | BOTH | candidate rule `both.merge-repeated-referents`, `ja.subject-inheritance` showed no measured effect |
| BH-P08 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P09 | BOTH | candidate rule `both.keep-certainty`, `ja.one-hedge` showed no measured effect |
| BH-P10 | EN | kept as `en.hyphenation` in `writing-en` |
| BH-P11 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| BH-SC0 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-P12 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P13 | BOTH | candidate rule `both.facts-not-praise` showed no measured effect |
| BH-P14 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| BH-P15 | EN | candidate rule `en.ing-rider` showed no measured effect |
| BH-P16 | BOTH | candidate rule `both.facts-not-praise` showed no measured effect |
| BH-P17 | BOTH | candidate rule `both.attribute-claims`, `ja.name-the-thinker` showed no measured effect |
| BH-P18 | EN | candidate rule `en.copula-verbs` showed no measured effect |
| BH-SD0 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P19 | BOTH | candidate rule `both.lists-vs-prose`, `both.sparing-bold` showed no measured effect |
| BH-P20a | EN | candidate rule `en.heading-case` showed no measured effect |
| BH-P20b | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P20c | BOTH | excluded at synthesis: de-AI on re-check (horizontal rules between headed sections are a surface layout habit) |
| BH-P20d | BOTH | excluded at synthesis: depends on the publishing platform, which the text does not show |
| BH-P20e | TECH | candidate rule `tech.headings-name-content` showed no measured effect |
| BH-P21 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-SE0 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-P22 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P23a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P23b | BOTH | candidate rule `both.claims-match-evidence`, `ja.name-the-thinker` showed no measured effect |
| BH-P24 | BOTH | candidate rule `both.no-empty-previews` showed no measured effect |
| BH-P25a | TECH | kept as `tech.describe-current-state` in `writing-tech` |
| BH-P25b | TECH | kept as `tech.no-production-narration` in `writing-tech` |
| BH-P25c | BOTH | candidate rule `both.no-empty-previews` showed no measured effect |
| BH-SF0 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-P26 | BOTH | candidate rule `both.answer-first-in-replies` showed no measured effect |
| BH-N01 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| BH-N02 | BOTH | candidate rule `both.keep-literals` showed no measured effect |
| BH-N03 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-N04 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-N05 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-K00 | PERSONAL | candidate rule `pers.keep-author-voice` showed no measured effect |
| BH-K01 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| BH-K02 | PERSONAL | candidate rule `pers.keep-mixed-feelings` showed no measured effect |
| BH-K03 | PERSONAL | candidate rule `pers.keep-author-voice` showed no measured effect |
| BH-K04 | PERSONAL | candidate rule `pers.first-person` showed no measured effect |
| BH-K05 | PERSONAL | candidate rule `pers.keep-author-voice` showed no measured effect |
| BH-SRC | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG08 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG09 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG-W00 | TECH | candidate rule `both.plain-words` showed no measured effect |
| BH-AG-W01 | TECH | kept as `tech.point-first` in `writing-tech` |
| BH-AG-W02 | TECH | candidate rule `both.plain-words` showed no measured effect |
| BH-AG-W03 | TECH | candidate rule `tech.short-sentences` showed no measured effect |
| BH-AG-W04 | TECH | candidate rule `both.define-and-keep-terms` showed no measured effect |
| BH-AG-W05 | TECH | kept as `en.spec-modals` in `writing-en`; kept as `ja.judgment-form` in `writing-ja`; kept as `tech.requirement-keywords` in `writing-tech` |
| BH-AG-W06 | BOTH | candidate rule `both.lists-vs-prose` showed no measured effect |
| BH-AG-W07 | BOTH | candidate rule `both.cut-needless-words`, `ja.plain-predicates` showed no measured effect |
| BH-AG-W08 | TECH | kept as `tech.first-mention` in `writing-tech` |
| BH-AG-W09 | TECH | kept as `both.positive-form` in `writing-personal`, `writing-tech` |
| BH-AG-W10 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-AG-W11 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-AG-E01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG-E02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-AG-E03 | TECH | excluded at synthesis: it governs revising an instruction file over time (adding exceptions) |

## hardikpandya/stop-slop

Audit: [`audits/stop-slop.md`](audits/stop-slop.md).

| Row | Audit destination | Outcome |
|---|---|---|
| SS-C1 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C2 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C3a | X-DUP | candidate rule `ja.subject-inheritance` showed no measured effect |
| SS-C3b | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C4a | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C4b | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C5 | X-DUP | candidate rule `ja.no-anata` showed no measured effect |
| SS-C6a | PERSONAL | candidate rule `pers.rhythm-follows-content` showed no measured effect |
| SS-C6b | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C6c | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C6d | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C7 | BOTH | candidate rule `both.keep-certainty`, `both.no-phantom-objections`, `both.write-for-the-reader` showed no measured effect |
| SS-C8 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-Q01 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q02 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q04 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q06 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q07 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q08 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q09 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q10 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q11 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-Q12 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-S1 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| SS-ST01 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST02 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST03 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST04 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST05 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST06 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| SS-ST07 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST08 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST09 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST10 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST11 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST12 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST13 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST14 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST15 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST16 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST17 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST18 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST19 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST20 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST21 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST22 | BOTH | kept as `both.positive-form` in `writing-personal`, `writing-tech` |
| SS-ST23 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| SS-ST24 | PERSONAL | kept as `pers.reader-in-scene` in `writing-personal` |
| SS-ST25 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST26 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST27 | BOTH | candidate rule `both.scope-claims` showed no measured effect |
| SS-ST28 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| SS-ST29 | EN | excluded at synthesis: not testable |
| SS-ST30 | EN | excluded at synthesis: see the audit row |
| SS-ST31 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST32 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST33 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST34 | PERSONAL | candidate rule `ja.taigen-dome` showed no measured effect |
| SS-ST35 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST36 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-ST37 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-ST38 | BOTH | candidate rule `both.scope-claims` showed no measured effect |
| SS-ST39 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-P01 | BOTH | candidate rule `both.no-empty-previews` showed no measured effect |
| SS-P02 | BOTH | candidate rule `both.show-not-label` showed no measured effect |
| SS-P03 | BOTH | candidate rule `both.plain-words` showed no measured effect |
| SS-P04 | BOTH | candidate rule `both.cut-needless-words`, `en.empty-emphasis` showed no measured effect |
| SS-P05 | BOTH | candidate rule `both.cut-needless-words` showed no measured effect |
| SS-P06 | PERSONAL | candidate rule `ja.empty-phrase-forms`, `pers.no-signposts` showed no measured effect |
| SS-P07 | PERSONAL | kept as `pers.specific-admission` in `writing-personal` |
| SS-P08 | BOTH | candidate rule `both.show-not-label` showed no measured effect |
| SS-P09 | BOTH | candidate rule `both.show-not-label` showed no measured effect |
| SS-E1 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-E2a | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-E2b | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| SS-E3 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-E4 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-E5 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-R1 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-R2 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-R3 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-R4 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| SS-L1 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L2 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L3 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L4 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L5 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L6 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L7 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L8 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-L9 | X-DUP | excluded at audit (X-DUP); see the audit row |

## Wikipedia: Signs of AI writing

Audit: [`audits/wikipedia.md`](audits/wikipedia.md).

| Row | Audit destination | Outcome |
|---|---|---|
| WP-G01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G08 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-G09 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-C00 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| WP-C01 | BOTH | candidate rule `both.facts-not-praise` showed no measured effect |
| WP-C01a | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C01b | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C01c | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C01d | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C02 | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| WP-C02a | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| WP-C02b | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-C03 | BOTH | candidate rule `both.facts-not-praise`, `en.ing-rider` showed no measured effect |
| WP-C04 | BOTH | candidate rule `both.facts-not-praise` showed no measured effect |
| WP-C04a | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C04b | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C05 | BOTH | candidate rule `both.be-specific` showed no measured effect |
| WP-C06 | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| WP-C06a | BOTH | candidate rule `both.list-what-is-there` showed no measured effect |
| WP-C07 | BOTH | candidate rule `both.facts-not-praise` showed no measured effect |
| WP-C08 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L00 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-L01 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L01a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L01b | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L01c | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L01d | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L01e | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L01f | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-L02 | BOTH | candidate rule `both.plain-words`, `en.copula-verbs` showed no measured effect |
| WP-L02a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-L03 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| WP-L03a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L03b | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L03c | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-L04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-L05 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-S01 | X-DEAI | candidate rule `en.heading-case` showed no measured effect |
| WP-S02 | BOTH | candidate rule `both.sparing-bold` showed no measured effect |
| WP-S03 | BOTH | candidate rule `both.lists-vs-prose` showed no measured effect |
| WP-S03a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S03b | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-S04a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S04b | BOTH | excluded at synthesis: see the audit row |
| WP-S04c | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S04d | TECH | kept as `tech.no-stacked-headings` in `writing-tech` |
| WP-S05 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-S06 | BOTH | candidate rule `both.lists-vs-prose` showed no measured effect |
| WP-S06a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S07 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-U01 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-U02 | BOTH | candidate rule `both.claims-match-evidence` showed no measured effect |
| WP-U02a | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-U03 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-U03a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-U03b | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-U03c | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M01a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M01b | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M01c | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M01d | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03b | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03c | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03d | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03e | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03f | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03g | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03h | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03i | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03j | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M03k | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-M05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R05a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-R07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T00 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T08 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-T09 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-T10 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-E00 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-E01 | TECH | candidate rule `tech.specific-change-summary` showed no measured effect |
| WP-E02 | TECH | candidate rule `tech.scope-statement` showed no measured effect |
| WP-E03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-E04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-E05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X04a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X07a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X07b | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-X08 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-HS01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-HS02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-HS03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-HS03a | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-HS03b | BOTH | candidate rule `both.plain-words` showed no measured effect |
| WP-HS03c | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-HS03d | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-HS03e | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-IE00 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE03 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-IE08 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-H00 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-H01 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H02 | BOTH | candidate rule `both.show-not-label`, `en.empty-emphasis` showed no measured effect |
| WP-H03 | BOTH | candidate rule `both.say-it-once` showed no measured effect |
| WP-H04 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H05 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H05a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H06 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-H08 | TECH | candidate rule `both.define-and-keep-terms` showed no measured effect |

## tropes.fyi tropes.md v2 and The Writing Whip (test material only)

Audit: [`audits/tropes-v2.md`](audits/tropes-v2.md).

| Row | Audit destination | Outcome |
|---|---|---|
| TV-00 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-01 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-02 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-03 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-04 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-05 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-06 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-07 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-08 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-09 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-10 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-11 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-12 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-13 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-14 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-15 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-16 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-17 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-18 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-19 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-20 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-21 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-22 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-23 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-24 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-25 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-26 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-27 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-28 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-29 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-30 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-31 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-32 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-33 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-34 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-35 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-36 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-37 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-38 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-39 | PERSONAL | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-40 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-41 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-42 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-43 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-44 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-45 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-46 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-47 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-48 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-49 | PERSONAL | test material for the ablation tests; see the audit row for the candidate rule it tests |
| TV-50 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-00 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-01 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R03 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R05 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R06 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R08 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R09 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R10 | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-R11 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B00 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-B10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T00 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T15 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T16 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T17 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T18 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T19 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T20 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T21 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T22 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T23 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T24 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T25 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T26 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T27 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T28 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T29 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T30 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T31 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T32 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T33 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T34 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T35 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T36 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T37 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T38 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| WH-T39 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |

## ninehills/skills deslop, deslop-en, deslop-zh (test material only)

Audit: [`audits/deslop.md`](audits/deslop.md).

| Row | Audit destination | Outcome |
|---|---|---|
| DZ-1.1a | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.1b | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.1c | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.2a | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.2b | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.2c | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.3 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.4a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.4b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.4c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.4d | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-1.4e | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.07 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.15 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-2.16 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.1 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.2 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.3 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.4 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.5 | PERSONAL | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.6 | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7a | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7b | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7c | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7d | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7e | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7f | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7g | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.7h | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.8a | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.8b | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.8c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.8d | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.8e | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.8f | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.8g | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.9a | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.9b | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.9c | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.9d | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.9e | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.10a | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.10b | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.10c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.11a | ZH/TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.11b | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.12a | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.12b | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.13 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.14a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.14b | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.14c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-3.14d | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1a | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1c | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1d | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1e | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1f | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1g | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1h | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1i | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1j | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.1k | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2a | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2c | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2d | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2e | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2f | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2g | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2h | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.2i | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3a | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3b | PERSONAL | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3c | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3d | PERSONAL | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3e | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3f | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3g | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3h | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.3i | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.4a | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.4b | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.4c | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.4d | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.4e | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.4f | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.4g | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5d | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5e | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5f | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5g | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.5h | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6b | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6c | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6d | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6e | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6f | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6g | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6h | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-4.6i | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.07 | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.08 | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.09 | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.15 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.16 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.17 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.18 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.19 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.20 | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-5.21 | ZH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-6.1 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-6.2 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-6.3 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-6.4 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-6.5 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-6.6 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-7.1 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-7.2 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-7.3 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-7.4 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-8 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DZ-9 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-C1 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-C2 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-C3 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-C4 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-Q14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P02a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P02b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P07 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P08 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P09 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P10 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P12 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P14 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P15 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P16 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P17 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P18 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P19 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P20 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P21 | PERSONAL | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P22 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P23 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P24 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-P25 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G03 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G15 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G16 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-G17 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V03 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V04 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V05 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V09 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V10 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V11 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V12 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V13 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V15 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V16 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V17 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V18 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V19 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V20 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V21 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V22 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V23 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V24 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V25 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-V26 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-H1 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-H2 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-H3 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-H4 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-H5 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-X1 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-X2 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-X3 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-X4 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-X5 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-X6 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-E1 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-E2 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-E3 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-E4 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-S1 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DE-R1 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-W1 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C1 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C2 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C3 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C4 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C5a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C5b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C5c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C5d | TECH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C6a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C6b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C7a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C7b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C7c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C7d | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C7e | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C7f | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C8a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C8b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C8c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C9 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C10a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C10b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-C10c | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q15 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q16 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-Q17 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-S1 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-R1 | X-SCOPE | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-E0a | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-E0b | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST15 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST16 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST17 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST18 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST19 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST20 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST21 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST22 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST23 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST24 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST25 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST26 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST27 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST28 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST29 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST30 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST31 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST32 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST33 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST34 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST35 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST36 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST37 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST38 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST39 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST40 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST41 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST42 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST43 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST44 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST45 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST46 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST47 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST48 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST49 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST50 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST51 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST52 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST53 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST54 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST55 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST56 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST57 | X-DEAI | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST58 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST59 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST60 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST61 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST62 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST63 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-ST64 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P05 | EN | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P13 | BOTH | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P15 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-P16 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX01 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX02 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX03 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX04 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX05 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX06 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX07 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX08 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX09 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX10 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX11 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX12 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX13 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX14 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
| DS-EX15 | X-DUP | test material for the ablation tests; see the audit row for the candidate rule it tests |
