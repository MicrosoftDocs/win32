---
description: The GetPinCount method retrieves the number of pins on the filter.
ms.assetid: 29039ada-fccd-4890-b36b-3dd5c0bbdc3e
title: CTransformFilter.GetPinCount method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.GetPinCount
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.GetPinCount method

The `GetPinCount` method retrieves the number of pins on the filter.

## Syntax


```C++
virtual int GetPinCount();
```



## Parameters

This method has no parameters.

## Return value

Returns 2.

## Remarks

This method overrides the [**CBaseFilter::GetPinCount**](cbasefilter-getpincount.md) method. The **CTransformFilter** class supports exactly one input pin and one output pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




