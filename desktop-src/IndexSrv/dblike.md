---
title: DBLIKE
description: DBLIKE
ms.assetid: 'cd015e0a-ecd3-4aa5-82c0-007fd293ebb9'
keywords: ["DBLIKE"]
---

# DBLIKE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBLIKE** structure represents specific information required by the DBOP\_like operator.

``` syntax
typedef struct tagDBLIKE {
  LONG lWeight;      // weight on the dbop_like node
  GUID guidDialect;  // system to use for "likeness". E.g. Reg. Ex.
} DBLIKE;
```

### Remarks

For more information about the DBOP\_like operator, see [Operators for Scalars](operators-for-scalars.md).

 

 




