---
description: The NewSegment method notifies the pin that media samples received after this call are grouped as a segment. Implements the IPin::NewSegment method.
ms.assetid: e334d5a7-0398-496c-882c-bf73e6545867
title: CBasePin.NewSegment method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.NewSegment
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.NewSegment method

The `NewSegment` method notifies the pin that media samples received after this call are grouped as a segment. Implements the [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment) method.

## Syntax


```C++
HRESULT NewSegment(
   REFERENCE_TIME tStart,
   REFERENCE_TIME tStop,
   double         dRate
);
```



## Parameters

<dl> <dt>

*tStart* 
</dt> <dd>

Starting media position of the segment, in 100-nanosecond units.

</dd> <dt>

*tStop* 
</dt> <dd>

End media position of the segment, in 100-nanosecond units.

</dd> <dt>

*dRate* 
</dt> <dd>

Rate at which this segment should be processed, as a percentage of the original rate.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method sets the [**CBasePin::m\_tStart**](cbasepin-m-tstart.md), [**CBasePin::m\_tStop**](cbasepin-m-tstop.md), and [**CBasePin::m\_dRate**](cbasepin-m-drate.md) member variables. In your derived class, override this method to pass the notification downstream.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




