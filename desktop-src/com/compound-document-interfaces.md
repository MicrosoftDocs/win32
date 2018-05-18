---
title: Compound Document Interfaces
description: Compound Document Interfaces
ms.assetid: '3192ee58-55fd-43cb-b7d5-7270e91b8131'
---

# Compound Document Interfaces

The following tables list the interfaces implemented by OLE containers, OLE servers, and compound document objects. The required interfaces must be implemented on the components for which they are listed. All other features are optional. If you want to include a particular feature in your application, however, you must implement the interfaces shown for that feature in the table below. All other interfaces are required only if you are including a particular feature.

The following table lists required and optional behaviors for OLE containers and which interfaces you must implement for each.



| Behavior                               | Interfaces                                                                                                                                                              |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required behaviors<br/>          | [**IOleClientSite**](ioleclientsite.md)<br/> [**IAdviseSink**](iadvisesink.md)<br/>                                                                       |
| Message filtering<br/>           | [**IMessageFilter**](imessagefilter.md)<br/>                                                                                                                     |
| Linking<br/>                     | none<br/>                                                                                                                                                         |
| Linking to embedded objects<br/> | [**IOleItemContainer**](ioleitemcontainer.md)<br/> [**IPersistFile**](ipersistfile.md)<br/> [**IClassFactory**](iclassfactory.md)<br/>             |
| In-place activation<br/>         | [**IOleInPlaceSite**](ioleinplacesite.md)<br/> [**IOleInPlaceFrame**](ioleinplaceframe.md)<br/> [**IOleInPlaceObject**](ioleinplaceobject.md)<br/> |
| Drag and drop<br/>               | [**IDropSource**](idropsource.md)<br/> [**IDropTarget**](idroptarget.md)<br/> [**IDataObject**](idataobject.md)<br/>                               |



 

The following table lists required and optional behaviors for OLE servers and their compound document objects and which interfaces you must implement for each. The table distinguishes OLE servers and their objects in order to clarify which component implements which interfaces. The table also notes the different requirements of objects provided by out-of-process versus in-process servers.



| Feature                        | OLE Server                                                                                                                                | Object (Out-of-process)                                                                                                                         | Object (In-process)                                                                                                                                                                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required behaviors             | [**IClassFactory**](iclassfactory.md)<br/>                                                                                         | [**IOleObject**](ioleobject.md)<br/> [**IDataObject**](idataobject.md)<br/> [**IPersistStorage**](ipersiststorage.md)<br/> | [**IOleObject**](ioleobject.md)<br/> [**IDataObject**](idataobject.md)<br/> [**IPersistStorage**](ipersiststorage.md)<br/> [**IViewObject2**](iviewobject2.md)<br/> [**IOleCache2**](iolecache2.md)<br/> |
| Message filtering<br/>   | [**IMessageFilter**](imessagefilter.md)<br/>                                                                                       |                                                                                                                                                 |                                                                                                                                                                                                                                             |
| Linking<br/>             | [**IOleItemContainer**](ioleitemcontainer.md)<br/> [**IPersistFile**](ipersistfile.md)<br/>                                 |                                                                                                                                                 | [**IOleLink**](iolelink.md)<br/> [**IExternalConnection**](iexternalconnection.md)<br/>                                                                                                                                       |
| In-place activation<br/> |                                                                                                                                           | [**IOleInPlaceObject**](ioleinplaceobject.md)<br/> [**IOleInPlaceActiveObject**](ioleinplaceactiveobject.md)<br/>                 | [**IOleInPlaceObject**](ioleinplaceobject.md)<br/> [**IOleInPlaceActiveObject**](ioleinplaceactiveobject.md)<br/>                                                                                                             |
| Drag and drop<br/>       | [**IDropSource**](idropsource.md)<br/> [**IDropTarget**](idroptarget.md)<br/> [**IDataObject**](idataobject.md)<br/> |                                                                                                                                                 |                                                                                                                                                                                                                                             |



 

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 





