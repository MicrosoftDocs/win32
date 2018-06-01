---
title: Deferring Nonindexed Trimming
description: Deferring Nonindexed Trimming
ms.assetid: 955327ea-334d-4e76-9e6d-7733048685c5
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Deferring Nonindexed Trimming

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Special support has been added to Indexing Service to optimize content queries that are sorted by descending rank (CiSort = Rank\[d\]). For such queries, minimal information can be retrieved from the index, before additional property and security tests are performed. However, if the total number of results matching the query is greater than [CiMaxRecordsInResultSet](https://www.bing.com/search?q=CiMaxRecordsInResultSet) then additional testing must be performed during index retrieval to remove items from this set that fail additional property and security tests. This frees space in the result set for items matching the full query. This processing uses up resources, and can be deferred by setting [CiDeferNonIndexedTrimming](https://www.bing.com/search?q=CiDeferNonIndexedTrimming) to TRUE. The query will then pick CiMaxRecordsInResultSet items first, and trim them. The end result may be a number of matching items that is less than CiMaxRecordsInResultSet. For queries with the scope set to the entire corpus, on a server with little or no security, you can consider setting CiDeferNonIndexedTrimming to TRUE to improve performance.

 

 




