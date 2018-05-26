---
title: DBPROP\_CI\_CATALOG\_NAME
description: DBPROP\_CI\_CATALOG\_NAME
ms.assetid: cdbef8a8-a6ce-4a80-abd6-712e247dccd7
keywords:
- DBPROP_CI_CATALOG_NAME
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBPROP\_CI\_CATALOG\_NAME

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBPROP\_CI\_CATALOG\_NAME** property specifies the names of the catalog(s) over which the query is processed.

### Summary



|                  |                               |
|------------------|-------------------------------|
| **Property Set** | DBPROPSET\_ FSCIFRMWRK\_EXT   |
| **Property ID**  | DBPROP\_CI\_CATALOG\_NAME     |
| **Value Type**   | DBTYPE\_ARRAY \| DBTYPE\_BSTR |
| **Default**      | None                          |



 

### Remarks

If more than one catalog or machine is specified, the [**DBPROP\_MACHINE**](dbprop-machine.md), **DBPROP\_CI\_CATALOG\_NAME**, [**DBPROP\_CI\_INCLUDE\_SCOPES**](dbprop-ci-include-scopes.md), and [**DBPROP\_CI\_SCOPE\_FLAGS**](dbprop-ci-scope-flags.md) properties all must have the same number of entries, or the count of scopes and flags can be either the count of catalogs and machines or 1.

When more than one machine or catalog is specified, the query is executed on multiple machines and the results are merged on the local machine.

The default catalog installed is named System.

This property corresponds to the *CiCatalog* variable in the [Internet Data Query Files](internet-data-query-files.md) of Indexing Service.

 

 




