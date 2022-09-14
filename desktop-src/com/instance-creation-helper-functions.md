---
title: Instance Creation Helper Functions
description: Instance Creation Helper Functions
ms.assetid: 0b9b7bcf-f0f0-42c4-945e-63a532640d4b
ms.topic: article
ms.date: 05/31/2018
---

# Instance Creation Helper Functions

In previous releases of COM, the primary mechanism used to create an object instance was the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function. This function encapsulates the process of creating a class object, using that to create a new instance and releasing the class object. Another function of this kind is the more specific [**OleCreate**](/windows/desktop/api/ole/nf-ole-olecreate), the OLE compound document helper that creates a class object and retrieves a pointer to a requested object.

To smooth the process of instance creation on distributed systems, COM has introduced four important new instance creation mechanisms:

-   Class monikers and [**IClassActivator**](/windows/desktop/api/ObjIdl/nn-objidl-iclassactivator)
-   [**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex)
-   [**CoGetInstanceFromFile**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromfile)
-   [**CoGetInstanceFromIStorage**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromistorage)

A class moniker permits you to identify the class of an object and is typically used with another moniker, like a file moniker, to indicate the location of the object. This permits you to bind to an object and specify the server that is to be launched for that object. Class monikers may also be composed to the right of monikers supporting binding to the [**IClassActivator**](/windows/desktop/api/ObjIdl/nn-objidl-iclassactivator) interface. For more information, see [Class Monikers](class-monikers.md).

[**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex) extends [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) to make it possible to create a single uninitialized object associated with the given CLSID on a specified remote machine. In addition, rather than requesting a single interface and obtaining a single pointer to that interface, **CoCreateInstanceEx** makes it possible to query for multiple interfaces and (if available) receive pointers to them in a single round-trip, thus permitting fewer round-trips between machines. This can make remote object interaction much more efficient. To do this, the function uses an array of [**MULTI\_QI**](/windows/win32/api/objidlbase/ns-objidlbase-multi_qi) structures.

Creating an object through [**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex) still requires that the object be initialized through a call to one of the initialization interfaces (such as [**IPersistStorage::Load**](/windows/desktop/api/ObjIdl/nf-objidl-ipersiststorage-load)). The helper functions [**CoGetInstanceFromFile**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromfile) and [**CoGetInstanceFromIStorage**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromistorage) encapsulate both the instance creation power of **CoCreateInstanceEx** and the initialization, the former from a file and the latter from a storage.

## Related topics

<dl> <dt>

[Creating an Object Through a Class Object](creating-an-object-through-a-class-object.md)
</dt> </dl>

 

 