---
title: Effect of Parameters on Query Performance
description: Effect of Parameters on Query Performance
ms.assetid: 03cf02c6-b21a-42a7-944d-06fce8a052cf
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Effect of Parameters on Query Performance

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The fastest query is a *sequential* query that uses the *content index*. Certain parameter settings will force the query engine to use a less-efficient method to resolve the query. To guarantee fast queries, set [CiSort](https://www.bing.com/search?q=CiSort) to nothing (or descending by rank) set [CiForceUseCi](https://www.bing.com/search?q=CiForceUseCi) to TRUE, and do not reference [CiMatchedRecordCount](https://www.bing.com/search?q=CiMatchedRecordCount), [CiRecordsNextPage](https://www.bing.com/search?q=CiRecordsNextPage), or [CiTotalNumberPages](https://www.bing.com/search?q=CiTotalNumberPages) in the .htx template.

 

 




