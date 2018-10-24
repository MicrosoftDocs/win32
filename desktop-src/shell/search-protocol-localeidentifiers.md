---
Description: The inputlocale and keywordlocale identifiers help the search engine use the correct word breakers by identifying the language of user-entered queries and the language the of Advanced Query Syntax keywords.
title: Locale Identifier Arguments
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Locale Identifier Arguments

The `inputlocale` and `keywordlocale` identifiers help the search engine use the correct word breakers by identifying the language of user-entered queries and the language the of Advanced Query Syntax keywords. These are not always the same language code identifiers (LCIDs) because Windows Search is offered in a number of international versions and also includes Multilingual User Interface (MUI) packs for more languages. The `inputlocale` identifies the LCID for the language users input their search query in, while the `keywordlocale` identifies the LCID the search engine uses for keywords.

## Example


```
search:query=matthew&inputlocale=2072&keywordlocale=1033
```



### Argument Information



|                          |                                         |
|--------------------------|-----------------------------------------|
| Minimum Operating System | Windows Vista with Service Pack 1 (SP1) |



 

 

 



