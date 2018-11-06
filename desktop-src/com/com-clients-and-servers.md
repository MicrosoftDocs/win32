---
title: COM Clients and Servers
description: A critical aspect of COM is how clients and servers interact.
ms.assetid: 5d1d8613-3087-443d-8547-a767c8ba4959
ms.topic: article
ms.date: 05/31/2018
---

# COM Clients and Servers

A critical aspect of COM is how clients and servers interact. A *COM client* is whatever code or object gets a pointer to a COM server and uses its services by calling the methods of its interfaces. A *COM server* is any object that provides services to clients; these services are in the form of COM interface implementations that can be called by any client that is able to get a pointer to one of the interfaces on the server object.

There are two main types of servers, *in-process* and *out-of-process*. In-process servers are implemented in a dynamic linked library (DLL), and out-of-process servers are implemented in an executable file (EXE). Out-of-process servers can reside either on the local computer or on a remote computer. In addition, COM provides a mechanism that allows an in-process server (a DLL) to run in a surrogate EXE process to gain the advantage of being able to run the process on a remote computer. For more information, see [DLL Surrogates](dll-surrogates.md).

The COM programming model and constructs have now been extended so that COM clients and servers can work together across the network, not just within a given computer. This enables existing applications to interact with new applications and with each other across networks with proper administration, and new applications can be written to take advantage of networking features.

COM client applications do not need to be aware of how server objects are packaged, whether they are packaged as in-process objects (in DLLs) or as local or remote objects (in EXEs). Distributed COM further allows objects to be packaged as service applications, synchronizing COM with the rich administrative and system-integration capabilities of Windows.

> [!Note]  
> Throughout this documentation the acronym COM is used in preference to DCOM. This is because DCOM is not separate;it is just COM with a longer wire. In cases where what is being described is specifically a remote operation, the term *distributed COM* is used.

 

COM is designed to make it possible to add the support for location transparency that extends across a network. It allows applications written for single computers to run across a network and provides features that extend these capabilities and add to the security necessary in a network. (For more information, see [Security in COM](security-in-com.md).)

COM specifies a mechanism by which the class code can be used by many different applications.

For more information, see the following topics:

-   [Getting a Pointer to an Object](getting-a-pointer-to-an-object.md)
-   [Creating an Object Through a Class Object](creating-an-object-through-a-class-object.md)
-   [COM Server Responsibilities](com-server-responsibilities.md)
-   [Persistent Object State](persistent-object-state.md)
-   [Providing Class Information](providing-class-information.md)
-   [Inter-Object Communication](inter-object-communication.md)

## Related topics

<dl> <dt>

[Call Synchronization](call-synchronization.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




