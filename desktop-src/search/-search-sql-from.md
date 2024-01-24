---
description: Following the SELECT statement, you use the FROM clause to specify where to search for matching documents.
ms.assetid: 437d36d1-dd6d-4405-8f35-c37fd04fa0f6
title: FROM Clause
ms.topic: article
ms.date: 05/31/2018
---

# FROM Clause

Following the SELECT statement, you use the FROM clause to specify where to search for matching documents. The following is the syntax of the FROM clause for a local query:


```
FROM [<ComputerName>.]SystemIndex
```



Currently, Windows Search supports only one catalog, SystemIndex. To query the local catalog of a remote computer, include the computer name before the catalog and a Universal Naming Convention (UNC) path on the remote computer in the SCOPE or DIRECTORY clause.

You specify a scope as a restriction in the WHERE clause, as described in the [SCOPE and DIRECTORY Predicates](-search-sql-folderdepth.md) topic.

## Examples


```
SELECT System.ItemName,System.ItemUrl
FROM SystemIndex WHERE CONTAINS('Microsoft')

SELECT System.Author,System.ItemName,System.ItemUrl
FROM zarascomputer.SystemIndex WHERE SCOPE='file://zarascomputer/SomeFolder' AND CONTAINS('Microsoft')

SELECT System.Author,System.ItemName,System.ItemUrl
FROM server.SystemIndex WHERE SCOPE='file://server/users' AND CONTAINS('Microsoft')
```



In the second of the preceding examples, the query targets a remote computer called "zarascomputer". Notice that this computer name appears in both the FROM and SCOPE clauses. In the third example, the query targets a share name "users" on a server named "server" (where the UNC path would be \\\\server\\users).

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Overview of the Search SQL Syntax](-search-sql-ovwofsearchquery.md)
</dt> <dt>

[SELECT Statement](-search-sql-select.md)
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> <dt>

[SCOPE and DIRECTORY Predicates](-search-sql-folderdepth.md)
</dt> </dl>

 

 



