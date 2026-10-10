---
name: writing-en
description: "Use when writing or editing English text, together with writing-tech or writing-personal. Covers English grammar, word choice and hyphenation."
---

# Writing English

These rules hold only for English. Use them together with `writing-tech` or `writing-personal`.

## Sources

- ASD-STE100 Simplified Technical English, Issue 9 (2025-01-15). The writing rules are paraphrased; the STE dictionary is not included, so text written with this skill is not certified STE.
- [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style) @ `05fc4f0d2b97b7c042dd9949ad658568e4a1324e`: William Strunk Jr., *The Elements of Style* (1918), Project Gutenberg #37134, public domain.
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) @ `f4518a8eab97b8bfebc66a89d34320a89bef6930`, MIT.
- [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 @ `8c307f367c91bd974002f10f2be2965d642c13df`, MIT.

## Rules

- Write the short English form of a wordy phrase: "to", not "in order to"; "because", not "due to the fact that"; "if", not "in the event that"; "can", not "has the ability to"; "now", not "at this point in time". Cut padding nouns such as "case", "nature", "character", "factor" and "system" when the sentence says the same without them ("many of the rooms", not "in many cases, the rooms"), and keep them in terms of art ("test case", "edge case", "two-factor", "build system"). <!-- r:en.plain-words -->
- Follow the house style for hyphens. If there is none, hyphenate a compound modifier before a noun ("a real-time dashboard", "up-to-date docs") and leave it open in other positions ("updates in real time", "the docs are up to date"), unless Merriam-Webster hyphenates the word in every position ("cross-functional"). Leave a compound with an -ly adverb open: "a widely used flag". <!-- r:en.hyphenation -->
- In requirements and specs, write "may" for a permission and "can" for a capability: "Clients may cache the response for 60 seconds" grants permission; "can cache" would only say that they are able to. Write "must" for a requirement, not "shall" or "will", unless the document follows a standard that defines "shall" (ISO) or RFC 2119 capitals. <!-- r:en.spec-modals -->
