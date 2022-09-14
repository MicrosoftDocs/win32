---
title: Pipes (RPC)
description: The pipe type constructor is a highly efficient mechanism for passing large amounts of data, or any quantity of data that is not all available in memory at one time.
ms.assetid: '913d5e2a-00ad-4060-9274-a6db23fb2817'
keywords:
- Remote Procedure Call RPC , described, pipes
ms.topic: article
ms.date: 05/31/2018
---

# Pipes (RPC)

The pipe type constructor is a highly efficient mechanism for passing large amounts of data, or any quantity of data that is not all available in memory at one time. By using a pipe, RPC run time handles the actual data transfer, eliminating the overhead associated with repeated remote procedure calls.

After a client invokes a remote procedure that has a pipe parameter, the client and server enter loops to transfer data. The data can be produced on the client or the server. Either way, the amount of data (in bytes) does not have to be known in advance. The data can be produced or consumed incrementally. While in the data-transfer loop, the server calls stub routines that load or unload a buffer of data. The client calls programmer-defined procedures to allocate buffers, load data into and unload data from the buffers.

This section provides an overview of using pipes for remote procedure calls. It presents the overview in the following topics:

-   [Essential Pipe Terminology](essential-pipe-terminology.md)
-   [The Pipe State](the-pipe-state.md)
-   [Defining Pipes in IDL Files](defining-pipes-in-idl-files.md)
-   [Client-Side Pipe Implementation](client-side-pipe-implementation.md)
-   [Server-Side Pipe Implementation](server-side-pipe-implementation.md)
-   [Rules for Multiple Pipes](rules-for-multiple-pipes.md)
-   [Combining Pipe and Nonpipe Parameters](combining-pipe-and-nonpipe-parameters.md)

For more information on pipe syntax and restrictions, see [pipe](/windows/desktop/Midl/pipe) in the MIDL Language Reference. The PIPES sample program in the Platform Software Development Kit (SDK) samples\\rpc directory demonstrates how to use **\[in,out\]** pipes to transfer data between a client and a server.

 

 
