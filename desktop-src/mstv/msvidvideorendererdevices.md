---
title: MSVidVideoRendererDevices
description: MSVidVideoRendererDevices
ms.assetid: cf8e1307-b4a5-464b-b9a6-32c195941309
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSVidVideoRendererDevices

This topic applies to Windows XP or later.

The **MSVidVideoRendererDevices** object represents a collection of video renderers.



|                           |                                                                  |
|---------------------------|------------------------------------------------------------------|
| Interfaces                | [**IMSVidVideoRendererDevices**](/windows/desktop/api/segment/nn-segment-imsvidvideorendererdevices) |
| Outgoing Event Interfaces | None.                                                            |



 

## Remarks

To obtain this collection, call the [**IMSVidCtl::get\_VideoRenderersAvailable**](imsvidctl-get-videorenderersavailable.md) method. In practice, this collection will only contain a single object, representing the Video Mixing Renderer filter.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




