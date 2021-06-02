---
title: Out-of-Context Hook Functions
ms.assetid: 'c0156485-db1e-42d3-bbbd-c51835a597ed'
description: "Learn more about: Out-of-Context Hook Functions"
ms.topic: article
ms.date: 05/31/2018
---

# Out-of-Context Hook Functions

The following list outlines the key aspects of out-of-context hook functions:

-   Out-of-context hook functions are located in the client's address space, whether it is in the code body or in a DLL.
-   Out-of-context hook functions are not mapped into the server's address space.
-   When an event is triggered, the parameters for the hook function are marshaled across process boundaries.
-   Out-of-context hook functions are noticeably slower than in-context hook functions due to marshaling.
-   The system queues the event notifications so that they arrive asynchronously (because of the time required to perform marshaling).

Although the event notifications are asynchronous, Microsoft Active Accessibility assures that the callback function receives all events in the order in which they are generated.

The USER component of the operating system allocates memory for events that are handled by out-of-context hook functions. The memory is freed when the hook functions return. If a hook function does not process events quickly enough, USER resources are lowered, eventually resulting in a fault or extremely slow response times. These problems may occur if:

-   Events are fired very rapidly.
-   The system is slow.
-   The hook function processes events slowly.
-   The client is running on Windows 9x.

 

 




