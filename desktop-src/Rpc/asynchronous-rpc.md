---
title: Asynchronous RPC
description: Asynchronous Remote Procedure Call (RPC) is a Microsoft extension that addresses several limitations of the traditional RPC model as defined by the Open Software Foundation \ 8211;Distributed Computing Environment (OSF-DCE).
ms.assetid: '2586c10e-8284-419f-a200-4f6b11953688'
keywords:
- Remote Procedure Call RPC , described, asynchronous RPC
- asynchronous RPC
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous RPC

Asynchronous Remote Procedure Call (RPC) is a Microsoft extension that addresses several limitations of the traditional RPC model as defined by the Open Software Foundation–Distributed Computing Environment (OSF-DCE). Asynchronous RPC separates a remote procedure call from its return value, which resolves the following limitations of traditional, synchronous RPC:

-   **Multiple outstanding calls from a single-threaded client.** In the traditional RPC model, a client is blocked in a remote procedure call until the call returns. This prevents a client from having multiple outstanding calls, while still having its thread available to do other work.
-   **Slow or delayed clients.** A client that is slow to produce data may want to make a remote procedure call with initial data and then supply additional data as it is produced. This is not possible with conventional (synchronous) RPC.
-   **Slow or delayed servers.** A remote procedure call that takes a long time to complete will tie up the dispatch thread for the duration of the task. With asynchronous RPC, the server can start a separate (asynchronous) operation to process the request and send back the reply when it is available. The server can also send the reply incrementally as results become available without having to tie up a dispatch thread for the duration of the remote call. By making the client application asynchronous, you can prevent a slow server from unnecessarily tying up a client application.
-   **Transfer of large amounts of data.** Transferring large amounts of data between the client and server, especially over slow links, ties up both the client thread and the server manager thread for the duration of the transfer. With asynchronous RPC and pipes, data transfer can take place incrementally, and without blocking the client or server from performing other tasks.

You take advantage of asynchronous RPC mechanisms by declaring functions with the \[[**async**](/windows/desktop/Midl/async)\] attribute. Because you make this declaration in an attribute configuration file (ACF), you do not have to make any changes to the Interface Definition Language (IDL) file; asynchronous RPC has no effect on the wire protocol (how the data is transmitted between client and server). This means that both synchronous and asynchronous clients can communicate with an asynchronous server application.

This section presents an overview of how to develop distributed applications using asynchronous RPC. The overview is presented in the following sections:

-   [Declaring Asynchronous Functions](declaring-asynchronous-functions.md)
-   [Client-side Asynchronous RPC](client-side-asynchronous-rpc.md)
-   [Server-side Asynchronous RPC](server-side-asynchronous-rpc.md)
-   [Causal Ordering of Asynchronous Calls](causal-ordering-of-asynchronous-calls.md)
-   [Error Handling](error-handling.md)
-   [Asynchronous RPC Over the Named Pipe Protocol](asynchronous-rpc-over-the-named-pipe-protocol.md)
-   [Using Asynchronous RPC with DCE Pipes](using-asynchronous-rpc-with-dce-pipes.md)
-   [Asynchronous DCOM](asynchronous-dcom.md)

 

 