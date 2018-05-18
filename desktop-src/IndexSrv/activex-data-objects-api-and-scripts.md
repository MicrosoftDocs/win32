---
title: ActiveX Data Objects API and Scripts
description: ActiveX Data Objects API and Scripts
ms.assetid: '97d59c4d-bcc7-4c0a-9ece-cbff64bf3477'
---

# ActiveX Data Objects API and Scripts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [ActiveX Data Objects (ADO) API](programming-apis.md#-idxs-activex-data-objects-api) provides the [**Connection**](mdobjconnection), [**Command**](mdobjcommand), and [**Recordset**](mdobjodbrec) objects for accessing and manipulating data from the [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md). Of these objects, an Indexing Service script typically uses only the **Recordset** object to represent the set of records that results from a query submitted by means of the [Query Helper API](programming-apis.md#-idxs-query-helper-api) (see [Query Helper API and Scripts](query-helper-api-and-scripts.md)).

The following table shows how to use the [**Query.CreateRecordset**](iixssoquery-createrecordset.md) method to create a [**Recordset**](mdobjodbrec) object in scripts.



| Object                       | Creation in VBScript                                        | Creation in JScript                                      |
|------------------------------|-------------------------------------------------------------|----------------------------------------------------------|
| [**Recordset**](mdobjodbrec) | `Set objRecordset = objQuery.CreateRecordset("sequential")` | `objRecordset = objQuery.CreateRecordset("sequential");` |



 

The msad\*.dll files contain the ADO objects.

 

 




