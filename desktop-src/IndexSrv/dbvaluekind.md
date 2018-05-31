---
title: DBVALUEKIND
description: DBVALUEKIND
ms.assetid: 9d03bbf8-0c39-4762-acfb-74ce4ad1d9d6
keywords:
- DBVALUEKIND
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBVALUEKIND

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBVALUEKIND** type defines a variable that indicates the type of union member inside a [**DBCOMMANDTREE**](dbcommandtree.md) structure.

``` syntax
typedef WORD DBVALUEKIND;
```

### Remarks

In each [**DBCOMMANDTREE**](dbcommandtree.md) structure representing a node in the command tree, **DBVALUEKIND** takes on the appropriate DBVALUEKIND\_\* operation value from the [**DBVALUEKINDENUM**](dbvaluekindenum.md) enumeration, as described in the [Data Manipulation Operators](data-manipulation-operators.md) and Data Definition Operators section of this reference.

## Related topics

<dl> <dt>

[**DBCOMMANDTREE**](dbcommandtree.md)
</dt> <dt>

[**DBVALUEKINDENUM**](dbvaluekindenum.md)
</dt> </dl>

 

 




