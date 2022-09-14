---
description: The Remove method removes the item at the specified position.
ms.assetid: a7b8f6fb-f13a-4c24-aa18-463446602e29
title: CGenericList.Remove method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.Remove
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.Remove method

The `Remove` method removes the item at the specified position.

## Syntax


```C++
OBJECT* Remove(
   POSITION pos
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

POSITION value indicating the item to remove.

</dd> </dl>

## Return value

Returns a pointer to an object of type **OBJECT** (the template type).

## Remarks

This method deletes the node from the list, but does not delete the item contained in that node.

If *pos* is **NULL**, the method returns **NULL**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




