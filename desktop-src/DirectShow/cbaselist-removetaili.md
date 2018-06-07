---
Description: The RemoveTailI method removes the last item in the list.
ms.assetid: 3e9f88a5-a681-4494-8977-d9a6ec62a849
title: CBaseList.RemoveTailI method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseList.RemoveTailI method

The `RemoveTailI` method removes the last item in the list.

## Syntax


```C++
void* RemoveTailI();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the item, or **NULL** if the list is empty.

## Remarks

This method deletes the list node, but not the item that is contained in the node.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




