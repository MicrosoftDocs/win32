---
description: The conditions that determine whether a document is included in the results returned by the query are specified by the WHERE clause.
ms.assetid: e3b5ee92-e817-49b8-aa8b-5d68254bb819
title: WHERE Clause (Windows Search)
ms.topic: article
ms.date: 05/31/2018
---

# WHERE Clause (Windows Search)

The conditions that determine whether a document is included in the results returned by the query are specified by the WHERE clause. At the highest level, there are two parts to the WHERE clause syntax:


```
...WHERE [<group_aliases>] <search_condition>
...WHERE ReuseWhere(<WHEREID>)
```



The optional <group\_alias> portion of the clause simplifies complex queries by assigning an alias to a group of one or more columns. This can improve the readability of complex queries that search for the same information across multiple columns specified by URLs. For more information about group aliases, see [WITH -- AS Group Alias Predicate](-search-sql-with-as.md).

The \<search condition\> portion of the WHERE clause is one or more search predicates that specify matching criteria for the search. Search predicates are expressions that assert some fact about some value.

The result of a search condition is a Boolean value, either **TRUE** if the document meets the specified search conditions, or **FALSE** if it does not. If the result is **TRUE**, the document is returned. If the result is **FALSE**, the document is not returned. Documents returned in a Microsoft Windows Search query are assigned rank values according to how well they match the search conditions. Each of the query search conditions can include a [RANKBY](-search-sql-rankby.md) clause that supports modifying the returned rank values.

The [ReuseWhere function](-search-sql-reusewhere.md) makes multiple queries that use the some of the same search conditions more efficient. The WHERE clause in a query specifies the set of items that match in a query. Subsequent queries can share the work performed for the previous evalution by using the ReuseWhere function in the new query WHERE clause.

## Search Predicates

A search condition consists of one or more predicates or search conditions that describe what the user is searching for (for example, WHERE System.DateCreated >'2006-04-19'). Search predicates can be combined using the logical operators **AND**, **OR**, or **NOT**. The optional unary operator **NOT** can be used only with **AND** and only to negate the logical value of a predicate or search condition. You can use parentheses to group and nest logical terms.

The following table shows the order of precedence for the logical operators.



| Order (precedence) | Logical operator |
|--------------------|------------------|
| First (highest)    | **NOT**          |
| Second             | **AND**          |
| Third (lowest)     | **OR**           |



 

Logical operators of the same type are associative, and there is no specified calculation order. For example, (A **AND** B) **AND** (C **AND** D) can be calculated (A **AND** D) **AND** (B **AND** C) with no change in the logical result.

> [!IMPORTANT]
>
> Incorrect: WHERE **NOT** CONTAINS ('computer')
>
> Correct: WHERE CONTAINS ('software') **AND NOT** CONTAINS ('computer')

 

In complex queries, you might want to place more emphasis on matches in some columns than in others. For example, when searching for documents that discuss "software design", finding the search term in the document title is more likely to be a good match than finding the individual words in the text of the document. To influence the ranking of documents in this manner, the Microsoft Windows Search query language supports weighting the search conditions. For more information about column weighting, see [CONTAINS Predicate](-search-sql-contains.md) and [FREETEXT Predicate](-search-sql-freetext.md).

There are three groups of search predicates in Windows Search: full-text, non-full-text, and folder depth searches. Full-text search predicates typically match the meaning of the content, title, and other columns, and support linguistic matching (for example, alternative word forms, phrases, and proximity searching). In contrast, non-full-text search predicates match the value of the specified columns and do not include any special linguistic processing, but in several cases offer character-based pattern matching. Folder depth predicates restrict the search scope to a specified path.

> [!Note]  
> If the query returns a document because a non-full-text predicate evaluates to **TRUE** for that document, the rank value is calculated as 1000. Using the [rank coercion function](-search-sql-rankby.md) can modify the rank value.

 

The following tables describe the full-text, non-full-text, and folder depth search predicates.



| Full-text predicate                  | Description                                                                                                                                                                                                                                                      |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CONTAINS](-search-sql-contains.md) | Supports complex searches for terms in document text columns (for example, title, contents). Can search for inflected forms of the search terms, test for proximity of the terms, and perform logical comparisons. Search terms can include wildcard characters. |
| [FREETEXT](-search-sql-freetext.md) | Searches for documents that match the meaning of the search phrase. Related words and similar phrases will match, with the rank column calculated based on how closely the document matches the search phrase. Search terms cannot include wildcard characters.  |



 



| Non-full-text predicate                                                    | Description                                                                                                                                                                           |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LIKE](-search-sql-like.md)                                               | Column values are compared using simple pattern matching with wildcard characters.                                                                                                    |
| [Literal Value Comparison](-search-sql-literalvaluecomparison.md)         | Column values are compared against string, date, time stamp, numeric, and other literal values. This predicate supports equality and inequalities such as greater than and less than. |
| [Multi-Valued (ARRAY) Comparisons](-search-sql-multivaluedcomparisons.md) | Multivalued columns are compared against a multivalued array of literals.                                                                                                             |
| [NULL](-search-sql-null.md)                                               | Column values that are undefined for the document can be detected by using the **NULL** predicate.                                                                                    |



 



| Folder Depth                             | Description                                                                                        |
|------------------------------------------|----------------------------------------------------------------------------------------------------|
| [SCOPE](-search-sql-folderdepth.md)     | Performs a deep traversal of the specified path, including the specific folder and all subfolders. |
| [DIRECTORY](-search-sql-folderdepth.md) | Performs a shallow traversal of the specified path, searching only the specific folder.            |



 

## Examples

For examples of the WHERE clause, see the individual predicate topics linked in the preceding table.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[ReuseWhere function](-search-sql-reusewhere.md)
</dt> <dt>

[Rowset Properties](-search-sql-rowset-properties.md)
</dt> <dt>

[FROM Clause](-search-sql-from.md)
</dt> <dt>

[Overview of the Search SQL Syntax](-search-sql-ovwofsearchquery.md)
</dt> <dt>

[WITH -- AS Group Alias Predicate](-search-sql-with-as.md)
</dt> <dt>

[SCOPE and DIRECTORY Predicates](-search-sql-folderdepth.md)
</dt> <dt>

[RANK BY Clause](-search-sql-rankby.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



