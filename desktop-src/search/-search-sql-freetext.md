---
description: The FREETEXT predicate is part of the WHERE clause and supports searching for words and phrases in text columns.
ms.assetid: 8afc95d1-25cd-4448-8bee-d132c2da22b3
title: FREETEXT Predicate
ms.topic: article
ms.date: 05/31/2018
---

# FREETEXT Predicate

The FREETEXT predicate is part of the [WHERE](-search-sql-where.md) clause and supports searching for words and phrases in text columns. Use the FREETEXT predicate to find documents containing combinations of the search words spread throughout the content or columns specified. To get the rank value, include System.Search.Rank, which is a ranking of relevence, as a column in the SELECT statment.

The FREETEXT predicate has the following syntax:


```
FREETEXT
(["<fulltext_column>",]'<freetext_condition>'[,<LCID>])...
```



The fulltext column reference is optional. With it, you can specify a single column, or a [column grouping alias](-search-sql-with-as.md) against which the FREETEXT predicate is tested. When the fulltext column is specified as "ALL" or "\*", all indexed text properties are searched. Although the column is not required to be a text property, the results might be meaningless if the column is some other data type. The column name can be either a regular or delimited [identifier](-search-sql-identifiers.md), and you must separate it from the condition by a comma. If no fulltext condition is supplied, the Contents column, which is the body of the document, is used.

You can specify a search locale to identify the appropriate word breaker and inflectional forms for the search query. Valid locale values are a Windows standard language code identifier (LCID). For example, 1033 is the LCID for United States-English. Place the LCID as the last item inside the parentheses of the FREETEXT clause. For important information about searching and languages, see [Using Localized Searches](-search-sql-usinglocsearches.md).

> [!Note]  
> The default search locale is the system default locale.

 

You must enclose the freetext condition portion in single quotation marks, and it must consist of one or more search terms. The FREETEXT predicate does not support logical operations. To search for a phrase as if it were a single word, enclose the phrase in double quotation marks.

When you use the FREETEXT predicate, the search query results return documents containing all of the search terms. The terms do not need to appear in any particular order. Documents that contain more of the search terms have higher rank column values.

## Examples

The following example searches for documents containing "computer", "software", "hardware", or combinations of those words:


```
WHERE FREETEXT('computer software hardware')
```



> [!Note]  
> You cannot use both single-word matching and phrase matching in the same FREETEXT predicate.

 

When performing queries with contractions, you must escape the quotation mark in the contraction when using FREETEXT, but not when using CONTAINS.

For example, the following syntax fails:


```
WHERE FREETEXT(*,'"We'll meet next week"')
```



The correct syntax includes two single quotation marks, not a double quotation mark.

The following syntax succeeds:


```
WHERE FREETEXT(*,'"We''ll meet next week"')
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[CONTAINS Predicate](-search-sql-contains.md)
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



