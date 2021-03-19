---
description: The GetPinVersion method retrieves a version number for the set of pins on this filter.
ms.assetid: 6cc186b2-4d9f-4d1c-a8b3-975e9c248df7
title: CBaseFilter.GetPinVersion method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.GetPinVersion
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.GetPinVersion method

The `GetPinVersion` method retrieves a version number for the set of pins on this filter.

## Syntax


```C++
virtual long GetPinVersion();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBaseFilter::m\_PinVersion**](cbasefilter-m-pinversion.md) member variable.

## Remarks

The **CBaseFilter** constructor initializes the pin version to 1. In the base class, this number never changes. If the filter dynamically creates or destroys pins, it should increment the pin version whenever the pins change. To increment the version number, call the [**CBaseFilter::IncrementPinVersion**](cbasefilter-incrementpinversion.md) method.

The pin enumerator object, which is implemented by the [**CEnumPins**](cenumpins.md) class, uses the pin version to keep itself synchronized with the filter.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




