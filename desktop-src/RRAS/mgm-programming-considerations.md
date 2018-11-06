---
title: MGM Programming Considerations
description: When you are developing multicast group manager clients, observe the following guidelines
ms.assetid: 48451a76-81e0-4d60-acb3-c9ec55de32b4
keywords:
- Multicast, Programming considerations
ms.topic: article
ms.date: 05/31/2018
---

# MGM Programming Considerations

When you are developing multicast group manager clients, observe the following guidelines:

-   Function calls must be made from within the router process. If functions are called from another process, their results will not be valid; the client will not interact with the multicast group manager.
-   Clients that use the MGM API must provide their own error checking, ensuring that only valid data is passed to the multicast group manager. MGM functions do not return detailed error messages about invalid parameters; the ERROR\_INVALID\_PARAMETER value is returned without explanation.
-   Clients should exercise caution in using locks while calling MGM functions. Doing so can prevent deadlocks. When calling MGM functions, clients should not hold any locks that might simultaneously be held in a callback from the multicast group manager.

 

 




