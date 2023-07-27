---
description: Advanced Capture Topics
ms.assetid: 407702b2-5f4f-424d-a3ec-b0473e1b0da3
title: Advanced Capture Topics
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Advanced Capture Topics

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes some advanced aspects of video capture in DirectShow. Most of the issues described in this section are automatically handled by the [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interface. However, the information here may be useful if you need to troubleshoot a video capture application. You should also read this section if your application builds a custom capture graph of some kind and you find that ICaptureGraphBuilder2 does not suit your needs. Finally, this section contains some information about using the Video Mixing Renderer (VMR) filter in a video capture application.

It is possible to build a video capture graph entirely using [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) methods. You can also combine the two interfaces, using ICaptureGraphBuilder2 for some tasks and IGraphBuilder for others.

This section contains the following topics:

-   [Handling Repaint Events in Video Capture](handling-repaint-events-in-video-capture.md)
-   [Working with Pin Categories](working-with-pin-categories.md)
-   [Using the Smart Tee Filter](using-the-smart-tee-filter.md)
-   [Using the Overlay Mixer in Video Capture](using-the-overlay-mixer-in-video-capture.md)
-   [Video Port Pins](video-port-pins.md)
-   [VideoInfo2 Format Type](videoinfo2-format-type.md)
-   [Creating Kernel-Mode Filters](creating-kernel-mode-filters.md)
-   [WDM Class Driver Filters](wdm-class-driver-filters.md)
-   [Using WDDM Capture in DirectShow](using-wddm-capture-in-directshow.md)

## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



