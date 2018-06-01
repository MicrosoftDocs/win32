---
title: Query Helper API and Scripts
description: Query Helper API and Scripts
ms.assetid: 7571f851-e100-4e53-9b5c-4722d9950cd0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query Helper API and Scripts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [Query Helper API](https://www.bing.com/search?q=Query Helper API) provides the [**Query**](iixssoquery.md) and [**Utility**](iixssoutil.md) objects for creating and managing queries to the [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md). A script can use these objects along with a Microsoft ActiveX Data Objects (ADO) [**Recordset**](https://www.bing.com/search?q=**Recordset**) object (see [ActiveX Data Objects API and Scripts](activex-data-objects-api-and-scripts.md)), which represents the resulting records from a query.

The following table shows how to create a [**Query**](iixssoquery.md) object and a [**Utility**](iixssoutil.md) object in scripts.



| Object                        | Creation in VBScript                                  | Creation in JScript                             |
|-------------------------------|-------------------------------------------------------|-------------------------------------------------|
| [**Query**](iixssoquery.md)  | `Set objQuery = WScript.CreateObject("IXSSO.Query")`  | `objQuery = new ActiveXObject("IXSSO.Query");`  |
| [**Utility**](iixssoutil.md) | `Set objUtility = WScript.CreateObject("IXSSO.Util")` | `objUtility = new ActiveXObject("IXSSO.Util");` |



 

The Ixsso.dll file contains the objects of the Query Helper API.

 

 




