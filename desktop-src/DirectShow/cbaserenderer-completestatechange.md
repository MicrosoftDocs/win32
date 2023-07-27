---
description: The CompleteStateChange method determines whether a transition to the paused state is complete.
ms.assetid: 505a0b31-deaa-46be-91e6-f9bc8e47dd3a
title: CBaseRenderer.CompleteStateChange method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.CompleteStateChange
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.CompleteStateChange method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CompleteStateChange` method determines whether a transition to the paused state is complete.

## Syntax


```C++
virtual HRESULT CompleteStateChange(
   FILTER_STATE OldState
);
```



## Parameters

<dl> <dt>

*OldState* 
</dt> <dd>

State prior to the transition.

</dd> </dl>

## Return value

Returns S\_OK if the transition is complete. Otherwise, returns S\_FALSE.

## Remarks

The [**CBaseRenderer::Pause**](cbaserenderer-pause.md) method calls this method to update the state-transition status. In general, the transition to paused does not finish until the filter receives a sample. However, in some situations the transition completes immediately: for example, if the filter is unconnected, or if the end of the stream was reached. This method checks the various criteria and then calls the [**CBaseRenderer::Ready**](cbaserenderer-ready.md) method or the [**CBaseRenderer::NotReady**](cbaserenderer-notready.md) method to update the transition status.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




