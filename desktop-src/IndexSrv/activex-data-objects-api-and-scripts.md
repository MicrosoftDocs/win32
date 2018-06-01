---
Description: ActiveX Data Objects API and Scripts
ms.assetid: 97d59c4d-bcc7-4c0a-9ece-cbff64bf3477
title: ActiveX Data Objects API and Scripts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ActiveX Data Objects API and Scripts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [ActiveX Data Objects (ADO) API](https://www.bing.com/search?q=ActiveX Data Objects (ADO) API) provides the [**Connection**](https://www.bing.com/search?q=**Connection**), [**Command**](https://www.bing.com/search?q=**Command**), and [**Recordset**](https://www.bing.com/search?q=**Recordset**) objects for accessing and manipulating data from the [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md). Of these objects, an Indexing Service script typically uses only the **Recordset** object to represent the set of records that results from a query submitted by means of the [Query Helper API](https://www.bing.com/search?q=Query Helper API) (see [Query Helper API and Scripts](query-helper-api-and-scripts.md)).

The following table shows how to use the [**Query.CreateRecordset**](iixssoquery-createrecordset.md) method to create a [**Recordset**](https://www.bing.com/search?q=**Recordset**) object in scripts.



| Object                       | Creation in VBScript                                        | Creation in JScript                                      |
|------------------------------|-------------------------------------------------------------|----------------------------------------------------------|
| [**Recordset**](https://www.bing.com/search?q=**Recordset**) | `Set objRecordset = objQuery.CreateRecordset("sequential")` | `objRecordset = objQuery.CreateRecordset("sequential");` |



 

The msad\*.dll files contain the ADO objects.

 

 



