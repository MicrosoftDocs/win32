---
title: Essential Pipe Terminology
description: Like other types of parameters to remote procedure calls, pipes can be \ in\ or \ out\ parameters.
ms.assetid: 377fb65a-e819-4e96-a5b7-9850afd97b73
ms.topic: article
ms.date: 05/31/2018
---

# Essential Pipe Terminology

Like other types of parameters to remote procedure calls, pipes can be \[ [**in**](/windows/desktop/Midl/in)\] or \[ [**out**](/windows/desktop/Midl/out-idl)\] parameters. Since the server controls the transfer of data through a pipe, pipes with the \[**in**\] attribute are said to *pull* data to the server. Similarly, output pipes *push* data from the server to the client. The procedures that do the data transfer are called the *pull procedure* and the *push procedure*, respectively.

The MIDL compiler generates the push and pull procedures for the server. In addition, it manages the allocation of data buffers in memory. However, the client must provide its own push and pull procedures. It must also provide a procedure for allocating the memory buffers used by the pipe. These are automatically called at the appropriate time by the client stub. The allocation procedure is often called the alloc procedure or the alloc function.

 

 