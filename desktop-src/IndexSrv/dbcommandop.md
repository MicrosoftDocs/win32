---
title: DBCOMMANDOP
description: DBCOMMANDOP
ms.assetid: '564e287b-ab3c-484e-8818-1d24ba5246ce'
keywords: ["DBCOMMANDOP"]
---

# DBCOMMANDOP

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCOMMANDOP** type specifies the operation for a command node in the OLE DB command tree.

``` syntax
typedef WORD DBCOMMANDOP;
```

### Remarks

In each [**DBCOMMANDTREE**](dbcommandtree.md) structure representing a node in the command tree, **DBCOMMANDOP** takes on the appropriate DBOP\_\* operation value from the [**DBCOMMANDOPENUM**](dbcommandopenum.md) enumeration, as described in the [Data Manipulation Operators](data-manipulation-operators.md) and Data Definition Operators section of this reference.

## Related topics

<dl> <dt>

[**DBCOMMANDOPENUM**](dbcommandopenum.md)
</dt> <dt>

[**DBCOMMANDTREE**](dbcommandtree.md)
</dt> </dl>

 

 




