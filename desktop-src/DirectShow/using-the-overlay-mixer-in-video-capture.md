---
description: Using the Overlay Mixer in Video Capture
ms.assetid: 43468fa2-6dea-439d-9e24-f47a053ad561
title: Using the Overlay Mixer in Video Capture
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Overlay Mixer in Video Capture

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are certain kinds of video that the [Video Renderer](video-renderer-filter.md) filter cannot display by itself. In these situations, the Video Renderer must work with the [Overlay Mixer](overlay-mixer-filter.md) filter. The Overlay Mixer manages the rendering, while the Video Renderer manages the video window. The Overlay Mixer is needed in the following situations:

-   Video port (VP) pins. If the capture device uses a video port, the Overlay Mixer manages the hardware overlay.
-   Interlaced video. For interlaced video, the decoder requires a [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) format, which the Video Renderer does not support.
-   Closed captions. The caption text is rendered as 8-bits-per-pixel bitmaps, which the Overlay Mixer overlays onto the video.

The Capture Graph Builder's **RenderStream** method inserts the Overlay Mixer whenever needed. If you are building the graph without using the Capture Graph Builder, however, you must check for each of these situations and insert the Overlay Mixer yourself.

-   ![Important]  
    > If the device has a VP pin, you must connect the Overlay Mixer even if you do not need preview functionality in your application. With a video port, the capture device always sends the video data to the hardware overlay, so the Overlay Mixer is always needed.

     

The Video Mixing Renderer filters (VMR-7 and VMR-9) both support interlaced video, and are able to mix closed caption bitmaps onto the primary video. If you are using the VMR for those scenarios, then you do not need to use the Overlay Mixer. The VMR-9 does not support VP pin connections. The VMR-7 supports VP pin connections through the Video Port Manager filter. However, you may find that some drivers do not work correctly with the Video Port Manager. For that reason, the Overlay Mixer is still recommended for VP pins.

## Related topics

<dl> <dt>

[Advanced Capture Topics](advanced-capture-topics.md)
</dt> <dt>

[Video Port Pins](video-port-pins.md)
</dt> <dt>

[VideoInfo2 Format Type](videoinfo2-format-type.md)
</dt> </dl>

 

 



