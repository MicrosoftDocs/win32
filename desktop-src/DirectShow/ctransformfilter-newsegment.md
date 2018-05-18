---
Description: 'The NewSegment method notifies the filter that media samples received after this call are grouped as a segment.'
ms.assetid: '78ddaac7-9c1f-47b6-835d-dd16b1f5b01f'
title: 'CTransformFilter.NewSegment method'
---

# CTransformFilter.NewSegment method

The `NewSegment` method notifies the filter that media samples received after this call are grouped as a segment.

## Syntax


```C++
virtual HRESULT NewSegment(
   REFERENCE_TIME tStart,
   REFERENCE_TIME tStop,
   double         dRate
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




