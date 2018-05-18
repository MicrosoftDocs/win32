---
title: Create a Query Object
description: Create a Query Object
ms.assetid: 'e4d08430-5536-48da-8308-7af43e0154dc'
---

# Create a Query Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the **CreateObject** method of the **WScript** (Windows Script Host) object to create objQ, a [**Query**](iixssoquery.md) object, from Ixsso.dll


```VB
Set objQ = WScript.CreateObject("IXSSO.Query")
```



 

 




