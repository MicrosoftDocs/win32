---
title: RpcSs Memory Management Package
description: The default allocator/deallocator pair used by the stubs and run time when allocating memory on behalf of the application is midl\_user\_allocate/midl\_user\_free.
ms.assetid: 9477e677-59cb-45d5-b485-ab0171ac17ba
ms.topic: article
ms.date: 05/31/2018
---

# RpcSs Memory Management Package

The default allocator/deallocator pair used by the stubs and run time when allocating memory on behalf of the application is **midl\_user\_allocate**/**midl\_user\_free**. However, you can choose the RpcSs package instead of the default by using the ACF attribute **\[enable\_allocate\]**. The RpcSs package consists of RPC functions that begin with the prefix **RpcSs** or **RpcSm**. The RpcSs package is not recommended for Windows applications.

> [!Note]  
> The Rpcss Memory Management Package is obsolete. It is recommended that [**midl\_user\_allocate**](/windows/desktop/Midl/midl-user-allocate-1) and [**midl\_user\_free**](/windows/desktop/Midl/midl-user-free-1) are used in its place.

 

In **/osf** mode, the RpcSs package is enabled for MIDL-generated stubs automatically when full pointers are used, when the arguments require memory allocation, or as a result of using the **\[enable\_allocate\]** attribute. In the default (Microsoft extended) mode, the RpcSs package is enabled only when the **\[enable\_allocate\]** attribute is used. The **\[enable\_allocate\]** attribute enables the RpcSs environment by the server-side stubs. The client side becomes alerted to the possibility that the RpcSs package may be enabled. In **/osf** mode, the client side is not affected.

When the RpcSs package is enabled, allocation of memory on the server side is accomplished with the private RpcSs memory management allocator and deallocator pair. You can allocate memory using the same mechanism by calling [**RpcSmAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmallocate) (or [**RpcSsAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcssallocate)). Upon return from the server stub, all the memory allocated by the RpcSs package is automatically freed. The following example shows how to enable the RpcSs package:

``` syntax
/* ACF file fragment */

[ 
    implicit_handle(handle_t GlobalHandle),
    enable_allocate
]
interface iface
{
}

/*Server management routine fragment. Replaces p=midl_user_allocate(size); */

    p=RpcSsAllocate(size);                /*raises exception */
    p=RpcSmAllocate(size, &status);       /*returns error code */
```

Your application can explicitly free memory by invoking the [**RpcSsFree**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcssfree) or [**RpcSmFree**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmfree) function. Note that these functions do not actually free memory. They mark it for deletion. The RPC library releases the memory when your program calls [**RpcSsDisableAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcssdisableallocate) or [**RpcSsDisableAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcssdisableallocate).

You can also enable the memory management environment for your application by calling the [**RpcSmEnableAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmenableallocate) routine (and you can disable it by calling the [**RpcSmDisableAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmdisableallocate) routine). Once enabled, application code can allocate and deallocate memory by calling functions from the RpcSs package.

 

 