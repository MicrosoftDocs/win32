---
title: Sending the Asynchronous Reply
description: When the asynchronous call is complete, the server sends a reply to the client by calling the RpcAsyncCompleteCall function and passing it the asynchronous handle.
ms.assetid: 458bc476-963e-4812-b4c2-9074ff0a8284
ms.topic: article
ms.date: 05/31/2018
---

# Sending the Asynchronous Reply

When the asynchronous call is complete, the server sends a reply to the client by calling the [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall) function and passing it the asynchronous handle. This call is necessary even if the asynchronous call has a void return value and no \[out\] parameters. If the function has a return value, it is passed by reference to **RpcAsyncCompleteCall**.

When the server calls [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall) or **RpcAsyncAbortCall**, or a call completes because an exception was raised in the server-manager routine, the RPC run-time library automatically destroys the server's asynchronous handle.

> [!Note]  
> The server must finish updating the \[in, out\] and \[out\] parameters before calling **RpcAsyncCompleteCall**. No changes can be made to those parameters or to the asynchronous handle after calling **RpcAsyncCompleteCall**. If the **RpcAsyncCompleteCall** function call fails, the RPC runtime frees the parameters.

 

The following example demonstrates a simple asynchronous procedure call.


```C++
#define DEFAULT_ASYNC_DELAY 20;
#define ASYNC_CANCEL_CHECK 100;

void AsyncFunc(IN PRPC_ASYNC_STATE pAsync,
               IN RPC_BINDING_HANDLE hBinding,
               IN OUT unsigned long nAsychDelay)
{
    int nReply = 1;
    RPC_STATUS status;
    unsigned long nTmpAsychDelay;
    int i;
 
    if (nAsychDelay < 0){
        nAsychDelay = DEFAULT_ASYNC_DELAY;
    }else if (nAsychDelay < 100){
        nAsychDelay = 100;
    }

    // We only call RpcServerTestCancel if the call
    // takes longer than ASYNC_CANCEL_CHECK ms
    if(nAsychDelay > ASYNC_CANCEL_CHECK){
        
        nTmpAsychDelay = nAsychDelay/100;
 
        for (i = 0; i < 100; i++){
            Sleep(nTmpAsychDelay);
 
            if (i%5 == 0){
                fprintf(stderr, 
                        "\rRunning AsyncFunc (%lu ms) (%d%c) ... ",
                        nAsychDelay, i+5, PERCENT);
 
                status = 
                    RpcServerTestCancel(
                        RpcAsyncGetCallHandle(pAsync));
                if (status == RPC_S_OK){
                    fprintf(stderr, 
                            "\nAsyncFunc has been canceled!!!\n");
                    break;
                }else if (status != RPC_S_CALL_IN_PROGRESS){
                    printf(
                        "RpcAsyncInitializeHandle returned 0x%x\n", 
                        status);
                    exit(status); 
                }
            }
        }
    }else{
        Sleep(nAsychDelay);
    }
 
    printf("\nCalling RpcAsyncCompleteCall\n");
    status = RpcAsyncCompleteCall(pAsync, &nReply);
    printf("RpcAsyncCompleteCall returned 0x%x\n", status);
    if (status){
        exit(status);
    }
}
```



For the sake of simplicity, this asynchronous server routine does not process actual data. It simply puts itself to sleep for awhile.

> [!Note]  
> The **RpcAsyncCompleteCall** function can be called either on the thread that received the call, or on any other thread in the process. If all the data necessary to complete the call are readily available, the server may fill them in on the same thread, and call the **RpcAsyncCompleteCall** on the same thread. This approach saves some context switching and improves performance. Such calls are called opportunistically asynchronous.

 

## Related topics

<dl> <dt>

[**RPC\_ASYNC\_STATE**](/windows/desktop/api/Rpcasync/ns-rpcasync-rpc_async_state)
</dt> <dt>

[**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall)
</dt> <dt>

[**RpcAsyncAbortCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall)
</dt> <dt>

[**RpcServerTestCancel**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcservertestcancel)
</dt> </dl>

 

 




