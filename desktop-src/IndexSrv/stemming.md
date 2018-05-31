---
title: Stemming
description: Stemming
ms.assetid: 19675a8c-dea5-43eb-b9cd-004ea7ac7035
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stemming

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service applies stemmers exclusively at query time to generate additional word forms for terms in FREETEXT and property queries. Stemmers perform morphological analysis and apply grammatical rules to generate a list of alternative, or inflected, forms for words. Alternative forms often have the same stem or base form. By generating the inflected forms for a word, Indexing Service returns query results that are statistically more relevant to a query. For example, a full-text query for "swim meet" matches documents that contain "swim, swim's, swims, swims', swimming, swam, swum" or "meet, meet's, meets, meets', meeting, met" and combinations of these terms.

Some languages require that inflected terms be generated at both index time and query time for both standard and variant inflections. In this case, stemming happens with the word breaker component, with minimal stemming work in the actual stemmer. For example, the Japanese word breaker performs stemming during both index creation and querying to enable a query to find different inflected forms of the search terms.

The following table shows some of the stemming functionality that the Japanese word breaker performs during index creation and querying.



| Japanese term                                | Inflected form or forms                                |
|----------------------------------------------|--------------------------------------------------------|
| ???????? ("to change sides")                 | ?????????? ("to change one's expression")              |
| ?????????? ("investigation," "inspection")   | ?????????? ("to investigate," "special investigation") |
| ???? ("to buy," inflected verb or adjective) | ?? ("to buy"), ??? ("to buy," inflected)               |



 

 

 




