---
title: Ambient Properties for Controls
description: Ambient Properties for Controls
ms.assetid: 19aa3bc2-1605-43e1-acf4-ab782d012539
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| DisplayAsDefault<br/> | -713<br/> | Only if the control is marked OLEMISC\_ACTSLIKEBUTTON (which means that support for keyboard mnemonics is provided, thus [**IOleControl::GetControlInfo**](/windows/win32/OCIdl/nf-ocidl-iolecontrol-getcontrolinfo?branch=master) and [**IOleControl::OnMnemonic**](/windows/win32/OCIdl/nf-ocidl-iolecontrol-onmnemonic?branch=master) must be implemented).<br/> |



 

As described previously, use of ambients requires both [**IOleControl**](/windows/win32/OCIdl/nn-ocidl-iolecontrol?branch=master) (for [**OnAmbientPropertyChange**](/windows/win32/OCIdl/nf-ocidl-iolecontrol-onambientpropertychange?branch=master) as a minimum) as well as [**IOleObject**](/windows/win32/OleIdl/nn-oleidl-ioleobject?branch=master) (for [**SetClientSite**](/windows/win32/OleIdl/nf-oleidl-ioleobject-setclientsite?branch=master) and [**GetClientSite**](/windows/win32/OleIdl/nf-oleidl-ioleobject-getclientsite?branch=master)).

The OLEMISC\_SETCLIENTSITEFIRST bit may not necessarily be supported by a container. In these circumstances, a control must resort to default values for the ambient properties that it requires.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 





