---
title: Aggregate Function Constants
description: Aggregate Function Constants
ms.assetid: 'b9b4ea13-9db7-498e-b62f-acbe76c2bb3b'
---

# Aggregate Function Constants

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The aggregate function constants specify which method of aggregation to use in a select operation.

``` syntax
#define DBSETFUNC_NONE     = 0x0
#define DBSETFUNC_ALL      = 0x1
#define DBSETFUNC_DISTINCT = 0x2
```

### Remarks

The **dwSetQuantifier** member of the [**DBSETFUNC**](dbsetfunc.md) structure uses these constants.

These constants are currently reserved for future use.

 

 




