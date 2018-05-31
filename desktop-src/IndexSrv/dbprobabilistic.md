---
title: DBPROBABILISTIC
description: DBPROBABILISTIC
ms.assetid: 5bb8f10a-83a6-4b03-b50b-cdfe41a8546a
keywords:
- DBPROBABILISTIC
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBPROBABILISTIC

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBPROBABILISTIC** structure is reserved for future use.

``` syntax
typedef struct tagDBPROBABILISTIC {
  LONG  lWeight;
  float flK1;
  float flK2;
  float flK3;
  float flB;
} DBPROBABILISTIC;
```

 

 




