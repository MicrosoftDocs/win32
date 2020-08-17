---
title: Making the Asynchronous Call
description: Before it can make an asynchronous remote call, the client must initialize the asynchronous handle. Client and server programs use pointers to the RPC\_ASYNC\_STATE structure for asynchronous handles.
ms.assetid: b40308ef-88ae-4c80-9118-29c5ffee77ad
keywords:
- Remote Procedure Call RPC , tasks, making asynchronous calls
ms.topic: article
ms.date: 05/31/2018
---

# Making the Asynchronous Call

Before it can make an asynchronous remote call, the client must initialize the asynchronous handle. Client and server programs use pointers to the [**RPC\_ASYNC\_STATE**](/windows/desktop/api/Rpcasync/ns-rpcasync-rpc_async_state) structure for asynchronous handles.

Every outstanding call must have its own unique asynchronous handle. The client creates the handle and passes it to the [**RpcAsyncInitializeHandle**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncinitializehandle) function. For the call to complete correctly, the client must ensure that the memory for the handle is not released until it receives the server's asynchronous reply. Also, before making another call on an existing asynchronous handle, the client must reinitialize the handle. Failure to do this can cause the client stub to raise an exception during the call. The client must also ensure that the buffers it supplies for \[[**out**](/windows/desktop/Midl/out-idl)\] parameters and \[[**in**](/windows/desktop/Midl/in), **out**\] parameters to an asynchronous remote procedure remain allocated until it has received the reply from the server.

When it invokes an asynchronous remote procedure, the client must select the method that the RPC run-time library will use to notify it of the call's completion. The client can receive this notification in any one of the following ways:

-   Event. The client can specify an event to be fired when the call has completed. For details, see [Event Objects](/windows/desktop/Sync/event-objects).
-   Polling. The client can repeatedly call [**RpcAsyncGetCallStatus**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncgetcallstatus). If the return value is anything other than RPC\_S\_ASYNC\_CALL\_PENDING, the call is complete. This method uses more CPU time than the other methods described here.
-   APC. The client can specify an [asynchronous procedure call (APC)](/windows/desktop/Sync/asynchronous-procedure-calls) that gets called when the call completes. For the prototype of the APC function, see [**RPCNOTIFICATION\_ROUTINE**](/previous-versions/aa375808(v=vs.80)). The APC is called with its Event parameter set to RpcCallComplete. For APCs to get dispatched, the client thread must be in an alertable wait state.

    If the **hThread** field in the asynchronous handle is set to 0, the APCs are queued on the thread that made the asynchronous call. If it is nonzero, the APCs are queued on the thread specified by m.

-   IOC. The I/O completion port is notified with the parameters specified in the asynchronous handle. For more information, see [**CreateIoCompletionPort**](/windows/desktop/FileIO/createiocompletionport).
-   Windows handle. A message is posted to the specified window handle (HWND).

The following code fragment shows the essential steps required for initializing an asynchronous handle and using it to make an asynchronous remote procedure call.


```C++
RPC_ASYNC_STATE Async;
RPC_STATUS status;
 
// Initialize the handle.
status = RpcAsyncInitializeHandle(&Async, sizeof(RPC_ASYNC_STATE));
if (status)
{
    // Code to handle the error goes here.
}
 
Async.UserInfo = NULL;
Async.NotificationType = RpcNotificationTypeEvent;
 
Async.u.hEvent = CreateEvent(NULL, FALSE, FALSE, NULL);
if (Async.u.hEvent == 0)
{
    // Code to handle the error goes here.
}
// Call an asynchronous RPC routine here
RpcTryExcept
{
    printf("\nCalling the remote procedure 'AsyncFunc'\n");
    AsyncFunc(&Async, AsyncRPC_ClientIfHandle, nAsychDelay);
}
RpcExcept(1)
{
    ulCode = RpcExceptionCode();
    printf("AsyncFunc: Run time reported exception 0x%lx = %ld\n", 
            ulCode, ulCode);
}
RpcEndExcept
 
// Call a synchronous routine while
// the asynchronous procedure is still running
RpcTryExcept
{
    printf("\nCalling the remote procedure 'NonAsyncFunc'\n");
    NonAsyncFunc(AsyncRPC_ClientIfHandle, pszMessage);
    fprintf(stderr, 
            "While 'AsyncFunc' is running asynchronously,\n"
            "we still can send message to the server in the mean "
            "time.\n\n");
}
RpcExcept(1)
{
    ulCode = RpcExceptionCode();
    printf("NonAsyncFunc: Run time reported exception 0x%lx = %ld\n", 
            ulCode, ulCode);
}
RpcEndExcept
```



As this example demonstrates, your client program can execute synchronous remote procedure calls while an asynchronous procedure call is still pending. This client creates an event object for the RPC run-time library to use to notify it when the asynchronous call completes.

> [!Note]  
> Notification of completion will not be returned from an asynchronous RPC routine if an RPC exception is raised during an asynchronous call.

 

 

 