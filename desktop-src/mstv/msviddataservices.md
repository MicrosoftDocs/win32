---
title: MSVidDataServices
description: MSVidDataServices
ms.assetid: 6f70aa63-849c-4170-80c1-359210be4d61
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSVidDataServices

This topic applies to Windows XP or later.

The **MSVidDataServices** object represents the data services feature.



|                           |                                                  |
|---------------------------|--------------------------------------------------|
| Interfaces                | [**IMSVidDataServices**](/windows/win32/segment/?branch=master) |
| Outgoing Event Interfaces | None.                                            |



 

## Remarks

The **IMSVidDataServices** interface inherits from [**IMSVidDevice**](/windows/win32/segment/nn-segment-imsviddevice?branch=master), but adds no new methods or properties.

To obtain this object, call the [**IMSVidCtl::get\_FeaturesActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_featuresactive?branch=master) or [**IMSVidCtl::get\_FeaturesAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_featuresavailable?branch=master) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




