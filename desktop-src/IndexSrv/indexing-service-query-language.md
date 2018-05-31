---
title: Indexing Service Query Language
description: Indexing Service Query Language
ms.assetid: 86151e29-0c08-41fe-a33a-9d9bc4fef749
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Indexing Service Query Language

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

New in Indexing Service 3.0 is the extensible Dialect 2 of the Indexing Service query language. Its short form contains as a subset — with a few incompatibilities — the syntax of the original Indexing Service query language, now called Dialect 1. Except for the few incompatibilities, Dialect 2 processes queries written in both its long form and its short form (Dialect 1 subset). Most applications and scripts will specify Indexing Service query language queries in Dialect 2. For compatibility with earlier releases, applications and scripts can submit a query written in Dialect 1 and specify that Indexing Service process it as a Dialect 1 query. An alternative to the Indexing Service query language is the [SQL query language](sql-query-language.md).

This section describes several features of the Indexing Service query language. It consists of the following topics.

-   [Query Submittal for Indexing Service Query Language](query-submittal-for-indexing-service-query-language.md)
-   [Query Syntax of Indexing Service Query Language](query-syntax-of-indexing-service-query-language.md)
-   [Content Queries](content-queries.md)
-   [CONTAINS Operator](contains-operator.md)
-   [Boolean and Proximity Operators](boolean-and-proximity-operators.md)
-   [Property-Value Queries](property-value-queries.md)
-   [Relational Queries](relational-queries.md)
-   [Pattern-Matching Queries](pattern-matching-queries.md)
-   [Term Weighting](term-weighting.md)
-   [Vector-Space Queries](vector-space-queries.md)
-   [Incompatibilities of Dialect 2 with Dialect 1](incompatibilities-of-dialect-2-with-dialect-1.md)

For a reference to the Indexing Service query language, see [Query-Language Dialects](query-language-dialects.md).

 

 




