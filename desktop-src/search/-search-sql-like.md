---
description: The LIKE predicate performs pattern-matching comparison on the specified column.
ms.assetid: d4bcf406-1253-4e56-b770-79edd4a98205
title: LIKE Predicate
ms.topic: article
ms.date: 05/31/2018
---

# LIKE Predicate

The LIKE predicate performs pattern-matching comparison on the specified column. It uses the following syntax:


```
...WHERE <column> LIKE '<wildcard_literal>'
```



The &lt;column&gt; can be a regular or delimited [identifier](-search-sql-identifiers.md). The column is limited to the properties in the property store.

The <wildcard\_literal> is a string literal. It is enclosed in quotation marks and optionally can contain wildcard characters. The match string can contain multiple wildcard characters if needed. The following table describes the wildcard characters that the LIKE predicate recognizes.



| Wildcard                | Description                                                                                                                                                                                     | Example                                                                                                                                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| % (percent)             | Matches zero or more of any characters.                                                                                                                                                         | 'comp%r' matches 'comp' followed by zero or more of any characters, ending in an r.                                                                                                                                  |
| \_ (underscore)         | Matches any single character.                                                                                                                                                                   | 'comp\_ter' matches 'comp' followed by exactly one of any character, followed by 'ter'.                                                                                                                              |
| \[ \] (square brackets) | Matches any single character within the specified range or set. For example, \[a-z\] specifies a range; \[aeiou\] specifies the set of vowels.                                                  | 'comp\[a-z\]re' matches 'comp' followed by a single character in the range of a through z, followed by 're'. 'comp\[ao\]' matches 'comp' followed by a single character that must be either an a or an o.<br/> |
| \[^ \] (caret)          | Matches any single character that is not within the specified range or set. For example, \[^a-z\] specifies a range that excludes a through z; \[^aeiou\] specifies a set that excludes vowels. | 'comp\[^u\]' matches 'comp' followed by any single character that is not a u.                                                                                                                                        |



 

If you create predicates with multiple ranges, the ranges must be in order.

> [!Note]  
> To match the wildcard characters as literal characters for matching and not as wildcard characters, place the character inside square brackets. For example, to match the percent sign, use '\[%\]'

 

## Examples


```
...WHERE System.ItemNameDisplay LIKE 'financ%'
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Literal Value Comparison](-search-sql-literalvaluecomparison.md)
</dt> <dt>

[Multi-Valued (ARRAY) Comparisons](-search-sql-multivaluedcomparisons.md)
</dt> <dt>

[NULL Predicate](-search-sql-null.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 




