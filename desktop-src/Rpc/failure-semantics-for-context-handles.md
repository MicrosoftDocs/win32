---
title: Failure Semantics for Context Handles
description: This topic discusses failure semantics for context handles.
ms.assetid: fcf28519-39ad-4823-bc27-f3502e4d540c
ms.topic: article
ms.date: 05/31/2018
---

# Failure Semantics for Context Handles

This topic discusses failure semantics for context handles.

## Failure Semantics when Closing the Context Handle Fails

Imagine a client application is attempting to close a context handle it opened on the server, without shutting down the client process. Also, assume the call to the server to close the context handle fails (for example, the client is out of memory). The proper way to handle this situation is to call the [**RpcSsDestroyClientContext**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcssdestroyclientcontext) function. In such a case the client cleans up its side of the context handle, and abortively closes the connection to the server. Since the connection is really a connection pool (see [RPC and the Network](rpc-and-the-network.md)), which is reference-counted with one reference for each opened binding or context handle, destroying the context handle by calling the **RpcSsDestroyClientContext** function does not actually destroy the connection. Rather, it decrements the reference count for the connection pool. For connections in the pool to be closed, the client needs to close all binding handles and context handles to that server from the client process. Then all connections in the pool are closed, and the server run-down mechanism is initiated and cleans up.

## Failure Semantics During Change of State of the Context Handle

The information in this section refers to Windows XP and later platforms.

Context handles are simply parameters to a function. All changes in the state of a context handle happen when parameters are marshaled or unmarshaled. For example, if a client opens a context handle (changes it from **NULL** to non-**NULL**), the RPC run-time does not actually open the RPC portion of the handle until the arguments are marshaled for sending to the client. Failures can occur during the interim. Due to a variety of possible network or low resource conditions, transmission of the packet to the client could fail. Or the server routine may throw an exception while attempting to change a context handle. In these or other failure situations, the client and server may get inconsistent views of the context handle. This section explains the rule for the state of the context handle, and the responsibility of client and server code during various failure conditions.

-   A **NULL** context handle arrives, but the server routine encounters a failure and throws an exception.

    It is the responsibility of the server routine to clean up any context handle–related state it may have created. The RPC run time cleans up its state.

-   A non-**NULL** context handles arrives, but the server routine encounters a failure and throws an exception.

    If the server routine closed the context handle, the client will not know about it, since the call will not succeed; further use of the context handle will result in an RPC\_X\_SS\_CONTEXT\_MISMATCH error on the client. If the server routine does not modify the context handle, the client can still use it. If the server routine changes the information stored in the server context, new calls from the client will use that information.

-   A non-**NULL** context handle arrives, and the server routine closes the handle, but either marshaling after the context handle was marshaled failed, or processing after marshaling failed.

    The context handle is closed, and further calls by this client using this context handle result in an RPC\_X\_SS\_CONTEXT\_MISMATCH error on the client.

-   A **NULL** context handle arrives, and the server creates its context for this handle, but either marshaling after the context handle was marshaled failed, or processing after marshaling failed.

    In this case, the RPC run time invokes the run down for this context handle, and cleans up the RPC state for this context handle. The context handle will not be created on the client side.

-   A non-**NULL** context handle arrives, and the server either does not change the context handle, or it changes the information stored in the server context, and marshaling fails after the context handle is marshaled.

    New calls from the client will use the context handle that the server has.

-   A **NULL** context handle arrives, and the server does not set it to anything other than **NULL**, but the call fails before the context handle is marshaled.

    In this case, no context handle is created on the client.

-   A non-**NULL** context handle arrives, and the server sets it to **NULL**, but marshaling fails before the context handle is marshaled.

    In this case, the context handle remains closed on the server, and the client gets RPC\_X\_SS\_CONTEXT\_MISMATCH errors when it tries to use the context handle.

-   A **NULL** context handle arrives on the server, and the server sets it to non-**NULL**, but marshaling fails before the context handle is marshaled.

    The context handle run down is to be invoked so that the server can clean up, and no context handle will be created on the client.

-   A non-**NULL** context handle arrives, and the server either does not change the context handle, or it changes the information stored in the server context, and marshaling fails before the context handle is marshaled.

    New calls from the client will use the state on the server.

-   A context handle is declared as a return value, and the server routine returns **NULL** for the context handle and marshaling fails before the context handle is marshaled.

    In this case, no new context is created on the client.

-   A context handle is declared as a return value, and the server routine returns non-**NULL** for the context handle and marshaling fails before the context handle is marshaled.

    The RPC run time calls the context handle run-down routine to give it a chance to clean up, and no new context is created on the client.

 

 




