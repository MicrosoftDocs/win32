---
title: Creating an Object Through a Class Object
description: Creating an Object Through a Class Object
ms.assetid: cecf21b0-e509-425f-8dd6-ca6b1ac04f5e
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Object Through a Class Object

With the increasing importance of computer networks, it has become necessary for clients and servers to interact easily and efficiently, whether they reside on the same machine or across a network. Crucial to this is a client's ability to launch a server, create an instance of the server's object, and have access to the methods of the interfaces on the object.

COM provides extensions to this basic COM process that make it virtually seamless across a network. If a client is able to identify the server through its CLSID, calling a few simple functions permit COM to do all the work of locating and launching the server and activating the object. Subkeys in the registry allow remote servers to register their location, so the client does not require that information. For applications that want to take advantage of networking features, the COM object creation functions allow more flexibility and efficiency.

For more information, see the following topics:

-   [COM Class Objects and CLSIDs](com-class-objects-and-clsids.md)
-   [Locating a Remote Object](locating-a-remote-object.md)
-   [Instance Creation Helper Functions](instance-creation-helper-functions.md)

## Related topics

<dl> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> </dl>

 

 




