---
description: The CONTAINSSEMANTIC predicate is part of the WHERE clause and supports semantic searching within indexed content.
title: CONTAINSSEMANTIC Predicate
ms.topic: article
ms.date: 05/31/2018
---

# CONTAINSSEMANTIC Predicate

The CONTAINSSEMANTIC predicate is part of the WHERE clause and supports semantic searching within indexed content. The clause can be used to search for text or images based on their semantic similarity, rather than just exact keyword matches.

The following is the basic syntax of the CONTAINSSEMANTIC predicate:

```SQL
...CONTAINSSEMANTIC (ContentType, [<fulltext_column or #list>,] search_text_phrase, LCID) ...
```

The *ContentType* parameter specifies whether the search is for text or images. Allowed values are "text" or "image".

The *fulltext_column* reference is optional. With it, you can limit the search to a single column or a column group against which the CONTAINSSEMANTIC predicate is tested. When *fulltext_column* is specified as "\*", all indexed text properties are searched. Although the column is not required to be a text property, the results might be meaningless if the column is some other data type. The column name can be either a regular or delimited [identifier](-search-sql-identifiers.md), and you must separate it from the condition by a comma. If no *fulltext_column* is specified, the System.Search.Contents column, which is the body of the document, is used.

The LCID portion of the predicate specifies the search locale. This instructs the search engine to use the appropriate word breaker and inflectional forms for the search query. To specify the locale, provide the Windows standard language code identifier (LCID). For example, 1033 is the LCID for United States-English. Place the LCID as the last item inside the parentheses of the CONTAINSSEMANTIC clause. For important information about searching and languages, see [Using Localized Searches](-search-sql-usinglocsearches.md).

The traditional indexing and search continue to work seamlessly for all supported language packs on Windows. However, the improved search is optimized only for these languages: 

| Language | LCID value |
|----------|------------|
| English (US) | 1033 |
| English (CA) | 4105 |
| English (AU) | 3081 |
| English (GB) | 2057 |
| French (FR) | 1036 |
| French (CA) | 3084 |
| German (DE) | 1031 |
| Spanish (ES) | 3082 |
| Spanish (MX) | 2058 |
| Japanese (JP) | 1041 |
| Chinese (Simplified) | 2052 |

> [!NOTE]  
> The default search locale is the system default locale.

For more information on LCID values, see [Windows Language Code Identifier (LCID) Reference](/openspecs/windows_protocols/ms-lcid/70feba9f-294e-491e-b6eb-56532684c37f).

The *search_text_phrase* portion must be enclosed in single quotation marks for single words or double quotation marks for phrases, and consists of one or more content search terms that are combined using the logical operators **AND** or **OR**. You can use the optional unary operator **NOT** after an **AND** operator to negate the logical value of a content search term.

> [!NOTE]  
> The **NOT** operator can occur only after **AND**. You cannot use the **NOT** operator if there is only one match condition, or after the **OR** operator.

You can use parentheses to group and nest content search terms. The following table describes the order of precedence for the logical operators.

| Order (precedence) | Logical operator |
|--------------------|------------------|
| First (highest)    | **NOT**          |
| Second             | **AND**          |
| Third (lowest)     | **OR**           |

Logical operators of the same type are associative, and there is no specified calculation order. For example, (A **AND** B) **AND** (C **AND** D) can be calculated (B **AND** C) **AND** (A **AND** D) with no change in the logical result.

## Example

The following example shows a query for documents and images related to the phrase "family on a beach" using the **CONTAINSSEMANTIC** clause.

```sql
SELECT * FROM SystemIndex  
WHERE CONTAINSSEMANTIC('text', *, 'family on a beach', 1033)  
OR CONTAINSSEMANTIC('image', *, 'family on a beach', 1033)  
RANK BY MERGE(merge_operation)
```


## Related topics

### Reference

[WHERE Clause](-search-sql-where.md)

### Conceptual

[Full-Text Predicates](-search-sql-fulltextpredicates.md)

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
