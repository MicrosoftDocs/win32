---
title: Waiting for the Asynchronous Reply
description: What the client does while it waits to be notified of a reply from the server depends on the notification mechanism it selects.
ms.assetid: b1d4ea54-26bc-49f9-8cc1-a74fd4ffced3
keywords:
- Remote Procedure Call RPC , tasks, waiting for asynchronous replies
ms.topic: article
ms.date: 05/31/2018
---

# Waiting for the Asynchronous Reply

What the client does while it waits to be notified of a reply from the server depends on the notification mechanism it selects.

If the client uses an event for notification, it will typically call the [**WaitForSingleObject**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject) function or the [**WaitForSingleObjectEx**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobjectex) function. The client enters a blocked state when it calls either of these functions. This is efficient because the client does not consume CPU run cycles while it is blocked.

When it uses polling to wait for its results, the client program enters a loop that repeatedly calls the function [**RpcAsyncGetCallStatus**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncgetcallstatus). This is an efficient method of waiting if your client program does other processing in the polling loop. For instance, it can prepare data in small chunks for a subsequent asynchronous remote procedure call. After each chunk is finished, your client can poll the outstanding asynchronous remote procedure call to see if it is complete.

Your client program can provide an asynchronous procedure call (APC), which is a type of callback function that the RPC run-time library will invoke when the asynchronous remote procedure call completes. Your client program must be in an alertable wait state. This typically means that the client calls a Windows API function to put itself in a blocked state. For more information, see [Asynchronous Procedure Calls](/windows/desktop/Sync/asynchronous-procedure-calls).

> [!Note]  
> Notification of completion will not be returned from an asynchronous RPC routine if an RPC exception is raised during a asynchronous call.

 

If your client program uses an I/O completion port to receive completion notification, it must call the [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function. When it does, it can either wait indefinitely for a response or continue to do other processing. If it does other processing while it waits for a reply, it must poll the completion port with the **GetQueuedCompletionStatus** function. In this case, it typically needs to set the *dwMilliseconds* to zero. This causes **GetQueuedCompletionStatus** to return immediately, even if the asynchronous call has not completed.

Client programs can also receive completion notification through their window message queues. In this situation, they simply process the completion message as they would any Windows message.

In a multithreaded application, an asynchronous call can be canceled by the client only after the thread that originated the call has returned successfully from the call. This ensures that the call is not canceled asynchronously by another thread after it failed a synchronous call. As standard practice, an asynchronous call that fails synchronously should not be canceled asynchronously. The client application must observe this behavior if calls may be issued and canceled on different threads. Also, after the call is canceled, the client code must wait for the completion notification and complete the call. The [**RpcAsyncCancelCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall) function simply rushes the completion notification; it is not a substitute for completing the call.

The following code fragment illustrates how a client program can use an event to wait for an asynchronous reply.


```C++
// This code fragment assumes that Async is a valid asynchronous
// RPC handle.
if (WaitForSingleObject(Async.u.hEvent, INFINITE) == WAIT_FAILED)
{
    RpcRaiseException(APP_ERROR);
}
```



Client programs that use an APC to receive notification of an asynchronous reply typically put themselves into a blocked state. The following code fragment shows this.


```C++
if (SleepEx(INFINITE, TRUE) != WAIT_IO_COMPLETION)
{
    RpcRaiseException(APP_ERROR);
}
```



In this case, the client program goes to sleep, consuming no CPU cycles, until the RPC run-time library calls the APC (not shown).

The next example demonstrates a client that uses an I/O completion port to wait for an asynchronous reply.


```C++
// This code fragment assumes that Async is a valid asynchronous
// RPC handle.
if (!GetQueuedCompletionStatus(
         Async.u.IOC.hIOPort,
         &Async.u.IOC.dwNumberOfBytesTransferred,
         &Async.u.IOC.dwCompletionKey,
         &Async.u.IOC.lpOverlapped,
         INFINITE))
{
    RpcRaiseException(APP_ERROR);
}
```



In the preceding example, the call to [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) waits indefinitely until the asynchronous remote procedure call completes.

One potential pitfall occurs when writing multithreaded applications. If a thread invokes a remote procedure call and then terminates before it receives notification that the send completed, the remote procedure call may fail and the client stub may close the connection to the server. Therefore, threads that call a remote procedure should not terminate before the call is completed or canceled when behavior is undesirable.

 

 