---
title: Instance Creation Helper Functions
description: Instance Creation Helper Functions
ms.assetid: 0b9b7bcf-f0f0-42c4-945e-63a532640d4b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Instance Creation Helper Functions

In previous releases of COM, the primary mechanism used to create an object instance was the [**CoCreateInstance**](/windows/win32/combaseapi/nf-combaseapi-cocreateinstance?branch=master) function. This function encapsulates the process of creating a class object, using that to create a new instance and releasing the class object. Another function of this kind is the more specific [**OleCreate**](/windows/win32/ole/nf-ole-olecreate?branch=master), the OLE compound document helper that creates a class object and retrieves a pointer to a requested object.

To smooth the process of instance creation on distributed systems, COM has introduced four important new instance creation mechanisms:

-   Class monikers and [**IClassActivator**](/windows/win32/ObjIdl/nn-objidl-iclassactivator?branch=master)
-   [**CoCreateInstanceEx**](/windows/win32/combaseapi/nf-combaseapi-cocreateinstanceex?branch=master)
-   [**CoGetInstanceFromFile**](/windows/win32/Objbase/nf-objbase-cogetinstancefromfile?branch=master)
-   [**CoGetInstanceFromIStorage**](/windows/win32/Objbase/nf-objbase-cogetinstancefromistorage?branch=master)

A class moniker permits you to identify the class of an object and is typically used with another moniker, like a file moniker, to indicate the location of the object. This permits you to bind to an object and specify the server that is to be launched for that object. Class monikers may also be composed to the right of monikers supporting binding to the [**IClassActivator**](/windows/win32/ObjIdl/nn-objidl-iclassactivator?branch=master) interface. For more information, see [Class Monikers](class-monikers.md).

[**CoCreateInstanceEx**](/windows/win32/combaseapi/nf-combaseapi-cocreateinstanceex?branch=master) extends [**CoCreateInstance**](/windows/win32/combaseapi/nf-combaseapi-cocreateinstance?branch=master) to make it possible to create a single uninitialized object associated with the given CLSID on a specified remote machine. In addition, rather than requesting a single interface and obtaining a single pointer to that interface, **CoCreateInstanceEx** makes it possible to query for multiple interfaces and (if available) receive pointers to them in a single round-trip, thus permitting fewer round-trips between machines. This can make remote object interaction much more efficient. To do this, the function uses an array of [**MULTI\_QI**](/windows/win32/objidlbase/ns-objidl-tagmulti_qi?branch=master) structures.

Creating an object through [**CoCreateInstanceEx**](/windows/win32/combaseapi/nf-combaseapi-cocreateinstanceex?branch=master) still requires that the object be initialized through a call to one of the initialization interfaces (such as [**IPersistStorage::Load**](/windows/win32/ObjIdl/nf-objidl-ipersiststorage-load?branch=master)). The helper functions [**CoGetInstanceFromFile**](/windows/win32/Objbase/nf-objbase-cogetinstancefromfile?branch=master) and [**CoGetInstanceFromIStorage**](/windows/win32/Objbase/nf-objbase-cogetinstancefromistorage?branch=master) encapsulate both the instance creation power of **CoCreateInstanceEx** and the initialization, the former from a file and the latter from a storage.

## Related topics

<dl> <dt>

[Creating an Object Through a Class Object](creating-an-object-through-a-class-object.md)
</dt> </dl>

 

 




