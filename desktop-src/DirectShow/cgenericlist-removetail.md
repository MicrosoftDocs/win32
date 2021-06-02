---
description: The RemoveTail method removes the last item in the list.
ms.assetid: 377af676-8042-430e-87a6-b41c00482a90
title: CGenericList.RemoveTail method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.RemoveTail
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.RemoveTail method

The `RemoveTail` method removes the last item in the list.

## Syntax


```C++
OBJECT* RemoveTail();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to an object of type **OBJECT** (the template type), or **NULL** if the list is empty.

## Remarks

This method deletes the list node, but not the item that is contained in the node.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




