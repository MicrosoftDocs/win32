---
title: MSVidVideoRendererDevices
description: MSVidVideoRendererDevices
ms.assetid: cf8e1307-b4a5-464b-b9a6-32c195941309
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSVidVideoRendererDevices

This topic applies to Windows XP or later.

The **MSVidVideoRendererDevices** object represents a collection of video renderers.



|                           |                                                                  |
|---------------------------|------------------------------------------------------------------|
| Interfaces                | [**IMSVidVideoRendererDevices**](/windows/win32/segment/nn-segment-imsvidvideorendererdevices?branch=master) |
| Outgoing Event Interfaces | None.                                                            |



 

## Remarks

To obtain this collection, call the [**IMSVidCtl::get\_VideoRenderersAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_videorenderersavailable?branch=master) method. In practice, this collection will only contain a single object, representing the Video Mixing Renderer filter.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




