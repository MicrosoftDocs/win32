---
Description: DBCOMMANDREUSE
ms.assetid: 0749eb01-c367-4290-a6c4-bbf0e1b97aec
title: DBCOMMANDREUSE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBCOMMANDREUSE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCOMMANDREUSE** type defines a variable that specifies whether a state from the previous command is retained.

``` syntax
typedef WORD DBCOMMANDREUSE;
```

### Remarks

In each [**DBCOMMANDTREE**](dbcommandtree.md) structure representing a node in the command tree,**DBCOMMANDREUSE** takes on the appropriate DBCOMMANDREUSE\_\* value from the [**DBCOMMANDREUSEENUM**](/previous-versions/windows/desktop/api/cmdtree/ne-cmdtree-dbcommandreuseenum) enumeration, as described in the [Data Manipulation Operators](data-manipulation-operators.md) and Data Definition Operators section of this reference.

## Related topics

<dl> <dt>

[**DBCOMMANDREUSEENUM**](/previous-versions/windows/desktop/api/cmdtree/ne-cmdtree-dbcommandreuseenum)
</dt> <dt>

[**DBCOMMANDTREE**](dbcommandtree.md)
</dt> </dl>

 

 



