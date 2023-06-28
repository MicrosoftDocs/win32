---
description: The NewSegment method notifies the filter that media samples received after this call are grouped as a segment.
ms.assetid: 78ddaac7-9c1f-47b6-835d-dd16b1f5b01f
title: CTransformFilter.NewSegment method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CTransformFilter.NewSegment method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




