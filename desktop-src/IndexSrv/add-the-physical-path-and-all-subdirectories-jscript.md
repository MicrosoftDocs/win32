---
title: Add the Physical Path and All Subdirectories
description: Add the Physical Path and All Subdirectories
ms.assetid: 826b4e01-05b6-4eaa-8a20-34cba907534f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Add the Physical Path and All Subdirectories

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**AddScopeToQuery**](iixssoutil-addscopetoquery.md) method of the objU [Utility](iixssoutil.md) object to add the scope "\\" and all its subdirectories to the query.


```JScript
objU.AddScopeToQuery(objQ, "\\", "deep");
```



 

 




