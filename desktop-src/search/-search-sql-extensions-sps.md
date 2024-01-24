---
description: Microsoft Windows Search, based on the SQL-92 and SQL-99 standards, improves full-text document-based searches in document-management or knowledge-management applications.
ms.assetid: 136af1ea-452a-491b-bec7-8c45fa01f87f
title: SQL Extensions in Microsoft Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# SQL Extensions in Microsoft Windows Search

Microsoft Windows Search, based on the SQL-92 and SQL-99 standards, improves full-text document-based searches in document-management or knowledge-management applications. Windows Search improvements include the following:

## 128-Character Identifier Names

While SQL-92 and SQL-99 restrict column and other identifiers to 18 characters, Windows Search supports 128-character column names. For more information, see [Identifiers](-search-sql-identifiers.md).

## Grouping Results by Columns

Queries can specify how to group results. You can specify the ranges by which to group, and you can specify more than one column for grouping. For example, you can group results over a range of file sizes (size < 100, 100 <= size < 1000; 1000 <= size), and you can nest groupings. For more information, see [GROUP ON ... OVER... Statement](-search-sql-group-on-over.md).

## Diacritic-Insensitive Searching

In addition to searching that is not case-sensitive, Windows Search supports searching that is not sensitive to diacritics (accent marks). For more information, see [Diacritic Sensitivity in Searches](-search-sql-accentinsensitivitysearches.md).

## Column Weighting

Queries that search more than one column can specify the importance of each column. The [CONTAINS](-search-sql-contains.md) and [FREETEXT](-search-sql-freetext.md) predicates both support column weighting.

## NULL Predicate

Although full-text content indexing has no defined set of columns, queries can require that members of the result set do or do not have specified columns. It is not possible to differentiate between a document has a specified property with the value set to **NULL**, and a document that does not have the property at all.

## Rank Modification

You can manipulate the search results ranking by using [weights](-search-sql-understandingrelevancevalues.md) on properties and on aliased groups of properties. Rank coercion supports direct manipulation of the relevance ranking based on the criteria you specify.

 

 



