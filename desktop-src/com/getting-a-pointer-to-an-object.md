---
title: Getting a Pointer to an Object
description: Getting a Pointer to an Object
ms.assetid: 4af9d356-402b-4e69-9f6e-8589057d3ac4
ms.topic: article
ms.date: 05/31/2018
---

# Getting a Pointer to an Object

Because COM does not have a strict class model, there are four ways that a client can instantiate or get a pointer to an interface on an object:

-   Call a COM library function that creates an object of a predetermined type; that is, the function will return a pointer to only one specific interface for a specific object class.
-   Call a COM library function that can create an object based on a class identifier (CLSID) and that returns any type of interface pointer requested.
-   Call a method of some interface that creates another object (or connects to an existing one) and returns an interface pointer on that separate object.
-   Implement an object with an interface through which other objects pass their interface pointer to the client directly.

For information on getting pointers to other interfaces on an object after you have the first one, see [QueryInterface: Navigating in an Object](queryinterface--navigating-in-an-object.md).

## Creating an Object of a Predetermined Type

There are numerous COM functions, such as [**CoGetMalloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetmalloc), that return pointers to specific interface implementations. (**CoGetMalloc** retrieves a pointer to the standard COM memory allocator.) Most of these are helper functions, and most of these functions are described in the reference sections of this documentation, under the specific area they are related to, such as storage or data transfer.

## Creating an Object Based on a CLSID

There are several functions that, given a CLSID, a client can call to create an object instance and get a pointer to it. All of these functions are based on the function [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject), which creates a class object and supplies a pointer to an interface that allows you to create instances of that class. While there must be information that says which system the server resides on, there is no need for that information to be contained in the client. The client needs to know only the CLSID and never the absolute path of the server code. For more information, see [Creating an Object Through a Class Object](creating-an-object-through-a-class-object.md).

## Returning a Pointer to a Separate Object

Among the many interface methods that return a pointer to a separate object are several that create and return a pointer to an *enumerator object*, which allows you to determine how many items of a given type an object maintains. COM defines interfaces for enumerating a wide variety of items, such as strings, important structures, monikers, and [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface pointers. The typical way to create an enumerator instance and get a pointer to its interface is to call a method from another interface. For example, the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface defines two methods, [**EnumDAdvise**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-enumdadvise) and [**EnumFormatEtc**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-enumformatetc), that return pointers to interfaces on two different enumeration objects. There are many other examples in COM of methods that return pointers to objects, such as the OLE compound document interface [**IOleObject::GetClientSite**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getclientsite), which, when called on the embedded or linked object, returns a pointer to the container object's implementation of [**IOleClientSite**](/windows/desktop/api/OleIdl/nn-oleidl-ioleclientsite).

## Implementing an Object Through Which to Pass an Interface Pointer Directly to the Client

When two objects, such as an OLE compound document container and server, need bidirectional communication, each implements an object containing an interface method through which it can pass an interface pointer to the other object. The implementing object, which is also the client of the created object, can then call the method and get the pointer that was passed.

## Related topics

<dl> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> <dt>

[COM Server Responsibilities](com-server-responsibilities.md)
</dt> </dl>

 

 




