---
description: MSYUV is a YUV-to-RGB color space converter codec.
ms.assetid: 77b00937-ac63-4b23-b546-c0896b3c57ba
title: MSYUV Color Space Converter Codec
ms.topic: reference
ms.date: 05/31/2018
---

# MSYUV Color Space Converter Codec

MSYUV is a YUV-to-RGB color space converter codec. It enables playback of video source data in YUV formats on clients whose video display adapter cannot be used for YUV-to-RGB conversions in hardware. The codec participates in filter graphs through the [AVI Decompressor](avi-decompressor-filter.md) wrapper filter.

Digital conferencing cameras with 1394 or USB interfaces can produce image data in various YUV formats. If the display hardware does not support on-board YUV-to-RGB conversion, or if the hardware conversion capability cannot be used for some other reason, then the YUV image data must be converted to RGB format before it is sent to the Video Renderer.

Because of the [Video Renderer](video-renderer-filter.md)'s requirement for an RGB input type at connection time, this filter might be inserted into a graph upstream from the Video Renderer during automatic graph building. Specifically, if the Graph Builder detects a YUV format in the media type of the upstream filter's output pin, the Graph Builder will insert the AVI Decompressor, which will then load the MSYUV codec and configure it initially to perform the conversion to RGB. After the graph first transitions to a run or paused state, the Video Renderer filter can detect whether the video display adapter can perform the conversion in hardware. If it can, then the AVI Decompressor is notified and it reconfigures MSYUV to operate in "pass-through mode," which causes the codec to skip the conversion and copy the YUV image data directly onto a DirectDraw overlay surface in video memory.

Because the Video Mixing Renderers (VMR-7 and VMR-9) never use GDI, they do not require an RGB type at connect time, and the MSYUV Color Space Converter is never inserted before the VMR in a graph.

MSYUV converts packed YUV formats to RGB, as shown in the following list:

-   Input formats: UYVY, YUY2, YVYU
-   Output formats: RGB 8, RGB 16, RGB 24, RGB 32

The MSYUV Color Space Converter Codec is a Video Compression Manager (VCM) codec. It is used in DirectShow through the [AVI Decompressor](avi-decompressor-filter.md) filter. For a more general-purpose color converter, use the [**Color Converter DSP**](../medfound/colorconverter.md).

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msyuv.dll</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 
