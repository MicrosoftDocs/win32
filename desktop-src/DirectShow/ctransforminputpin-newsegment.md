---
description: The NewSegment method notifies the pin that media samples received after this call are grouped as a segment. This method implements the IPin::NewSegment method.
ms.assetid: 8925b8b5-13dd-4127-82d8-96525bd4d6fc
title: CTransformInputPin.NewSegment method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CTransformInputPin.NewSegment method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 




