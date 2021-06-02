---
description: Generally, synchronization is not required when you have a single-threaded apartment (STA) because the apartment provides the synchronization for you.
ms.assetid: a05de040-0115-44aa-80e2-55eff2ec894d
title: COM+ Synchronization Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Synchronization Concepts

Generally, synchronization is not required when you have a single-threaded apartment (STA) because the apartment provides the synchronization for you. Synchronization becomes important when you have a multithreaded apartment (MTA) and a free-threaded object. In the past, free-threaded objects have had to handle locking. You can eliminate the need to use locking by setting the synchronization attribute for a component.

Synchronization has the following properties:

-   Allows one caller to enter the component at a time.
-   Prohibits flow across process or across computer.
-   Flows from component to component within a process.
-   Allows reentrancy from the same caller.

Unlike apartments, activities span contexts from multiple processes and hosts. Synchronization determines which activity will contain an object. Objects can reside in any of the following activities:

-   Creator's activity
-   New activity
-   No activity

COM+ ensures concurrency by a series of locks for each activity. If a caller tries to enter a COM+ synchronized component that is already being used by another caller, the call is blocked until the lock is released. This blocking behavior will not time out and cannot be configured to time out. If the lock is not in use, the lock is acquired and the call is processed. After completing, the lock is released for the next caller. To prevent deadlock, COM+ manages access to all objects across activities by a nested series of calls chained throughout the network.

COM+ provides the following synchronization settings:

-   Disabled
-   Not Supported
-   Supported
-   Required
-   Requires New

> [!Note]  
> Some synchronization settings work in conjunction with other COM+ component settings. For example, synchronization is required if the [COM+ just-in-time (JIT) activation](com--just-in-time-activation.md) service is enabled. JIT is required if you enable transactions; therefore, COM+ [transaction processing](com--transactions.md) requires synchronization as well. So, classes with the setting of JIT=True must also have the setting of either Synchronization=Required or Synchronization=RequiresNew.

 

For instructions about setting synchronization options by using the Component Services administrative tool, see [Setting the Synchronization Attribute](setting-the-synchronization-attribute.md).

To obtain more information on using the COM+ Administration Library to set synchronization options, see [Automating COM+ Administration](automating-com--administration.md).

## Related topics

<dl> <dt>

[COM+ Synchronization Tasks](com--synchronization-tasks.md)
</dt> </dl>

 

 



