---
Description: Close the Parent Recordset Object
ms.assetid: 03738755-de3a-4330-a91e-7079ee00e0eb
title: Close the Parent Recordset Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Close the Parent Recordset Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**Close**](https://www.bing.com/search?q=**Close**) method of the objRS\_Parent [**Recordset**](https://www.bing.com/search?q=**Recordset**) object to free the system resources of the parent recordset. Setting the objRS\_Parent **Recordset** object to Null removes the parent object from memory.


```JScript
objRS_Parent.Close;
objRS_Parent = null;
```



 

 



