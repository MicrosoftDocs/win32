---
title: MPEG2ComponentType Object
description: MPEG2ComponentType Object
ms.assetid: 16059b17-9145-4aad-97ce-c31fdfe1db69
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MPEG2ComponentType Object

The **MPEG2ComponentType** object represents a component type associated with an MPEG-2 stream component.



|                           |                                                    |
|---------------------------|----------------------------------------------------|
| Interfaces                | [**IMPEG2ComponentType**](impeg2componenttype.md) |
| Outgoing Event Interfaces | None                                               |
| CLSID                     | CLSID\_MPEG2ComponentType                          |



 

## Remarks

To get the component type from an existing component object, use the [**IComponent::get\_Type**](icomponent-get-type.md) method. The CLSID is provided for clients that need to set the type on a component, or set a default preferred type on a tuning space.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




