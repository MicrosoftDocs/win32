---
description: Windows Search provides content crawling and search features that support full-text searching. The query language used by Windows Search extends the standard SQL-92 and SQL-99 database query syntax to enhance its usefulness with text-based searches.
ms.assetid: a2eb550a-bb55-4dbd-9ca1-60b776eb9339
title: Querying the Index with Windows Search SQL Syntax
ms.topic: article
ms.date: 05/31/2018
---

# Querying the Index with Windows Search SQL Syntax

Windows Search provides content crawling and search features that support full-text searching. The query language used by Windows Search extends the standard SQL-92 and SQL-99 database query syntax to enhance its usefulness with text-based searches.

All features of Windows Search Structured Query Language (SQL) are compatible with Windows Search on Windows Vista, and later, including all versions of Windows 10.

This section provides an overview of SQL syntax in Windows Search, and includes the following topics:

- [Overview of Windows Search SQL Syntax](-search-sql-ovwofsearchquery.md)
- [General Query Language Information](-search-sql-generalqueryinfo.md)
- [GROUP ON ... OVER... Statement](-search-sql-group-on-over.md)
- [SELECT Statement](-search-sql-select.md)
- [FROM Clause](-search-sql-from.md)
- [WHERE Clause](-search-sql-where.md)
- [ORDER BY Clause](-search-sql-orderby.md)
- [RANK BY Clause](-search-sql-rankby.md)
- [SET Statement](-search-sql-set.md)
- [Rowset Properties](-search-sql-rowset-properties.md)

This documentation assumes familiarity with Object Linking and Embedding Database (OLE DB), and SQL.

## Code samples

The WSSQL code sample demonstrates how to communicate between Microsoft OLE DB and Windows Search through SQL. The WSOleDB code sample illustrates Active Template Library (ATL) OLE DB access to Windows Search applications, and two additional methods for retrieving results from Windows Search. Both samples are available in the [Windows Search Samples](-search-samples-ovw.md) and the [Windows 10 SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk)

## Related topics

[Querying the Index Programmatically](-search-3x-wds-qryidx-overview.md)

[Using SQL and AQS Approaches to Query the Index](-search-3x-wds-qryidx-overview.md)

[Querying the Index with ISearchQueryHelper](-search-3x-wds-qryidx-searchqueryhelper.md)

[Querying the Index with the search-ms Protocol](-search-3x-wds-qryidx-searchms.md)

[Querying the Index with Windows Search SQL Syntax](-search-sql-windowssearch-entry.md)

[Using Advanced Query Syntax Programmatically](-search-3x-advancedquerysyntax.md)
