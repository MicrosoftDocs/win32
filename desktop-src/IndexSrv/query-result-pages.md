---
Description: Query Result Pages
ms.assetid: fe340a76-2716-4780-abc3-481d9169039d
title: Query Result Pages
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query Result Pages

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses the .htx file mainly to format the results of a query. Query results are split into pages based upon the parameter [CiMaxRecordsPerPage](https://www.bing.com/search?q=CiMaxRecordsPerPage). The total number of query result records is governed by the parameter [CiMaxRecordsInResultSet](https://www.bing.com/search?q=CiMaxRecordsInResultSet). The current page number in the result set is given in the variable [CiCurrentPageNumber](https://www.bing.com/search?q=CiCurrentPageNumber). For a nonsequential query, the [CiTotalNumberPages](https://www.bing.com/search?q=CiTotalNumberPages) variable gives the total number of pages in the result and [CiRecordsNextPage](https://www.bing.com/search?q=CiRecordsNextPage) gives the number of records on the next page. The variables [CiContainsFirstRecord](https://www.bing.com/search?q=CiContainsFirstRecord) and [CiContainsLastRecord](https://www.bing.com/search?q=CiContainsLastRecord) indicate if the current page is the first or last in the result set. For an example of how to navigate between pages See [Navigating Between Pages in Query Results](navigating-between-pages-in-query-results.md).

 

 



