---
title: COM Server Responsibilities
description: COM Server Responsibilities
ms.assetid: 9853bbf5-b989-45b7-8fa8-8cd2f0d48d3c
ms.topic: article
ms.date: 05/31/2018
---

# COM Server Responsibilities

One of the most important ways for a client to get a pointer to an object is for the client to ask that a server be launched and that an instance of the object provided by the server be created and activated. It is the responsibility of the server to ensure that this happens properly. There are several important parts to this.

The server must implement code for a class object through an implementation of either the [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) or [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2) interface.

The server must register its CLSID in the system registry on the machine on which it resides and further, has the option of publishing its machine location to other systems on a network to allow clients to call it without requiring the client to know the server's location.

The server is primarily responsible for security; that is, for the most part, the server determines whether it will provide a pointer to one of its objects to a client.

In-process servers should implement and export certain functions that allow the client process to instantiate them.

The following topics detail the responsibilities of the COM server:

-   [Implementing IClassFactory](implementing-iclassfactory.md)
-   [Licensing and IClassFactory2](licensing-and-iclassfactory2.md)
-   [Registering COM Servers](registering-com-servers.md)
-   [Out-of-Process Server Implementation Helpers](out-of-process-server-implementation-helpers.md)
-   [GUID Creation and Optimizations](guid-creation-and-optimizations.md)

## Related topics

<dl> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> </dl>

 

 