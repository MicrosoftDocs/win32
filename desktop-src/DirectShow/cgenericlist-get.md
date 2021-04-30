---
description: The Get method retrieves the item at the specified position.
ms.assetid: cafa4083-96e6-4ed3-afbc-5828b7f1c5be
title: CGenericList.Get method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.Get
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.Get method

The `Get` method retrieves the item at the specified position.

## Syntax


```C++
OBJECT* Get(
   POSITION pos
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position indicator for the item to retrieve.

</dd> </dl>

## Return value

Returns a pointer to an object of type **OBJECT** (the template type).

## Remarks

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

 

 




