---
title: ATSCLocator Object
description: ATSCLocator Object
ms.assetid: 5fe75e72-1feb-4e30-a7f5-cf29a6c9f201
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ATSCLocator Object

The **ATSCLocator** object contains tuning information for an ATSC tuning space.



|                           |                                      |
|---------------------------|--------------------------------------|
| Interfaces                | [**IATSCLocator**](iatsclocator.md) |
| Outgoing Event Interfaces | None                                 |
| CLSID                     | CLSID\_ATSCLocator                   |



 

## Remarks

The default ATSC tuning space contains a default ATSC locator. For more information, see [Default Tuning Spaces](default-tuning-spaces.md).

The most important information in this object is the physical channel, which can be obtained by calling the [**IATSCLocator::get\_PhysicalChannel**](iatsclocator-get-physicalchannel.md) method.

## Related topics

<dl> <dt>

[Locators](locators.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




