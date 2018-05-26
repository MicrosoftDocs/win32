---
Description: Multiple processes can have handles to the same event, mutex, semaphore, or timer object, so these objects can be used to accomplish interprocess synchronization.
ms.assetid: 1738e586-580f-4b74-95dc-ede300b6ac9a
title: Interprocess Synchronization
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interprocess Synchronization

Multiple processes can have handles to the same event, mutex, semaphore, or timer object, so these objects can be used to accomplish interprocess synchronization. The process that creates an object can use the handle returned by the creation function ([**CreateEvent**](/windows/win32/WinBase/nf-synchapi-createeventa?branch=master), [**CreateMutex**](/windows/win32/WinBase/nf-synchapi-createmutexa?branch=master), [**CreateSemaphore**](/windows/win32/WinBase/nf-winbase-createsemaphorea?branch=master), or [**CreateWaitableTimer**](/windows/win32/WinBase/nf-winbase-createwaitabletimera?branch=master)). Other processes can open a handle to the object by using its name, or through inheritance or duplication. For more information, see the following topics:

-   [Object Names](object-names.md)
-   [Object Inheritance](object-inheritance.md)
-   [Object Duplication](object-duplication.md)

 

 



