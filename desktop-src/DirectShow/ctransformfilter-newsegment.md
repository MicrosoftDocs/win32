---
description: The NewSegment method notifies the filter that media samples received after this call are grouped as a segment.
ms.assetid: 78ddaac7-9c1f-47b6-835d-dd16b1f5b01f
title: CTransformFilter.NewSegment method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.NewSegment
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.NewSegment method

The `NewSegment` method notifies the filter that media samples received after this call are grouped as a segment.

## Syntax


```C++
virtual HRESULT NewSegment(
   REFERENCE_TIME tStart,
   REFERENCE_TIME tStop,
   double         dRate
);
```



## Parameters

<dl> <dt>

*tStart* 
</dt> <dd>

Start time of the segment, relative to the original source.

</dd> <dt>

*tStop* 
</dt> <dd>

Stop time of the segment, relative to the original source.

</dd> <dt>

*dRate* 
</dt> <dd>

Rate at which the segment should be processed.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

The input pin's [**CTransformInputPin::NewSegment**](ctransforminputpin-newsegment.md) method calls this method. This method delivers the `NewSegment` call to the downstream input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




