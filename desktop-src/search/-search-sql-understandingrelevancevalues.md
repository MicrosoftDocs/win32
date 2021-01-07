---
description: In a relational database, rows that are returned by a search query must meet all the conditions called for by the query. In contrast, a Windows Search query can return documents that meet the search conditions to varying degrees.
ms.assetid: 9f37b494-9b7a-45a6-9ee4-6d582742cbd7
title: Understanding Relevance Values
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Relevance Values

In a relational database, rows that are returned by a search query must meet all the conditions called for by the query. In contrast, a Windows Search query can return documents that meet the search conditions to varying degrees.

For example, a search for the term "program" in a relational database produces records that contain that specific spelling of the word. Whether a record contains one or one hundred instances of the word has no impact on the results. In contrast, Windows Search returns a relevance value associated with the matching documents. The relevance of documents having "program" in the title is higher than those that contain the word only in the last paragraph. Similarly, documents containing variations of the search term, for example "programs" and "programming" also match and are returned by the query.

Windows Search queries return integer relevance values in the column named "rank".

In addition:

-   Rank values returned by the query are integers ranging from 0 to 1000.
-   Higher rank values indicate documents that better match the search conditions.
-   Rank values apply only to the current query, so they cannot be compared for results across queries.
-   Rank values are relative to the other documents matching the query. Therefore, the rank value of a particular document depends on the other documents that also match the query.
-   Rank values for items matching a purely relational predicate are 1000.

You can manipulate the returned rank values by using column weights in the [CONTAINS](-search-sql-contains.md) and [FREETEXT](-search-sql-freetext.md) WHERE clause predicates, and the RANK BY clause.

 

 



