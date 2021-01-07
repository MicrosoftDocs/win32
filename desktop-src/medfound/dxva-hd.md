---
description: Microsoft DirectX Video Acceleration High Definition (DXVA-HD) is an API for hardware-accelerated video processing.
ms.assetid: 38ebec28-c4fc-4e72-ac87-1e41707d1908
title: DXVA-HD
ms.topic: article
ms.date: 05/31/2018
---

# DXVA-HD

Microsoft DirectX Video Acceleration High Definition (DXVA-HD) is an API for hardware-accelerated video processing. DXVA-HD uses the GPU to perform functions such as deinterlacing, compositing, and color-space conversion.

DXVA-HD is similar to [DXVA Video Processing](dxva-video-processing.md) (DXVA-VP), but offers enhanced features and a simpler processing model. By providing a more flexible composition model, DXVA-HD is designed to support the next generation of HD optical formats and broadcast standards.

The DXVA-HD API requires either a WDDM display driver that supports the DXVA-HD device driver interface (DDI), or a plug-in software processor.

-   [Improvements over DXVA-VP](#improvements-over-dxva-vp)
-   [Related topics](#related-topics)

## Improvements over DXVA-VP

DXVA-HD expands the set of features provided by DXVA-VP. Enhancements include:

-   RGB and YUV mixing. Any stream can be either RGB or YUV. There is no longer a distinction between the primary stream and the substreams.
-   Deinterlacing of multiple streams. Any stream can be either progressive or interlaced. Moreover, the cadence and frame rate can can vary from one input stream to the next.
-   RGB background colors. Previously, only YUV background colors were supported.
-   Luma keying. When luma keying is enabled, luma values that fall within a designated range become transparent.
-   Dynamic switching between deinterlace modes.

DXVA-HD also defines some advanced features that drivers can support. However, applications should not assume that all drivers will support these features. The advanced features include:

-   Inverse telecine (for example, 60i to 24p).
-   Frame-rate conversion (for example, 24p to 120p).
-   Alpha-fill modes.
-   Noise reduction and edge enhancement filtering.
-   Anamorphic non-linear scaling.
-   Extended YCbCr (xvYCC).

This section contains the following topics.

-   [Creating a DXVA-HD Video Processor](creating-a-dxva-hd-video-processor.md)
-   [Checking Supported DXVA-HD Formats](checking-supported-dxva-hd-formats.md)
-   [Creating DXVA-HD Video Surfaces](creating-dxva-hd-video-surfaces.md)
-   [Setting DXVA-HD States](setting-dxva-hd-states.md)
-   [Performing the DXVA-HD Blit](performing-the-dxva-hd-blit.md)

## Related topics

<dl> <dt>

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)
</dt> <dt>

[DXVA-HD Sample](dxva-hd-sample.md)
</dt> </dl>

 

 



