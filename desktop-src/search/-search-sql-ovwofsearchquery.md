---
description: The Windows Search Structured Query Language (SQL) is similar to a standard SQL query.
ms.assetid: 7d992fa2-4606-46ca-904c-b45056a9bbc2
title: Overview of Windows Search SQL Syntax
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Windows Search SQL Syntax

The Windows Search Structured Query Language (SQL) is similar to a standard SQL query. It is shown in the following two syntaxes:


```SQL
SELECT [TOP <positive integer>] <columns>
FROM [machinename.]SystemIndex
[WHERE <conditions>]
[ORDER BY <column>]
```

```SQL
GROUP ON <column> [<ranges>]
[AGGREGATE <aggregate_list>]
[ORDER BY <column> [ASC/DESC]]
OVER (<GROUP ON ...> | <SELECT...>) 
```

In the following query example, the page count and date created values are returned for all documents which have more than 50 pages, sorted is ascending order of page count.

```SQL
SELECT System.Document.PageCount, System.DateCreated
FROM SystemIndex
WHERE (System.Document.PageCount > 50)
ORDER BY System.Document.PageCount
```

The Windows Search query syntax supports many options, enabling more complicated queries.

The following table describes each clause in the SELECT or GROUP ON statements and the features supported.

| Clause                                              | Description                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GROUP ON...OVER...](-search-sql-group-on-over.md) | Specifies how to group results returned by the query. You can specify the ranges by which to group and specify more than one column for grouping. For example, you can group results over a range of file sizes (size < 100, 100 <= size < 1000; 1000 <= size) and nest groupings.                                                                                                       |
| [SELECT](-search-sql-select.md)                    | Specifies the columns returned by the query.                                                                                                                                                                                                                                                                                                                                                         |
| [FROM](-search-sql-from.md)                        | Specifies the machine and catalog to search.                                                                                                                                                                                                                                                                                                                                                         |
| [WHERE](-search-sql-where.md)                      | Specifies what constitutes a matching document. This clause has many options, enabling rich control over the search conditions. For example, you can match against words, phrases, inflectional word forms, strings, numeric and bitwise values, and multi-valued arrays. You can also apply statistical weights to the matching conditions, and combine matching conditions with Boolean operators. |
| [ORDER BY](-search-sql-orderby.md)                 | Specifies the sort order for the results returned by the query. You can specify more than one field on which the results are sorted, and you can use ascending or descending ordering.                                                                                                                                                                                                               |

### Code samples

The WSSQL code sample demonstrates how to communicate between Microsoft OLE DB and Windows Search through SQL. The WSOleDB code sample illustrates Active Template Library (ATL) OLE DB access to Windows Search applications, and two additional methods for retrieving results from Windows Search. Both samples are available on [GitHub](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch).

## Related topics

### Reference

[Literals](-search-sql-literals.md)

[Using Localized Searches](-search-sql-usinglocsearches.md)

[Understanding Relevance Values](-search-sql-understandingrelevancevalues.md)

[Property Mappings](-search-3x-wds-propertymappings.md)

[Advanced Query Syntax](-search-3x-advancedquerysyntax.md)

### Conceptual

[SQL Extensions in Microsoft Windows Search](-search-sql-extensions-sps.md)

[SQL Features Unavailable in Microsoft Windows Search](-search-sql-featuresunavailableinspssearch.md)

[Identifiers](-search-sql-identifiers.md)

[Case Sensitivity in Searches](-search-sql-casesensitivityinsearches.md)

[Diacritic Sensitivity in Searches](-search-sql-accentinsensitivitysearches.md)

[Casting the Data Type of a Column](-search-sql-castingdatacolumntype.md)

[Data Type Mappings](-search-sql-datatypemappings.md)
