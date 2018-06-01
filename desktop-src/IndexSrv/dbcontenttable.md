---
Description: DBCONTENTTABLE
ms.assetid: 31a82f8a-1675-474d-b477-0acdf6accdfb
title: DBCONTENTTABLE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBCONTENTTABLE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCONTENTTABLE** structure represents the machine and catalog names for a command tree.

``` syntax
typedef struct tagDBCONTENTTABLE {
  LPOLESTR pwszMachine;  // machine on which to process query
  LPOLESTR pwszCatalog;  // catalog over which to process query
} DBCONTENTTABLE;
```

 

 



