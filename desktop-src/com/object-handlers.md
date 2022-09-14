---
title: Object Handlers
description: Object Handlers
ms.assetid: a5b51e07-246d-42a2-b33f-2bd0c608f41a
ms.topic: article
ms.date: 05/31/2018
---

# Object Handlers

If an OLE server application is a local server, meaning that it runs in its own process space, communication between container and server must occur across process boundaries. Because this process is expensive, OLE relies on a surrogate object loaded into the container's process space to act on behalf of a local server application. This surrogate object, known as an *object handler*, services container requests that do not require the attention of the server application, such as requests for drawing. When a container requests something that the object handler cannot provide, the handler communicates with the server application using COM's out-of-process communication mechanism.

An object handler is unique to an object class. When you create an instance of a handler for one class, you cannot use it for another. When used for a compound document, the object handler implements the container-side data structures when objects of a particular class are accessed remotely.

OLE provides a default object handler that local server applications can use. For applications that require special behaviors, developers can implement a custom handler that either replaces the default handler or uses it to provide certain default behaviors.

An object handler is a DLL containing several interacting components. These components include remoting pieces to manage communication between the handler and its server application, a cache for storing an object's data, along with information on how that data should be formatted and displayed, and a controlling object that coordinates the activities of the DLL's other components. In addition, if an object is a link, the DLL also includes a linking component, or *linked object*, which keeps track of the name and location of the link source.

The *cache* contains data and presentation information sufficient for the handler to display a loaded, but not running, object in its container. OLE provides an implementation of the cache used by OLE's default object handler and the link object. The cache stores data in formats needed by the object handler to satisfy container draw requests. When an object's data changes, the object sends a notification to the cache so that an update can occur. For more information on the cache, see [View Caching](view-caching.md).

For more information, see the following topic:

-   [The Default Handler and Custom Handlers](the-default-handler-and-custom-handlers.md)

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 




