---
title: Optional Methods in Control Interfaces
description: Optional Methods in Control Interfaces
ms.assetid: a26f7078-9286-4b21-b924-4b03d3849909
ms.topic: article
ms.date: 05/31/2018
---

# Optional Methods in Control Interfaces

Implementing an interface doesn't necessarily mean implementing all methods of that interface to do anything more than return E\_NOTIMPL or S\_OK as appropriate. The following table identifies the methods of the interfaces listed in the [What Support for an Interface Means](what-support-for-an-interface-means.md) topic that a control may implement in this manner. Any method not listed here must be fully implemented if the interface is supported.



| IOleControl                                                                                                   | Comments                                                                       |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**GetControlInfo**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-getcontrolinfo), [**OnMnemonic**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-onmnemonic)<br/> | Mandatory for controls with mnemonics.<br/>                              |
| [**IOleControl::OnAmbientPropertyChange**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-onambientpropertychange)<br/>                | Mandatory for controls that use ambient properties.<br/>                 |
| [**IOleControl::FreezeEvents**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-freezeevents)<br/>                                      | See [Event Freezing](event-freezing.md)<br/>                            |
| IOleObject                                                                                                    |                                                                                |
| [**SetMoniker**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-setmoniker)<br/>                                                        | Mandatory if the control is not marked with OLEMISC\_CANTLINKINSIDE<br/> |
| [**GetMoniker**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getmoniker)<br/>                                                        | Mandatory if the control is not marked with OLEMISC\_CANTLINKINSIDE<br/> |
| [**InitFromData**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-initfromdata)<br/>                                                    | Optional<br/>                                                            |
| [**GetClipboardData**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getclipboarddata)<br/>                                            | Optional<br/>                                                            |
| [**SetExtent**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-setextent)<br/>                                                          | Mandatory only for DVASPECT\_CONTENT<br/>                                |
| [**GetExtent**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getextent)<br/>                                                          | Mandatory only for DVASPECT\_CONTENT<br/>                                |
| [**SetColorScheme**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-setcolorscheme)<br/>                                                | Optional<br/>                                                            |
| [**DoVerb**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-doverb)<br/>                                                                | See note 1<br/>                                                          |
| IOleInPlaceObject                                                                                             |                                                                                |
| [**ContextSensitiveHelp**](/windows/desktop/api/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp)<br/>                                    | Optional<br/>                                                            |
| [**ReactivateAndUndo**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceobject-reactivateandundo)<br/>                                   | Optional<br/>                                                            |
| IOleInPlaceActiveObject                                                                                       |                                                                                |
| [**ContextSensitiveHelp**](/windows/desktop/api/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp)<br/>                                    | Optional<br/>                                                            |
| IViewObject2                                                                                                  |                                                                                |
| [**Freeze**](/windows/desktop/api/OleIdl/nf-oleidl-iviewobject-freeze)<br/>                                                               | Optional<br/>                                                            |
| [**Unfreeze**](/windows/desktop/api/OleIdl/nf-oleidl-iviewobject-unfreeze)<br/>                                                           | Optional<br/>                                                            |
| [**GetColorSet**](/windows/desktop/api/OleIdl/nf-oleidl-iviewobject-getcolorset)<br/>                                                     | Optional<br/>                                                            |
| IPersistStream, IPersistStreamInit, IPersistMemory                                                            |                                                                                |
| [**GetSizeMax**](/windows/desktop/api/ObjIdl/nf-objidl-ipersiststream-getsizemax)<br/>                                                    | See note 2<br/>                                                          |



 

1.  A control with property pages must support [**IOleObject::DoVerb**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-doverb) for the OLEIVERB\_PROPERTIES and OLEIVERB\_PRIMARY verbs. A control that can be active must support **DoVerb** for the OLEIVERB\_INPLACEACTIVATE verb. A control that can be UI active must also support **DoVerb** for the OLEIVERB\_UIACTIVATE verb.
2.  If a control supports [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream) or [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit) and can return an accurate value, then it should do so.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 





