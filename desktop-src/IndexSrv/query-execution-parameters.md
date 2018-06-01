---
title: Query Execution Parameters
description: Query Execution Parameters
ms.assetid: 9134acb9-13c6-488c-9e88-5f3868f601a4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query Execution Parameters

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A number of situations leading to unexpected query results are flagged by using built-in variables available in the .htx file. Most .htx pages should include a &lt;%if...%&gt; test on these variables.

[CiOutOfDate](https://www.bing.com/search?q=CiOutOfDate) will be set to the value 1 if the content index has files to filter or scans to complete. Missing results are possible because information about particular documents is either from an old version of the document or missing. When this variable is set, it is possible to get results including deleted files, and files whose current version does not match the query.

[CiQueryTimedOut](https://www.bing.com/search?q=CiQueryTimedOut) will be set to the value 1 when the amount of CPU time spent executing the query exceeds the limit specified in the *MaxQueryExecutionTime* parameter in the registry. The variable will be valid for all pages in the result for nonsequentially executed queries. For sequentially executed queries, the CiQueryTimedOut variable is valid only after all available results for the query have been displayed.

[CiQueryIncomplete](https://www.bing.com/search?q=CiQueryIncomplete) will be set to the value 1 if some portion of the query restriction was ignored. This can occur when a query is forced to use the Content Index.

 

 




