---
title: Error Handling (RPC)
description: In synchronous RPC, a client makes a remote call that returns with either a success or failure code.
ms.assetid: 7dfc9f84-ce3c-49f3-8f72-b212095133fd
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling (RPC)

In synchronous RPC, a client makes a remote call that returns with either a success or failure code. Asynchronous RPC provides more opportunities for a call to fail, and these failures are handled differently, depending on where and when they occur. The following table describes the ways in which a call can fail, and how it is handled.

## Client-side Cleanup



| Failure symptom                                                                                                                                  | Cleanup                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Client catches an exception when it calls the remote procedure.                                                                                  | No RPC API calls are necessary. All RPC state has been cleaned up.                                                              |
| Client receives a call complete notification, but when it calls [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall), it receives an error code. | No RPC API calls are necessary. All RPC state has been cleaned up.                                                              |
| Client issues non-abortive or abortive cancel.                                                                                                   | Client must wait for notification, and call [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall) when the notification arrives. |



 

In server side cleanup, a key concept is the hand-off point. During the server side processing of an asynchronous call, some processing is usually performed on the thread that received the call (also known as the *dispatcher thread*), and then, optionally, the dispatcher thread puts enough state into a memory block and signals another thread (also known as *worker thread*) to continue processing for the call. The moment at which the dispatcher thread successfully signals that the worker thread is called the *hand-off point*.

## Server Side Cleanup



| Error encountered      | Cleanup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Before hand-off point. | Throw exception. No call to [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall) is necessary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| After hand-off point.  | Call [**RpcAsyncAbortCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall) or, if the error is not fatal and results can still be returned to the client, [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall). If the **RpcAsyncCompleteCall** function call fails, the RPC runtime frees the parameters. The user must not access those parameters. The dispatcher thread must not perform any substantial processing that may fail after the hand off point, because it no longer can safely abort the call. Specifically, it must not throw an exception after the hand off point, or the server may crash. |



 

## Special Error Handling Cases for Pipes

There are special cases for error handling when using pipes. The following list explains the source of the failure, and how to handle the error.



| Source of failure                                                                                                 | How handled                                                                                                |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Client calls push and the call fails.                                                                             | No RPC API calls are necessary. All RPC state has been cleaned up.                                         |
| Client calls [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall) before the [**in**](/windows/desktop/Midl/in) pipes are drained. | Call fails with the appropriate pipe-filling error code.                                                   |
| Client calls pull and the call fails.                                                                             | No RPC API calls are necessary. All RPC state has been cleaned up.                                         |
| Either client or server calls push or pull in the wrong order.                                                    | Run-time returns pipe-filling error status.                                                                |
| Server calls push or pull and the call fails.                                                                     | Push returns a failure code. No call to [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall) is necessary. |
| Server calls **RpcAsyncCompleteCall** before the pipes have been drained.                                         | The pipe call returns a pipe filling error status.                                                         |
| After the dispatch, a receive operation fails.                                                                    | The next time the server calls pull to receive pipe data, an error is returned.                            |



 

 

 
