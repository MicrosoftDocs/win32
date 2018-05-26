---
title: ComponentType Object
description: ComponentType Object
ms.assetid: 45c0c3ce-1313-4203-a5e6-af4aed8f0324
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ComponentType Object

The **ComponentType** object represents a generic component type.



|                           |                                          |
|---------------------------|------------------------------------------|
| Interfaces                | [**IComponentType**](/windows/previous-versions/tuner/nn-tuner-icomponenttype?branch=master) |
| Outgoing Event Interfaces | None                                     |
| CLSID                     | CLSID\_ComponentType                     |



 

## Remarks

To get the component type from an existing component object, use the [**IComponent::get\_Type**](/windows/previous-versions/tuner/nf-tuner-icomponent-get_type?branch=master) method. The CLSID is provided for clients that need to set the type on a component, or set a default preferred type on a tuning space.

For MPEG-2 streams, use the [MPEG2ComponentType](mpeg2componenttype-object.md) object.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




