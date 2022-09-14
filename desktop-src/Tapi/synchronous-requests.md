---
description: Service provider designers should try to keep the execution time of synchronous operations short.
ms.assetid: eb264ab7-15bb-4cd5-8af8-f979f02a7a39
title: Synchronous Requests
ms.topic: article
ms.date: 05/31/2018
---

# Synchronous Requests

Service provider designers should try to keep the execution time of synchronous operations short. For example, there is an "Open" operation called at initialization time that prepares the service provider and TAPI for subsequent operations on a device. A service provider whose implementation is split between the client computer and a dedicated server may have reasonable confidence that it can communicate with its remote server. Its implementation of "Open" might just allocate and initialize data structures to represent the device and return, postponing end-to-end communication until some real operation is requested.

Any such "optimistic" implementation of a synchronous operation can later encounter resource limitations or remote communication failures. In general, even a "conservative" approach cannot entirely prevent these problems; service-provider designers must choose the best tradeoff between reliability and performance. A failure of this kind should be handled gracefully wherever possible. From the point of view of TSPI devices, they should remain valid for "bookkeeping" purposes even if they return failure status for any operation requested.

Implementing an optimistic approach for synchronous requests should not be done at the expense of correct semantics for the operation. Returning to the "Open" example, if opening a device needs to compete for and reserve a scarce, nonsharable resource such as communication ports, it should probably do so even if it is time-consuming.

**TAPI 2.x:** An operation that completes synchronously performs all of its processing in the function call made by the application. The function returns different values depending on its success or failure:

-   **Synchronous Success.** If the request or service corresponding to the function has been carried out successfully, the function returns zero, indicating success. Any values written as a result of the function call are reliable and can be used immediately.
-   **Synchronous Failure.** If the function detects an error and the request is not carried out, a negative error number is returned to identify the error.

 

 



