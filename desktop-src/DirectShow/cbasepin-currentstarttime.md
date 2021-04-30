---
description: The CurrentStartTime method retrieves the segment start time, set by the CBasePin::NewSegment method.
ms.assetid: 6bf7407e-0b23-47cf-925e-3fed183c76fa
title: CBasePin.CurrentStartTime method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.CurrentStartTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.CurrentStartTime method

The `CurrentStartTime` method retrieves the segment start time, set by the [**CBasePin::NewSegment**](cbasepin-newsegment.md) method.

## Syntax


```C++
REFERENCE_TIME CurrentStartTime();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CBasePin::m\_tStart**](cbasepin-m-tstart.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




