---
title: Memory-Management Models
description: Memory-Management Models
ms.assetid: 1690901b-2a1e-455b-a440-2674f5e5dfa4
ms.topic: article
ms.date: 05/31/2018
---

# Memory-Management Models

As a developer, you have several choices for how memory is allocated and freed. Consider a complex data structure that consists of nodes connected with pointers, such as a linked list or a tree. You can apply attributes that select one of the following models:

-   [Node-by-node allocation and deallocation](node-by-node-allocation-and-deallocation.md).
-   [A single linear buffer allocated by the stub for the entire tree](stub-allocated-buffers.md).
-   [Server stub memory management](server-stub-memory-management.md)
-   [A single linear buffer allocated by the client application for the entire tree](application-allocated-buffer.md).
-   [Persistent storage on the server](persistent-storage-on-the-server.md).

 

 




