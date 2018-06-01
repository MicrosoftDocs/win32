---
Description: Close the Child Recordset Object
ms.assetid: d013bb41-bbb3-481e-a131-b51ae2918cf1
title: Close the Child Recordset Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Close the Child Recordset Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment uses the [**Close**](https://www.bing.com/search?q=**Close**) method of the objRS\_Child [**Recordset**](https://www.bing.com/search?q=**Recordset**) object to free the system resources of the child recordset. Setting the objRS\_Child **Recordset** object to null removes the child object from memory.


```JScript
objRS_Child.Close;
Set objRS_Child = null;
```



 

 



