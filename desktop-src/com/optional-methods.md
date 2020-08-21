---
title: Optional Methods
description: Optional Methods
ms.assetid: 8cdb5686-177c-48c9-8315-e5921520007c
ms.topic: reference
ms.date: 05/31/2018
---

# Optional Methods

An OLE component can implement an interface without implementing all the semantics of every method in the interface, instead returning E\_NOTIMPL or S\_OK as appropriate. The following table describes those methods that an ActiveX control container is not required to implement (i.e. the control container can return E\_NOTIMPL).

The table below describes optional methods; note that the method must still exist, but can simply return E\_NOTIMPL instead of implementing real semantics. Note that any method from a mandatory interface that is not listed below must be considered mandatory and may not return E\_NOTIMPL.

## IOleClientSite



| Method                                                     | Comments                                                                                                 |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**SaveObject**](/windows/desktop/api/OleIdl/nf-oleidl-ioleclientsite-saveobject)<br/> | Necessary for persistence to be successfully supported.<br/>                                       |
| [**GetMoniker**](/windows/desktop/api/OleIdl/nf-oleidl-ioleclientsite-getmoniker)<br/> | Necessary only if the container supports linking to controls within its own form or document.<br/> |



 

## IOleInPlaceSite



| Method                                                                     | Comments                                                 |
|----------------------------------------------------------------------------|----------------------------------------------------------|
| [**ContextSensitiveHelp**](/windows/desktop/api/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp)<br/> | Optional<br/>                                      |
| [**Scroll**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplacesite-scroll)<br/>                        | May return S\_FALSE with no action.<br/>           |
| [**DiscardUndoState**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplacesite-discardundostate)<br/>    | Can return S\_OK with no action.<br/>              |
| [**DeactivateAndUndo**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplacesite-deactivateandundo)<br/>  | Deactivation is mandatory; Undo is optional. <br/> |



 

## IOleControlSite



| Method                                                                          | Comments                                                                                                                                                            |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetExtendedControl**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-getextendedcontrol)<br/>     | Necessary for containers that support extended controls.<br/>                                                                                                 |
| [**ShowPropertyFrame**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-showpropertyframe)<br/>       | Necessary for containers that wish to include their own property pages to handle extended control properties in addition to those provided by a control.<br/> |
| [**TranslateAccelerator**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-translateaccelerator)<br/> | May return S\_FALSE with no action.<br/>                                                                                                                      |
| [**LockInPlaceActive**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-lockinplaceactive)<br/>       | Optional<br/>                                                                                                                                                 |



 

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
| [**ContextSensitiveHelp**](/windows/desktop/api/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp)<br/>       |                                                                         |
| [**GetBorder**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceuiwindow-getborder)<br/>                    | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**RequestBorderSpace**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceuiwindow-requestborderspace)<br/>  | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**SetBorderSpace**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceuiwindow-setborderspace)<br/>          | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**InsertMenus**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceframe-insertmenus)<br/>                   | Necessary for containers with menu UI (which is optional)<br/>    |
| [**SetMenu**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceframe-setmenu)<br/>                           | Necessary for containers with menu UI (which is optional)<br/>    |
| [**RemoveMenus**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceframe-removemenus)<br/>                   | Necessary for containers with menu UI (which is optional)<br/>    |
| [**SetStatusText**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceframe-setstatustext)<br/>               | Necessary only for containers that have a status line<br/>        |
| [**EnableModeless**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceframe-enablemodeless)<br/>             | Optional<br/>                                                     |
| [**TranslateAccelerator**](/windows/desktop/api/OleIdl/nf-oleidl-ioleinplaceframe-translateaccelerator)<br/> | Optional<br/>                                                     |



 

## IOleContainer



| Method                                                                    | Comments                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ParseDisplayName**](/windows/desktop/api/OleIdl/nf-oleidl-iparsedisplayname-parsedisplayname)<br/> | Only if linking to controls or other embeddings in the container is supported, as this is necessary for moniker binding.<br/>                                                                                                                  |
| [**LockContainer**](/windows/desktop/api/OleIdl/nf-oleidl-iolecontainer-lockcontainer)<br/>           | As for ParseDisplayName<br/>                                                                                                                                                                                                                   |
| [**EnumObjects**](/windows/desktop/api/OleIdl/nf-oleidl-iolecontainer-enumobjects)<br/>               | Returns all ActiveX controls through an enumerator with [**IEnumUnknown**](/windows/win32/api/objidlbase/nn-objidlbase-ienumunknown), but not necessarily all objects (because there's no guarantee that all objects are ActiveX controls; some may be regular Windows controls).<br/> |



 

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

