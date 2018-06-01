---
Description: DBCONTENTVECTOR
ms.assetid: 73b06bb8-f880-4901-b5fd-efdf7ad1424d
title: DBCONTENTVECTOR
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBCONTENTVECTOR

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCONTENTVECTOR** structure represents specific information required by the DBOP\_content\_vector\_or operator.

``` syntax
typedef struct tagDBCONTENTVECTOR {
  DWORD dwRankingMethod;  // jaccard, dice, etc.
  LONG  lWeights;         // node weight
} DBCONTENTVECTOR ;
```

### Remarks

For valid values of the **dwRankingMethod** member, see [Vector Rank Constants](vector-rank-constants.md).

For more information on the DBOP\_content\_vector operator, see [Content Search Operators](content-search-operators.md).

 

 



