---
title: Close the Child Recordset Object
description: Close the Child Recordset Object
ms.assetid: 61ac7d77-8377-4fd7-815c-4f3d2cfd45df
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Close the Child Recordset Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment uses the [**Close**](https://www.bing.com/search?q=**Close**) method of the objRS\_Child [**Recordset**](https://www.bing.com/search?q=**Recordset**) object to free the system resources of the child recordset. Setting the objRS\_Child **Recordset** object to **Nothing** removes the child object from memory.


```VB
objRS_Child.Close
Set objRS_Child = Nothing
```



 

 




