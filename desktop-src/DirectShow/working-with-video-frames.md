---
description: Working with Video Frames
ms.assetid: a5ad74dd-abfd-4810-a512-42e4b98a6c59
title: Working with Video Frames
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Video Frames

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Uncompressed video is a sequence of bitmaps played in rapid succession, typically at a rate of about 30 frames per second. Because most video enters a DirectShow filter graph in a compressed format, the video stream generally goes through a decoder for decompression. Many decoders output data in a YUV format and leave the final conversion to RGB for the video hardware just prior to rendering. If a decoder uses DirectX Video Acceleration, the video hardware performs additional work to decode the image. Thus, final decompression of the bitmaps may not be performed until the data reaches the video hardware.

But to perform many types of video analysis, processing, or editing, it is often necessary to work on uncompressed bitmaps in some type of RGB or YUV format before they are rendered or written to file. This work is typically done within a transform filter based on the [**CTransformFilter**](ctransformfilter.md) base class, specifically in the **Transform** method. This method receives a pointer to an [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) object that encapsulates the video data. The **IMediaSample::GetPointer** method returns a pointer to the first byte of the raw data. For uncompressed frames, this data consists of pixels that can be accessed or modified directly by the filter. The following sections provide background information that will help you work effectively with DIB data in this manner.

> [!Note]  
> You can also modify the bits by using GDI, GDI+, DirectDraw or Direct3D functions, but these techniques are beyond the scope of this article.

 

This section contains the following topics:

-   [Top-Down vs. Bottom-Up DIBs](top-down-vs--bottom-up-dibs.md)
-   [Working with 16-bit RGB](working-with-16-bit-rgb.md)

 

 



