---
title: DBSETFUNC
description: DBSETFUNC
ms.assetid: '8d2f5482-1e65-4b1c-8743-414041d27b0f'
keywords: ["DBSETFUNC"]
---

# DBSETFUNC

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBSETFUNC** structure specifies the aggregation function to use in a select operation.

``` syntax
typedef struct tagDBSETFUNC {
  DWORD dwSetQuantifier;  // which aggregation method to use
} DBSETFUNC;
```

### Remarks

For valid values of the **dwSetQuantifier** member, see [Aggregate Function Constants](aggregate-function-constants.md).

 

 




