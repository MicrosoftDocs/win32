---
description: COM+ Resource Dispenser Thread Types
ms.assetid: 3ab67adb-311f-404c-a3ca-d274af53f91c
title: COM+ Resource Dispenser Thread Types
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Resource Dispenser Thread Types

Calls into a COM+ resource dispenser may originate in one of the following thread types:

-   Apartment thread (STA)
-   Free thread (MTA)
-   Non-COM thread (application or the [dispenser manager](com--dispenser-manager.md) garbage-collector thread)

If a resource dispenser is not a COM object, it must be able to handle calls arriving from any thread at any time. If a resource dispenser is a COM object, the COM object should be registered with a threading model of **Both**. This allows STA or MTA threads to create and use the resource dispenser without a thread switch.

If a resource dispenser creates and uses another COM object (for example, an out-of-process resource manager), the resource dispenser might need to maintain multiple proxies to this other COM object and ensure that calls to the object are made using the appropriate proxy for the calling thread. When the resource dispenser creates this object, it marshals and saves the reference. Before calling the object again, it must unmarshal to create a proxy for the calling thread.

It might be more efficient to cache these per-thread proxies by keeping a map from the thread ID to a proxy pointer. This map expands as new threads are used in the process.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> </dl>

 

 



