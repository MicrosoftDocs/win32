---
Description: DBGROUPINFO
ms.assetid: 37cea731-5289-4b5e-bcf5-2d29887aa31c
title: DBGROUPINFO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBGROUPINFO

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBGROUPINFO** structure represents specific information required by grouping operators, such as project\_list\_ elements used for grouping.

``` syntax
typedef struct tagDBGROUPINFO {
  LCID lcid;  // local ID for text portion of query
} DBGROUPINFO ;
```

 

 



