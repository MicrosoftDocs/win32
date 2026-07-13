---
description: The SourceThreadCanWait method holds or releases the streaming thread.
ms.assetid: f68f5f0b-ef5b-49a9-a768-c4cc065c0cb3
title: CBaseRenderer.SourceThreadCanWait method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.SourceThreadCanWait
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.SourceThreadCanWait method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SourceThreadCanWait` method holds or releases the streaming thread.

## Syntax


```C++
virtual HRESULT SourceThreadCanWait(
   BOOL bCanWait
);
```



## Parameters

<dl> <dt>

*bCanWait* 
</dt> <dd>

Boolean value indicating whether to hold the streaming thread. If **TRUE**, the streaming thread is blocked while the filter waits to render the next samples. If **FALSE**, the streaming thread is released.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

Calling the `SourceThreadCanWait` method with the value **FALSE** forces the filter to return from a blocked [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) call. When the filter is running, it blocks **Receive** calls until the current sample's presentation time. When the filter is paused, it blocks **Receive** calls indefinitely. This behavior regulates the flow of data in the stream. When the filter is stopped or flushing, however, it should not block.

The blocking is controlled by the [**CBaseRenderer::WaitForRenderTime**](cbaserenderer-waitforrendertime.md) method, which waits on two events: [**CBaseRenderer::m\_RenderEvent**](cbaserenderer-m-renderevent.md) and [**CBaseRenderer::m\_ThreadSignal**](cbaserenderer-m-threadsignal.md). The **m\_RenderEvent** event is signaled when the presentation time arrives. The **m\_ThreadSignal** event is signaled when `SourceThreadCanWait` is called with the value **FALSE**. Calling `SourceThreadCanWait` with the value **TRUE** resets the event.

The [**CBaseRenderer::Stop**](cbaserenderer-stop.md) and [**CBaseRenderer::BeginFlush**](cbaserenderer-beginflush.md) methods call `SourceThreadCanWait` with the value **FALSE** (releasing the streaming thread). The [**CBaseRenderer::Pause**](cbaserenderer-pause.md), [**CBaseRenderer::Run**](cbaserenderer-run.md), and [**CBaseRenderer::EndFlush**](cbaserenderer-endflush.md) methods call `SourceThreadCanWait` with the value **TRUE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




