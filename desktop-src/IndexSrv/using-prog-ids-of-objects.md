---
title: Using Prog IDs of Objects
description: Using Prog IDs of Objects
ms.assetid: 88b3a919-c751-44d8-9737-dad9d6beb2e0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Prog IDs of Objects

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

You can declare and create objects from the Indexing Service APIs using the prog IDs of the objects. The following table lists the APIs and each object of an API with a prog ID.



| API          | Object                                                       | Prog ID                           |
|--------------|--------------------------------------------------------------|-----------------------------------|
| Admin Helper | [AdminIndexServer](iadminindexserver.md)                    | Microsoft.ISAdm                   |
| Query Helper | [Query](iixssoquery.md)[Utility](iixssoutil.md)<br/> | IXSSO.Query IXSSO.Util<br/> |
| ADO          | [Recordset](mdobjodbrec)                                     | ADODB.Recordset                   |



 

See [Creating Objects with Early and Late Binding](creating-objects-with-early-and-late-binding.md) for details on using this information.

 

 





