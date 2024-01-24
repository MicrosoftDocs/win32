---
description: The WHERE clause in a query specifies a set of items to match results against.
ms.assetid: ed51edd5-6edc-4fcd-a69b-cb48c399ba7c
title: ReuseWhere Function
ms.topic: article
ms.date: 05/31/2018
---

# ReuseWhere Function

The [WHERE](-search-sql-where.md) clause in a query specifies a set of items to match results against. Subsequent queries can share the work performed for a previous query by using the ReuseWhere function in a new query WHERE clause. Queries that take advantage of this function execute faster.

## Examples

The following scenario shows how to use the ReuseWhere function:

1.  You issue the following query:
    ```
    SELECT System.ItemName FROM SystemIndex 
    WHERE CONTAINS(*, 'pencil') AND System.ItemDate > '2007-3-5'
    ```

    

2.  From the returned rowset, you get a [Where ID](-search-sql-rowset-properties.md), *Query1WhereID*.

    The Where ID is a rowset property with PROPSET {aa6ee6b0-e828-11d0-b2-3e-00-aa-00-47-fc-01 }, PROPID 8, and type UI4.

3.  You issue a second query with the ReuseWhere function, passing in the *Query1WhereID* from step 2:
    ```
    SELECT System.ItemUrl FROM SystemIndex 
    WHERE ReuseWhere(Query1WhereID) AND SCOPE='file:'
    ```

    

The second query is equivalent to the following:


```
SELECT System.ItemUrl, System.ItemName FROM SystemIndex 
WHERE CONTAINS(*, 'pencil') AND System.ItemDate > '2007-3-5' AND Scope='file:'
```



The ReuseWhere function can be used anwhere in the [WHERE](-search-sql-where.md) clause.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> <dt>

[Rowset Properties](-search-sql-rowset-properties.md)
</dt> </dl>

 

 



