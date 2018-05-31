---
title: Extensions to SQL for Indexing Service
description: Extensions to SQL for Indexing Service
ms.assetid: dae72fc7-e034-4814-babe-ff9570ee8208
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extensions to SQL for Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The SQL query language includes extensions to the standard SQL data manipulation language (DML) for querying the indexed contents of Indexing Service catalogs. Conceptually, the SQL query language considers a catalog to be a table with columns containing properties and rows containing documents. (For additional details, see [Representing the Catalog Conceptually](representing-the-catalog-conceptually.md).) The extensions include the following.

-   [Extensions for Properties](extensions-for-properties.md)
-   [Extensions for Queries](extensions-for-queries.md)

The SQL extensions for Indexing Service do not support cross-data source queries. You need to issue separate queries to another source — for example, the ODBC Provider to Microsoft SQL Server™ — when combining information from more than one source.

 

 




