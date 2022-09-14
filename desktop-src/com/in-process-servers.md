---
title: In-Process Servers
description: In-Process Servers
ms.assetid: cc0c4350-fa75-4321-834f-711158776cb2
ms.topic: article
ms.date: 05/31/2018
---

# In-Process Servers

If you implement an OLE server application as an in-process server — a DLL running in the process space of the container application — rather than as a local server — an EXE running in its own process space — communication between container and server is simplified because communication between the two can take the form of normal function calls. Remote procedure calls are not required because the two applications run in the same process space. As you would expect, the objects that manage the marshaling of parameters are also unnecessary, although they may be aggregated within the DLL without interfering with the communication between container and server.

When an OLE server application is implemented as an in-process server, a separate object handler is not required because the server itself lives in the client's process space. The main difference between an in-process server and object handler is that the server is able to manage the object in a running state while the handler cannot. One consequence of this difference is that a server must provide a user interface for manipulating the running object, while a handler delegates this requirement to the object's server. In creating an in-process server, you can aggregate on the OLE default handler, letting it handle basic chores, such as display, storage, and notifications while you implement only those services that the handler either does not provide or does not implement in the way you require.

For more information, see the following topics:

-   [Advantages](advantages.md)
-   [Disadvantages](disadvantages.md)

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 




