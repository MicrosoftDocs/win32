---
description: The CurrentStopTime method retrieves the segment stop time, set by the CBasePin::NewSegment method.
ms.assetid: 2066c4a5-2d39-4a2e-b2d6-48c615862aec
title: CBasePin.CurrentStopTime method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.CurrentStopTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.CurrentStopTime method

The `CurrentStopTime` method retrieves the segment stop time, set by the [**CBasePin::NewSegment**](cbasepin-newsegment.md) method.

## Syntax


```C++
REFERENCE_TIME CurrentStopTime();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CBasePin::m\_tStop**](cbasepin-m-tstop.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




