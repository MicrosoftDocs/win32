---
description: The Microsoft Windows Search query language supports six non-full-text search predicates. The predicates described in this section are listed in the following table.
ms.assetid: 74aa6dbc-5c0d-433e-96d9-a8db63907342
title: Non-Full-Text Predicates
ms.topic: article
ms.date: 05/31/2018
---

# Non-Full-Text Predicates

The Microsoft Windows Search query language supports six non-full-text search predicates. The predicates described in this section are listed in the following table.



| Non-full-text predicate                                                    | Description                                                                                                                                                                             |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ALL BITWISE and SOME BITWISE](all-bitwise.md)                            | Is a set of keywords that are about testing the bits in an integral type.                                                                                                               |
| [DATEADD Function](-search-sql-dateadd.md)                                | Performs time and date calculations for matching properties having date types. Use the DATEADD function to obtain dates and times in a specified amount of time before the present.     |
| [LIKE Predicate](-search-sql-like.md)                                     | Compares column values using simple pattern matching with wildcard characters.                                                                                                          |
| [Literal Value Comparison](-search-sql-literalvaluecomparison.md)         | Compares column values against string, date, time stamp, numeric, and other literal values. This predicate supports inequalities such as greater than ('>'), and less than ('<'). |
| [Multi-Valued (ARRAY) Comparisons](-search-sql-multivaluedcomparisons.md) | Compares multivalued columns against a multivalued array of literals.                                                                                                                   |
| [NULL Predicate](-search-sql-null.md)                                     | Detects column values that are undefined for the document.                                                                                                                              |



 

> [!IMPORTANT]
> Search queries using the **NULL** predicate can require that Windows Search scan the entire catalog, which might slow down the query's performance.

 

## Related topics

<dl> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> </dl>

 

 



