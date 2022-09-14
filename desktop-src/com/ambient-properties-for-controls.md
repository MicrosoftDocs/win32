---
title: Ambient Properties for Controls
description: Ambient Properties for Controls
ms.assetid: 19aa3bc2-1605-43e1-acf4-ab782d012539
ms.topic: article
ms.date: 05/31/2018
---

# Ambient Properties for Controls

If a control supports any ambient properties at all, it must at least respect the values of the following ambient properties under the conditions stated in the following table using the standard dispids.



| Ambient Property            | Dispid          | Comment/Conditions for Use                                                                                                                                                                                                                                                                |
|-----------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LocaleID<br/>         | -705<br/> | If Locale is significant to the control, e.g. for text output<br/>                                                                                                                                                                                                                  |
| UserMode <br/>        | -709<br/> | If the control behaves differently in user (design) mode and run mode<br/>                                                                                                                                                                                                          |
| UIDead<br/>           | -710<br/> | If the control reacts to UI events, then it should honor this ambient property<br/>                                                                                                                                                                                                 |
| ShowGrabHandles<br/>  | -711<br/> | If the control support in-place resizing of itself<br/>                                                                                                                                                                                                                             |
| ShowHatching<br/>     | -712<br/> | If the control support in-place activation and UI activation<br/>                                                                                                                                                                                                                   |
| DisplayAsDefault<br/> | -713<br/> | Only if the control is marked OLEMISC\_ACTSLIKEBUTTON (which means that support for keyboard mnemonics is provided, thus [**IOleControl::GetControlInfo**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-getcontrolinfo) and [**IOleControl::OnMnemonic**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-onmnemonic) must be implemented).<br/> |



 

As described previously, use of ambients requires both [**IOleControl**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrol) (for [**OnAmbientPropertyChange**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-onambientpropertychange) as a minimum) as well as [**IOleObject**](/windows/desktop/api/OleIdl/nn-oleidl-ioleobject) (for [**SetClientSite**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-setclientsite) and [**GetClientSite**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getclientsite)).

The OLEMISC\_SETCLIENTSITEFIRST bit may not necessarily be supported by a container. In these circumstances, a control must resort to default values for the ambient properties that it requires.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 





