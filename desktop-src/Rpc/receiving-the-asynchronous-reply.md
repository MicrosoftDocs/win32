---
title: Receiving the Asynchronous Reply
description: After it is notified that the server has sent a reply, the client calls RpcAsyncCompleteCall with the asynchronous handle so that it can receive the reply.
ms.assetid: 48fb3777-d90a-474b-a1fa-9d034b5791e5
ms.topic: article
ms.date: 05/31/2018
---

# Receiving the Asynchronous Reply

After it is notified that the server has sent a reply, the client calls [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall) with the asynchronous handle so that it can receive the reply. When **RpcAsyncCompleteCall** has completed successfully, the *Reply* parameter points to a buffer that contains the return value of the remote function. Any buffers supplied by the client program as \[[**out**](/windows/desktop/Midl/out-idl)\] or \[[**in**](/windows/desktop/Midl/in), **out**\] parameters to the asynchronous remote function contain valid data. If the client calls **RpcAsyncCompleteCall** before the server has sent the reply, that call will fail and return a value of RPC\_S\_ASYNC\_CALL\_PENDING.

If your client program uses I/O completion ports or events for notification, it must call [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) to release the port or handle when it no longer needs them.

 

 