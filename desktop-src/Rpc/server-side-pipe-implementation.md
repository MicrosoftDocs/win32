---
title: Server-Side Pipe Implementation
description: Server programs for distributed applications that use pipes need not implement any push, pull, or alloc functions.
ms.assetid: de733075-5767-4d46-b294-089c7e3cc695
ms.topic: article
ms.date: 05/31/2018
---

# Server-Side Pipe Implementation

Server programs for distributed applications that use pipes need not implement any push, pull, or alloc functions. They do need to contain procedures that clients can invoke remotely to initiate data transfers. In the following topics, this section explains how the server's remote procedures can be implemented.

-   [Implementing Input Pipes on the Server](implementing-input-pipes-on-the-server.md)
-   [Implementing Output Pipes on the Server](implementing-output-pipes-on-the-server.md)

 

 




