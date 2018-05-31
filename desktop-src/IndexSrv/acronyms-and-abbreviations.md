---
title: Acronyms and Abbreviations
description: Acronyms and Abbreviations
ms.assetid: e2bce6b5-6011-4ebe-b2a6-251e9de9b079
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Acronyms and Abbreviations

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Acronyms and abbreviations merit consideration when you implement a word breaker. In many languages, individual letters of acronyms are separated by periods. Occasionally, words that are not recognized acronyms or abbreviations are abbreviated. For example, "United States of America" may be abbreviated as either "USA" or "U.S.A." Word breakers included with Indexing Service usually identify single-letter words as noise words and treat those words as placeholders during query time. During query time, a word breaker that is not aware of common acronyms, or that does not recognize abbreviations, converts the abbreviation "U.S.A." into "U," "S," and "A." This decomposition does not provide enough information to match words in the full-text index because all the query terms are noise words. When you create a word breaker, it is recommended that the word breaker remove the periods that separate the letters of acronyms. In the example, "U.S.A." is stored as "USA" and a query term that contains "U.S.A." actually queries for "USA." If a word breaker processes an abbreviation, the period in that abbreviation is not treated as an EOS break. Because of this, a word breaker might not correctly identify an EOS break if the abbreviation is at the end of the sentence.

 

 




