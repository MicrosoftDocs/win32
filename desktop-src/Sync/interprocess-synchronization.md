---
Description: 'Multiple processes can have handles to the same event, mutex, semaphore, or timer object, so these objects can be used to accomplish interprocess synchronization.'
ms.assetid: '1738e586-580f-4b74-95dc-ede300b6ac9a'
title: Interprocess Synchronization
---

# Interprocess Synchronization

Multiple processes can have handles to the same event, mutex, semaphore, or timer object, so these objects can be used to accomplish interprocess synchronization. The process that creates an object can use the handle returned by the creation function ([**CreateEvent**](createevent.md), [**CreateMutex**](createmutex.md), [**CreateSemaphore**](createsemaphore.md), or [**CreateWaitableTimer**](createwaitabletimer.md)). Other processes can open a handle to the object by using its name, or through inheritance or duplication. For more information, see the following topics:

-   [Object Names](object-names.md)
-   [Object Inheritance](object-inheritance.md)
-   [Object Duplication](object-duplication.md)

 

 



