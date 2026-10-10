# Coverage of upstream rules

Every rule of every upstream source has one row here with its final outcome. The audit files in `audits/` give the reason for each destination. A rule that reached a candidate skill rule was kept only if the ablation tests in `evals/` showed an effect.

Rows: 1214. Kept through a skill rule: 199. Reached a candidate rule that showed no effect: 101. Excluded at audit or synthesis: 403. Test material only: 511.

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
| STE-2 | EN/TECH | kept as `en.sentence-length` in `writing-en`; kept as `tech.short-sentences` in `writing-tech` |
| STE-3 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| STE-4 | EN/TECH | kept as `tech.operation-state` in `writing-tech`; candidate rule `en.tense-by-event`, `zh.state-markers` showed no measured effect |
| STE-5 | EN/TECH | candidate rule `en.ing-clauses` showed no measured effect |
| STE-6 | TECH | kept as `en.plain-words` in `writing-en` |
| STE-7 | BOTH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |
| STE-8 | EN/TECH | kept as `tech.established-terms` in `writing-tech` |
| STE-9 | EN/TECH | kept as `en.noun-clusters` in `writing-en` |
| STE-10 | EN | kept as `en.complete-sentences` in `writing-en`; candidate rule `tech.format-conventions` showed no measured effect |
| STE-11 | BOTH | kept as `both.one-topic-per-paragraph` in `writing-personal`; candidate rule `en.paragraph-length` showed no measured effect |
| STE-12 | TECH | candidate rule `tech.vertical-lists` showed no measured effect |
| STE-13 | TECH | kept as `tech.warning-placement` in `writing-tech` |
| STE-14 | TECH | kept as `tech.established-terms` in `writing-tech` |

## obra/the-elements-of-style

Audit: [`audits/eos.md`](audits/eos.md).

| Row | Audit destination | Outcome |
|---|---|---|
| EOS-I01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| EOS-R01 | EN | kept as `en.usage-reference` in `writing-en` |
| EOS-R02 | EN | excluded at synthesis: see the audit row |
| EOS-R03 | EN | excluded at synthesis: see the audit row |
| EOS-R04 | EN | excluded at synthesis: see the audit row |
| EOS-R04b | BOTH | kept as `both.name-the-relation` in `writing-tech`; candidate rule `ja.weak-ga` showed no measured effect |
| EOS-R04c | EN | candidate rule `en.unambiguous-conjunctions` showed no measured effect |
| EOS-R05 | EN | excluded at synthesis: see the audit row |
| EOS-R06 | EN | kept as `en.complete-sentences` in `writing-en` |
| EOS-R07 | EN | candidate rule `en.ing-clauses` showed no measured effect |
| EOS-R08 | BOTH | kept as `both.one-topic-per-paragraph` in `writing-personal` |
| EOS-R08b | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| EOS-R08c | BOTH | excluded at synthesis: too narrow (dialogue layout in fiction and transcripts) |
| EOS-R09 | TECH | kept as `tech.point-first` in `writing-tech` |
| EOS-R10 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| EOS-R10b | EN | excluded at synthesis: see the audit row |
| EOS-R10c | BOTH | kept as `ja.plain-predicates` in `writing-ja`; candidate rule `both.plain-words` showed no measured effect |
| EOS-R10d | EN | candidate rule `en.real-actor`, `ja.inanimate-subject` showed no measured effect |
| EOS-R11 | BOTH | kept as `both.positive-form` in `writing-personal`, `writing-tech` |
| EOS-R11b | BOTH | kept as `both.positive-form` in `writing-personal`, `writing-tech` |
| EOS-R12 | BOTH | kept as `both.be-specific` in `writing-tech` |
| EOS-R13 | BOTH | kept as `both.cut-needless-words` in `writing-tech` |
| EOS-R13b | EN | kept as `en.plain-words` in `writing-en` |
| EOS-R13c | EN | excluded at synthesis: see the audit row |
| EOS-R13d | BOTH | candidate rule `both.merge-repeated-referents` showed no measured effect |
| EOS-R14 | BOTH | kept as `both.name-the-relation` in `writing-tech`; candidate rule `ja.weak-ga` showed no measured effect |
| EOS-R15 | BOTH | candidate rule `both.parallel-form` showed no measured effect |
| EOS-R15b | EN | excluded at synthesis: see the audit row |
| EOS-R15c | BOTH | kept as `both.lists-vs-prose` in `writing-tech` |
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
| EOS-V06 | EN/TECH | kept as `tech.requirement-keywords` in `writing-tech`; candidate rule `en.spec-modals` showed no measured effect |
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
| EOS-V31 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech` |
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
| EOS-V50 | EN | candidate rule `en.spec-modals` showed no measured effect |
| EOS-V51 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-V52 | EN | candidate rule `en.empty-emphasis` showed no measured effect |
| EOS-V53 | X-DUP | excluded at audit (X-DUP); see the audit row |
| EOS-V54 | EN | excluded at synthesis: dated (Chicago and M-W accept a split infinitive) |
| EOS-V55 | EN | excluded at synthesis: not checked |
| EOS-V56 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V57 | EN | kept as `en.plain-words` in `writing-en` |
| EOS-V58 | EN | excluded at synthesis: letter etiquette, not checked |
| EOS-V59 | EN | excluded at synthesis: see the audit row |
| EOS-V60 | BOTH | kept as `both.cut-needless-words` in `writing-tech`; candidate rule `en.empty-emphasis` showed no measured effect |
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
| JTW-1.0 | BOTH | kept as `both.one-topic-per-paragraph` in `writing-personal` |
| JTW-1.1 | BOTH | kept as `both.one-topic-per-paragraph` in `writing-personal` |
| JTW-1.2 | TECH | kept as `tech.point-first` in `writing-tech` |
| JTW-1.3 | BOTH | kept as `both.name-the-relation` in `writing-tech` |
| JTW-1.4 | BOTH | kept as `both.say-it-once` in `writing-tech` |
| JTW-1.5 | BOTH | excluded at synthesis: too narrow (where caveats about an example go in a narrated scene) |
| JTW-1.6 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| JTW-1.7 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| JTW-1.8a | BOTH | candidate rule `both.parallel-form` showed no measured effect |
| JTW-1.8b | BOTH | excluded at synthesis: too narrow (one callback construction) |
| JTW-1.8c | JA | kept as `ja.kagi-quotes` in `writing-ja` |
| JTW-1.8d | BOTH | kept as `both.name-the-relation` in `writing-tech` |
| JTW-1.8e | JA | candidate rule `ja.subject-inheritance` showed no measured effect |
| JTW-1.9 | BOTH | excluded at synthesis: too narrow (voice of a concession in a book argument) |
| JTW-1.10 | BOTH | excluded at synthesis: see the audit row |
| JTW-1.11 | BOTH | kept as `ja.kagi-quotes` in `writing-ja` |
| JTW-1.12 | BOTH | excluded at synthesis: not testable at case length (placement of forward references in long text) |
| JTW-2.0 | BOTH | kept as `both.claims-match-evidence` in `writing-tech` |
| JTW-2.1 | BOTH | kept as `both.keep-certainty` in `writing-personal`; kept as `ja.one-hedge` in `writing-ja` |
| JTW-2.2 | BOTH | kept as `both.name-every-cause` in `writing-personal` |
| JTW-2.3 | BOTH | kept as `both.name-every-cause` in `writing-personal` |
| JTW-2.4 | BOTH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |
| JTW-2.5 | BOTH | kept as `both.state-the-mechanism` in `writing-tech` |
| JTW-2.6 | TECH | candidate rule `tech.tool-limits` showed no measured effect |
| JTW-2.7 | BOTH | kept as `both.scope-claims` in `writing-tech` |
| JTW-2.8 | BOTH | excluded at synthesis: not testable at case length (a deferred point resolved in a later section) |
| JTW-2.9 | BOTH | excluded at synthesis: too narrow (what follows a concession in long-form argument) |
| JTW-2.10 | BOTH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |
| JTW-2.11 | BOTH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |
| JTW-3.0 | BOTH | excluded at synthesis: framing statement with no behavior of its own |
| JTW-3.1a | BOTH | excluded at synthesis: not observable in a short text (reader load raised one level at a time) |
| JTW-3.1b | BOTH | excluded at synthesis: revision bookkeeping after cuts in a long document |
| JTW-3.1c | BOTH | candidate rule `both.write-for-the-reader` showed no measured effect |
| JTW-3.2 | TECH | kept as `tech.identifiers-when-used` in `writing-tech` |
| JTW-3.3 | BOTH | kept as `both.one-reading` in `writing-tech` |
| JTW-3.4 | BOTH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech`; kept as `ja.type-before-modifiers` in `writing-ja` |
| JTW-3.5 | BOTH | excluded at synthesis: too narrow (sequencing several worked examples in long-form text) |
| JTW-3.6a | TECH | candidate rule `tech.media-roles` showed no measured effect |
| JTW-3.6b | TECH | excluded at synthesis: a permission (examples in different media may differ) |
| JTW-3.6c | TECH | candidate rule `tech.media-roles` showed no measured effect |
| JTW-3.6d | TECH | candidate rule `tech.media-roles` showed no measured effect |
| JTW-3.6e | JA | excluded at synthesis: too narrow |
| JTW-3.7 | BOTH | kept as `both.be-specific` in `writing-tech` |
| JTW-3.8 | BOTH | kept as `both.be-specific` in `writing-tech` |
| JTW-4.1 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| JTW-4.2 | BOTH | kept as `both.be-specific` in `writing-tech` |
| JTW-4.3 | JA | kept as `ja.no-anata` in `writing-ja` |
| JTW-4.4 | BOTH | kept as `both.be-specific` in `writing-tech` |
| JTW-4.5 | BOTH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |
| JTW-4.6 | TECH | kept as `tech.established-terms` in `writing-tech` |
| JTW-4.7 | JA | kept as `ja.person-names` in `writing-ja` |
| JTW-4.8 | TECH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |
| JTW-4.9 | JA | kept as `ja.i-adjective-desu` in `writing-ja` |
| JTW-5.0 | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| JTW-5.1 | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| JTW-5.2a | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| JTW-5.2b | JA | candidate rule `ja.taigen-dome` showed no measured effect |
| JTW-5.3 | BOTH | kept as `both.sparing-bold` in `writing-tech` |
| JTW-5.4 | JA | kept as `ja.judgment-form` in `writing-ja` |
| JTW-5.5 | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| JTW-5.6 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech` |
| JTW-5.7 | X-DUP | candidate rule `ja.empty-phrase-forms` showed no measured effect |
| JTW-5.8 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| JTW-5.9a | TECH | kept as `tech.plain-effect` in `writing-tech` |
| JTW-5.9b | BOTH | kept as `both.literal-claims` in `writing-tech` |
| JTW-6.0a | X-DUP | excluded at audit (X-DUP); see the audit row |
| JTW-6.0b | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech` |
| JTW-6.0c | BOTH | kept as `both.cut-needless-words` in `writing-tech` |
| JTW-6.1 | BOTH | kept as `both.no-empty-previews` in `writing-tech`; candidate rule `ja.empty-phrase-forms` showed no measured effect |
| JTW-6.2 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech` |
| JTW-6.3 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech`; candidate rule `en.empty-emphasis` showed no measured effect |
| JTW-6.4 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech` |
| JTW-6.5 | BOTH | kept as `both.cut-needless-words` in `writing-tech`; candidate rule `ja.empty-phrase-forms` showed no measured effect |
| JTW-6.6 | BOTH | kept as `both.cut-needless-words` in `writing-tech`; kept as `both.keep-certainty` in `writing-personal`; kept as `ja.one-hedge` in `writing-ja` |
| JTW-7.0 | BOTH | kept as `both.literal-claims` in `writing-tech` |
| JTW-7.1 | BOTH | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1a | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1b | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1c | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.1d | JA | kept as `ja.calque-verbs` in `writing-ja` |
| JTW-7.2 | JA | candidate rule `ja.inanimate-subject` showed no measured effect |
| JTW-7.2a | TECH | kept as `both.literal-claims` in `writing-tech` |
| JTW-7.2b | JA | candidate rule `ja.inanimate-subject` showed no measured effect |
| JTW-7.3 | TECH | kept as `tech.plain-effect` in `writing-tech`; candidate rule `ja.spoken-jargon` showed no measured effect |
| JTW-7.3a | JA/TECH | kept as `tech.plain-effect` in `writing-tech`; candidate rule `ja.spoken-jargon` showed no measured effect |
| JTW-7.3b | JA/TECH | candidate rule `ja.spoken-jargon` showed no measured effect |
| JTW-7.4a | BOTH | kept as `both.literal-claims` in `writing-tech` |
| JTW-7.4b | BOTH | kept as `both.literal-claims` in `writing-tech`; candidate rule `en.literal-verbs` showed no measured effect |
| JTW-8.0 | BOTH | kept as `both.cut-needless-words` in `writing-tech` |
| JTW-8.1 | BOTH | kept as `both.say-it-once` in `writing-tech` |
| JTW-8.2 | BOTH | kept as `both.say-it-once` in `writing-tech` |
| JTW-8.3 | BOTH | kept as `both.say-it-once` in `writing-tech` |
| JTW-8.4 | BOTH | candidate rule `both.merge-repeated-referents` showed no measured effect |
| JTW-8.5 | BOTH | kept as `both.cut-needless-words` in `writing-tech` |
| JTW-8.6 | BOTH | kept as `both.cut-needless-words` in `writing-tech` |
| JTW-8.7a | TECH | kept as `both.state-dont-stage` in `writing-personal` |
| JTW-8.7b | TECH | kept as `both.state-dont-stage` in `writing-personal` |
| JTW-8.8 | BOTH | kept as `both.no-empty-previews` in `writing-tech` |
| JTW-8.9 | TECH | candidate rule `tech.scope-statement` showed no measured effect |
| JTW-8.10 | BOTH | candidate rule `both.write-for-the-reader` showed no measured effect |
| JTW-8.11 | X-DUP | excluded at audit (X-DUP); see the audit row |
| JTW-8.12 | BOTH | kept as `both.keep-certainty` in `writing-personal`; kept as `ja.one-hedge` in `writing-ja` |
| JTW-8.13 | JA | excluded at synthesis: not testable as an improvement |
| JTW-9.0 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.1 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.2 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.3 | X-DUP | excluded at audit (X-DUP); see the audit row |
| JTW-9.4 | BOTH | excluded at synthesis: see the audit row |
| JTW-9.5 | BOTH | excluded at synthesis: a choice of tone with no fixed behavior to test |
| JTW-10.1 | BOTH | kept as `both.no-phantom-objections` in `writing-personal`, `writing-tech` |
| JTW-10.2 | BOTH | excluded at synthesis: conflicts with both.attribute-claims (unattributed 'people often say' as grounds) |
| JTW-10.3 | BOTH | kept as `both.claims-match-evidence` in `writing-tech` |

## op7418/Humanizer-zh

Audit: [`audits/op7418.md`](audits/op7418.md).

| Row | Audit destination | Outcome |
|---|---|---|
| OP-H01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-H02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P00 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| OP-P01 | BOTH | kept as `both.claims-match-evidence` in `writing-tech`; kept as `both.keep-certainty` in `writing-personal`; candidate rule `both.revise-without-loss`, `both.separate-non-causes`, `zh.state-markers` showed no measured effect |
| OP-P02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P03 | BOTH | candidate rule `both.match-house-and-voice` showed no measured effect |
| OP-P04 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| OP-P05 | BOTH | kept as `both.be-specific` in `writing-tech` |
| OP-P06 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-P08 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-P09 | X-DUP | excluded at audit (X-DUP); see the audit row |
| OP-V01 | PERSONAL | kept as `pers.no-invented-reactions` in `writing-personal` |
| OP-V02 | TECH | kept as `tech.operation-state` in `writing-tech`; candidate rule `tech.tool-limits` showed no measured effect |
| OP-V03 | TECH | kept as `tech.neutral-register` in `writing-tech`; candidate rule `zh.four-char` showed no measured effect |
| OP-V04 | BOTH | kept as `both.name-the-relation` in `writing-tech` |
| OP-V05 | BOTH | kept as `both.lists-vs-prose` in `writing-tech` |
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
| OP-C02 | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| OP-C03 | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| OP-C04 | BOTH | kept as `both.no-empty-previews` in `writing-tech`; candidate rule `ja.empty-phrase-forms` showed no measured effect |
| OP-C05 | BOTH | kept as `both.no-phantom-objections` in `writing-personal`, `writing-tech` |
| OP-C06 | BOTH | candidate rule `both.list-what-is-there` showed no measured effect |
| OP-C07 | BOTH | candidate rule `both.merge-repeated-referents`, `zh.subject-omission` showed no measured effect |
| OP-C08 | BOTH | kept as `both.name-the-relation` in `writing-tech`; candidate rule `zh.dash-form` showed no measured effect |
| OP-C09 | BOTH | kept as `both.keep-certainty` in `writing-personal` |
| OP-C10 | BOTH | kept as `en.hyphenation` in `writing-en` |
| OP-C11 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| OP-C12 | BOTH | candidate rule `both.plain-words`, `zh.plain-words` showed no measured effect |
| OP-C13 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech`; candidate rule `zh.significance-tail` showed no measured effect |
| OP-C14 | BOTH | kept as `both.be-specific` in `writing-tech` |
| OP-C15 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech`; candidate rule `en.ing-rider`, `zh.significance-tail` showed no measured effect |
| OP-C16 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech` |
| OP-C17 | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| OP-C18 | BOTH | candidate rule `both.plain-words` showed no measured effect |
| OP-C19 | BOTH | kept as `both.sparing-bold` in `writing-tech` |
| OP-C20a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| OP-C20b | EN | kept as `en.heading-case` in `writing-en` |
| OP-C21 | ZH | kept as `ja.kagi-quotes` in `writing-ja`; kept as `zh.full-width-punct` in `writing-zh` |
| OP-C22 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| OP-C23 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| OP-C24 | BOTH | kept as `both.no-empty-previews` in `writing-tech` |
| OP-C25 | BOTH | excluded at synthesis: see the audit row |
| OP-CF0 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| OP-C26 | ZH | kept as `en.noun-clusters` in `writing-en`; kept as `zh.de-chain` in `writing-zh` |
| OP-C27 | ZH | kept as `ja.plain-predicates` in `writing-ja`; kept as `zh.jinxing-verb` in `writing-zh`; candidate rule `zh.state-markers` showed no measured effect |
| OP-C28 | ZH | kept as `zh.bei-passive` in `writing-zh` |
| OP-C29 | ZH | candidate rule `zh.four-char` showed no measured effect |
| OP-C30 | ZH | kept as `zh.background-opener` in `writing-zh` |
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
| BH-C01 | BOTH | kept as `both.say-it-once` in `writing-tech` |
| BH-C02 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-C03 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-W00 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-W1.1 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-W1.2 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-W2.1 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| BH-W2.2 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| BH-W2.3 | BOTH | kept as `both.claims-match-evidence` in `writing-tech` |
| BH-W2.4 | BOTH | kept as `both.claims-match-evidence` in `writing-tech` |
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
| BH-V06 | TECH | kept as `tech.neutral-register` in `writing-tech` |
| BH-V07 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-R01 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-R02 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-R03 | BOTH | candidate rule `both.keep-literals` showed no measured effect |
| BH-R04 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-R05 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-SA0 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P01 | BOTH | candidate rule `both.real-contrasts` showed no measured effect |
| BH-P02a | BOTH | kept as `both.say-it-once` in `writing-tech` |
| BH-P02b | BOTH | kept as `both.state-dont-stage` in `writing-personal`; candidate rule `ja.taigen-dome` showed no measured effect |
| BH-P02c | EN | candidate rule `en.caps-emphasis` showed no measured effect |
| BH-P03 | BOTH | kept as `both.state-dont-stage` in `writing-personal` |
| BH-P04 | BOTH | kept as `both.no-empty-previews` in `writing-tech`; candidate rule `ja.empty-phrase-forms` showed no measured effect |
| BH-P05 | BOTH | kept as `both.no-phantom-objections` in `writing-personal`, `writing-tech` |
| BH-SB0 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-P06 | BOTH | candidate rule `both.list-what-is-there` showed no measured effect |
| BH-P07 | BOTH | candidate rule `both.merge-repeated-referents`, `ja.subject-inheritance` showed no measured effect |
| BH-P08 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P09 | BOTH | kept as `both.keep-certainty` in `writing-personal`; kept as `ja.one-hedge` in `writing-ja` |
| BH-P10 | EN | kept as `en.hyphenation` in `writing-en` |
| BH-P11 | BOTH | kept as `both.name-the-actor` in `writing-tech` |
| BH-SC0 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-P12 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P13 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech` |
| BH-P14 | BOTH | kept as `both.be-specific` in `writing-tech` |
| BH-P15 | EN | candidate rule `en.ing-rider` showed no measured effect |
| BH-P16 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech` |
| BH-P17 | BOTH | kept as `ja.name-the-thinker` in `writing-ja`; candidate rule `both.attribute-claims` showed no measured effect |
| BH-P18 | EN | candidate rule `en.copula-verbs` showed no measured effect |
| BH-SD0 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P19 | BOTH | kept as `both.lists-vs-prose` in `writing-tech`; kept as `both.sparing-bold` in `writing-tech` |
| BH-P20a | EN | kept as `en.heading-case` in `writing-en` |
| BH-P20b | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P20c | BOTH | excluded at synthesis: de-AI on re-check (horizontal rules between headed sections are a surface layout habit) |
| BH-P20d | BOTH | excluded at synthesis: depends on the publishing platform, which the text does not show |
| BH-P20e | TECH | candidate rule `tech.headings-name-content` showed no measured effect |
| BH-P21 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-SE0 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| BH-P22 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P23a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-P23b | BOTH | kept as `both.claims-match-evidence` in `writing-tech`; kept as `ja.name-the-thinker` in `writing-ja` |
| BH-P24 | BOTH | kept as `both.no-empty-previews` in `writing-tech` |
| BH-P25a | TECH | kept as `tech.describe-current-state` in `writing-tech` |
| BH-P25b | TECH | kept as `tech.no-production-narration` in `writing-tech` |
| BH-P25c | BOTH | kept as `both.no-empty-previews` in `writing-tech` |
| BH-SF0 | X-DUP | excluded at audit (X-DUP); see the audit row |
| BH-P26 | BOTH | kept as `both.answer-first-in-replies` in `writing-personal`, `writing-tech` |
| BH-N01 | BOTH | candidate rule `both.revise-without-loss` showed no measured effect |
| BH-N02 | BOTH | candidate rule `both.keep-literals` showed no measured effect |
| BH-N03 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-N04 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-N05 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| BH-K00 | PERSONAL | candidate rule `pers.keep-author-voice` showed no measured effect |
| BH-K01 | BOTH | kept as `both.be-specific` in `writing-tech` |
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
| BH-AG-W03 | TECH | kept as `tech.short-sentences` in `writing-tech` |
| BH-AG-W04 | TECH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |
| BH-AG-W05 | TECH | kept as `ja.judgment-form` in `writing-ja`; kept as `tech.requirement-keywords` in `writing-tech`; candidate rule `en.spec-modals` showed no measured effect |
| BH-AG-W06 | BOTH | kept as `both.lists-vs-prose` in `writing-tech` |
| BH-AG-W07 | BOTH | kept as `both.cut-needless-words` in `writing-tech`; kept as `ja.plain-predicates` in `writing-ja` |
| BH-AG-W08 | TECH | candidate rule `tech.first-mention` showed no measured effect |
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
| SS-C5 | X-DUP | kept as `ja.no-anata` in `writing-ja` |
| SS-C6a | PERSONAL | candidate rule `pers.rhythm-follows-content` showed no measured effect |
| SS-C6b | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C6c | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C6d | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-C7 | BOTH | kept as `both.keep-certainty` in `writing-personal`; kept as `both.no-phantom-objections` in `writing-personal`, `writing-tech`; candidate rule `both.write-for-the-reader` showed no measured effect |
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
| SS-ST27 | BOTH | kept as `both.scope-claims` in `writing-tech` |
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
| SS-ST38 | BOTH | kept as `both.scope-claims` in `writing-tech` |
| SS-ST39 | X-DUP | excluded at audit (X-DUP); see the audit row |
| SS-P01 | BOTH | kept as `both.no-empty-previews` in `writing-tech` |
| SS-P02 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech` |
| SS-P03 | BOTH | candidate rule `both.plain-words` showed no measured effect |
| SS-P04 | BOTH | kept as `both.cut-needless-words` in `writing-tech`; candidate rule `en.empty-emphasis` showed no measured effect |
| SS-P05 | BOTH | kept as `both.cut-needless-words` in `writing-tech` |
| SS-P06 | PERSONAL | candidate rule `ja.empty-phrase-forms`, `pers.no-signposts` showed no measured effect |
| SS-P07 | PERSONAL | kept as `pers.specific-admission` in `writing-personal` |
| SS-P08 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech` |
| SS-P09 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech` |
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
| WP-C00 | BOTH | kept as `both.be-specific` in `writing-tech` |
| WP-C01 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech` |
| WP-C01a | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C01b | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C01c | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C01d | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C02 | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| WP-C02a | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| WP-C02b | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-C03 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech`; candidate rule `en.ing-rider` showed no measured effect |
| WP-C04 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech` |
| WP-C04a | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C04b | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-C05 | BOTH | kept as `both.be-specific` in `writing-tech` |
| WP-C06 | BOTH | candidate rule `both.attribute-claims` showed no measured effect |
| WP-C06a | BOTH | candidate rule `both.list-what-is-there` showed no measured effect |
| WP-C07 | BOTH | kept as `both.facts-not-praise` in `writing-personal`, `writing-tech` |
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
| WP-S01 | X-DEAI | kept as `en.heading-case` in `writing-en` |
| WP-S02 | BOTH | kept as `both.sparing-bold` in `writing-tech` |
| WP-S03 | BOTH | kept as `both.lists-vs-prose` in `writing-tech` |
| WP-S03a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S03b | X-DUP | excluded at audit (X-DUP); see the audit row |
| WP-S04a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S04b | BOTH | excluded at synthesis: see the audit row |
| WP-S04c | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S04d | TECH | candidate rule `tech.no-stacked-headings` showed no measured effect |
| WP-S05 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-S06 | BOTH | kept as `both.lists-vs-prose` in `writing-tech` |
| WP-S06a | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-S07 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-U01 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-U02 | BOTH | kept as `both.claims-match-evidence` in `writing-tech` |
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
| WP-H02 | BOTH | kept as `both.show-not-label` in `writing-personal`, `writing-tech`; candidate rule `en.empty-emphasis` showed no measured effect |
| WP-H03 | BOTH | kept as `both.say-it-once` in `writing-tech` |
| WP-H04 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H05 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H05a | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H06 | X-DEAI | excluded at audit (X-DEAI); see the audit row |
| WP-H07 | X-SCOPE | excluded at audit (X-SCOPE); see the audit row |
| WP-H08 | TECH | kept as `both.define-and-keep-terms` in `writing-personal`, `writing-tech` |

## tropes.fyi tropes.md v2 and The Writing Whip (test material only)

Audit: [`audits/tropes-v2.md`](audits/tropes-v2.md).

| Row | Audit destination | Outcome |
|---|---|---|
| TV-00 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| TV-01 | BOTH | test material: global check `trope-negative-parallelism`; probed in cases `tropes-cache-article-ja`, `tropes-design-doc-edit-en`, `tropes-launch-post-en`, `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-oss-newsletter-zh`, `tropes-postmortem-en`, `tropes-readme-en`, `tropes-recipe-ending-en`, `tropes-release-notes-zh` |
| TV-02 | X-DEAI | test material: global check `trope-dash-overuse`; probed in cases `tropes-oss-newsletter-zh`, `tropes-postmortem-en`, `tropes-readme-en` |
| TV-03 | BOTH | test material: global check `trope-staged-emphasis`; probed in cases `tropes-cache-article-ja`, `tropes-ja-logging-chapter`, `tropes-launch-post-en`, `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-oss-newsletter-zh`, `tropes-readme-en` |
| TV-04 | BOTH | test material: global check `trope-reasoning-leak`; probed in cases `tropes-beam-reply-ja`, `tropes-oss-newsletter-zh`, `tropes-partner-request-en` |
| TV-05 | BOTH | test material: global check `trope-premise-stacking`; probed in cases `tropes-beam-reply-ja`, `tropes-migration-status-zh`, `tropes-partner-request-en` |
| TV-06 | BOTH | test material: global check `trope-preamble`; probed in cases `tropes-beam-reply-ja`, `tropes-cache-article-ja`, `tropes-design-doc-edit-en`, `tropes-exec-summary-en`, `tropes-ja-logging-chapter`, `tropes-migration-status-zh`, `tropes-partner-request-en`, `tropes-tutorial-en` |
| TV-07 | BOTH | test material: global check `trope-inflated-stakes`; probed in cases `tropes-design-doc-edit-en`, `tropes-exec-summary-en`, `tropes-launch-post-en`, `tropes-leaving-essay-ja`, `tropes-migration-status-zh`, `tropes-oss-newsletter-zh`, `tropes-recipe-ending-en`, `tropes-release-notes-zh` |
| TV-08 | X-DEAI | test material: global check `trope-compulsive-counting`; probed in cases `tropes-beam-reply-ja`, `tropes-exec-summary-en`, `tropes-launch-post-en`, `tropes-migration-status-zh`, `tropes-partner-request-en` |
| TV-09 | BOTH | test material: global check `trope-unstable-terms`; probed in cases `tropes-cache-article-ja`, `tropes-oss-newsletter-zh`, `tropes-postmortem-en` |
| TV-10 | X-DEAI | test material: global check `trope-padded-series`; probed in cases `tropes-metrics-essay-en`, `tropes-release-notes-zh` |
| TV-11 | BOTH | test material: global check `trope-phantom-objections`; probed in cases `tropes-beam-reply-ja`, `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-partner-request-en` |
| TV-12 | BOTH | test material: global check `trope-empty-emphasis`; probed in cases `tropes-design-doc-edit-en`, `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-partner-request-en`, `tropes-postmortem-en`, `tropes-readme-en`, `tropes-release-notes-zh` |
| TV-13 | BOTH | test material: global check `trope-restating-close`; probed in cases `tropes-beam-reply-ja`, `tropes-design-doc-edit-en`, `tropes-partner-request-en` |
| TV-14 | BOTH | test material: global check `trope-borrowed-authority`; probed in cases `tropes-ja-logging-chapter`, `tropes-oss-newsletter-zh`, `tropes-release-notes-zh` |
| TV-15 | BOTH | test material: global check `trope-self-echo`; probed in cases `tropes-leaving-essay-ja`, `tropes-metrics-essay-en` |
| TV-16 | BOTH | test material: global check `trope-staged-emphasis`; probed in cases `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-recipe-ending-en` |
| TV-17 | BOTH | test material: global check `trope-forced-figures`; probed in cases `tropes-cache-article-ja`, `tropes-metrics-essay-en`, `tropes-tutorial-en` |
| TV-18 | BOTH | test material: global check `trope-restating-close`; probed in cases `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-oss-newsletter-zh`, `tropes-recipe-ending-en` |
| TV-19 | X-DEAI | test material: global check `trope-significance-tails`; probed in cases `tropes-metrics-essay-en` |
| TV-20 | BOTH | test material: global check `trope-unstable-terms`; probed in cases `tropes-cache-article-ja`, `tropes-postmortem-en` |
| TV-21 | BOTH | test material: global check `trope-borrowed-authority`; probed in cases `tropes-cache-article-ja`, `tropes-oss-newsletter-zh`, `tropes-release-notes-zh` |
| TV-22 | BOTH | test material: global check `trope-promotional`; probed in cases `tropes-exec-summary-en`, `tropes-launch-post-en`, `tropes-readme-en`, `tropes-release-notes-zh` |
| TV-23 | X-DEAI | test material: global check `trope-heading-teasers`; probed in cases `tropes-cache-article-ja`, `tropes-design-doc-edit-en`, `tropes-exec-summary-en`, `tropes-migration-status-zh`, `tropes-readme-en` |
| TV-24 | BOTH | test material: global check `trope-forced-figures`; probed in cases `tropes-design-doc-edit-en`, `tropes-ja-logging-chapter`, `tropes-readme-en` |
| TV-25 | BOTH | test material: global check `trope-vague-we`; probed in cases `tropes-launch-post-en`, `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-oss-newsletter-zh`, `tropes-recipe-ending-en` |
| TV-26 | X-DUP | test material: global check `trope-negative-parallelism`; probed in cases `tropes-launch-post-en`, `tropes-postmortem-en`, `tropes-readme-en` |
| TV-27 | BOTH | test material: global checks `trope-staged-emphasis`, `trope-re-reveal-setups`; probed in cases `tropes-launch-post-en`, `tropes-metrics-essay-en`, `tropes-postmortem-en`, `tropes-tutorial-en` |
| TV-28 | BOTH | test material: global checks `trope-repetition`, `trope-preamble`, `trope-restating-close`; probed in cases `tropes-cache-article-ja`, `tropes-design-doc-edit-en`, `tropes-leaving-essay-ja`, `tropes-oss-newsletter-zh` |
| TV-29 | BOTH | test material: global check `trope-ordinal-prose`; probed in cases `tropes-cache-article-ja`, `tropes-design-doc-edit-en`, `tropes-exec-summary-en`, `tropes-migration-status-zh`, `tropes-postmortem-en` |
| TV-30 | EN | test material: global check `trope-title-case`; probed in cases `tropes-exec-summary-en`, `tropes-launch-post-en`, `tropes-readme-en` |
| TV-31 | BOTH | test material: global checks `trope-ornate-words`, `trope-re-ai-vocab`; probed in cases `tropes-design-doc-edit-en`, `tropes-exec-summary-en`, `tropes-recipe-ending-en`, `tropes-release-notes-zh` |
| TV-32 | BOTH | test material: global check `trope-staged-emphasis`; probed in cases `tropes-cache-article-ja`, `tropes-migration-status-zh`, `tropes-postmortem-en` |
| TV-33 | BOTH | test material: global check `trope-anaphora`; probed in cases `tropes-ja-logging-chapter`, `tropes-metrics-essay-en`, `tropes-oss-newsletter-zh` |
| TV-34 | X-DEAI | test material: global check `trope-bold-labels`; probed in cases `tropes-design-doc-edit-en`, `tropes-exec-summary-en`, `tropes-launch-post-en`, `tropes-readme-en`, `tropes-release-notes-zh` |
| TV-35 | BOTH | test material: global check `trope-forced-figures`; probed in cases `tropes-readme-en`, `tropes-tutorial-en` |
| TV-36 | X-DEAI | test material: global check `trope-dash-overuse`; probed in cases `tropes-readme-en` |
| TV-37 | BOTH | test material: global check `trope-borrowed-authority`; probed in cases `tropes-design-doc-edit-en` |
| TV-38 | X-DEAI | test material: global check `trope-inflated-stakes`; probed in cases `tropes-launch-post-en`, `tropes-leaving-essay-ja`, `tropes-oss-newsletter-zh` |
| TV-39 | PERSONAL | test material: global check `trope-false-vulnerability`; probed in cases `tropes-leaving-essay-ja`, `tropes-oss-newsletter-zh`, `tropes-recipe-ending-en` |
| TV-40 | BOTH | test material: global check `trope-padded-series`; probed in cases `tropes-release-notes-zh` |
| TV-41 | BOTH | test material: global check `trope-ornate-words`; probed in cases `tropes-cache-article-ja`, `tropes-readme-en`, `tropes-release-notes-zh` |
| TV-42 | BOTH | test material: global check `trope-repetition`; probed in cases `tropes-leaving-essay-ja` |
| TV-43 | BOTH | test material: global check `trope-repetition`; probed in cases `tropes-cache-article-ja` |
| TV-44 | X-DEAI | test material: global checks `trope-re-ai-vocab`, `trope-ornate-words`; probed in cases `tropes-design-doc-edit-en`, `tropes-readme-en` |
| TV-45 | BOTH | test material: global checks `trope-empty-emphasis`, `trope-re-worth-noting`; probed in cases `tropes-design-doc-edit-en`, `tropes-postmortem-en`, `tropes-release-notes-zh` |
| TV-46 | BOTH | test material: global checks `trope-preamble`, `trope-re-reveal-setups`; probed in cases `tropes-cache-article-ja`, `tropes-ja-logging-chapter`, `tropes-tutorial-en` |
| TV-47 | BOTH | test material: global check `trope-significance-tails`; probed in cases `tropes-metrics-essay-en`, `tropes-readme-en`, `tropes-release-notes-zh` |
| TV-48 | BOTH | test material: global check `trope-inflated-stakes`; probed in cases `tropes-exec-summary-en`, `tropes-launch-post-en`, `tropes-oss-newsletter-zh`, `tropes-release-notes-zh` |
| TV-49 | PERSONAL | test material: global check `trope-restating-close`; probed in cases `tropes-cache-article-ja`, `tropes-ja-logging-chapter`, `tropes-leaving-essay-ja`, `tropes-metrics-essay-en`, `tropes-migration-status-zh`, `tropes-oss-newsletter-zh`, `tropes-recipe-ending-en` |
| TV-50 | X-DEAI | test material; no case that uses its examples survived the case ablation |
| WH-00 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| WH-01 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| WH-R01 | X-DUP | test material: global check `trope-preamble`; probed in cases `tropes-beam-reply-ja` |
| WH-R02 | X-DUP | test material: global check `trope-restating-close` |
| WH-R03 | BOTH | test material in cases `tropes-beam-reply-ja`, `tropes-tutorial-en` |
| WH-R04 | X-DUP | test material: global check `trope-reasoning-leak` |
| WH-R05 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| WH-R06 | BOTH | test material in cases `tropes-tutorial-en` |
| WH-R07 | X-DUP | test material; no case that uses its examples survived the case ablation |
| WH-R08 | BOTH | test material in cases `tropes-beam-reply-ja` |
| WH-R09 | BOTH | test material in cases `tropes-beam-reply-ja`, `tropes-tutorial-en` |
| WH-R10 | TECH | test material in cases `tropes-tutorial-en` |
| WH-R11 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| WH-B00 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| WH-B01 | X-DUP | test material: global check `trope-reasoning-leak`; probed in cases `tropes-partner-request-en` |
| WH-B02 | X-DUP | test material: global check `trope-premise-stacking`; probed in cases `tropes-partner-request-en` |
| WH-B03 | X-DUP | test material: global check `trope-preamble` |
| WH-B04 | X-DUP | test material: global check `trope-compulsive-counting` |
| WH-B05 | X-DUP | test material: global check `trope-phantom-objections` |
| WH-B06 | X-DUP | test material: global check `trope-restating-close` |
| WH-B07 | X-DUP | test material: global check `trope-repetition` |
| WH-B08 | X-DUP | test material: global check `trope-staged-emphasis` |
| WH-B09 | X-DUP | test material: global check `trope-repetition` |
| WH-B10 | X-DUP | test material: global check `trope-restating-close` |
| WH-T00 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| WH-T01 | X-DUP | test material: global check `trope-negative-parallelism` |
| WH-T02 | X-DUP | test material: global check `trope-dash-overuse` |
| WH-T03 | X-DUP | test material: global check `trope-staged-emphasis` |
| WH-T04 | X-DUP | test material: global check `trope-inflated-stakes` |
| WH-T05 | X-DUP | test material: global check `trope-unstable-terms` |
| WH-T06 | X-DUP | test material: global check `trope-padded-series` |
| WH-T07 | X-DUP | test material: global check `trope-empty-emphasis` |
| WH-T08 | X-DUP | test material: global check `trope-borrowed-authority` |
| WH-T09 | X-DUP | test material: global check `trope-self-echo` |
| WH-T10 | X-DUP | test material: global check `trope-staged-emphasis` |
| WH-T11 | X-DUP | test material: global check `trope-forced-figures` |
| WH-T12 | X-DUP | test material: global check `trope-restating-close` |
| WH-T13 | X-DUP | test material: global check `trope-significance-tails` |
| WH-T14 | X-DUP | test material: global check `trope-unstable-terms` |
| WH-T15 | X-DUP | test material: global check `trope-borrowed-authority` |
| WH-T16 | X-DUP | test material: global check `trope-promotional` |
| WH-T17 | X-DUP | test material: global check `trope-heading-teasers` |
| WH-T18 | X-DUP | test material: global check `trope-forced-figures` |
| WH-T19 | X-DUP | test material: global check `trope-vague-we` |
| WH-T20 | X-DUP | test material: global check `trope-negative-parallelism` |
| WH-T21 | X-DUP | test material: global check `trope-re-reveal-setups` |
| WH-T22 | X-DUP | test material: global check `trope-ordinal-prose` |
| WH-T23 | X-DUP | test material: global check `trope-title-case` |
| WH-T24 | X-DUP | test material: global check `trope-ornate-words` |
| WH-T25 | X-DUP | test material: global check `trope-anaphora` |
| WH-T26 | X-DUP | test material: global check `trope-bold-labels` |
| WH-T27 | X-DUP | test material: global check `trope-forced-figures` |
| WH-T28 | X-DUP | test material: global check `trope-dash-overuse` |
| WH-T29 | X-DUP | test material: global check `trope-borrowed-authority` |
| WH-T30 | X-DUP | test material: global check `trope-inflated-stakes` |
| WH-T31 | X-DUP | test material: global check `trope-false-vulnerability` |
| WH-T32 | X-DUP | test material: global check `trope-padded-series` |
| WH-T33 | X-DUP | test material: global check `trope-ornate-words` |
| WH-T34 | X-DUP | test material: global check `trope-repetition` |
| WH-T35 | X-DUP | test material: global check `trope-re-ai-vocab` |
| WH-T36 | X-DUP | test material: global check `trope-re-worth-noting` |
| WH-T37 | X-DUP | test material: global check `trope-re-reveal-setups`; probed in cases `tropes-tutorial-en` |
| WH-T38 | X-DUP | test material: global check `trope-significance-tails` |
| WH-T39 | X-DUP | test material: global check `trope-inflated-stakes` |

## ninehills/skills deslop, deslop-en, deslop-zh (test material only)

Audit: [`audits/deslop.md`](audits/deslop.md).

| Row | Audit destination | Outcome |
|---|---|---|
| DZ-1.1a | BOTH | test material in cases `deslop-zh-tech-k8s-blog` |
| DZ-1.1b | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-1.1c | BOTH | test material; no case that uses its examples survived the case ablation |
| DZ-1.2a | BOTH | test material; no case that uses its examples survived the case ablation |
| DZ-1.2b | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-1.2c | BOTH | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-1.3 | BOTH | test material; no case that uses its examples survived the case ablation |
| DZ-1.4a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-1.4b | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-1.4c | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-1.4d | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-1.4e | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.02 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.03 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.04 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.05 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.06 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.07 | BOTH | test material in cases `deslop-zh-tech-search-article` |
| DZ-2.08 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.09 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.10 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.11 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.12 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.13 | X-DUP | test material in cases `deslop-zh-tech-cache-article`, `deslop-zh-tech-paper-abstract` |
| DZ-2.14 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-2.15 | X-DUP | test material in cases `deslop-zh-pers-market-reply` |
| DZ-2.16 | X-DUP | test material in cases `deslop-zh-tech-arch-note` |
| DZ-3.1 | BOTH | test material in cases `deslop-zh-tech-cache-article`, `deslop-zh-tech-search-article` |
| DZ-3.2 | BOTH | test material in cases `deslop-zh-pers-rewrite-blog` |
| DZ-3.3 | X-DUP | test material in cases `deslop-zh-pers-book-note`, `deslop-zh-tech-cache-article` |
| DZ-3.4 | BOTH | test material in cases `deslop-zh-pers-book-note`, `deslop-zh-tech-cache-article`, `deslop-zh-tech-search-article` |
| DZ-3.5 | PERSONAL | test material in cases `deslop-zh-pers-book-note`, `deslop-zh-pers-rewrite-blog` |
| DZ-3.6 | ZH | test material in cases `deslop-zh-pers-rewrite-blog`, `deslop-zh-tech-k8s-blog` |
| DZ-3.7a | ZH | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-3.7b | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DZ-3.7c | BOTH | test material in cases `deslop-zh-pers-travel-post`, `deslop-zh-tech-paper-abstract` |
| DZ-3.7d | BOTH | test material in cases `deslop-zh-pers-travel-post`, `deslop-zh-tech-paper-abstract` |
| DZ-3.7e | BOTH | test material in cases `deslop-zh-pers-travel-post`, `deslop-zh-tech-api-quickstart` |
| DZ-3.7f | BOTH | test material in cases `deslop-zh-pers-travel-post` |
| DZ-3.7g | BOTH | test material in cases `deslop-zh-pers-travel-post` |
| DZ-3.7h | BOTH | test material in cases `deslop-zh-pers-travel-post`, `deslop-zh-tech-paper-abstract` |
| DZ-3.8a | ZH | test material; no case that uses its examples survived the case ablation |
| DZ-3.8b | ZH | test material in cases `deslop-zh-tech-k8s-blog` |
| DZ-3.8c | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-3.8d | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DZ-3.8e | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DZ-3.8f | ZH | test material in cases `deslop-zh-tech-k8s-blog` |
| DZ-3.8g | ZH | test material; no case that uses its examples survived the case ablation |
| DZ-3.9a | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DZ-3.9b | X-DEAI | test material in cases `deslop-zh-tech-ops-note` |
| DZ-3.9c | TECH | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-3.9d | ZH | test material in cases `deslop-zh-tech-ops-note` |
| DZ-3.9e | ZH | test material in cases `deslop-zh-tech-ops-note` |
| DZ-3.10a | ZH | test material; no case that uses its examples survived the case ablation |
| DZ-3.10b | ZH | test material; no case that uses its examples survived the case ablation |
| DZ-3.10c | X-DUP | test material in cases `deslop-zh-tech-api-quickstart`, `deslop-zh-tech-ops-note` |
| DZ-3.11a | ZH/TECH | test material; no case that uses its examples survived the case ablation |
| DZ-3.11b | BOTH | test material in cases `deslop-zh-tech-search-article` |
| DZ-3.12a | BOTH | test material in cases `deslop-zh-pers-reply-comments`, `deslop-zh-tech-cache-article` |
| DZ-3.12b | BOTH | test material in cases `deslop-zh-tech-search-article` |
| DZ-3.13 | BOTH | test material in cases `deslop-zh-tech-cache-article` |
| DZ-3.14a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-3.14b | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DZ-3.14c | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-3.14d | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DZ-4.1a | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-4.1b | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.1c | BOTH | test material in cases `deslop-zh-tech-api-quickstart`, `deslop-zh-tech-k8s-blog` |
| DZ-4.1d | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.1e | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.1f | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.1g | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.1h | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.1i | TECH | test material in cases `deslop-zh-tech-search-article` |
| DZ-4.1j | TECH | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-4.1k | TECH | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-4.2a | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-4.2b | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.2c | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-4.2d | ZH | test material in cases `deslop-zh-pers-rewrite-blog`, `deslop-zh-tech-search-article` |
| DZ-4.2e | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.2f | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.2g | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.2h | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.2i | BOTH | test material in cases `deslop-zh-tech-search-article` |
| DZ-4.3a | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.3b | PERSONAL | test material; no case that uses its examples survived the case ablation |
| DZ-4.3c | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.3d | PERSONAL | test material; no case that uses its examples survived the case ablation |
| DZ-4.3e | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.3f | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.3g | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.3h | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.3i | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.4a | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-4.4b | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-4.4c | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-4.4d | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.4e | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DZ-4.4f | BOTH | test material; no case that uses its examples survived the case ablation |
| DZ-4.4g | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.5a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.5b | X-DUP | test material in cases `deslop-zh-tech-paper-abstract` |
| DZ-4.5c | X-DUP | test material in cases `deslop-zh-tech-paper-abstract` |
| DZ-4.5d | X-DUP | test material in cases `deslop-zh-tech-paper-abstract` |
| DZ-4.5e | BOTH | test material in cases `deslop-zh-tech-paper-abstract` |
| DZ-4.5f | X-DUP | test material in cases `deslop-zh-tech-k8s-blog` |
| DZ-4.5g | X-DUP | test material in cases `deslop-zh-tech-paper-abstract` |
| DZ-4.5h | X-DUP | test material in cases `deslop-zh-tech-paper-abstract` |
| DZ-4.6a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.6b | ZH | test material in cases `deslop-zh-tech-ops-note` |
| DZ-4.6c | BOTH | test material; no case that uses its examples survived the case ablation |
| DZ-4.6d | TECH | test material; no case that uses its examples survived the case ablation |
| DZ-4.6e | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-4.6f | ZH | test material in cases `deslop-zh-tech-search-article` |
| DZ-4.6g | ZH | test material in cases `deslop-zh-tech-search-article` |
| DZ-4.6h | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-4.6i | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.02 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.03 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.04 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.05 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.06 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.07 | ZH | test material; no case that uses its examples survived the case ablation |
| DZ-5.08 | ZH | test material; no case that uses its examples survived the case ablation |
| DZ-5.09 | ZH | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-5.10 | X-DUP | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-5.11 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.12 | X-DUP | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-5.13 | X-DUP | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-5.14 | X-DUP | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-5.15 | X-DUP | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-5.16 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.17 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.18 | X-DUP | test material in cases `deslop-zh-tech-paper-abstract` |
| DZ-5.19 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-5.20 | ZH | test material in cases `deslop-zh-pers-travel-post` |
| DZ-5.21 | ZH | test material; no case that uses its examples survived the case ablation |
| DZ-6.1 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-6.2 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-6.3 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-6.4 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-6.5 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-6.6 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-7.1 | X-DUP | test material in cases `deslop-zh-tech-k8s-blog` |
| DZ-7.2 | X-DUP | test material in cases `deslop-zh-tech-api-quickstart` |
| DZ-7.3 | X-DUP | test material in cases `deslop-zh-tech-arch-note` |
| DZ-7.4 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DZ-8 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DZ-9 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DE-C1 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-C2 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-C3 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-C4 | BOTH | test material; no case that uses its examples survived the case ablation |
| DE-Q01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q02 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q03 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q04 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q05 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q06 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q07 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q08 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q09 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q10 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q11 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q12 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q13 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-Q14 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-P01 | X-DUP | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-tech-outbox-blog` |
| DE-P02a | X-DUP | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-pers-travel-post`, `deslop-en-tech-readme`, `deslop-pers-reproducibility-essay` |
| DE-P02b | X-DUP | test material in cases `deslop-en-tech-abstract` |
| DE-P03 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-P04 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-P05 | X-DUP | test material in cases `deslop-en-tech-outbox-blog` |
| DE-P06 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DE-P07 | BOTH | test material in cases `deslop-en-pers-pipelines` |
| DE-P08 | X-DEAI | test material in cases `deslop-en-pers-newsletter-api` |
| DE-P09 | BOTH | test material in cases `deslop-en-pers-pipelines` |
| DE-P10 | BOTH | test material in cases `deslop-en-pers-newsletter-api` |
| DE-P11 | X-DUP | test material in cases `deslop-en-tech-outbox-blog` |
| DE-P12 | EN | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-abstract` |
| DE-P13 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-P14 | BOTH | test material in cases `deslop-en-tech-outbox-blog`, `deslop-en-tech-readme`, `deslop-pers-reproducibility-essay` |
| DE-P15 | BOTH | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-abstract`, `deslop-en-tech-cover-letter` |
| DE-P16 | BOTH | test material in cases `deslop-en-pers-newsletter-api` |
| DE-P17 | BOTH | test material in cases `deslop-en-pers-newsletter-api` |
| DE-P18 | BOTH | test material in cases `deslop-en-pers-newsletter-api` |
| DE-P19 | X-DUP | test material in cases `deslop-en-pers-pipelines`, `deslop-en-pers-travel-post`, `deslop-pers-reproducibility-essay` |
| DE-P20 | X-DUP | test material in cases `deslop-en-pers-travel-post` |
| DE-P21 | PERSONAL | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-pers-pipelines`, `deslop-pers-reproducibility-essay` |
| DE-P22 | BOTH | test material in cases `deslop-en-tech-outbox-blog` |
| DE-P23 | BOTH | test material in cases `deslop-en-tech-outbox-blog`, `deslop-en-tech-readme` |
| DE-P24 | BOTH | test material in cases `deslop-en-tech-readme` |
| DE-P25 | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DE-G01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G02 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DE-G03 | BOTH | test material in cases `deslop-pers-reproducibility-essay` |
| DE-G04 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G05 | X-DUP | test material in cases `deslop-en-tech-discussion` |
| DE-G06 | X-DUP | test material in cases `deslop-sci-grant-aims` |
| DE-G07 | X-DUP | test material in cases `deslop-en-tech-discussion` |
| DE-G08 | X-DUP | test material in cases `deslop-en-tech-discussion`, `deslop-sci-grant-aims` |
| DE-G09 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G10 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G11 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G12 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G13 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G14 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G15 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G16 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-G17 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-V01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-V02 | X-DUP | test material in cases `deslop-en-pers-travel-post` |
| DE-V03 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V04 | EN | test material; no case that uses its examples survived the case ablation |
| DE-V05 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V06 | X-DUP | test material in cases `deslop-en-pers-travel-post` |
| DE-V07 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-V08 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-V09 | EN | test material in cases `deslop-en-tech-discussion` |
| DE-V10 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V11 | EN | test material in cases `deslop-sci-grant-aims` |
| DE-V12 | EN | test material; no case that uses its examples survived the case ablation |
| DE-V13 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V14 | X-DUP | test material in cases `deslop-en-tech-readme`, `deslop-sci-grant-aims` |
| DE-V15 | EN | test material in cases `deslop-en-pers-travel-post` |
| DE-V16 | EN | test material in cases `deslop-sci-grant-aims` |
| DE-V17 | EN | test material in cases `deslop-en-pers-travel-post` |
| DE-V18 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V19 | EN | test material in cases `deslop-en-tech-abstract` |
| DE-V20 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V21 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V22 | EN | test material; no case that uses its examples survived the case ablation |
| DE-V23 | EN | test material in cases `deslop-en-tech-python-glossary`, `deslop-en-tech-readme` |
| DE-V24 | EN | test material; no case that uses its examples survived the case ablation |
| DE-V25 | EN | test material in cases `deslop-en-tech-readme` |
| DE-V26 | EN | test material; no case that uses its examples survived the case ablation |
| DE-H1 | EN | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-discussion` |
| DE-H2 | EN | test material in cases `deslop-en-pers-travel-post`, `deslop-sci-grant-aims` |
| DE-H3 | X-DUP | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-readme` |
| DE-H4 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-H5 | X-DUP | test material in cases `deslop-en-tech-cover-letter`, `deslop-en-tech-discussion`, `deslop-en-tech-outbox-blog`, `deslop-en-tech-readme` |
| DE-X1 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DE-X2 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-X3 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DE-X4 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DE-X5 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DE-X6 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DE-E1 | X-DUP | test material in cases `deslop-en-tech-outbox-blog` |
| DE-E2 | X-DUP | test material in cases `deslop-en-tech-abstract` |
| DE-E3 | X-DUP | test material in cases `deslop-en-tech-cover-letter` |
| DE-E4 | X-DUP | test material in cases `deslop-sci-grant-aims` |
| DE-S1 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DE-R1 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DS-W1 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DS-C1 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C2 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C3 | X-DUP | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-abstract`, `deslop-en-tech-discussion` |
| DS-C4 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C5a | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-C5b | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-C5c | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-C5d | TECH | test material in cases `deslop-en-tech-discussion`, `deslop-sci-grant-aims` |
| DS-C6a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C6b | X-DUP | test material in cases `deslop-sci-grant-aims` |
| DS-C7a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C7b | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C7c | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C7d | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C7e | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C7f | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C8a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C8b | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C8c | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C9 | X-DUP | test material in cases `deslop-en-tech-discussion`, `deslop-en-tech-readme` |
| DS-C10a | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C10b | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-C10c | X-DUP | test material in cases `deslop-en-pers-newsletter-api` |
| DS-Q01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q02 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q03 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q04 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q05 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q06 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q07 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q08 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q09 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q10 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q11 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q12 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q13 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q14 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q15 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q16 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-Q17 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-S1 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DS-R1 | X-SCOPE | test material; no case that uses its examples survived the case ablation |
| DS-E0a | X-DUP | test material in cases `deslop-en-tech-cover-letter` |
| DS-E0b | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-ST01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST02 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST03 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST04 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST05 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST06 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST07 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST08 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST09 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST10 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST11 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST12 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST13 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST14 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-ST15 | X-DEAI | test material in cases `deslop-en-tech-readme` |
| DS-ST16 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST17 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST18 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST19 | X-DUP | test material in cases `deslop-en-pers-newsletter-api` |
| DS-ST20 | X-DUP | test material in cases `deslop-en-pers-newsletter-api` |
| DS-ST21 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-ST22 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-ST23 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST24 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST25 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST26 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST27 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-ST28 | X-DUP | test material in cases `deslop-en-pers-newsletter-api` |
| DS-ST29 | X-DUP | test material in cases `deslop-en-pers-newsletter-api` |
| DS-ST30 | X-DUP | test material in cases `deslop-en-pers-newsletter-api` |
| DS-ST31 | BOTH | test material in cases `deslop-en-pers-newsletter-api` |
| DS-ST32 | X-DUP | test material in cases `deslop-en-tech-readme` |
| DS-ST33 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST34 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST35 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST36 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST37 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST38 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST39 | X-DUP | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-tech-discussion` |
| DS-ST40 | X-DUP | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-discussion` |
| DS-ST41 | X-DUP | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-pers-travel-post`, `deslop-en-tech-python-glossary` |
| DS-ST42 | BOTH | test material in cases `deslop-en-pers-newsletter-api` |
| DS-ST43 | X-DUP | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-discussion` |
| DS-ST44 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST45 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST46 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST47 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST48 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST49 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST50 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST51 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST52 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST53 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST54 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST55 | X-DUP | test material in cases `deslop-en-tech-readme` |
| DS-ST56 | X-DEAI | test material in cases `deslop-en-tech-readme` |
| DS-ST57 | X-DEAI | test material; no case that uses its examples survived the case ablation |
| DS-ST58 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST59 | BOTH | test material in cases `deslop-en-tech-discussion` |
| DS-ST60 | X-DUP | test material in cases `deslop-pers-reproducibility-essay` |
| DS-ST61 | BOTH | test material; no case that uses its examples survived the case ablation |
| DS-ST62 | BOTH | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-pers-pipelines` |
| DS-ST63 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-ST64 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-P01 | X-DUP | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-pers-pipelines`, `deslop-en-tech-outbox-blog`, `deslop-en-tech-reply-issue` |
| DS-P02 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-P03 | X-DUP | test material in cases `deslop-en-tech-discussion`, `deslop-en-tech-outbox-blog`, `deslop-en-tech-readme`, `deslop-pers-reproducibility-essay` |
| DS-P04 | X-DUP | test material in cases `deslop-en-tech-cover-letter`, `deslop-en-tech-readme`, `deslop-sci-grant-aims` |
| DS-P05 | EN | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-discussion`, `deslop-en-tech-readme`, `deslop-sci-grant-aims` |
| DS-P06 | X-DUP | test material in cases `deslop-en-tech-abstract` |
| DS-P07 | X-DUP | test material in cases `deslop-en-pers-travel-post`, `deslop-en-tech-readme`, `deslop-pers-reproducibility-essay` |
| DS-P08 | X-DUP | test material in cases `deslop-en-tech-abstract` |
| DS-P09 | X-DUP | test material in cases `deslop-en-tech-cover-letter`, `deslop-en-tech-discussion`, `deslop-en-tech-outbox-blog`, `deslop-en-tech-reply-issue`, `deslop-pers-reproducibility-essay` |
| DS-P10 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-P11 | X-DUP | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-pers-pipelines`, `deslop-pers-reproducibility-essay` |
| DS-P12 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-P13 | BOTH | test material in cases `deslop-en-pers-newsletter-api`, `deslop-pers-reproducibility-essay` |
| DS-P14 | X-DUP | test material in cases `deslop-en-pers-pipelines`, `deslop-en-tech-outbox-blog` |
| DS-P15 | X-DUP | test material in cases `deslop-en-pers-newsletter-api`, `deslop-en-pers-pipelines`, `deslop-en-pers-travel-post` |
| DS-P16 | X-DUP | test material in cases `deslop-en-tech-readme`, `deslop-sci-grant-aims` |
| DS-EX01 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-EX02 | X-DUP | test material in cases `deslop-en-tech-cover-letter` |
| DS-EX03 | X-DUP | test material in cases `deslop-sci-grant-aims` |
| DS-EX04 | X-DUP | test material in cases `deslop-en-tech-discussion` |
| DS-EX05 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-EX06 | X-DUP | test material in cases `deslop-en-tech-abstract` |
| DS-EX07 | X-DUP | test material in cases `deslop-en-pers-pipelines` |
| DS-EX08 | X-DUP | test material in cases `deslop-en-tech-discussion` |
| DS-EX09 | X-DUP | test material in cases `deslop-pers-reproducibility-essay` |
| DS-EX10 | X-DUP | test material in cases `deslop-en-pers-newsletter-api` |
| DS-EX11 | X-DUP | test material in cases `deslop-sci-grant-aims` |
| DS-EX12 | X-DUP | test material; no case that uses its examples survived the case ablation |
| DS-EX13 | X-DUP | test material in cases `deslop-pers-reproducibility-essay` |
| DS-EX14 | X-DUP | test material in cases `deslop-en-tech-discussion` |
| DS-EX15 | X-DUP | test material; no case that uses its examples survived the case ablation |
