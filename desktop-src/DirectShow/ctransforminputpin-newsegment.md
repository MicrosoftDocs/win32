---
description: The NewSegment method notifies the pin that media samples received after this call are grouped as a segment. This method implements the IPin::NewSegment method.
ms.assetid: 8925b8b5-13dd-4127-82d8-96525bd4d6fc
title: CTransformInputPin.NewSegment method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin.NewSegment
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformInputPin.NewSegment method

The `NewSegment` method notifies the pin that media samples received after this call are grouped as a segment. This method implements the [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment) method.

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

Start time of the segment.

</dd> <dt>

*tStop* 
</dt> <dd>

Stop time of the segment.

</dd> <dt>

*dRate* 
</dt> <dd>

Rate of the segment.

</dd> </dl>

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

This method overrides the [**CBasePin::NewSegment**](cbasepin-newsegment.md) method. It calls the filter's [**CTransformFilter::NewSegment**](ctransformfilter-newsegment.md) method to deliver the call downstream.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




