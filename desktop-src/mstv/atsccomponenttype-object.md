---
title: ATSCComponentType Object
description: ATSCComponentType Object
ms.assetid: 45c0c3ce-1313-4203-a5e6-af4aed8f0324
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ATSCComponentType Object

The **ATSCComponentType** object represents an ATSC component type. The ATSC component type indicates whether an audio stream is in AC-3 format.



|                           |                                                  |
|---------------------------|--------------------------------------------------|
| Interfaces                | [**IATSCComponentType**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatsccomponenttype) |
| Outgoing Event Interfaces | None                                             |
| CLSID                     | CLSID\_ATSCComponentType                         |



 

## Remarks

This object is obtained through the [**IComponent::get\_Type**](/previous-versions/windows/desktop/api/tuner/nf-tuner-icomponent-get_type) method of a component object for an ATSC tune request. It may also be used as a default preferred component type on the tuning space, or the preferred type on a tune request. In this case, it is obtained through the Components collection object.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




