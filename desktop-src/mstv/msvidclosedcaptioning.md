---
title: MSVidClosedCaptioning
description: MSVidClosedCaptioning
ms.assetid: 070a208b-cf4c-41e1-9a5f-76cc444285c9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSVidClosedCaptioning

This topic applies to Windows XP or later.

The **MSVidClosedCaptioning** object represents the closed captioning feature.



|                           |                                                                                                                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IMSVidClosedCaptioning**](/windows/desktop/api/segment/nn-segment-imsvidclosedcaptioning), [**IMSVidClosedCaptioning2**](/windows/desktop/api/segment/nn-segment-imsvidclosedcaptioning2), [**IMSVidClosedCaptioning3**](/windows/desktop/api/segment/nn-segment-imsvidclosedcaptioning3) |
| Outgoing Event Interfaces | None.                                                                                                                                                                            |



 

## Remarks

To obtain this object, call the [**IMSVidCtl::get\_FeaturesActive**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-get_featuresactive) method or the [**IMSVidCtl::get\_FeaturesAvailable**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-get_featuresavailable) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Displaying Closed Captioning in C++](displaying-closed-captioning-in-c.md)
</dt> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




