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
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1380716549), revision 1380716549, CC BY-SA 4.0.

## Rules

- Write the short English form of a wordy phrase: "to", not "in order to"; "because", not "due to the fact that"; "if", not "in the event that"; "can", not "has the ability to"; "now", not "at this point in time". Cut padding nouns such as "case", "nature", "character", "factor" and "system" when the sentence says the same without them ("many of the rooms", not "in many cases, the rooms"), and keep them in terms of art ("test case", "edge case", "two-factor", "build system"). <!-- r:en.plain-words -->
- Follow the house style for hyphens. If there is none, hyphenate a compound modifier before a noun ("a real-time dashboard", "up-to-date docs") and leave it open in other positions ("updates in real time", "the docs are up to date"), unless Merriam-Webster hyphenates the word in every position ("cross-functional"). Leave a compound with an -ly adverb open: "a widely used flag". <!-- r:en.hyphenation -->
- In running text, write full sentences with their articles, verbs and subjects: "Restart the service after you change the config", not "Restart service after config change". Join a phrase that only continues the sentence before it with a comma, not a period. Keep the short forms that a format sets (headings, list items, labels, table cells, commit subjects, log and error strings, CLI help lines), and keep a short emphatic sentence such as "No reply." if it cannot be read as the end of the sentence before it. <!-- r:en.complete-sentences -->
- Write headings in the case that the house style or the existing document uses. If neither sets one, use sentence case: capitalize only the first word and proper nouns, as in "Restore a Postgres backup". <!-- r:en.heading-case -->
- In technical text, if more than three nouns stand in a row, unpack the cluster with a preposition or a clause and keep what modifies what: "the timeout for database connection retries", not "the database connection retry timeout". Keep a cluster that is a name in the product, API or UI, such as the name of a setting. <!-- r:en.noun-clusters -->
- In technical text, keep a procedural sentence to 20 words or fewer and a descriptive sentence to 25 words or fewer, and do not count code, commands, paths or identifiers. If splitting a long sentence would repeat a noun phrase or drop a link such as "because", "while", "so" or "unless", shorten it by cutting words instead. <!-- r:en.sentence-length -->
- Form the possessive of a singular noun the way the house style does; if there is none, add 's even after a final s: "Charles's", "the class's". Write the possessive pronouns "its", "hers", "theirs" and "yours" without an apostrophe; "it's" means only "it is" or "it has". <!-- r:en.usage-reference -->
