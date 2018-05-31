---
title: Create a Parent Recordset Object for the Query
description: Create a Parent Recordset Object for the Query
ms.assetid: 23b1011e-5637-4027-9796-293457e811bf
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Create a Parent Recordset Object for the Query

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [CreateRecordset](iixssoquery-createrecordset.md) method of the [Query](iixssoquery.md) object to execute the query and to create objRS\_Parent, an ADO parent [Recordset](mdobjodbrec) object of query results.


```VB
Set objRS_Parent = objQ.CreateRecordset("nonsequential")
```



For a description of the "nonsequential" parameter, see [Sequential and Nonsequential Execution](sequential-and-nonsequential-execution.md).

 

 




