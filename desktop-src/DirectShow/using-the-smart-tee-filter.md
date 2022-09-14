---
description: Using the Smart Tee Filter
ms.assetid: d2828269-6841-41a8-8d45-f864c7e85857
title: Using the Smart Tee Filter
ms.topic: article
ms.date: 05/31/2018
---

# Using the Smart Tee Filter

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

 

 



