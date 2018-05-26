---
title: DBPROP\_DEFERNONINDEXEDTRIMMING
description: DBPROP\_DEFERNONINDEXEDTRIMMING
ms.assetid: fd3d03aa-98c9-47a2-857e-a5171cb73f7a
keywords:
- DBPROP_DEFERNONINDEXEDTRIMMING
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBPROP\_DEFERNONINDEXEDTRIMMING

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROP\_DEFERNONINDEXEDTRIMMING property optimizes query execution for a specific type of query.

### Summary



|                  |                                 |
|------------------|---------------------------------|
| **Property Set** | DBPROPSET\_QUERYEXT             |
| **Property ID**  | DBPROP\_DEFERNONINDEXEDTRIMMING |
| **Value Type**   | DBTYPE\_BOOL                    |
| **Default**      | VARIANT\_FALSE                  |



 

### Remarks

If the value is VARIANT\_TRUE, a maximum number of rows for the result is specified, and the sort order is by rank descending. Scope and security checking are deferred until the maximum number of rows is reached or the query is completed. This may result in less than the expected number of hits for queries in which scope checks or security trimming remove some results. The default is to optimize for recall; the result set trimming occurs in the course of executing the query.

This flag is best used when the query scope encompasses the entire catalog and all files in the result set have the same security access control lists.

This property corresponds to the *CiDeferNonIndexedTrimming* variable in the [Internet Data Query Files](internet-data-query-files.md) of Indexing Service.

This property corresponds to the *OptimizeFor* variable in Indexing Service's [**Query**](iixssoquery.md) object.

 

 




