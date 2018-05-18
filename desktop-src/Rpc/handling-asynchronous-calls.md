---
title: Handling Asynchronous Calls
description: The manager routine of an asynchronous function always receives the asynchronous handle as the first parameter. The server must keep track of this handle and use it to send the reply when the asynchronous remote procedure call finishes.
ms.assetid: '4f38b68b-0bea-4fa7-8c7e-dd09e7daf8bf'
---

# Handling Asynchronous Calls

The manager routine of an asynchronous function always receives the asynchronous handle as the first parameter. The server must keep track of this handle and use it to send the reply when the asynchronous remote procedure call finishes.

If the server needs to abort an asynchronous RPC, it calls [**RpcAsyncAbortCall**](rpcasyncabortcall.md). This function performs the same server-side cleanup as [**RpcAsyncCompleteCall**](rpcasynccompletecall.md) and propagates an exception code (provided by the server application) back to the client, except that it does not perform marshalling of the out arguments.

For an example of an asynchronous procedure, see [Sending the Asynchronous Reply](sending-the-asynchronous-reply.md).

 

 




