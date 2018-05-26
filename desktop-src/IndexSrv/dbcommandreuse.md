---
title: DBCOMMANDREUSE
description: DBCOMMANDREUSE
ms.assetid: 0749eb01-c367-4290-a6c4-bbf0e1b97aec
keywords:
- DBCOMMANDREUSE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBCOMMANDREUSE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCOMMANDREUSE** type defines a variable that specifies whether a state from the previous command is retained.

``` syntax
typedef WORD DBCOMMANDREUSE;
```

### Remarks

In each [**DBCOMMANDTREE**](dbcommandtree.md) structure representing a node in the command tree,**DBCOMMANDREUSE** takes on the appropriate DBCOMMANDREUSE\_\* value from the [**DBCOMMANDREUSEENUM**](/windows/previous-versions/cmdtree/ne-cmdtree-dbcommandreuseenum?branch=master) enumeration, as described in the [Data Manipulation Operators](data-manipulation-operators.md) and Data Definition Operators section of this reference.

## Related topics

<dl> <dt>

[**DBCOMMANDREUSEENUM**](/windows/previous-versions/cmdtree/ne-cmdtree-dbcommandreuseenum?branch=master)
</dt> <dt>

[**DBCOMMANDTREE**](dbcommandtree.md)
</dt> </dl>

 

 




