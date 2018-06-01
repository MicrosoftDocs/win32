---
Description: Sequential and Nonsequential Execution
ms.assetid: 4658699a-79a0-4f10-80bd-920b56abd0de
title: Sequential and Nonsequential Execution
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sequential and Nonsequential Execution

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A query can be executed sequentially (results fetched as needed) or it can be executed nonsequentially (results cached on the server). A sequential query requires fewer server resources, but also has some limitations. Backward scrolling ([CiBookmarkSkipCount](https://www.bing.com/search?q=CiBookmarkSkipCount) &lt; 0) will re-execute the query and scroll forward to the specified position. Sequential queries cannot refer to the following variables: [CiMatchedRecordCount](https://www.bing.com/search?q=CiMatchedRecordCount), [CiRecordsNextPage](https://www.bing.com/search?q=CiRecordsNextPage), and [CiTotalNumberPages](https://www.bing.com/search?q=CiTotalNumberPages).

Either of the following actions will force a query to be nonsequential:

-   Referring to the [CiMatchedRecordCount](https://www.bing.com/search?q=CiMatchedRecordCount), [CiRecordsNextPage](https://www.bing.com/search?q=CiRecordsNextPage) or [CiTotalNumberPages](https://www.bing.com/search?q=CiTotalNumberPages) variables in the .htx page.
-   Setting the [CiSort](https://www.bing.com/search?q=CiSort) parameter to sort of query results other than the native order of the result. CiSort can safely be set to sort ascending on WorkId (CiSort=WorkId\[a\]) or descending on Rank (CiSort=Rank\[d\]).

 

 



