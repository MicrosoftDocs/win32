---
title: Create a Utility Object
description: Create a Utility Object
ms.assetid: ec145653-d60a-464d-b22b-38c423046b81
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create a Utility Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment creates objU, a [Utility](iixssoutil.md) object, as a new ActiveXObject object from Ixsso.dll


```JScript
objU = new ActiveXObject("IXSSO.Util");
```



 

 




