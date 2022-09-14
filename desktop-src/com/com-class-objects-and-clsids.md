---
title: COM Class Objects and CLSIDs
description: A COM server is implemented as a COM class.
ms.assetid: 0073acdf-38a8-4f1a-aa26-379456a95fca
ms.topic: article
ms.date: 05/31/2018
---

# COM Class Objects and CLSIDs

A COM server is implemented as a COM class. A *COM class* is an implementation of a group of interfaces in code executed whenever you interact with a given object. There is an important distinction between a C++ class and a COM class: In C++, a class is a type, while a COM class is simply a definition of the object and carries no type, although a C++ programmer might implement it by using a C++ class. COM is designed to allow a class to be used by different applications, including applications written without knowledge of that particular class's existence. Therefore, class code for a given type of object exists either in a dynamic linked library (DLL) or in another executable application (EXE).

Each COM class is identified by a *CLSID*, a unique 128-bit GUID, which the server must register. COM uses this CLSID, at the request of a client, to associate specific data with the DLL or EXE containing the code that implements the class, thus creating an instance of the object.

For clients and servers on the same computer, the CLSID of the server is all the client ever needs. On each computer, COM maintains a database (it makes use of the system registry on Microsoft Windows and Macintosh platforms) of all the CLSIDs for the servers installed on the system. This is a mapping between each CLSID and the location of the DLL or EXE that houses the code for that CLSID. COM consults this database whenever a client wants to create an instance of a COM class and use its services, so the client never needs to know the absolute location of the code on the computer.

For distributed systems, COM provides registry entries that allow a remote server to register itself for use by a client. While applications need know only a server's CLSID, because they can rely on the registry to locate the server, COM allows clients to override registry entries and to specify server locations, to take full advantage of the network. (See [Locating a Remote Object](locating-a-remote-object.md).)

The basic way to create an instance of a class is through a COM *class object*. This is simply an intermediate object that supports functions common to creating new instances of a given class. Most class objects used to create objects from a CLSID support the [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) interface, an interface that includes the important [**CreateInstance**](/windows/desktop/api/Unknwn/nf-unknwn-iclassfactory-createinstance) method. You implement an **IClassFactory** interface for each class of object that you offer to be instantiated. (For more information about implementing **IClassFactory**, see [Implementing IClassFactory](implementing-iclassfactory.md).)

> [!Note]  
> Servers that support some other custom class factory interface are not required to support [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) specifically. However, calls to activation functions other than [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) (such as [**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex)) require that the server support **IClassFactory**.

 

When a client wants to create an instance of the server's object, it uses the desired object's CLSID in a call to [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject). (This call can be either direct or implicit, through one of the object creation helper functions.) This function locates the code associated with the CLSID, and creates a class object, and supplies a pointer to the interface requested. (**CoGetClassObject** takes a *riid* param that specifies the client's desired interface pointer.)

> [!Note]  
> COM has just a few functions upon which many of the others are built. The most important of these is probably [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject), which underlies all of the instance creation functions.

 

With this pointer, the caller can create an instance of the object and retrieve a pointer to a requested interface on the object. This is usually an initialization interface, used to activate the object (put it in the running state) so that the client can do whatever work with the object that it wants to. Using COM's basic functions, the client must also take care to release all object pointers.

Another mechanism for activating object instances is through the class moniker. Class monikers bind to the class object of the class for which they are created. For more information, see [Class Monikers](class-monikers.md).

COM provides several helper functions that reduce the work of creating object instances. These are described in [Instance Creation Helper Functions](instance-creation-helper-functions.md).

## Related topics

<dl> <dt>

[Creating an Object Through a Class Object](creating-an-object-through-a-class-object.md)
</dt> </dl>

 

 