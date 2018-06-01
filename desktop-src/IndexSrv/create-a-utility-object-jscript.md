---
Description: Create a Utility Object
ms.assetid: ec145653-d60a-464d-b22b-38c423046b81
title: Create a Utility Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Create a Utility Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment creates objU, a [Utility](iixssoutil.md) object, as a new ActiveXObject object from Ixsso.dll


```JScript
objU = new ActiveXObject("IXSSO.Util");
```



 

 



