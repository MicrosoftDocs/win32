---
description: The NULL predicate indicates whether the document has a value for the indicated column.
ms.assetid: 078ffd99-2020-4da2-8968-301dba8cc436
title: NULL Predicate
ms.topic: article
ms.date: 05/31/2018
---

# NULL Predicate

The **NULL** predicate indicates whether the document has a value for the indicated column.

The **NULL** predicate has the following syntax:


```
...WHERE <column> IS [NOT] NULL
```



The optional NOT keyword negates the result. The column can be a regular or delimited [identifier](-search-sql-identifiers.md).

> [!IMPORTANT]
> To test whether a column has the **NULL** value, you must use the **NULL** predicate. It is not valid to use the **NULL** value in a comparison predicate. "WHERE column IS **NULL**" is correct. "WHERE column = **NULL**" is not valid.

 

## Example

The following example returns documents that do not have a System.Video.Director value.


```
...WHERE System.Video.Director IS NULL
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[LIKE Predicate](-search-sql-like.md)
</dt> <dt>

[Literal Value Comparison](-search-sql-literalvaluecomparison.md)
</dt> <dt>

[Multi-Valued (ARRAY) Comparisons](-search-sql-multivaluedcomparisons.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



