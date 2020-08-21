---
title: The midl_user_allocate Function
description: The midl\_user\_allocate function is a procedure that must be supplied by developers of RPC applications.
ms.assetid: 3def405c-da05-4cce-9dc4-499864a0de6e
ms.topic: article
ms.date: 05/31/2018
---

# The midl\_user\_allocate Function

The **midl\_user\_allocate** function is a procedure that must be supplied by developers of RPC applications. It allocates memory for the RPC stubs and library routines. Your **midl\_user\_allocate** function must match the following prototype:

``` syntax
void __RPC_FAR * __RPC_USER midl_user_allocate (size_t cBytes);
```

The *cBytes* parameter specifies the number of bytes to allocate. Both client applications and server applications must implement the **midl\_user\_allocate** function unless you are compiling in OSF-compatibility (/osf) mode. Applications and generated stubs call **midl\_user\_allocate** directly or indirectly to manage allocated objects. For example:

-   The client and server applications call **midl\_user\_allocate** to allocate memory for the application, such as when creating a new node in a tree or linked list.
-   The server stub calls **midl\_user\_allocate** when unmarshaling data into the server address space.
-   The client stub calls **midl\_user\_allocate** when unmarshaling data from the server that is referenced by an \[out\] pointer. Note that for \[in\], \[out\], and \[unique\] pointers, the client stub calls **midl\_user\_allocate** only if the \[unique\] pointer value was null on input and changes to a non-null value during the call. If the \[unique\] pointer was non-null on input, the client stub writes the associated data into existing memory.

If **midl\_user\_allocate** fails to allocate memory, it should return a null pointer.

The **midl\_user\_allocate** function should return an 8-byte aligned pointer.

For example, the sample programs provided with the Platform Software Development Kit (SDK) implement **midl\_user\_allocate** in terms of the C function [**malloc**](pointers-and-memory-allocation.md):


```C++
void __RPC_FAR * __RPC_USER midl_user_allocate(size_t cBytes)
{
    return((void __RPC_FAR *) malloc(cBytes));
}
```



> [!Note]  
> If the RpcSs package is enabled (for example, as the result of using the \[ [**enable\_allocate**](/windows/desktop/Midl/enable-allocate)\] attribute), use [**RpcSmAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmallocate) to allocate memory on the server side. For additional information on \[**enable\_allocate**\], see [MIDL Reference](/windows/desktop/Midl/midl-language-reference).

 

 

 