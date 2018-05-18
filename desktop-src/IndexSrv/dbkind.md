---
title: DBKIND
description: DBKIND
ms.assetid: '06e054f6-4d77-463e-91cb-5b2168145d89'
keywords: ["DBKIND"]
---

# DBKIND

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBKIND** type defines a variable that specifies the type of database object in a command tree.

``` syntax
typedef WORD DBKIND;
```

### Remarks

In each [**DBCOMMANDTREE**](dbcommandtree.md) structure representing a node in the command tree, **DBKIND** takes on the appropriate DBKIND\_\* value from the [**DBKINDENUM**](dbkindenum.md) enumeration, as described in the [Data Manipulation Operators](data-manipulation-operators.md) and Data Definition Operators section of this reference.

## Related topics

<dl> <dt>

[**DBCOMMANDTREE**](dbcommandtree.md)
</dt> <dt>

[**DBKINDENUM**](dbkindenum.md)
</dt> </dl>

 

 




