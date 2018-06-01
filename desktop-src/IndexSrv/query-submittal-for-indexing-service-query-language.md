---
Description: Query Submittal for Indexing Service Query Language
ms.assetid: b1cb4053-44bc-4835-b93e-cb0f7f0ec0f3
title: Query Submittal for Indexing Service Query Language
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query Submittal for Indexing Service Query Language

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To use the Indexing Service query language, either Dialect 1 or Dialect 2, an application or script must use one of three APIs to submit a query. In general, these APIs feature ease of programming rather than flexibility or the fastest execution. The following table lists the APIs and summarizes how to select the dialect.



| API                                                                 | Select Dialect By                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ISAPI Extensions](https://www.bing.com/search?q=ISAPI Extensions) | Specifying a value of the *CiDialect* variable in the .idq file.                                                                                                                                                                                              |
| [OLE DB Helper](https://www.bing.com/search?q=OLE DB Helper)       | Specifying a value from the [ISQLANG\_\* constants](isqlang-constants.md) for the *ulDialect* parameter of a [**CITextToFullTreeEx**](/windows/desktop/api/Ntquery/nf-ntquery-citexttofulltreeex) or [**CITextToSelectTreeEx**](/windows/desktop/api/Ntquery/nf-ntquery-citexttoselecttreeex) function call that constructs a query. |
| [Query Helper](https://www.bing.com/search?q=Query Helper)         | Specifying an appropriate value for the [**Query.Dialect**](iixssoquery-dialect.md) property of a query.                                                                                                                                                     |



 

For information about which languages and tools you can use with these APIs, see [Combinations of Tasks, Languages, and APIs](combinations-of-tasks--languages--and-apis.md). For additional information about using these APIs to submit queries and for examples, see [Using Indexing Service with File Systems](using-indexing-service-with-file-systems.md) and [Using Indexing Service with Web Servers](using-indexing-service-with-web-servers.md).

 

 



