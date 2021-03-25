---
description: The CurrentRate method retrieves the segment rate, set by the CBasePin::NewSegment method.
ms.assetid: 19780dd2-2dcf-4e5d-8a70-a46be05e040c
title: CBasePin.CurrentRate method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.CurrentRate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.CurrentRate method

The `CurrentRate` method retrieves the segment rate, set by the [**CBasePin::NewSegment**](cbasepin-newsegment.md) method.

## Syntax


```C++
double CurrentRate();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CBasePin::m\_dRate**](cbasepin-m-drate.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




