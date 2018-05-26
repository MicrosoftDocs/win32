---
title: MSVidClosedCaptioning
description: MSVidClosedCaptioning
ms.assetid: 070a208b-cf4c-41e1-9a5f-76cc444285c9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSVidClosedCaptioning

This topic applies to Windows XP or later.

The **MSVidClosedCaptioning** object represents the closed captioning feature.



|                           |                                                                                                                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IMSVidClosedCaptioning**](/windows/win32/segment/nn-segment-imsvidclosedcaptioning?branch=master), [**IMSVidClosedCaptioning2**](/windows/win32/segment/nn-segment-imsvidclosedcaptioning2?branch=master), [**IMSVidClosedCaptioning3**](/windows/win32/segment/nn-segment-imsvidclosedcaptioning3?branch=master) |
| Outgoing Event Interfaces | None.                                                                                                                                                                            |



 

## Remarks

To obtain this object, call the [**IMSVidCtl::get\_FeaturesActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_featuresactive?branch=master) method or the [**IMSVidCtl::get\_FeaturesAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_featuresavailable?branch=master) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Displaying Closed Captioning in C++](displaying-closed-captioning-in-c.md)
</dt> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




