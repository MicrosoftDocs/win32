---
title: The midl_user_free Function
description: The midl\_user\_free function must be supplied by RPC developers.
ms.assetid: 5e940e93-bdd4-48cc-b84e-654637699719
ms.topic: article
ms.date: 05/31/2018
---

# The midl\_user\_free Function

The **midl\_user\_free** function must be supplied by RPC developers. It allocates memory for the RPC stubs and library routines. Your **midl\_user\_free** function must match the following prototype:

``` syntax
void __RPC_USER midl_user_free(void * pBuffer);
```

The *pBuffer* parameter specifies a pointer to the memory that is to be freed. Both client application and server application must implement the **midl\_user\_free** function unless you are compiling in OSF-compatibility ([**/osf**](/windows/desktop/Midl/-osf)) mode. The **midl\_user\_free** function must be able to free all storage allocated by [**midl\_user\_allocate**](the-midl-user-allocate-function.md).

Applications and stubs call **midl\_user\_free** when dealing with allocated objects:

-   The server application should call **midl\_user\_free** to free memory allocated by the application, such as when deleting a dynamically allocated node of data.
-   The server stub calls **midl\_user\_free** to release memory on the server after marshaling all \[out\] arguments, \[in\],\[out\] arguments, and the function return value.

For example, the RPC Windows sample program that displays "Hello, world" implements **midl\_user\_free** in terms of the C function free:


```C++
void __RPC_USER midl_user_free(void __RPC_FAR * p)
{
    free(p);
}
```



> [!Note]  
> If the RpcSs package is enabled (for example, as the result of using the \[ [**enable\_allocate**](/windows/desktop/Midl/enable-allocate)\] attribute), your server program should use [**RpcSmFree**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmfree) to free memory. For more information, see [RpcSs Memory Management Package](rpcss-memory-management-package.md).

 

 

 