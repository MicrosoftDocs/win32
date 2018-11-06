---
title: Generating Error Information
description: If a server or application encounters a fatal error while being called through RPC, it should indicate to the RPC run time that it has encountered a failure, and ideally, should add information about the failure to facilitate troubleshooting.
ms.assetid: 6658c387-94df-4d85-9749-53858f9e0f5f
ms.topic: article
ms.date: 05/31/2018
---

# Generating Error Information

If a server or application encounters a fatal error while being called through RPC, it should indicate to the RPC run time that it has encountered a failure, and ideally, should add information about the failure to facilitate troubleshooting.

## Indicating Fatal Errors to the RPC Run Time

To indicate a failure to the RPC run time, call the [**RpcRaiseException**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcraiseexception) function while on the RPC thread the exception was called on, or [**RpcAsyncAbortCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall) if processing the call asynchronously on another thread. Returning an error code from the server routine, such as the manager routine, is not sufficient—according to the RPC specification, the return value of the function has no error semantics on the server, regardless of the idl/acf file settings.

When a fatal error occurs in your component, perform any cleanup deemed necessary and then call the [**RpcRaiseException**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcraiseexception) function with the error code. The only difference between **RpcRaiseException** and returning an error code is when the **RpcRaiseException** is called, the out parameters are not marshaled. This is usually an advantage, since avoiding uninitialized out parameters becomes unnecessary.

## Generating Additional Extended Error Information

Just as the RPC run time builds a chain of error records, your server or application can add its own records to the chain. This approach often helps in the troubleshooting process. For example, a server may attempt to open a given file and receive a file not found error. Simply returning error 2 would not be helpful in determining which file is missing.

Instead, your server could call the [**RpcErrorAddRecord**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcerroraddrecord) function and provide a string parameter, either ANSI or Unicode, in the error record indicating the full path of the file it was looking for. When all this information appears on the user screen on a remote computer, troubleshooting becomes trivial; a simple check of whether the file exists can be done, especially since the name of the computer in question is already provided by the RPC run time.

The [**RpcErrorAddRecord**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcerroraddrecord) function call may fail if enough memory is not available, even though it requires only a few bytes of heap space. Also, records added by **RpcErrorAddRecord** accumulate in a given thread. The runtime normally cleans those records up before it calls your server routine, but if extended error information is used outside RPC, take care of cleaning up the accumulated extended error in the thread by calling [**RpcErrorClearInformation**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcerrorclearinformation).

 

 




