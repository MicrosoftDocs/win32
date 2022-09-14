---
title: Client-Side Pipe Implementation
description: Client-side pipe implementation in Remote Procedure Call (RPC).
ms.assetid: d790f859-47a9-4b6c-a218-8cbe05db21b6
ms.topic: article
ms.date: 05/31/2018
---

# Client-Side Pipe Implementation

The client application must implement the following procedures, which the client stub will call during data transfer:

-   A pull procedure (for an input pipe)
-   A push procedure (for an output pipe)
-   An alloc procedure to allocate a buffer for the transfer data

All of these procedures must use the arguments specified by the MIDL-generated header file. In addition, the client application must have a state variable to identify where to locate or place data.

The alloc procedure can also be as simple or as complex as needed. For example, it can return a pointer to the same buffer every time the stub calls the function, or it can allocate a different amount of memory each time. If your data is already in the proper form (an array of pipe elements, for example) you can coordinate the alloc procedure with the pull procedure to allocate a buffer that already contains the data. In that case, your pull procedure could be an empty routine.

The buffer allocation must be in bytes. The push and pull procedures, on the other hand, manipulate elements, whose size in bytes depends on how they were defined.

This section discusses the client implementation of input and output pipes in the following sections:

-   [Implementing Input Pipes on the Client](implementing-input-pipes-on-the-client.md)
-   [Implementing Output Pipes on the Client](implementing-output-pipes-on-the-client.md)

 

 




