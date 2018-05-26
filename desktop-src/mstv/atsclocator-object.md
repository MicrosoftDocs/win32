---
title: ATSCLocator Object
description: ATSCLocator Object
ms.assetid: 5fe75e72-1feb-4e30-a7f5-cf29a6c9f201
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ATSCLocator Object

The **ATSCLocator** object contains tuning information for an ATSC tuning space.



|                           |                                      |
|---------------------------|--------------------------------------|
| Interfaces                | [**IATSCLocator**](/windows/previous-versions/tuner/nn-tuner-iatsclocator?branch=master) |
| Outgoing Event Interfaces | None                                 |
| CLSID                     | CLSID\_ATSCLocator                   |



 

## Remarks

The default ATSC tuning space contains a default ATSC locator. For more information, see [Default Tuning Spaces](default-tuning-spaces.md).

The most important information in this object is the physical channel, which can be obtained by calling the [**IATSCLocator::get\_PhysicalChannel**](/windows/previous-versions/tuner/nf-tuner-iatsclocator-get_physicalchannel?branch=master) method.

## Related topics

<dl> <dt>

[Locators](locators.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




