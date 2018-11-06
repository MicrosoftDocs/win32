---
title: Single-Threaded and Multithreaded Communication
description: Single-Threaded and Multithreaded Communication
ms.assetid: 8d3a855c-b52d-48bb-9fdf-efbf8005c374
ms.topic: article
ms.date: 05/31/2018
---

# Single-Threaded and Multithreaded Communication

A client or server that supports both single-threaded and multithreaded apartments will have one multithreaded apartment, containing all threads initialized as free-threaded, and one or more single-threaded apartments. Interface pointers must be marshaled between apartments but can be used without marshaling within an apartment. Calls to objects in a single-threaded apartment will be synchronized by COM. Calls to objects in the multithreaded apartment will not be synchronized by COM.

All of the information on single-threaded apartments applies to the threads marked as apartment model, and all of the information on multithreaded apartments applies to all of the threads marked as free-threaded. Apartment threading rules apply to inter-apartment communication, requiring that interface pointers be marshaled between apartments with calls to [**CoMarshalInterThreadInterfaceInStream**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterthreadinterfaceinstream) and [**CoGetInterfaceAndReleaseStream**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetinterfaceandreleasestream), as described in [Single-Threaded Apartments](single-threaded-apartments.md).

> [!Note]  
> Some special considerations apply when dealing with in-process servers. For more information, see [In-Process Server Threading Issues](in-process-server-threading-issues.md).

 

## Related topics

<dl> <dt>

[Accessing Interfaces Across Apartments](accessing-interfaces-across-apartments.md)
</dt> <dt>

[Choosing the Threading Model](choosing-the-threading-model.md)
</dt> <dt>

[Multithreaded Apartments](multithreaded-apartments.md)
</dt> <dt>

[In-Process Server Threading Issues](in-process-server-threading-issues.md)
</dt> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> <dt>

[Single-Threaded Apartments](single-threaded-apartments.md)
</dt> </dl>

 

 




