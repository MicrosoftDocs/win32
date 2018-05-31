---
title: DBCONTENTPROXIMITY
description: DBCONTENTPROXIMITY
ms.assetid: 68baff08-435c-4486-84d8-34dcb8991d69
keywords:
- DBCONTENTPROXIMITY
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBCONTENTPROXIMITY

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCONTENTPROXIMITY** structure represents specific information required by the DBOP\_content\_proximity operator.

``` syntax
typedef struct  tagDBCONTENTPROXIMITY    {
  DWORD dwProximityUnit;      // words, paras, chapters etc.
  ULONG ulProximityDistance;  // how near is "near"?
  LONG  lWeight;              // weight of the proximity node
} DBCONTENTPROXIMITY;
```

### Remarks

For valid values of the **dwProximityUnit** member, see [Proximity Unit Constants](proximity-unit-constants.md).

For more information on the DBOP\_content\_proximity operator, see [Content Search Operators](content-search-operators.md).

 

 




