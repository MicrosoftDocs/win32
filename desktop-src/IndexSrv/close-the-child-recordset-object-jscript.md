---
title: Close the Child Recordset Object
description: Close the Child Recordset Object
ms.assetid: d013bb41-bbb3-481e-a131-b51ae2918cf1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Close the Child Recordset Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment uses the [**Close**](mdmthclose) method of the objRS\_Child [**Recordset**](mdobjodbrec) object to free the system resources of the child recordset. Setting the objRS\_Child **Recordset** object to null removes the child object from memory.


```JScript
objRS_Child.Close;
Set objRS_Child = null;
```



 

 




