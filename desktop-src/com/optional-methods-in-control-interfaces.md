---
title: Optional Methods in Control Interfaces
description: Optional Methods in Control Interfaces
ms.assetid: a26f7078-9286-4b21-b924-4b03d3849909
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Optional Methods in Control Interfaces

Implementing an interface doesn't necessarily mean implementing all methods of that interface to do anything more than return E\_NOTIMPL or S\_OK as appropriate. The following table identifies the methods of the interfaces listed in the [What Support for an Interface Means](what-support-for-an-interface-means.md) topic that a control may implement in this manner. Any method not listed here must be fully implemented if the interface is supported.



| IOleControl                                                                                                   | Comments                                                                       |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**GetControlInfo**](/windows/win32/OCIdl/nf-ocidl-iolecontrol-getcontrolinfo?branch=master), [**OnMnemonic**](/windows/win32/OCIdl/nf-ocidl-iolecontrol-onmnemonic?branch=master)<br/> | Mandatory for controls with mnemonics.<br/>                              |
| [**IOleControl::OnAmbientPropertyChange**](/windows/win32/OCIdl/nf-ocidl-iolecontrol-onambientpropertychange?branch=master)<br/>                | Mandatory for controls that use ambient properties.<br/>                 |
| [**IOleControl::FreezeEvents**](/windows/win32/OCIdl/nf-ocidl-iolecontrol-freezeevents?branch=master)<br/>                                      | See [Event Freezing](event-freezing.md)<br/>                            |
| IOleObject                                                                                                    |                                                                                |
| [**SetMoniker**](/windows/win32/OleIdl/nf-oleidl-ioleobject-setmoniker?branch=master)<br/>                                                        | Mandatory if the control is not marked with OLEMISC\_CANTLINKINSIDE<br/> |
| [**GetMoniker**](/windows/win32/OleIdl/nf-oleidl-ioleobject-getmoniker?branch=master)<br/>                                                        | Mandatory if the control is not marked with OLEMISC\_CANTLINKINSIDE<br/> |
| [**InitFromData**](/windows/win32/OleIdl/nf-oleidl-ioleobject-initfromdata?branch=master)<br/>                                                    | Optional<br/>                                                            |
| [**GetClipboardData**](/windows/win32/OleIdl/nf-oleidl-ioleobject-getclipboarddata?branch=master)<br/>                                            | Optional<br/>                                                            |
| [**SetExtent**](/windows/win32/OleIdl/nf-oleidl-ioleobject-setextent?branch=master)<br/>                                                          | Mandatory only for DVASPECT\_CONTENT<br/>                                |
| [**GetExtent**](/windows/win32/OleIdl/nf-oleidl-ioleobject-getextent?branch=master)<br/>                                                          | Mandatory only for DVASPECT\_CONTENT<br/>                                |
| [**SetColorScheme**](/windows/win32/OleIdl/nf-oleidl-ioleobject-setcolorscheme?branch=master)<br/>                                                | Optional<br/>                                                            |
| [**DoVerb**](/windows/win32/OleIdl/nf-oleidl-ioleobject-doverb?branch=master)<br/>                                                                | See note 1<br/>                                                          |
| IOleInPlaceObject                                                                                             |                                                                                |
| [**ContextSensitiveHelp**](/windows/win32/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp?branch=master)<br/>                                    | Optional<br/>                                                            |
| [**ReactivateAndUndo**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceobject-reactivateandundo?branch=master)<br/>                                   | Optional<br/>                                                            |
| IOleInPlaceActiveObject                                                                                       |                                                                                |
| [**ContextSensitiveHelp**](/windows/win32/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp?branch=master)<br/>                                    | Optional<br/>                                                            |
| IViewObject2                                                                                                  |                                                                                |
| [**Freeze**](/windows/win32/OleIdl/nf-oleidl-iviewobject-freeze?branch=master)<br/>                                                               | Optional<br/>                                                            |
| [**Unfreeze**](/windows/win32/OleIdl/nf-oleidl-iviewobject-unfreeze?branch=master)<br/>                                                           | Optional<br/>                                                            |
| [**GetColorSet**](/windows/win32/OleIdl/nf-oleidl-iviewobject-getcolorset?branch=master)<br/>                                                     | Optional<br/>                                                            |
| IPersistStream, IPersistStreamInit, IPersistMemory                                                            |                                                                                |
| [**GetSizeMax**](/windows/win32/ObjIdl/nf-objidl-ipersiststream-getsizemax?branch=master)<br/>                                                    | See note 2<br/>                                                          |



 

1.  A control with property pages must support [**IOleObject::DoVerb**](/windows/win32/OleIdl/nf-oleidl-ioleobject-doverb?branch=master) for the OLEIVERB\_PROPERTIES and OLEIVERB\_PRIMARY verbs. A control that can be active must support **DoVerb** for the OLEIVERB\_INPLACEACTIVATE verb. A control that can be UI active must also support **DoVerb** for the OLEIVERB\_UIACTIVATE verb.
2.  If a control supports [**IPersistStream**](/windows/win32/ObjIdl/nn-objidl-ipersiststream?branch=master) or [**IPersistStreamInit**](/windows/win32/OCIdl/nn-ocidl-ipersiststreaminit?branch=master) and can return an accurate value, then it should do so.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 





