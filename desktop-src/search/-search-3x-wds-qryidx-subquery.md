---
description: A subquery is a saved search file (\*.search-ms) that you can use as a filter for a new query.
ms.assetid: a92c774f-310b-4c40-be1c-0c2b0cac907b
title: SUBQUERY Argument (Windows Search)
ms.topic: article
ms.date: 05/31/2018
---

# SUBQUERY Argument (Windows Search)

A subquery is a saved search file (\*.search-ms) that you can use as a filter for a new query. The results of the subquery are used as the source for the new query. For example, let's say you have several saved search files that restrict a query by email distribution list: mydepartment.search-ms, teamproject.search-ms, and corporatewide.search-ms. Using the `subquery` argument enables you to limit email searches to any or all of these saved searches.

This topic is organized as follows:

-   [Example](#example)
-   [Related topics](#related-topics)

## Example


```
 search-ms:query=vacation&subquery=mydepartment.search-ms
```



## Related topics

<dl> <dt>

[Getting Started with Parameter-Value Arguments](getting-started-with-parameter-value-arguments.md)
</dt> <dt>

[Locale Identifier Arguments](-search-3x-wds-qryidx-localeidentifiers.md)
</dt> <dt>

[CRUMB Argument](-search-3x-wds-qryidx-crumb.md)
</dt> <dt>

[SYNTAX Argument](-search-3x-wds-qryidx-syntaxargument.md)
</dt> <dt>

[STACKEDBY Argument](-search-3x-wds-qryidx-stackedby.md)
</dt> </dl>

 

 



