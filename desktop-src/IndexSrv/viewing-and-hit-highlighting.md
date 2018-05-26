---
title: Viewing and Hit-Highlighting
description: Viewing and Hit-Highlighting
ms.assetid: 9d8a360c-1808-4242-b217-2aee1af34ee5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Viewing and Hit-Highlighting

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When a document shows in a results list as having a match to a query string, you may naturally want to view that document and see where the hits are. The document viewer then calls the [IFilter](/windows/win32/Filter/nn-filter-ifilter?branch=master) methods to filter the document, process the results to be an index, and search that in-memory index for query hits. The viewer can then highlight and navigate from hit to hit. This process is known as hit-highlighting.

For an example of hit-highlighting implemented with Indexing Service and Internet Information Services (IIS), see [Highlighting Search Hits](highlighting-search-hits.md).

 

 




