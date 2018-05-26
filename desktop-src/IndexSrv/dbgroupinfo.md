---
title: DBGROUPINFO
description: DBGROUPINFO
ms.assetid: 37cea731-5289-4b5e-bcf5-2d29887aa31c
keywords:
- DBGROUPINFO
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBGROUPINFO

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBGROUPINFO** structure represents specific information required by grouping operators, such as project\_list\_ elements used for grouping.

``` syntax
typedef struct tagDBGROUPINFO {
  LCID lcid;  // local ID for text portion of query
} DBGROUPINFO ;
```

 

 




