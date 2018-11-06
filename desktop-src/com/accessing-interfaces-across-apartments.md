---
title: Accessing Interfaces Across Apartments
description: Accessing Interfaces Across Apartments
ms.assetid: 4e0467b9-bbf1-410c-8aab-40450a7f963a
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Interfaces Across Apartments

COM provides a way for any apartment in a process to get access to an interface implemented on an object in any other apartment in the process. This is done through the [**IGlobalInterfaceTable**](/windows/desktop/api/ObjIdl/nn-objidl-iglobalinterfacetable) interface. This interface has three methods, which allow you to do the following:

-   Register an interface as a *global* (processwide) interface.
-   Get a pointer to that interface from any other apartment through a cookie.
-   Revoke the global registration of an interface.

The [**IGlobalInterfaceTable**](/windows/desktop/api/ObjIdl/nn-objidl-iglobalinterfacetable) interface is an efficient way for a process to store an interface pointer in a memory location that can be accessed from multiple apartments within the process, such as process-wide variables and *agile* objects (free-threaded, marshaled objects) containing interface pointers to other objects.

An agile object is unaware of the underlying COM infrastructure in which it runs; in other words, what apartment, context, and thread it is executing on. The object may be holding on to interfaces that are specific to an apartment or context. For this reason, calling these interfaces from wherever the agile component is executing might not always work properly. The global interface table avoids this problem by guaranteeing that a valid proxy (or direct pointer) to the object is used, based on where the agile object is executing.

> [!Note]  
> The global interface table is not portable across process or machine boundaries, so it cannot be used in place of the normal parameter-passing mechanism.

 

For information about creating and using a global interface table, see the following topics:

-   [Creating the Global Interface Table](creating-the-global-interface-table.md)
-   [When to Use the Global Interface Table](when-to-use-the-global-interface-table.md)

## Related topics

<dl> <dt>

[Choosing the Threading Model](choosing-the-threading-model.md)
</dt> <dt>

[Multithreaded Apartments](multithreaded-apartments.md)
</dt> <dt>

[In-Process Server Threading Issues](in-process-server-threading-issues.md)
</dt> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> <dt>

[Single-Threaded and Multithreaded Communication](single-threaded-and-multithreaded-communication.md)
</dt> <dt>

[Single-Threaded Apartments](single-threaded-apartments.md)
</dt> </dl>

 

 




