---
title: Indexing Component
description: Indexing Component
ms.assetid: 54e663dd-0aed-4abc-b661-f3dfe8ea094e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Indexing Component

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The Indexing component calls the [Filtering component](filtering-component.md) to extract the text and values from files that need to be filtered. After additional processing, it merges the resulting word lists into an index that is saved to disk. Indexing Service eventually merges content information (the text within a file) into the master index and saves value information (properties internal to the file) in the property cache.

The cisvc.exe file contains the Indexing component.

 

 




