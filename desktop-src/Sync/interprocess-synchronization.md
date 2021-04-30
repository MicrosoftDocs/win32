---
description: Multiple processes can have handles to the same event, mutex, semaphore, or timer object, so these objects can be used to accomplish interprocess synchronization.
ms.assetid: 1738e586-580f-4b74-95dc-ede300b6ac9a
title: Interprocess Synchronization
ms.topic: article
ms.date: 05/31/2018
---

# Interprocess Synchronization

Multiple processes can have handles to the same event, mutex, semaphore, or timer object, so these objects can be used to accomplish interprocess synchronization. The process that creates an object can use the handle returned by the creation function ([**CreateEvent**](/windows/win32/api/synchapi/nf-synchapi-createeventa), [**CreateMutex**](/windows/win32/api/synchapi/nf-synchapi-createmutexa), [**CreateSemaphore**](/windows/desktop/api/WinBase/nf-winbase-createsemaphorea), or [**CreateWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw)). Other processes can open a handle to the object by using its name, or through inheritance or duplication. For more information, see the following topics:

-   [Object Names](object-names.md)
-   [Object Inheritance](object-inheritance.md)
-   [Object Duplication](object-duplication.md)

 

 
