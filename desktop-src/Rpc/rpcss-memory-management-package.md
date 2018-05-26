---
title: RpcSs Memory Management Package
description: The default allocator/deallocator pair used by the stubs and run time when allocating memory on behalf of the application is midl\_user\_allocate/midl\_user\_free.
ms.assetid: 9477e677-59cb-45d5-b485-ab0171ac17ba
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RpcSs Memory Management Package

The default allocator/deallocator pair used by the stubs and run time when allocating memory on behalf of the application is **midl\_user\_allocate**/**midl\_user\_free**. However, you can choose the RpcSs package instead of the default by using the ACF attribute **\[enable\_allocate\]**. The RpcSs package consists of RPC functions that begin with the prefix **RpcSs** or **RpcSm**. The RpcSs package is not recommended for Windows applications.

> [!Note]  
> The Rpcss Memory Management Package is obsolete. It is recommended that [**midl\_user\_allocate**](https://msdn.microsoft.com/library/windows/desktop/aa367095) and [**midl\_user\_free**](https://msdn.microsoft.com/library/windows/desktop/aa367096) are used in its place.

 

In **/osf** mode, the RpcSs package is enabled for MIDL-generated stubs automatically when full pointers are used, when the arguments require memory allocation, or as a result of using the **\[enable\_allocate\]** attribute. In the default (Microsoft extended) mode, the RpcSs package is enabled only when the **\[enable\_allocate\]** attribute is used. The **\[enable\_allocate\]** attribute enables the RpcSs environment by the server-side stubs. The client side becomes alerted to the possibility that the RpcSs package may be enabled. In **/osf** mode, the client side is not affected.

When the RpcSs package is enabled, allocation of memory on the server side is accomplished with the private RpcSs memory management allocator and deallocator pair. You can allocate memory using the same mechanism by calling [**RpcSmAllocate**](/windows/win32/Rpcndr/nf-rpcndr-rpcsmallocate?branch=master) (or [**RpcSsAllocate**](/windows/win32/Rpcndr/nf-rpcndr-rpcssallocate?branch=master)). Upon return from the server stub, all the memory allocated by the RpcSs package is automatically freed. The following example shows how to enable the RpcSs package:

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

Your application can explicitly free memory by invoking the [**RpcSsFree**](/windows/win32/Rpcndr/nf-rpcndr-rpcssfree?branch=master) or [**RpcSmFree**](/windows/win32/Rpcndr/nf-rpcndr-rpcsmfree?branch=master) function. Note that these functions do not actually free memory. They mark it for deletion. The RPC library releases the memory when your program calls [**RpcSsDisableAllocate**](/windows/win32/Rpcndr/nf-rpcndr-rpcssdisableallocate?branch=master) or [**RpcSsDisableAllocate**](/windows/win32/Rpcndr/nf-rpcndr-rpcssdisableallocate?branch=master).

You can also enable the memory management environment for your application by calling the [**RpcSmEnableAllocate**](/windows/win32/Rpcndr/nf-rpcndr-rpcsmenableallocate?branch=master) routine (and you can disable it by calling the [**RpcSmDisableAllocate**](/windows/win32/Rpcndr/nf-rpcndr-rpcsmdisableallocate?branch=master) routine). Once enabled, application code can allocate and deallocate memory by calling functions from the RpcSs package.

 

 




