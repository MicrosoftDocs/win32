---
description: The ScheduleSample method schedules a sample for rendering.
ms.assetid: 08c218d1-6d0a-4c66-bbde-a39e5d31561c
title: CBaseRenderer.ScheduleSample method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.ScheduleSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.ScheduleSample method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ScheduleSample` method schedules a sample for rendering.

## Syntax


```C++
virtual BOOL ScheduleSample(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

Returns **TRUE** if the sample was scheduled, or **FALSE** if the sample was dropped.

## Remarks

This method first determines whether the sample should be rendered immediately, rendered in the future, or dropped. (To do so, it calls the [**CBaseRenderer::GetSampleTimes**](cbaserenderer-getsampletimes.md) method.) If the sample should be rendered immediately, the method signals the [**CBaseRenderer::m\_RenderEvent**](cbaserenderer-m-renderevent.md) event. If the sample should be rendered in the future, the method calls the [**IReferenceClock::AdviseTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-advisetime) method for scheduling.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




