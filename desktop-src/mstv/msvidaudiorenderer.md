---
title: MSVidAudioRenderer
description: MSVidAudioRenderer
ms.assetid: 'f822b5a6-c88e-48c9-91f4-611a3f147fe0'
---

# MSVidAudioRenderer

This topic applies to Windows XP or later.

The **MSVidAudioRenderer** object represents the audio renderer.



|                           |                                                              |
|---------------------------|--------------------------------------------------------------|
| Interfaces                | [**IMSVidAudioRenderer**](imsvidaudiorenderer.md)           |
| Outgoing Event Interfaces | [**IMSVidAudioRendererEvent**](imsvidaudiorendererevent.md) |



 

## Remarks

To obtain this object, either call the [**IMSVidCtl::get\_AudioRendererActive**](imsvidctl-get-audiorendereractive.md) method, or call the [**IMSVidCtl::get\_AudioRenderersAvailable**](imsvidctl-get-audiorenderersavailable.md) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




