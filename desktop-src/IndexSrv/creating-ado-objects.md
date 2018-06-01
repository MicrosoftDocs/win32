---
title: Creating ADO Objects
description: Creating ADO Objects
ms.assetid: 0f149af0-c0e7-4165-ab65-c1f3fb100c1d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating ADO Objects

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [ActiveX Data Objects (ADO) API](https://www.bing.com/search?q=ActiveX Data Objects (ADO) API) provides the [**Connection**](https://www.bing.com/search?q=**Connection**), [**Command**](https://www.bing.com/search?q=**Command**), and [**Recordset**](https://www.bing.com/search?q=**Recordset**) objects for accessing and manipulating data from the [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md). Of these objects, an Indexing Service application typically uses just the **Recordset** object to represent the set of records resulting from a query submitted using the [Query Helper API](https://www.bing.com/search?q=Query Helper API) (see [Creating Query Helper Objects](creating-query-helper-objects.md)).

The following table shows how to declare a **Recordset** object with either early or late binding.



| Object                                  | Early Binding                                                                                               | Late Binding                            |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| [**Recordset**](https://www.bing.com/search?q=**Recordset**)<br/> | `Dim objRecordset as ADODB.Recordset`<br/> Or<br/> `Reference to ADODB Type Library`<br/> | `Dim objRecordset as Object`<br/> |



 

You subsequently can use either of the following statements to create the **Recordset** object.


```VB
Set objRecordset = New ADODB.Recordset
Set objRecordset = objQuery.CreateRecordset("ADODB.Recordset")
```



 

 





