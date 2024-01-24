---
description: You can specify the language used in search queries.
ms.assetid: 3a7ecf8f-38ae-41d1-be70-e9ab23977a01
title: Specifying Languages
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Languages

You can specify the language used in search queries. Both the FREETEXT and CONTAINS predicates in the WHERE clause support specifying a language. You can indicate the query language by providing a numeric language code identifier (LCID) in the CONTAINS or FREETEXT predicate. This LCID specifies which word breaker to use to parse the query string. It uses the following syntax:


```
CONTAINS | FREETEXT
([<column_identifier>,]'<content_search_condition>' [,LCID]) 
```



For more information, see the syntax for the [CONTAINS](-search-sql-contains.md) and [FREETEXT](-search-sql-freetext.md) predicates.

 

 



