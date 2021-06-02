---
title: In-Context Hook Functions
ms.assetid: bf12bda6-b00e-4fbe-a576-b989aa428b54
description: "Learn more about: In-Context Hook Functions"
ms.topic: article
ms.date: 05/31/2018
---

# In-Context Hook Functions

The following list outlines the key aspects of in-context hook functions:

-   In-context hooks functions must be located in a dynamic-link library (DLL) that the system maps into the server's address space.
-   In-context hook functions share the address space with the server.
-   When the server triggers an event, the system calls a hook function without marshaling (packaging and sending interface parameters across process boundaries).
-   In-context hook functions tend to be very fast and receive event notifications synchronously because there is no marshaling.
-   Some events may be delivered out-of-process, even though you request that they be delivered in-process (using the WINEVENT\_INCONTEXT flag). You might see this situation with 64-bit and 32-bit application interoperability issues and with Windows console events.

 

 




