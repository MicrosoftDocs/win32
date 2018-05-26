---
title: Create a Child Recordset Object for Chaptered Columns
description: Create a Child Recordset Object for Chaptered Columns
ms.assetid: b6f04900-ab94-4c25-b12c-f277e1448220
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create a Child Recordset Object for Chaptered Columns

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment uses the **Value** property of the "Chapter" [Field](mdobjfield) object of the parent objRS\_Parent [Recordset](mdobjodbrec) object to create a child objRS\_Child **Recordset** object.


```JScript
objRS_Child = objRS_Parent.Fields("Chapter").Value;
```



 

 




