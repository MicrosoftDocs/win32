---
title: LanguageComponentType Object
description: LanguageComponentType Object
ms.assetid: d1601651-84a2-4fd8-9318-653aa569e747
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LanguageComponentType Object

The **LanguageComponentType** object represents a component type that has a defined language code.



|                           |                                                          |
|---------------------------|----------------------------------------------------------|
| Interfaces                | [**ILanguageComponentType**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ilanguagecomponenttype) |
| Outgoing Event Interfaces | None                                                     |
| CLSID                     | CLSID\_LanguageComponentType                             |



 

## Remarks

To get the component type from an existing component object, use the [**IComponent::get\_Type**](/previous-versions/windows/desktop/api/tuner/nf-tuner-icomponent-get_type) method. The CLSID is provided for clients that need to set the type on a component, or set a default preferred type on a tuning space.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




