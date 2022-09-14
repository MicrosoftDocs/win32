---
title: View Caching
description: View Caching
ms.assetid: d19c111c-1367-43a2-97a9-35dc0ff5dcc8
ms.topic: article
ms.date: 05/31/2018
---

# View Caching

A container application must be able to obtain a presentation of an object for the purpose of displaying or printing it for users when the document is open but the object's server application is not running or is not installed on the user's machine. To assume, however, that the servers for all the objects that might conceivably be found in a document are installed on every user's machine and can always run on demand is unrealistic. The default object handler, which is available at all times, solves this dilemma by caching object presentations in the document's storage and manipulating these presentations on any platform regardless of the availablility of the object server on any particular installation of the container.

Containers can maintain drawing presentations for one or more specific target devices in addition to the one required to maintain the object on screen. Moreover, if you port the object from one platform to another, OLE automatically converts the object's data formats to ones supported on the new platform. For example, if you move an object from Windows to the Macintosh, OLE will convert its metafile presentations to PICT formats.

In order to present an accurate representation of an embedded object to the user, the object's container application initiates a dialog with the object handler, requesting data and drawing instructions. To be able to fulfill the container's requests, the handler must implement the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject), [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2), and [**IOleCache**](/windows/desktop/api/OleIdl/nn-oleidl-iolecache) interfaces.

[**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) enables an OLE container application to get data from and send data to its embedded or linked objects. When data changes in an object, this interface provides a way for the object to make its new data available to its container and provides the container with a way to update the data in its copy of the object. (For a discussion of data transfer in general, see Chapter 4, Data Transfer.)

The [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2) interface is very much like the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface except that it asks an object to draw itself on a device context, such as a screen, printer, or metafile, rather than move or copy its data to memory or some other transfer medium. The purpose of the interface is to enable an OLE container to obtain alternative pictorial representations of its embedded objects, whose data it already has, thereby avoiding the overhead of having to transfer entirely new instances of the same data objects simply to obtain new drawing instructions. Instead, the **IViewObject2**interface enables the container to ask an object to provide a pictorial representation of itself by drawing on a device context specified by the container.

When calling the [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2) interface, a container application can also specify that the object draw itself on a target device different than the one on which it will actually be rendered. This enables the container, as needed, to generate different renderings from a single object. For example, the caller could ask the object to compose itself for a printer even though the resulting drawing will be rendered on screen. The result, of course, would be a print-preview of the object.

The [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2)interface also provides methods that enable containers to register for view-change notifications. As with data and OLE advisories, a view advisory connection enables a container to update its renderings of an object at its own convenience rather than in response to a call from the object. For example, if a new version of an object's server application were to offer additional views of the same data, the object's default handler would call each container's implementation of [**IAdviseSink::OnViewChange**](/windows/desktop/api/ObjIdl/nf-objidl-iadvisesink-onviewchange) to let them know that the new presentations were available. The container would retrieve this information from the advise sink only when needed.

Because Windows device contexts have meaning only within a single process, you cannot pass [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2) pointers across process boundaries. As a result, OLE local and remote servers have no need whatsoever to implement the interface, which wouldn't work properly even if they did. Only object handlers and in-process servers implement the **IViewObject2**interface. OLE provides a default implementation, which you can use in your own OLE in-process servers and object handlers simply by aggregating the OLE default handler. Or you can write your own implementation of **IViewObject2**.

An object implements the [**IOleCache**](/windows/desktop/api/OleIdl/nn-oleidl-iolecache) interface in order to let the handler know what capabilities it should cache. The object handler also owns the cache and ensures it is kept up to date. As the embedded object enters the running state, the handler sets up appropriate advisory connections on the server object, with itself acting as the sink. The [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) and [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2)interface implementations operate out of data cached on the client side. The handler's implementation of **IViewObject2**is responsible for determining what data formats to cache in order to satisfy client draw requests. The handler's implementation of **IDataObject** is responsible for getting data in various formats, etc., between memory and the underlying [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) instance of the embedded object. Custom handlers can use these implementations by aggregating on the default handler.

> [!Note]  
> The [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2) interface is a simple functional extension of [**IViewObject**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject) and should be implemented instead of the latter interface, which is now obsolete. In addition to providing the **IViewObject** methods, the **IViewObject2** interface provides a single additional member, [**GetExtent**](/windows/desktop/api/OleIdl/nf-oleidl-iviewobject2-getextent), which enables a container application to get the size of an object's presentation from the cache without first having to move the object into the running state with a call to [**IOleObject::GetExtent**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getextent).

 

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 