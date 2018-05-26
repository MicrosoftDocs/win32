---
title: Compound Document Interfaces
description: Compound Document Interfaces
ms.assetid: 3192ee58-55fd-43cb-b7d5-7270e91b8131
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Compound Document Interfaces

The following tables list the interfaces implemented by OLE containers, OLE servers, and compound document objects. The required interfaces must be implemented on the components for which they are listed. All other features are optional. If you want to include a particular feature in your application, however, you must implement the interfaces shown for that feature in the table below. All other interfaces are required only if you are including a particular feature.

The following table lists required and optional behaviors for OLE containers and which interfaces you must implement for each.



| Behavior                               | Interfaces                                                                                                                                                              |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required behaviors<br/>          | [**IOleClientSite**](/windows/win32/OleIdl/nn-oleidl-ioleclientsite?branch=master)<br/> [**IAdviseSink**](/windows/win32/ObjIdl/nn-objidl-iadvisesink?branch=master)<br/>                                                                       |
| Message filtering<br/>           | [**IMessageFilter**](/windows/win32/ObjIdl/nn-objidl-imessagefilter?branch=master)<br/>                                                                                                                     |
| Linking<br/>                     | none<br/>                                                                                                                                                         |
| Linking to embedded objects<br/> | [**IOleItemContainer**](/windows/win32/OleIdl/nn-oleidl-ioleitemcontainer?branch=master)<br/> [**IPersistFile**](/windows/win32/ObjIdl/nn-objidl-ipersistfile?branch=master)<br/> [**IClassFactory**](/windows/win32/unknwnbase/nn-unknwn-iclassfactory?branch=master)<br/>             |
| In-place activation<br/>         | [**IOleInPlaceSite**](/windows/win32/OleIdl/nn-oleidl-ioleinplacesite?branch=master)<br/> [**IOleInPlaceFrame**](/windows/win32/OleIdl/nn-oleidl-ioleinplaceframe?branch=master)<br/> [**IOleInPlaceObject**](/windows/win32/OleIdl/nn-oleidl-ioleinplaceobject?branch=master)<br/> |
| Drag and drop<br/>               | [**IDropSource**](/windows/win32/OleIdl/nn-oleidl-idropsource?branch=master)<br/> [**IDropTarget**](/windows/win32/OleIdl/nn-oleidl-idroptarget?branch=master)<br/> [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master)<br/>                               |



 

The following table lists required and optional behaviors for OLE servers and their compound document objects and which interfaces you must implement for each. The table distinguishes OLE servers and their objects in order to clarify which component implements which interfaces. The table also notes the different requirements of objects provided by out-of-process versus in-process servers.



| Feature                        | OLE Server                                                                                                                                | Object (Out-of-process)                                                                                                                         | Object (In-process)                                                                                                                                                                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required behaviors             | [**IClassFactory**](/windows/win32/unknwnbase/nn-unknwn-iclassfactory?branch=master)<br/>                                                                                         | [**IOleObject**](/windows/win32/OleIdl/nn-oleidl-ioleobject?branch=master)<br/> [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master)<br/> [**IPersistStorage**](/windows/win32/ObjIdl/nn-objidl-ipersiststorage?branch=master)<br/> | [**IOleObject**](/windows/win32/OleIdl/nn-oleidl-ioleobject?branch=master)<br/> [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master)<br/> [**IPersistStorage**](/windows/win32/ObjIdl/nn-objidl-ipersiststorage?branch=master)<br/> [**IViewObject2**](/windows/win32/OleIdl/nn-oleidl-iviewobject2?branch=master)<br/> [**IOleCache2**](/windows/win32/OleIdl/nn-oleidl-iolecache2?branch=master)<br/> |
| Message filtering<br/>   | [**IMessageFilter**](/windows/win32/ObjIdl/nn-objidl-imessagefilter?branch=master)<br/>                                                                                       |                                                                                                                                                 |                                                                                                                                                                                                                                             |
| Linking<br/>             | [**IOleItemContainer**](/windows/win32/OleIdl/nn-oleidl-ioleitemcontainer?branch=master)<br/> [**IPersistFile**](/windows/win32/ObjIdl/nn-objidl-ipersistfile?branch=master)<br/>                                 |                                                                                                                                                 | [**IOleLink**](/windows/win32/OleIdl/nn-oleidl-iolelink?branch=master)<br/> [**IExternalConnection**](/windows/win32/objidlbase/nn-objidl-iexternalconnection?branch=master)<br/>                                                                                                                                       |
| In-place activation<br/> |                                                                                                                                           | [**IOleInPlaceObject**](/windows/win32/OleIdl/nn-oleidl-ioleinplaceobject?branch=master)<br/> [**IOleInPlaceActiveObject**](/windows/win32/OleIdl/nn-oleidl-ioleinplaceactiveobject?branch=master)<br/>                 | [**IOleInPlaceObject**](/windows/win32/OleIdl/nn-oleidl-ioleinplaceobject?branch=master)<br/> [**IOleInPlaceActiveObject**](/windows/win32/OleIdl/nn-oleidl-ioleinplaceactiveobject?branch=master)<br/>                                                                                                             |
| Drag and drop<br/>       | [**IDropSource**](/windows/win32/OleIdl/nn-oleidl-idropsource?branch=master)<br/> [**IDropTarget**](/windows/win32/OleIdl/nn-oleidl-idroptarget?branch=master)<br/> [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master)<br/> |                                                                                                                                                 |                                                                                                                                                                                                                                             |



 

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 





