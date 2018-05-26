---
title: MSVidAudioRenderer
description: MSVidAudioRenderer
ms.assetid: f822b5a6-c88e-48c9-91f4-611a3f147fe0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSVidAudioRenderer

This topic applies to Windows XP or later.

The **MSVidAudioRenderer** object represents the audio renderer.



|                           |                                                              |
|---------------------------|--------------------------------------------------------------|
| Interfaces                | [**IMSVidAudioRenderer**](/windows/win32/segment/nn-segment-imsvidaudiorenderer?branch=master)           |
| Outgoing Event Interfaces | [**IMSVidAudioRendererEvent**](/windows/win32/segment/?branch=master) |



 

## Remarks

To obtain this object, either call the [**IMSVidCtl::get\_AudioRendererActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_audiorendereractive?branch=master) method, or call the [**IMSVidCtl::get\_AudioRenderersAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_audiorenderersavailable?branch=master) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




