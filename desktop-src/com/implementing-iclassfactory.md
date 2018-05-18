---
title: Implementing IClassFactory
description: Implementing IClassFactory
ms.assetid: '96466756-c135-4ee5-a48c-f31129878473'
---

# Implementing IClassFactory

When a client uses a CLSID to request the creation of an object instance, the first step is creation of a class object, an intermediate object that contains an implementation of the methods of the [**IClassFactory**](iclassfactory.md) interface. While COM provides several instance creation functions, the first step in the implementation of these functions is the creation of a class object.

As a result, all servers must implement the methods of the [**IClassFactory**](iclassfactory.md) interface, which contains two methods:

-   [**CreateInstance**](iclassfactory-createinstance.md). This method must create an uninitialized instance of the object and return a pointer to a requested interface on the object.
-   [**LockServer**](iclassfactory-lockserver.md). This method just increments the reference count on the class object to ensure that the server stays in memory and does not shut down before the client is ready for it to do so.

To enable a server to be responsible for its own licensing, COM defines [**IClassFactory2**](iclassfactory2.md), which inherits its definition from [**IClassFactory**](iclassfactory.md). Thus, a server implementing **IClassFactory2** must, by definition, implement the methods of **IClassFactory**.

COM also provides helper functions for implementing out-of-process servers. For more information, see [Out-of-Process Server Implementation Helpers](out-of-process-server-implementation-helpers.md).

## Related topics

<dl> <dt>

[COM Server Responsibilities](com-server-responsibilities.md)
</dt> <dt>

[Licensing and IClassFactory2](licensing-and-iclassfactory2.md)
</dt> </dl>

 

 




