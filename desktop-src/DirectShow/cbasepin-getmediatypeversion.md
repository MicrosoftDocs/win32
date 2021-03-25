---
description: The GetMediaTypeVersion method retrieves a version number for the set of preferred media types.
ms.assetid: bd7b8070-eac5-458c-ada0-7fb0d789dd54
title: CBasePin.GetMediaTypeVersion method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.GetMediaTypeVersion
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.GetMediaTypeVersion method

The `GetMediaTypeVersion` method retrieves a version number for the set of preferred media types.

## Syntax


```C++
virtual LONG GetMediaTypeVersion();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBasePin::m\_TypeVersion**](cbasepin-m-typeversion.md) member variable.

## Remarks

The **CBasePin** constructor initializes the version number to 1. In the base class, this number never changes. If the pin dynamically changes its list of preferred media types, it should increment the version number whenever the list changes. To increment the version number, call the [**CBasePin::IncrementTypeVersion**](cbasepin-incrementtypeversion.md) method.

The media type enumerator, which is implemented by the [**CEnumMediaTypes**](cenummediatypes.md) class, uses the version number to keep itself synchronized with the pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




