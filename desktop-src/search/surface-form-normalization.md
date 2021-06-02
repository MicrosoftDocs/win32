---
description: Although words and linguistic rules differ dramatically, there are some considerations, such as numbers, dates, and times, that are handled consistently across all word breakers.
ms.assetid: 62545566-f0ba-4876-93da-e6c2b9c23484
title: Surface Form Normalization
ms.topic: article
ms.date: 05/31/2018
---

# Surface Form Normalization

Although words and linguistic rules differ dramatically, there are some considerations, such as numbers, dates, and times, that are handled consistently across all word breakers. This topic documents normalization considerations that may affect your word breaker implementation.

This topic is organized as follows:

-   [Hyphenation](#hyphenation)
-   [Possessives](#possessives)
-   [Diacritics](#diacritics)
-   [Clitics](#clitics)

## Hyphenation

Hyphens (-) are used between the parts of a compound word or name. They are also used between the syllables of a word when the word is divided at the end of a line of text. In English, words are joined with hyphens to indicate a special relationship in context, but those words may not normally be hyphenated in other contexts; for example, "step-by-step." During index creation, the word breaker should treat the hyphen as a word separator. For example, "data-base" would be stored as "data" plus "base." At query time, a hyphenated phrase should be replaced with two alternatives: the two-word variant and the true compound. For example, "data-base" would be replaced by "data" plus "base" and "database." This difference between index and query time increases the combinations of representations for hyphenated words and makes the words easier to match in a query.

The following table shows how treating hyphens as word separators in the English language increases the number of matched query terms for each term included in the index.



| Terms included in the index | Query-time matches   |
|-----------------------------|----------------------|
| Data base                   | data base, data-base |
| Data-base                   | data base, data-base |
| Database                    | data-base, database  |



 

## Possessives

Possessives are variations in a noun that indicate possession. English possessives are represented by appending an apostrophe (') or an apostrophe and an s ('s) to a word. For example, to indicate possession, the word "Mary" is represented as "Mary's." The word breaker generates both the apostrophe and the apostrophe-s forms at query time. Queries for "Mary" should match both "Mary" and "Mary's."

## Diacritics

Diacritics are marks added to a letter or phoneme to indicate a special phonetic value for pronunciation. Diacritics can distinguish words that are otherwise graphically identical; for example, "resume" and "resumé" in English. However, saving diacritics to the index increases the number of unique word keys in the index, which slows down query performance. If diacritics are used only minimally in a language, the word breaker for that language should remove them during both index creation and querying. For example, the English word breaker generates "resume" when processing "resumé," causing only minimal impact on the relevance of the query results.

## Clitics

A clitic is an unstressed word that is incapable of standing on its own and attaches to a stressed word to form a single unit. Clitics cannot be easily classified as phonological, syntactic, or morphological. Clitics come in two types: *proclitics* and *enclitics*. Proclitics attach themselves to the beginning of a word. Enclitics attach themselves to the end of a word.

Clitics are more difficult to parse in languages such as Spanish. A Spanish verb may generate many surface forms, depending on the tense. Considerations must be made between removing the clitic during index creation and generating the surface forms through stemming at query time. Removing clitics in cases where the morphology of clitic composition is ambiguous can lead to unpredictable results. Generating a large number of surface forms for a word increases the size of the full-text index and may slow down query performance. It is recommended that the stemmer generate only a small number of surface forms.

 

 



