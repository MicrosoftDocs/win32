---
title: Vector Rank Constants
description: Vector Rank Constants
ms.assetid: dc495ce3-4cae-48a9-8193-f13b64c3cc01
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Vector Rank Constants

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The vector rank constants specify the ranking method to use to evaluate the rank of a match in a vector space query.

``` syntax
#define VECTOR_RANK_MIN     ( 0 )  // Use minimum algorithm
#define VECTOR_RANK_MAX     ( 1 )  // Use maximum algorithm
#define VECTOR_RANK_INNER   ( 2 )  // Use inner product algorithm
#define VECTOR_RANK_DICE    ( 3 )  // Use Dice coefficient algorithm
#define VECTOR_RANK_JACCARD ( 4 )  // Use Jaccard coefficient algorithm
```

### Remarks

The **dwRankingMethod** member of the [**DBCONTENTVECTOR**](dbcontentvector.md) structure uses these constants.

 

 




