---
Description: DBSORTINFO
ms.assetid: 4ab784d9-0458-4690-b5ba-f98c9df056a9
title: DBSORTINFO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBSORTINFO

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBSORTINFO** structure stores the order in which a column will be sorted (that is, ascending or descending). This information is stored inside a DBOP\_sort\_list\_element node.

``` syntax
typedef struct  tagDBSORTINFO {
  BOOL fDesc;  // TRUE = ascending, FALSE = descending
  LCID lcid;   // locale identifier
} DBSORTINFO;
```

### Remarks

The locale identifier (LCID) specifies a set of user preference information related to the user's language. It determines how times are formatted, how items are alphabetically sorted, and how strings are compared.

For additional information on LCIDs see [Locales](https://www.bing.com/search?q=Locales).

 

 



