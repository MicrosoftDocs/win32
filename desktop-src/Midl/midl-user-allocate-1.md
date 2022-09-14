---
title: midl_user_allocate attribute
description: The midl\_user\_allocate function is a function that client and server applications provide to allocate memory.
ms.assetid: 0eaf6df5-791d-4f6d-8f49-cc1ce64e7ab4
keywords:
- midl_user_allocate attribute MIDL
topic_type:
- apiref
api_name:
- midl_user_allocate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# midl\_user\_allocate attribute

The **midl\_user\_allocate** function is a function that client and server applications provide to allocate memory.

``` syntax
void __RPC_FAR * __RPC_API midl_user_allocate (size_t cBytes);
```

## Parameters

<dl> <dt>

*cBytes* 
</dt> <dd>

Specifies the count of bytes to allocate.

</dd> </dl>

## Remarks

Both client applications and server applications must implement the **midl\_user\_allocate** function, unless you are compiling in OSF-compatibility ([**/osf**](-osf.md)) mode. Applications and generated stubs call **midl\_user\_allocate** when dealing with objects referenced by pointers:

-   The server application should call **midl\_user\_allocate** to allocate memory for the applicationâ€”for example, when creating a new node.
-   The server stub calls **midl\_user\_allocate** when unmarshaling pointed-at data into the server address space.
-   The client stub calls **midl\_user\_allocate** when unmarshaling data from the server that is referenced by an [**out**](out-idl.md) pointer. Note that for **\[**[**in**](in.md)**\]**, **\[out\]**, and **\[**[**unique**](unique.md)**\]** pointers, the client stub calls **midl\_user\_allocate** only if the **\[unique\]** pointer value was **NULL** on input and changes to a non-**NULL** value during the call. If the **\[unique\]** pointer was non-**NULL** on input, the client stub writes the associated data into existing memory.

If **midl\_user\_allocate** fails to allocate memory, it must return a **NULL** pointer.

It is recommended that **midl\_user\_allocate** return a pointer that is 8 bytes aligned.

## Examples


```C++
#include <windows.h>

void __RPC_FAR * __RPC_API midl_user_allocate(size_t cBytes) 
{ 
    return(malloc(cBytes)); 
}
```



## See also

<dl> <dt>

[**allocate**](allocate.md)
</dt> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers)
</dt> <dt>

[Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**midl\_user\_free**](/windows/desktop/Rpc/the-midl-user-free-function)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 