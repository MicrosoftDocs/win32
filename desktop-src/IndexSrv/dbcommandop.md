---
Description: DBCOMMANDOP
ms.assetid: 564e287b-ab3c-484e-8818-1d24ba5246ce
title: DBCOMMANDOP
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBCOMMANDOP

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCOMMANDOP** type specifies the operation for a command node in the OLE DB command tree.

``` syntax
typedef WORD DBCOMMANDOP;
```

### Remarks

In each [**DBCOMMANDTREE**](dbcommandtree.md) structure representing a node in the command tree, **DBCOMMANDOP** takes on the appropriate DBOP\_\* operation value from the [**DBCOMMANDOPENUM**](/previous-versions/windows/desktop/api/cmdtree/ne-cmdtree-dbcommandopenum) enumeration, as described in the [Data Manipulation Operators](data-manipulation-operators.md) and Data Definition Operators section of this reference.

## Related topics

<dl> <dt>

[**DBCOMMANDOPENUM**](/previous-versions/windows/desktop/api/cmdtree/ne-cmdtree-dbcommandopenum)
</dt> <dt>

[**DBCOMMANDTREE**](dbcommandtree.md)
</dt> </dl>

 

 



