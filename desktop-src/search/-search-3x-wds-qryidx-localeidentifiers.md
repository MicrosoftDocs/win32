---
description: The inputlocale and keywordlocale identifiers help the search engine use the correct word breakers by identifying the language of user-entered queries and the language the of Advanced Query Syntax keywords.
ms.assetid: dc610f49-5106-47f9-b29b-84949dd2c42b
title: Locale Identifier Arguments (Windows Search)
ms.topic: article
ms.date: 05/31/2018
---

# Locale Identifier Arguments (Windows Search)

The `inputlocale` and `keywordlocale` identifiers help the search engine use the correct word breakers by identifying the language of user-entered queries and the language the of Advanced Query Syntax keywords. These are not always the same language code identifiers (LCIDs) because Windows Search is offered in a number of international versions and also includes MUI packs for more languages. The inputlocale identifies the LCID for the language users input their search query in, while the keywordlocale identifies the LCID the search engine uses for keywords.

This topic is organized as follows:

-   [Example](#example)
-   [Related topics](#related-topics)

## Example


```
 search-ms:query=matthew&inputlocale=2072&keywordlocale=1033
```



## Related topics

<dl> <dt>

[Getting Started with Parameter-Value Arguments](getting-started-with-parameter-value-arguments.md)
</dt> <dt>

[CRUMB Argument](-search-3x-wds-qryidx-crumb.md)
</dt> <dt>

[SYNTAX Argument](-search-3x-wds-qryidx-syntaxargument.md)
</dt> <dt>

[STACKEDBY Argument](-search-3x-wds-qryidx-stackedby.md)
</dt> <dt>

[SUBQUERY Argument](-search-3x-wds-qryidx-subquery.md)
</dt> </dl>

 

 



