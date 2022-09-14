---
description: The RemoveHeadI method removes the first item in the list.
ms.assetid: 7e448e32-ea31-4015-9219-1f990bf8763d
title: CBaseList.RemoveHeadI method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.RemoveHeadI
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




