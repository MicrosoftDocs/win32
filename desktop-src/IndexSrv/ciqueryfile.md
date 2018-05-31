---
title: CiQueryFile
description: CiQueryFile
ms.assetid: 5fe2bb09-c576-4caf-97c0-36f74e028d09
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CiQueryFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Format: **CiQueryFile**=*Virtual path*

Specifies the *Virtual path* of the .idq file containing the \[Names\] section describing the custom properties. You must pass this parameter for all queries involving custom properties. If you try to hit-highlight a document with a query that has a custom property and do not specify the appropriate .idq file, the error message “No such property” will be displayed. This parameter is optional.

 

 




