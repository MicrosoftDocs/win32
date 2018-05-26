---
title: Scanning Component
description: Scanning Component
ms.assetid: e2ccd999-13fe-4610-b8fd-704b4dbd85fa
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Scanning Component

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The Scanning component detects file modifications that trigger filtering of the files. If all indexed files exist on drives that support change notification in some way, scanning operations are only necessary the first time a catalog is created or during crash recovery. Otherwise, the [Indexing component](indexing-component.md) calls the Scanning component when the operating system has no way to flag change notifications.

The cisvc.exe file contains the Scanning component.

 

 




