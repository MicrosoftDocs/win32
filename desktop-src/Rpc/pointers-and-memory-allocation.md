---
title: Pointers and Memory Allocation
description: The ability to change memory through pointers often requires that the server and the client allocate enough memory for the elements in the array.
ms.assetid: 8a49582a-9ae4-4f26-a172-bc8fe2aab65a
ms.topic: article
ms.date: 05/31/2018
---

# Pointers and Memory Allocation

The ability to change memory through pointers often requires that the server and the client allocate enough memory for the elements in the array.

When a stub must allocate or free memory, it calls run-time library functions that in turn call the functions [**midl\_user\_allocate**](/windows/desktop/Midl/midl-user-allocate-1) and [**midl\_user\_free**](/windows/desktop/Midl/midl-user-free-1). These functions are not included as part of the run-time library. You need to write your own versions of these functions and link them with your application. In this way, you can decide how to manage memory. When compiling your IDL file in OSF-compatibility (**/osf**) mode, you do not need to implement these functions. You must write these functions to the following prototypes:

``` syntax
void __RPC_FAR * __RPC_API midl_user_allocate(size_t len)

void __RPC_API midl_user_free(void __RPC_FAR * ptr)
```

For example, the versions of these functions for an application can simply call standard library functions:


```C++
void __RPC_FAR * __RPC_API midl_user_allocate(size_t len)
{
    return(malloc(len));
}

void __RPC_API midl_user_free(void __RPC_FAR * ptr)
{
    free(ptr);
}
```



 

 