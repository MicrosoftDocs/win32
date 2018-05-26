---
title: Hyphenation
description: Hyphenation
ms.assetid: 4bc6673d-6fd4-4f70-a669-bf6c5bbd6596
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Hyphenation

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Hyphens (-) are used between the parts of a compound word or name. They are also used between the syllables of a word when the word is divided at the end of a line of text. In English, words are joined with hyphens to indicate a special relationship in context, but those words may not normally be hyphenated in other contexts—for example, "step-by-step." During index creation, the word breaker should treat the hyphen as a word separator. For example, "data-base" would be stored as "data" plus "base." At query time, a hyphenated phrase should be replaced with two alternatives: the two-word variant and the true compound. For example, "data-base" would be replaced by "data" plus "base" and "database." This difference between index and query time increases the combinations of representations for hyphenated words and makes the words easier to match in a query.

The following table shows how treating hyphens as word separators in the English language increases the number of matched query terms for each term included in the index.



| Terms included in the index | Query-time matches   |
|-----------------------------|----------------------|
| Data base                   | data base, data-base |
| Data-base                   | data base, data-base |
| Database                    | data-base, database  |



 

Treating the hyphen as a word separator may be an ineffective strategy in languages other than English. For example, in French, hyphens are used both as word separators and as [clitics](clitics.md), usually with verbs. In this case, it is not advantageous to break words on hyphens because it is difficult for the word breaker to determine which hyphens are used as clitics and which are used as word separators. Therefore, the word breaker is unable to generate both the base and the full form of the word.

 

 




