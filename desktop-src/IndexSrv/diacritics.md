---
title: Diacritics
description: Diacritics
ms.assetid: '20884efe-d2dd-4ec8-afe1-f76f336061c5'
---

# Diacritics

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Diacritics are marks added to a letter or phoneme to indicate a special phonetic value. Diacritics can distinguish words that are otherwise graphically identical—for example, "resume" and "résumé" in English. However, saving diacritics to the index increases the number of unique word keys in the index, which has a negative affect on query performance. If diacritics are used only minimally in a language, the word breaker for that language should remove them during both index creation and querying. For example, the English word breaker generates "resume" when processing "résumé," causing only minimal impact on the relevance of the query results.

Some languages, such as German, have alternative spellings for words that contain diacritical markings. For example, "ö" can be represented as "oe," and "ü" can be represented as "ue." During index creation, the word breaker generates the word as it appears in the source text. For example, "über" is stored as "über" in the index. When you create a word breaker, it is recommended that at query time, you ensure that the word breaker generates the alternate spellings "über" and "ueber." The word breaker must employ language heuristics to determine whether to perform the inverse action. In this example, the word breaker determines whether to generate "ü" when it encounters "ue."

 

 




