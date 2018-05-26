---
title: DBCONTENT
description: DBCONTENT
ms.assetid: 10481e54-8b01-43e4-802f-b77bf79b14cb
keywords:
- DBCONTENT
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBCONTENT

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCONTENT** structure represents specific information required by the DBOP\_content operator.

``` syntax
typedef struct tagDBCONTENT {
  LPWSTR pwszPhrase;        // text
  DWORD  dwGenerateMethod;  // exact, prefix, stemmed
  LONG   lWeight;           // weight of node
  LCID   lcid;              // locale
} DBCONTENT;
```

### Remarks

For valid values of the **dwGenerateMethod** member, see [Generate Method Constants](generate-method-constants.md).

For more information on the DBOP\_content operator, see [Content Search Operators](content-search-operators.md).

 

 




