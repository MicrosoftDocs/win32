---
Description: The RemoveHeadI method removes the first item in the list.
ms.assetid: 7e448e32-ea31-4015-9219-1f990bf8763d
title: CBaseList.RemoveHeadI method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseList.RemoveHeadI method

The `RemoveHeadI` method removes the first item in the list.

## Syntax


```C++
void* RemoveHeadI();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the item, or **NULL** if the list is empty.

## Remarks

This method deletes the list node, but not the item that the node contains.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




