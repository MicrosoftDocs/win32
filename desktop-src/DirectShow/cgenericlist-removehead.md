---
description: The RemoveHead method removes the first item in the list.
ms.assetid: 95902028-d2c2-4c16-9ca6-ef57174a9292
title: CGenericList.RemoveHead method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.RemoveHead
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.RemoveHead method

The `RemoveHead` method removes the first item in the list.

## Syntax


```C++
OBJECT* RemoveHead();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to an object of type **OBJECT** (the template type), or **NULL** if the list is empty.

## Remarks

This method deletes the list node, but not the item that the node contains.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




