---
title: Optional Methods in Control Interfaces
description: Optional Methods in Control Interfaces
ms.assetid: 'a26f7078-9286-4b21-b924-4b03d3849909'
---

# Optional Methods in Control Interfaces

Implementing an interface doesn't necessarily mean implementing all methods of that interface to do anything more than return E\_NOTIMPL or S\_OK as appropriate. The following table identifies the methods of the interfaces listed in the [What Support for an Interface Means](what-support-for-an-interface-means.md) topic that a control may implement in this manner. Any method not listed here must be fully implemented if the interface is supported.



| IOleControl                                                                                                   | Comments                                                                       |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**GetControlInfo**](iolecontrol-getcontrolinfo.md), [**OnMnemonic**](iolecontrol-onmnemonic.md)<br/> | Mandatory for controls with mnemonics.<br/>                              |
| [**IOleControl::OnAmbientPropertyChange**](iolecontrol-onambientpropertychange.md)<br/>                | Mandatory for controls that use ambient properties.<br/>                 |
| [**IOleControl::FreezeEvents**](iolecontrol-freezeevents.md)<br/>                                      | See [Event Freezing](event-freezing.md)<br/>                            |
| IOleObject                                                                                                    |                                                                                |
| [**SetMoniker**](ioleobject-setmoniker.md)<br/>                                                        | Mandatory if the control is not marked with OLEMISC\_CANTLINKINSIDE<br/> |
| [**GetMoniker**](ioleobject-getmoniker.md)<br/>                                                        | Mandatory if the control is not marked with OLEMISC\_CANTLINKINSIDE<br/> |
| [**InitFromData**](ioleobject-initfromdata.md)<br/>                                                    | Optional<br/>                                                            |
| [**GetClipboardData**](ioleobject-getclipboarddata.md)<br/>                                            | Optional<br/>                                                            |
| [**SetExtent**](ioleobject-setextent.md)<br/>                                                          | Mandatory only for DVASPECT\_CONTENT<br/>                                |
| [**GetExtent**](ioleobject-getextent.md)<br/>                                                          | Mandatory only for DVASPECT\_CONTENT<br/>                                |
| [**SetColorScheme**](ioleobject-setcolorscheme.md)<br/>                                                | Optional<br/>                                                            |
| [**DoVerb**](ioleobject-doverb.md)<br/>                                                                | See note 1<br/>                                                          |
| IOleInPlaceObject                                                                                             |                                                                                |
| [**ContextSensitiveHelp**](iolewindow-contextsensitivehelp.md)<br/>                                    | Optional<br/>                                                            |
| [**ReactivateAndUndo**](ioleinplaceobject-reactivateandundo.md)<br/>                                   | Optional<br/>                                                            |
| IOleInPlaceActiveObject                                                                                       |                                                                                |
| [**ContextSensitiveHelp**](iolewindow-contextsensitivehelp.md)<br/>                                    | Optional<br/>                                                            |
| IViewObject2                                                                                                  |                                                                                |
| [**Freeze**](iviewobject-freeze.md)<br/>                                                               | Optional<br/>                                                            |
| [**Unfreeze**](iviewobject-unfreeze.md)<br/>                                                           | Optional<br/>                                                            |
| [**GetColorSet**](iviewobject-getcolorset.md)<br/>                                                     | Optional<br/>                                                            |
| IPersistStream, IPersistStreamInit, IPersistMemory                                                            |                                                                                |
| [**GetSizeMax**](ipersiststream-getsizemax.md)<br/>                                                    | See note 2<br/>                                                          |



 

1.  A control with property pages must support [**IOleObject::DoVerb**](ioleobject-doverb.md) for the OLEIVERB\_PROPERTIES and OLEIVERB\_PRIMARY verbs. A control that can be active must support **DoVerb** for the OLEIVERB\_INPLACEACTIVATE verb. A control that can be UI active must also support **DoVerb** for the OLEIVERB\_UIACTIVATE verb.
2.  If a control supports [**IPersistStream**](ipersiststream.md) or [**IPersistStreamInit**](ipersiststreaminit.md) and can return an accurate value, then it should do so.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 





