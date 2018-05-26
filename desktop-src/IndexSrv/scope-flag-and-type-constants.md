---
title: Scope Flag and Type Constants
description: Scope Flag and Type Constants
ms.assetid: 1385982d-ebf7-48a3-9697-2f348f5d13e8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Scope Flag and Type Constants

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The scope flag and type constants specify whether to include a scope and its subdirectories and whether the scope is a physical or virtual path.

``` syntax
#define SCOPE_FLAG_MASK    ( 0x000000ff )  // mask to select flag
#define SCOPE_FLAG_INCLUDE ( 0x00000001 )  // include scope
#define SCOPE_FLAG_DEEP    ( 0x00000002 )  // include subdirectories
 
#define SCOPE_TYPE_MASK    ( 0xffffff00 )  // mask to select type
#define SCOPE_TYPE_WINPATH ( 0x00000100 )  // scope is physical
#define SCOPE_TYPE_VPATH   ( 0x00000200 )  // scope is virtual
```

 

 




