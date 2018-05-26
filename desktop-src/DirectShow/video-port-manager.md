---
Description: Video Port Manager
ms.assetid: d70558a5-9820-432a-b4f3-ccf7bb2a34d5
title: Video Port Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Port Manager

The Video Port Manager filter (VPM) enables the Video Mixing Renderer Filter 7 (VMR-7) to work with video capture devices or hardware decoders that use a video port. A video port is a direct hardware connection to the graphics chip. It enables video to be transferred directly to the graphics chip without going over the system bus.

> [!Note]  
> The Video Port Manager is not compatible with the VMR-9, because the VMR-9 does not support video ports.

 



|                                          |                                                                                                                                                                                                                      |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMVideoDecimationProperties**](/windows/win32/Strmif/nn-strmif-iamvideodecimationproperties?branch=master), [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IKsPropertySet**](ikspropertyset.md), [**IQualProp**](/windows/win32/Amvideo/nn-amvideo-iqualprop?branch=master), [**IVPManager**](/windows/win32/Strmif/nn-strmif-ivpmanager?branch=master) |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_VPVideo or MEDIASUBTYPE\_VPVBI, FORMAT\_None                                                                                                                                         |
| Input Pin Interfaces                     | [**IKsPin**](ikspin.md), [**IKsPropertySet**](ikspropertyset.md), [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IPinConnection**](/windows/win32/Strmif/nn-strmif-ipinconnection?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) |
| Output Pin Media Types                   | MEDIATYPE\_Video, FORMAT\_VideoInfo2                                                                                                                                                                                 |
| Output Pin Interfaces                    | [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                                                                                                     |
| Filter CLSID                             | CLSID\_VideoPortManager                                                                                                                                                                                              |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                                                                                                                                                        |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                        |



 

## Remarks

The Video Port Manager combines the video port functionality of the [Overlay Mixer Filter](overlay-mixer-filter.md) and the functionality of the [VBI Surface Allocator](vbi-surface-allocator.md). The VPM allocates video ports and surfaces, and synchronizes data capture from the video port. It allows video port-based capture that is independent of rendering. If preview is desired, the VPM coordinates with the VMR-7 to display captured video port data. When a video port is present on the system, the capture filter requires additional buffers to extract VBI data from the video stream. These buffers are provided by the VPM. Once the capture filter has extracted the VBI data, it delivers it on a separate pin to filters such as the CC Decoder. The following illustration shows the VPM and its connections in a filter graph.

![video port manager filter graph segment](images/vpm.png)

The DVD Graph Builder adds the VPM to the filter graph automatically when a video port is detected on the system. Once added to the graph, the VPM uses a DirectDraw object provided by the Video Mixing Renderer to allocate two or three surfaces. These surfaces receive the digitized frames from the upstream capture filter. In response to user-mode event notifications sent when data is present in the surface, the VPM performs an automatic blit to an offscreen surface provided by the VMR.

The fact that the VPM uses multiple surfaces for its input buffers means that it requires more VRAM than the previous DirectShow video port implementation. The extra blit from the VPM to the VMR-7 requires additional video memory bandwidth. And since hardware auto-flipping is not used any longer, there is a theoretical potential for dropped frames, but the empirical evidence suggests that this does not occur.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[**IVPManager Interface**](/windows/win32/Strmif/nn-strmif-ivpmanager?branch=master)
</dt> </dl>

 

 



