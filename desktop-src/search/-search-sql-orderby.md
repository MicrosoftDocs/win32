---
description: "Learn more about: ORDER BY Clause"
ms.assetid: e720cf0d-b034-48e2-a13e-e97dd23b2beb
title: ORDER BY Clause
ms.topic: article
ms.date: 05/31/2018
---

# ORDER BY Clause

The ORDER BY clause sorts the results based on the value of one or more columns you specify. Following is the syntax of the ORDER BY clause:


```
ORDER BY <column> [<direction>] [,<column> [<direction>]]
```



The column specifier must be a valid column. You can use the column specifier to refer to columns by the order that they appear in the query. The first column in the query is numbered 1. You can include more than one column in the ORDER BY clause, separated by commas.

The optional direction specifier can be either "ASC" for ascending (low to high) or "DESC" for descending (high to low). If you do not provide a direction specifier, the default, ascending, is used. If you specify more than one column, but do not specify all directions, the direction you specify last is applied to each column until you explicitly change the direction.

For example, in the following ORDER BY clause, the columns A, B, C, and G are sorted in ascending order, while columns D, E, and F are sorted in descending order.


```
ORDER BY A ASC, B, C, D DESC, E, F, G ASC
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[FROM Clause](-search-sql-from.md)
</dt> <dt>

[RANK BY Clause](-search-sql-rankby.md)
</dt> <dt>

[SELECT Statement](-search-sql-select.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



