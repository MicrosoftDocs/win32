---
description: The SendRepaint method sends a repaint event to the filter graph manager.
ms.assetid: 78e5c46c-ca5d-4c5d-9dfc-992ce6b150ad
title: CBaseRenderer.SendRepaint method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.SendRepaint
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.SendRepaint method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SendRepaint` method sends a repaint event to the filter graph manager.

## Syntax


```C++
void SendRepaint();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method sends an [**EC\_REPAINT**](ec-repaint.md) event to the filter graph manager if the following conditions are true:

-   The input pin is connected.
-   The filter is not flushing data.
-   The end-of-stream was not reached.
-   The [**CBaseRenderer::m\_bAbort**](cbaserenderer-m-babort.md) flag is **FALSE**.
-   The [**CBaseRenderer::m\_bRepaintStatus**](cbaserenderer-m-brepaintstatus.md) flag is **TRUE**.

Depending on the state of the graph, the EC\_REPAINT event can cause the upstream filter to re-send a sample; the filter graph to seek to its current location; or the filter graph manager to pause momentarily. (See [**EC\_REPAINT**](ec-repaint.md).) This event is potentially inefficient, so it should be used sparingly. However, video renderers sometimes need to refresh the display.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




