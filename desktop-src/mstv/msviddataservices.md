---
title: MSVidDataServices
description: MSVidDataServices
ms.assetid: '6f70aa63-849c-4170-80c1-359210be4d61'
---

# MSVidDataServices

This topic applies to Windows XP or later.

The **MSVidDataServices** object represents the data services feature.



|                           |                                                  |
|---------------------------|--------------------------------------------------|
| Interfaces                | [**IMSVidDataServices**](imsviddataservices.md) |
| Outgoing Event Interfaces | None.                                            |



 

## Remarks

The **IMSVidDataServices** interface inherits from [**IMSVidDevice**](imsviddevice.md), but adds no new methods or properties.

To obtain this object, call the [**IMSVidCtl::get\_FeaturesActive**](imsvidctl-get-featuresactive.md) or [**IMSVidCtl::get\_FeaturesAvailable**](imsvidctl-get-featuresavailable.md) method and enumerate the returned collection.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




