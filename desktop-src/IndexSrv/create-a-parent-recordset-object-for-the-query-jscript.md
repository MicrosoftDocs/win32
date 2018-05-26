---
title: Create a Parent Recordset Object for the Query
description: Create a Parent Recordset Object for the Query
ms.assetid: ce533ecc-db03-471d-b7d5-f5d374749aea
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create a Parent Recordset Object for the Query

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [CreateRecordset](iixssoquery-createrecordset.md) method of the [Query](iixssoquery.md) object to execute the query and to create objRS\_Parent, an ADO parent [Recordset](mdobjodbrec) object of query results.


```JScript
objRS_Parent = objQ.CreateRecordset("nonsequential");
```



For a description of the "nonsequential" parameter, see [Sequential and Nonsequential Execution](sequential-and-nonsequential-execution.md).

 

 




