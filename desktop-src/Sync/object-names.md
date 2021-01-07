---
description: Named objects provide an easy way for processes to share object handles.
ms.assetid: 00a00227-45fc-49a1-8ff5-aeccb172d16a
title: Object Names
ms.topic: article
ms.date: 05/31/2018
---

# Object Names

Named objects provide an easy way for processes to share object handles. After a process has created a named event, mutex, semaphore, or timer object, other processes can use the name to call the appropriate function ( [**OpenEvent**](/windows/win32/api/synchapi/nf-synchapi-openeventa), [**OpenMutex**](/windows/win32/api/synchapi/nf-synchapi-openmutexw), [**OpenSemaphore**](/windows/win32/api/synchapi/nf-synchapi-opensemaphorew), or [**OpenWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-openwaitabletimerw)) to open a handle to the object. Name comparison is case sensitive.

The names of event, semaphore, mutex, waitable timer, file-mapping, and job objects share the same namespace. If you try to create an object using a name that is in use by an object of another type, the function fails and [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **ERROR\_INVALID\_HANDLE**. Therefore, when creating named objects, use unique names and be sure to check function return values for duplicate-name errors.

If you try to create an object using a name that is in use by an object of same type, the function succeeds, returning a handle to the existing object, and [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **ERROR\_ALREADY\_EXISTS**. For example, if the name specified in a call to the [**CreateMutex**](/windows/win32/api/synchapi/nf-synchapi-createmutexa) function matches the name of an existing mutex object, the function returns a handle to the existing object. In this case, the call to **CreateMutex** is equivalent to a call to the [**OpenMutex**](/windows/win32/api/synchapi/nf-synchapi-openmutexw) function. Having multiple processes use **CreateMutex** for the same mutex is therefore equivalent to having one process that calls **CreateMutex** while the other processes call **OpenMutex**, except that it eliminates the need to ensure that the creating process is started first. When using this technique for mutex objects, however, none of the calling processes should request immediate ownership of the mutex. If multiple processes do request immediate ownership, it can be difficult to predict which process actually gets the initial ownership.

A Terminal Services environment has a global namespace for events, semaphores, mutexes, waitable timers, file-mapping objects, and job objects. In addition, each Terminal Services client session has its own separate namespace for these objects. Terminal Services client processes can use object names with a "Global\\" or "Local\\" prefix to explicitly create an object in the global or session namespace. For more information, see [Kernel Object Namespaces](../termserv/kernel-object-namespaces.md). Fast user switching is implemented using Terminal Services sessions (each user logs into a different session). Kernel object names must follow the guidelines outlined for Terminal Services so that applications can support multiple users.

Synchronization objects can be created in a private namespace. For more information, see [Object Namespaces](object-namespaces.md).

## Related topics

<dl> <dt>

[Using Named Objects](using-named-objects.md)
</dt> </dl>

 

 
