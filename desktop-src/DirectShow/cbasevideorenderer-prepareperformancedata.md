---
description: The PreparePerformanceData method sets the m\_trLate and m\_trFrame values of the current frame.
ms.assetid: c4c5701b-eccd-4259-a1d1-7c5000f6b2df
title: CBaseVideoRenderer.PreparePerformanceData method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.PreparePerformanceData
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseVideoRenderer.PreparePerformanceData method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `PreparePerformanceData` method sets the **m\_trLate** and **m\_trFrame** values of the current frame.

## Syntax


```C++
void PreparePerformanceData(
   int trLate,
   int trFrame
);
```



## Parameters

<dl> <dt>

*trLate* 
</dt> <dd>

Value indicating how late the sample was beyond its due time, in reference time units.

</dd> <dt>

*trFrame* 
</dt> <dd>

Interframe time, in reference time units.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This member function sets **m\_trLate** to the value of *trLate* and **m\_trFrame** to the value of *trFrame*.

When the [**CBaseVideoRenderer::RecordFrameLateness**](cbasevideorenderer-recordframelateness.md) member function is called from either [**CBaseVideoRenderer::OnRenderStart**](cbasevideorenderer-onrenderstart.md) or [**CBaseVideoRenderer::OnDirectRender**](cbasevideorenderer-ondirectrender.md), it passes the values of **m\_trLate** and **m\_trFrame** for it to update the statistics. `PreparePerformanceData` is called from [**CBaseVideoRenderer::OnWaitEnd**](cbasevideorenderer-onwaitend.md) to set these data member values.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




