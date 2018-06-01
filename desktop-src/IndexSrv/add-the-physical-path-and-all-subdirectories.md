---
Description: Add the Physical Path and All Subdirectories
ms.assetid: cf6f0196-dd35-477f-a987-e80600974a49
title: Add the Physical Path and All Subdirectories
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add the Physical Path and All Subdirectories

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**AddScopeToQuery**](iixssoutil-addscopetoquery.md) method of the objU [Utility](iixssoutil.md) object to add the scope "\\" and all its subdirectories to the query.


```VB
objU.AddScopeToQuery objQ, "\", "deep"
```



 

 



