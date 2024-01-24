---
title: Examples (RPC)
description: Examples that demonstrate Remote Procedure Call (RPC) concepts.
ms.assetid: d5db3085-6df0-4539-a605-d60055f4f4ec
keywords:
- Remote Procedure Call RPC , examples
ms.topic: article
ms.date: 05/31/2018
---

# Examples (RPC)

The Platform Software Development Kit (SDK) includes examples that demonstrate a variety of Remote Procedure Call (RPC) concepts, as follows:

-   ASYNCRPC illustrates the structure of an RPC application that uses asynchronous remote procedure calls. It also demonstrates various methods of notification of the call's completion.
-   CLUUID demonstrates use of the client-object UUID to enable a client to select from multiple implementations of a remote procedure.
-   DATA directory contains four programs: DUNION illustrates discriminated (nonencapsulated) unions; INOUT demonstrates [\[in\]](../midl/in.md), [\[out\]](../midl/out-idl.md) parameters; REPAS demonstrates the [represent\_as](/windows/desktop/Midl/represent-as) attribute; XMIT demonstrates the [transmit\_as](/windows/desktop/Midl/transmit-as) attribute.
-   DYNEPT demonstrates a client application managing its connection to the server through dynamic endpoints.
-   FILEREP directory contains four samples illustrating how developers can write a simple file replication service, a multi-user file replication service, a service supporting security features, and a service using RPC asynchronous pipes.
-   HANDLES directory contains three programs, AUTO, CXHNDL, USRDEF, which demonstrate [auto\_handle](/windows/desktop/Midl/auto-handle), \[context\_handle\], and generic (user-defined) handles, respectively.
-   HELLO is a client/server implementation of "Hello, world."
-   PICKLE directory contains two programs: PICKLP demonstrates data procedure serialization; PICKLT demonstrates data type serialization; both programs use the [\[encode\]](../midl/encode.md) and [\[decode\]](../midl/decode.md) attributes.
-   PIPES demonstrates the use of the pipe-type constructor.
-   RPCSVC demonstrates the implementation of a service with RPC.
-   STROUT demonstrates how to allocate memory at a server for a two-dimensional object (an array of pointers) and pass it back to the client as an \[out\]-only parameter. The client then frees the memory. This technique allows the stub to call the server without knowing in advance how much data will be returned.

    This program also allows the user to compile either for UNICODE or ANSI.

All of the source files and makefiles for these programs are located in the Platform SDK.

For basic RPC application development and simpler examples, please see the [Tutorial](tutorial.md) topics.

 

 
