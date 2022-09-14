---
title: Containers and Servers
description: Containers and Servers
ms.assetid: 4918fa52-3598-4f4d-b2e7-7a47a37b216d
ms.topic: article
ms.date: 05/31/2018
---

# Containers and Servers

Compound document applications are of two basic types: container applications and server applications. OLE container applications provide users with the ability to create, edit, save, and retrieve compound documents. OLE server applications provide users with the means to create documents and other data representations that can be contained as either links or embeddings in container applications. An OLE application can be a container application, a server application, or both.

OLE server applications also differ in whether they are implemented as *in-process servers* or *local servers*. An in-process server is a dynamic link library (DLL) that runs in the container application's process space. You can run an in-process server only from within the container application.

> [!Note]  
> Future releases of OLE will enable linking and embedding across computer boundaries, so that a container application on one computer will be able to use a compound document object provided by a *remote server* running on another computer. From a container application's point of view, any OLE server application that runs in its own process space, whether on the same computer or a remote computer, is an *out-of-processÂ server*.

 

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> <dt>

[In-Process Servers](in-process-servers.md)
</dt> </dl>

 

 




