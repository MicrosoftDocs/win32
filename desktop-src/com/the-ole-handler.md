---
title: The OLE Handler
description: An OLE handler is a DLL containing several interacting components used for linking and embedding.
ms.assetid: 5a01b4be-38cf-4019-ba20-ee67b836a3e0
ms.topic: article
ms.date: 05/31/2018
---

# The OLE Handler

An *OLE handler* is a DLL containing several interacting components used for linking and embedding. To avoid the expense of constant interprocess communication between a container and its server, the handler is loaded into the container's process space to act on behalf of a server as a sort of surrogate process. The OLE handler manages container requests that do not require the attention of the server application, such as requests for drawing. When a container requests something that the object handler cannot provide, the handler communicates with the server application using the COM out-of-process communication mechanism.

The OLE handler components include remoting pieces to manage communication between the handler and its server, a cache for storing an object's data (along with information on how that data should be formatted and displayed), and a controlling object that coordinates the activities of the DLL's other components. In addition, if an object is a link, the DLL also includes a linking component, or *linked object*, which keeps track of the name and location of the link source.

OLE provides a default handler that most applications use for linking and embedding. If the default does not match the requirements of your server, you can either completely replace the default handler or use parts of the functionality it provides where appropriate. In the latter case, the application handler is implemented as an aggregate object composed of a new control object and the default handler. Combination application/default handlers are also known as *in-process handlers*. The *remoting handler* is used for objects that are not assigned a CLSID in the system registry or that have no specified handler. All that is required from a handler for these types of objects is that they pass information across the process boundary. To create a new instance of the default handler, call [**OleCreateDefaultHandler**](/windows/desktop/api/Ole2/nf-ole2-olecreatedefaulthandler). For some special circumstances, call [**OleCreateEmbeddingHelper**](/windows/desktop/api/Ole2/nf-ole2-olecreateembeddinghelper).

When you create an instance of a handler for one class, you cannot use it for another. When used for a compound document, the OLE handler implements the container-side data structures when objects of a particular class are accessed remotely.

OLE defined the default handler for clients of compound document local servers. The default handler implemented a number of interfaces that the typical server did not. When OLE subsequently allowed in-process servers for compound documents, they had to create an embedding helper that implemented these extra interfaces so that clients could seamlessly work with them.

Framework designers that define and implement a client-side handler should consider this issue in their design and should provide an equivalent in-process helper for the same reasons. Even if the designers currently don't implement interfaces on the handler that the servers don't expose, they may want to define a helper now so that they can add them in the future. Alternatively, one could implement the extra interfaces on the server object itself.

## Related topics

<dl> <dt>

[The Lightweight Client-Side Handler](the-lightweight-client-side-handler.md)
</dt> </dl>

 

 




