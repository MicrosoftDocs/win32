---
title: MSVidAudioRenderer
description: MSVidAudioRenderer
ms.assetid: f822b5a6-c88e-48c9-91f4-611a3f147fe0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSVidAudioRenderer

This topic applies to Windows XP or later.

The **MSVidAudioRenderer** object represents the audio renderer.



|                           |                                                              |
|---------------------------|--------------------------------------------------------------|
| Interfaces                | [**IMSVidAudioRenderer**](/windows/desktop/api/segment/nn-segment-imsvidaudiorenderer)           |
| Outgoing Event Interfaces | [**IMSVidAudioRendererEvent**](/windows/desktop/api/segment/) |



 

## Remarks

To obtain this object, either call the [**IMSVidCtl::get\_AudioRendererActive**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-get_audiorendereractive) method, or call the [**IMSVidCtl::get\_AudioRenderersAvailable**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-get_audiorenderersavailable) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




