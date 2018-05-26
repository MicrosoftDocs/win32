---
title: Create a Utility Object
description: Create a Utility Object
ms.assetid: e3128aaa-fc4a-499b-8b93-39396088663c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create a Utility Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the **CreateObject** method of the **WScript** object to create objU, a [**Utility**](iixssoutil.md) object, from Ixsso.dll


```VB
Set objU = WScript.CreateObject("IXSSO.Util")
```



 

 




