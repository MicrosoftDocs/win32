---
title: Visual Representation
description: A control supports positioning and displaying itself within its container through compound document technology and OLE drag and drop technology that involves both the control and its container.
ms.assetid: 'a7940560-360c-4c0d-9ac1-d051adb0b83e'
---

# Visual Representation

A control supports positioning and displaying itself within its container through compound document technology and OLE drag and drop technology that involves both the control and its container. The control must be able to draw itself while the container manages the position of the control and its size.

Controls add to the basic functions provided by OLE documents. A control calls its client's [**IOleClientSite::RequestNewObjectLayout**](ioleclientsite-requestnewobjectlayout.md) method to tell its container that it wants to change its size. The client calls the control's [**IOleObject::GetExtent**](ioleobject-getextent.md) to get the new size and calls [**IOleInPlaceObject::SetObjectRects**](ioleinplaceobject-setobjectrects.md) to set the control to its new size.

Controls that support only [**IPersistStream**](ipersiststream.md) or [**IPersistStreamInit**](ipersiststreaminit.md) do not support caching through [**IOleCache2**](iolecache2.md) because the cache requires support for [**IPersistStorage**](ipersiststorage.md). However, these controls should provide a way for the client to render the control through [**IDataObject::GetData**](idataobject-getdata.md) so the client can optionally create and manage its own cache of the presentation data for the control.

Controls use the HIMETRIC type for its coordinates. However, different containers can use different coordinate systems. The container wants to receive coordinates in its own system, but the control does not necessarily know what coordinates its container is using. To communicate successfully, the control needs a way to convert values to its container's coordinates. The container provides a site object with the [**IOleControlSite::TransformCoords**](iolecontrolsite-transformcoords.md) method. The control calls this method on its container's client site first to convert its coordinates into the appropriate coordinates for the container. Then, it can pass the converted coordinates to the container.

Controls can call [**IOleControlSite::LockInPlaceActive**](iolecontrolsite-lockinplaceactive.md) in the container's site object to prevent the container from attempting to demote the control out of the in-place active state. Demoting the control in this way causes the control to be deactivated and its window destroyed, so if the control must maintain its window for a known duration it can call **LockInPlaceActive** to guarantee its state.

## Related topics

<dl> <dt>

[ActiveX Controls](activex-controls.md)
</dt> </dl>

 

 




