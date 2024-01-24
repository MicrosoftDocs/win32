---
description: Using the Smart Tee Filter
ms.assetid: d2828269-6841-41a8-8d45-f864c7e85857
title: Using the Smart Tee Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Smart Tee Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If a capture filter has separate capture and preview pins, you can capture from one while previewing from the other. But if the filter has no preview pin, you can do the same thing by including the [Smart Tee](smart-tee-filter.md) filter in the graph. This filter splits data from the capture pin into two identical streams, one for capture and one for preview. The following diagram illustrates this process.

![capture graph with smart tee filter](images/vidcap05.png)

The [**ICaptureGraphBuilder2::RenderStream**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-renderstream) method automatically inserts the Smart Tee Filter if it is required. However, if you use **IGraphBuilder** methods to build your graph, and not **RenderStream**, you may need to insert the Smart Tee filter.

Before you render pins on the capture filter, check whether the filter has a preview pin or a video port pin. If it does not, and you wish to preview, add the Smart Tee filter to the graph and connect it to the capture pin on the capture filter.

> [!Note]  
> You can treat a video port (VP) pin as a kind of preview pin, so a filter with a VP pin does not need a Smart Tee filter. However, VP pins have some other special requirements. For more information, see [Video Port Pins](video-port-pins.md).

 

## Related topics

<dl> <dt>

[Advanced Capture Topics](advanced-capture-topics.md)
</dt> <dt>

[Combining Video Capture and Preview](combining-video-capture-and-preview.md)
</dt> <dt>

[Working with Pin Categories](working-with-pin-categories.md)
</dt> </dl>

 

 



