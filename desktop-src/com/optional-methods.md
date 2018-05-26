---
title: Optional Methods
description: Optional Methods
ms.assetid: 8cdb5686-177c-48c9-8315-e5921520007c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Optional Methods

An OLE component can implement an interface without implementing all the semantics of every method in the interface, instead returning E\_NOTIMPL or S\_OK as appropriate. The following table describes those methods that an ActiveX control container is not required to implement (i.e. the control container can return E\_NOTIMPL).

The table below describes optional methods; note that the method must still exist, but can simply return E\_NOTIMPL instead of implementing real semantics. Note that any method from a mandatory interface that is not listed below must be considered mandatory and may not return E\_NOTIMPL.

## IOleClientSite



| Method                                                     | Comments                                                                                                 |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**SaveObject**](/windows/win32/OleIdl/nf-oleidl-ioleclientsite-saveobject?branch=master)<br/> | Necessary for persistence to be successfully supported.<br/>                                       |
| [**GetMoniker**](/windows/win32/OleIdl/nf-oleidl-ioleclientsite-getmoniker?branch=master)<br/> | Necessary only if the container supports linking to controls within its own form or document.<br/> |



 

## IOleInPlaceSite



| Method                                                                     | Comments                                                 |
|----------------------------------------------------------------------------|----------------------------------------------------------|
| [**ContextSensitiveHelp**](/windows/win32/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp?branch=master)<br/> | Optional<br/>                                      |
| [**Scroll**](/windows/win32/OleIdl/nf-oleidl-ioleinplacesite-scroll?branch=master)<br/>                        | May return S\_FALSE with no action.<br/>           |
| [**DiscardUndoState**](/windows/win32/OleIdl/nf-oleidl-ioleinplacesite-discardundostate?branch=master)<br/>    | Can return S\_OK with no action.<br/>              |
| [**DeactivateAndUndo**](/windows/win32/OleIdl/nf-oleidl-ioleinplacesite-deactivateandundo?branch=master)<br/>  | Deactivation is mandatory; Undo is optional. <br/> |



 

## IOleControlSite



| Method                                                                          | Comments                                                                                                                                                            |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetExtendedControl**](/windows/win32/OCIdl/nf-ocidl-iolecontrolsite-getextendedcontrol?branch=master)<br/>     | Necessary for containers that support extended controls.<br/>                                                                                                 |
| [**ShowPropertyFrame**](/windows/win32/OCIdl/nf-ocidl-iolecontrolsite-showpropertyframe?branch=master)<br/>       | Necessary for containers that wish to include their own property pages to handle extended control properties in addition to those provided by a control.<br/> |
| [**TranslateAccelerator**](/windows/win32/OCIdl/nf-ocidl-iolecontrolsite-translateaccelerator?branch=master)<br/> | May return S\_FALSE with no action.<br/>                                                                                                                      |
| [**LockInPlaceActive**](/windows/win32/OCIdl/nf-ocidl-iolecontrolsite-lockinplaceactive?branch=master)<br/>       | Optional<br/>                                                                                                                                                 |



 

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
| [**ContextSensitiveHelp**](/windows/win32/OleIdl/nf-oleidl-iolewindow-contextsensitivehelp?branch=master)<br/>       |                                                                         |
| [**GetBorder**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceuiwindow-getborder?branch=master)<br/>                    | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**RequestBorderSpace**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceuiwindow-requestborderspace?branch=master)<br/>  | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**SetBorderSpace**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceuiwindow-setborderspace?branch=master)<br/>          | Necessary for containers with toolbar UI (which is optional)<br/> |
| [**InsertMenus**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-insertmenus?branch=master)<br/>                   | Necessary for containers with menu UI (which is optional)<br/>    |
| [**SetMenu**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-setmenu?branch=master)<br/>                           | Necessary for containers with menu UI (which is optional)<br/>    |
| [**RemoveMenus**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-removemenus?branch=master)<br/>                   | Necessary for containers with menu UI (which is optional)<br/>    |
| [**SetStatusText**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-setstatustext?branch=master)<br/>               | Necessary only for containers that have a status line<br/>        |
| [**EnableModeless**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-enablemodeless?branch=master)<br/>             | Optional<br/>                                                     |
| [**TranslateAccelerator**](/windows/win32/OleIdl/nf-oleidl-ioleinplaceframe-translateaccelerator?branch=master)<br/> | Optional<br/>                                                     |



 

## IOleContainer



| Method                                                                    | Comments                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ParseDisplayName**](/windows/win32/OleIdl/nf-oleidl-iparsedisplayname-parsedisplayname?branch=master)<br/> | Only if linking to controls or other embeddings in the container is supported, as this is necessary for moniker binding.<br/>                                                                                                                  |
| [**LockContainer**](/windows/win32/OleIdl/nf-oleidl-iolecontainer-lockcontainer?branch=master)<br/>           | As for ParseDisplayName<br/>                                                                                                                                                                                                                   |
| [**EnumObjects**](/windows/win32/OleIdl/nf-oleidl-iolecontainer-enumobjects?branch=master)<br/>               | Returns all ActiveX controls through an enumerator with [**IEnumUnknown**](/windows/win32/objidlbase/nn-objidl-ienumunknown?branch=master), but not necessarily all objects (because there's no guarantee that all objects are ActiveX controls; some may be regular Windows controls).<br/> |



 

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 





