---
title: DBPROP\_CI\_INCLUDE\_SCOPES
description: DBPROP\_CI\_INCLUDE\_SCOPES
ms.assetid: 7a57c196-8db9-467c-b2e7-d0a4ca213bb3
keywords:
- DBPROP_CI_INCLUDE_SCOPES
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBPROP\_CI\_INCLUDE\_SCOPES

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBPROP\_CI\_INCLUDE\_SCOPES** property specifies the names of the file path(s) over which the query is processed.

### Summary



|                  |                               |
|------------------|-------------------------------|
| **Property Set** | DBPROPSET\_ FSCIFRMWRK\_EXT   |
| **Property ID**  | DBPROP\_CI\_INCLUDE\_SCOPES   |
| **Value Type**   | DBTYPE\_ARRAY \| DBTYPE\_BSTR |
| **Default**      | "\\" (the entire catalog)     |



 

### Remarks

If more than one catalog or machine is specified, the [**DBPROP\_MACHINE**](dbprop-machine.md), [**DBPROP\_CI\_CATALOG\_NAME**](dbprop-ci-catalog-name.md), **DBPROP\_CI\_INCLUDE\_SCOPES**, and [**DBPROP\_CI\_SCOPE\_FLAGS**](dbprop-ci-scope-flags.md) properties all must have the same number of entries, or the count of scopes and flags can be either the count of catalogs and machines or 1.

When more than one machine or catalog is specified, the query is executed on multiple machines and the results are merged on the local machine.

The scope "\\" covers the entire catalog. The scope "/" covers the entire Microsoft Internet Information Services (IIS) virtual path namespace. Scopes can be letter-based paths on the local drive or remote universal naming convention (UNC) paths.

This property corresponds to the *CiScope* variable in the [Internet Data Query Files](internet-data-query-files.md) of Indexing Service.

 

 




