---
title: Optional Methods
description: Optional Methods
ms.assetid: '8cdb5686-177c-48c9-8315-e5921520007c'
---

# Optional Methods

An OLE component can implement an interface without implementing all the semantics of every method in the interface, instead returning E\_NOTIMPL or S\_OK as appropriate. The following table describes those methods that an ActiveX control container is not required to implement (i.e. the control container can return E\_NOTIMPL).

The table below describes optional methods; note that the method must still exist, but can simply return E\_NOTIMPL instead of implementing real semantics. Note that any method from a mandatory interface that is not listed below must be considered mandatory and may not return E\_NOTIMPL.

## IOleClientSite



| Method                                                     | Comments                                                                                                 |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**SaveObject**](ioleclientsite-saveobject.md)<br/> | Necessary for persistence to be successfully supported.<br/>                                       |
| [**GetMoniker**](ioleclientsite-getmoniker.md)<br/> | Necessary only if the container supports linking to controls within its own form or document.<br/> |



 

## IOleInPlaceSite



| Method                                                                     | Comments                                                 |
|----------------------------------------------------------------------------|----------------------------------------------------------|
| [**ContextSensitiveHelp**](iolewindow-contextsensitivehelp.md)<br/> | Optional<br/>                                      |
| [**Scroll**](ioleinplacesite-scroll.md)<br/>                        | May return S\_FALSE with no action.<br/>           |
| [**DiscardUndoState**](ioleinplacesite-discardundostate.md)<br/>    | Can return S\_OK with no action.<br/>              |
| [**DeactivateAndUndo**](ioleinplacesite-deactivateandundo.md)<br/>  | Deactivation is mandatory; Undo is optional. <br/> |



 

## IOleControlSite



| Method                                                                          | Comments                                                                                                                                                            |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetExtendedControl**](iolecontrolsite-getextendedcontrol.md)<br/>     | Necessary for containers that support extended controls.<br/>                                                                                                 |
| [**ShowPropertyFrame**](iolecontrolsite-showpropertyframe.md)<br/>       | Necessary for containers that wish to include their own property pages to handle extended control properties in addition to those provided by a control.<br/> |
| [**TranslateAccelerator**](iolecontrolsite-translateaccelerator.md)<br/> | May return S\_FALSE with no action.<br/>                                                                                                                      |
| [**LockInPlaceActive**](iolecontrolsite-lockinplaceactive.md)<br/>       | Optional<br/>                                                                                                                                                 |



 

## IDispatch (Ambient properties)



| Method                      | Comments                                                                          |
|-----------------------------|-----------------------------------------------------------------------------------|
| GetTypeInfoCount<br/> | Necessary for containers that support non-standard ambient properties.<br/> |
| GetTypeInfo<br/>      | Necessary for containers that support non-standard ambient properties.<br/> |
| GetIDsOfNames<br/>    | Necessary for containers that support non-standard ambient properties.<br/> |



 

## IDispatch (Event sink)



| Method                      | Comments                                                                               |
|-----------------------------|----------------------------------------------------------------------------------------|
| GetTypeInfoCount<br/> | The control knows its own type information, so it has no need to call this.<br/> |
| GetTypeInfo<br/>      | The control knows its own type information, so it has no need to call this.<br/> |
| GetIDsOfNames<br/>    | The control knows its own type information, so it has no need to call this.<br/> |



 

## IOleInPlaceFrame



| Method                                                                           | Comments                                                                |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**ContextSensitiveHelp**](iolewindow-contextsensitivehelp.md)<br/>       |                                                                         |
| [**GetBorder**](ioleinplaceuiwindow-getborder.md)<br/>                    | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**RequestBorderSpace**](ioleinplaceuiwindow-requestborderspace.md)<br/>  | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**SetBorderSpace**](ioleinplaceuiwindow-setborderspace.md)<br/>          | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**InsertMenus**](ioleinplaceframe-insertmenus.md)<br/>                   | Necessary for containers with menu UI (which is optional)<br/>    |
| [**SetMenu**](ioleinplaceframe-setmenu.md)<br/>                           | Necessary for containers with menu UI (which is optional)<br/>    |
| [**RemoveMenus**](ioleinplaceframe-removemenus.md)<br/>                   | Necessary for containers with menu UI (which is optional)<br/>    |
| [**SetStatusText**](ioleinplaceframe-setstatustext.md)<br/>               | Necessary only for containers that have a status line<br/>        |
| [**EnableModeless**](ioleinplaceframe-enablemodeless.md)<br/>             | Optional<br/>                                                     |
| [**TranslateAccelerator**](ioleinplaceframe-translateaccelerator.md)<br/> | Optional<br/>                                                     |



 

## IOleContainer



| Method                                                                    | Comments                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ParseDisplayName**](iparsedisplayname-parsedisplayname.md)<br/> | Only if linking to controls or other embeddings in the container is supported, as this is necessary for moniker binding.<br/>                                                                                                                  |
| [**LockContainer**](iolecontainer-lockcontainer.md)<br/>           | As for ParseDisplayName<br/>                                                                                                                                                                                                                   |
| [**EnumObjects**](iolecontainer-enumobjects.md)<br/>               | Returns all ActiveX controls through an enumerator with [**IEnumUnknown**](ienumunknown.md), but not necessarily all objects (because there's no guarantee that all objects are ActiveX controls; some may be regular Windows controls).<br/> |



 

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 





