---
title: Linked Objects and Monikers
description: Linked objects, like embedded objects, rely on an object handler to communicate with server applications.
ms.assetid: f72557b9-cd24-4d96-8144-94a5344ec2ae
ms.topic: article
ms.date: 05/31/2018
---

# Linked Objects and Monikers

Linked objects, like embedded objects, rely on an object handler to communicate with server applications. The linked object itself, however, manages the naming and tracking of link sources. The linked object acts like an in-process server. For example, when activated, a linked object locates and launches the OLE server application that is the link source.

A linked object's handler is made up of two main components: the handler component and the linking component. The handler component contains the controlling and remoting pieces and functions much like a handler for an embedded object. The linking component has its own controller and cache and provides access to the object's structured storage. The linking components controller supports source naming through the use of monikers, and binding, the process of locating and running the link source. (For more information on monikers and binding, see [The Component Object Model](the-component-object-model.md).)

When a user initially creates a linked object or loads an existing one from storage, the container loads an instance of the linking component into memory, along with the object handler. The linking component supplies interfaces — most notably [**IOleLink**](/windows/desktop/api/OleIdl/nn-oleidl-iolelink)— that identify the object as a link and enable it to manage the naming, tracking, and updating of its link source.

By implementing the [**IOleLink**](/windows/desktop/api/OleIdl/nn-oleidl-iolelink) interface, a linked object provides its container with functions that support linking. Only linked objects implement **IOleLink**, and by querying for this interface a container can determine whether a given object is embedded or linked. The most important function provided by **IOleLink** enables a container to binding to the source of the linked object, that is, to activate the connection to the document that stores the linked object's native data. **IOleLink** also defines functions for managing information about the linked object, such as cached presentation data and the location of the link source.

When a compound document containing a linked object is saved, the link's data is saved with the link source, not with the container. Only information about its name and location is saved along with the compound document. This behavior is in contrast to that of an embedded object, whose data is stored along with that of its container.

Container applications can provide information about their embedded objects such that the latter, or portions thereof, can act as link sources. By implementing support for linking to your container's embedded objects, you make nested embeddings possible, relieving the user of having to track down the originals of every embedding object to which a link is desired. For example, if a user wants to embed a Microsoft Excel worksheet in Microsoft Word, and the worksheet contains a bitmap created in Paintbrush, the user can link to a copy of the bitmap contained in the worksheet rather than the original.

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> <dt>

[In-Process Servers](in-process-servers.md)
</dt> <dt>

[Object Handlers](object-handlers.md)
</dt> </dl>

 

 




