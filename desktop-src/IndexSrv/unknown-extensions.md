---
title: Unknown Extensions
description: Unknown Extensions
ms.assetid: bb1123cd-963e-4d78-8dfa-6d6406c61d92
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Unknown Extensions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A file with an extension that does not have an association in the registry is treated as an unknown extension. The behavior of Indexing Service depends upon the registry setting [FilterFilesWithUnknownExtensions](filterfileswithunknownextensions.md). If this value is set to zero, the null filter is used to filter those files. Otherwise, the default filter is used to filter the contents.

 

 




