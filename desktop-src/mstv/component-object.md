---
title: Component Object
description: Component Object
ms.assetid: a164cebb-92e2-4d20-a5b9-878998977971
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Component Object

The **Component** object represents a generic program component.



|                           |                                  |
|---------------------------|----------------------------------|
| Interfaces                | [**IComponent**](/windows/previous-versions/tuner/nn-tuner-icomponent?branch=master) |
| Outgoing Event Interfaces | None                             |
| CLSID                     | CLSID\_Component                 |



 

## Remarks

This object describes a component (such as audio or video) in a program. It contains a [ComponentType](componenttype-object.md) object that has additional information about the component.

To get this object from an existing tune request, use the [**ITuneRequest::get\_Components**](/windows/previous-versions/tuner/nf-tuner-itunerequest-get_components?branch=master) method to enumerate the components collection on the tune request. The CLSID is provided for guide store loaders that need to set the component information for a tune request.

For MPEG-2 streams, use the [MPEG2Component](mpeg2component-object.md) object.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




