---
title: Query Submittal for Indexing Service Query Language
description: Query Submittal for Indexing Service Query Language
ms.assetid: b1cb4053-44bc-4835-b93e-cb0f7f0ec0f3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Query Submittal for Indexing Service Query Language

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To use the Indexing Service query language, either Dialect 1 or Dialect 2, an application or script must use one of three APIs to submit a query. In general, these APIs feature ease of programming rather than flexibility or the fastest execution. The following table lists the APIs and summarizes how to select the dialect.



| API                                                                 | Select Dialect By                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ISAPI Extensions](programming-apis.md#-idxs-isapi-extensions-api) | Specifying a value of the *CiDialect* variable in the .idq file.                                                                                                                                                                                              |
| [OLE DB Helper](programming-apis.md#-idxs-ole-db-helper-api)       | Specifying a value from the [ISQLANG\_\* constants](isqlang-constants.md) for the *ulDialect* parameter of a [**CITextToFullTreeEx**](/windows/win32/Ntquery/nf-ntquery-citexttofulltreeex?branch=master) or [**CITextToSelectTreeEx**](/windows/win32/Ntquery/nf-ntquery-citexttoselecttreeex?branch=master) function call that constructs a query. |
| [Query Helper](programming-apis.md#-idxs-query-helper-api)         | Specifying an appropriate value for the [**Query.Dialect**](iixssoquery-dialect.md) property of a query.                                                                                                                                                     |



 

For information about which languages and tools you can use with these APIs, see [Combinations of Tasks, Languages, and APIs](combinations-of-tasks--languages--and-apis.md). For additional information about using these APIs to submit queries and for examples, see [Using Indexing Service with File Systems](using-indexing-service-with-file-systems.md) and [Using Indexing Service with Web Servers](using-indexing-service-with-web-servers.md).

 

 




