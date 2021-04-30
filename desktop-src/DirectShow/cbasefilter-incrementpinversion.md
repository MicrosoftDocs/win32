---
description: The IncremementPinVersion method increments the version number on the set of pins.
ms.assetid: e1b3ec33-104d-4a12-9b11-f8bea09690a7
title: CBaseFilter.IncrementPinVersion method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.IncrementPinVersion
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.IncrementPinVersion method

The `IncremementPinVersion` method increments the version number on the set of pins.

## Syntax


```C++
void IncrementPinVersion();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method increments the [**CBaseFilter::m\_PinVersion**](cbasefilter-m-pinversion.md) member variable. If the filter dynamically creates or destroys pins, call this method whenever the pins change.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> <dt>

[**CBaseFilter::GetPinVersion**](cbasefilter-getpinversion.md)
</dt> </dl>

 

 




