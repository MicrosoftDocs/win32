---
Description: Default or Plain Text Filter
ms.assetid: f710b317-ac1e-4f3b-9a9b-2791abd6d37d
title: Default or Plain Text Filter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Default or Plain Text Filter

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

For plain-text files and files of unregistered origin, Indexing Service uses the default filter (in Query.dll). It filters both the system properties (such as file names) and the contents of a file. The default filter does not “understand” any document formats; when filtering the contents of a file, it treats the file as a sequence of characters. (It does check for the Unicode byte-order mark at the beginning of the file.) Indexing Service uses the default filter when the file-name extension of a file has no association in the registry, and if the value of the [FilterFilesWithUnknownExtensions](filterfileswithunknownextensions.md) registry entry is one.

 

 



