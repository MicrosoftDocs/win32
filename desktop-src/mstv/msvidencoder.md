---
title: MSVidEncoder
description: MSVidEncoder
ms.assetid: 37d03dff-ae40-4e7f-a66f-facd0c1f6eee
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSVidEncoder

This topic applies to Windows XP Service Pack 1 or later.

The **MSVidEncoder** object represents the encoder feature, which is required for using the Stream Buffer Engine with the Video Control.



|                           |                                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Interfaces                | [**IMSVidDevice2**](/windows/desktop/api/segment/nn-segment-imsviddevice2), [**IMSVidEncoder**](/windows/desktop/api/segment/nn-segment-imsvidencoder) |
| Outgoing Event Interfaces | None.                                                                          |



 

## Remarks

To obtain this object, call the [**IMSVidCtl::get\_FeaturesAvailable**](imsvidctl-get-featuresavailable.md) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Using the Stream Buffer Engine with the Video Control](using-the-stream-buffer-engine-with-the-video-control.md)
</dt> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




