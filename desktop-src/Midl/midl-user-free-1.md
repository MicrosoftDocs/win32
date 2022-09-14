---
title: midl_user_free attribute
description: The midl\_user\_free function is provided by client and server applications to deallocate dynamically allocated memory.
ms.assetid: b5d8f133-ddd9-4b92-8540-611a03835be0
keywords:
- midl_user_free attribute MIDL
topic_type:
- apiref
api_name:
- midl_user_free
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# midl\_user\_free attribute

The **midl\_user\_free** function is provided by client and server applications to deallocate dynamically allocated memory.

``` syntax
void __RPC_API midl_user_free(void __RPC_FAR * p);
```

## Parameters

<dl> <dt>

*p* 
</dt> <dd>

A pointer to the memory block to be freed.

</dd> </dl>

## Remarks

Both client application and server application must implement the **midl\_user\_free** function, unless you are compiling in OSF-compatibility ([**/osf**](-osf.md)) mode. The **midl\_user\_free** function must be able to free all storage allocated by [**midl\_user\_allocate**](/windows/desktop/Rpc/the-midl-user-allocate-function).

Applications and stubs call **midl\_user\_free** when dealing with objects referenced by pointers:

-   The server application should call **midl\_user\_free** to free memory allocated by the applicationâ€”for example, when deleting a specified node.
-   The server stub calls **midl\_user\_free** to release memory on the server after marshaling all **\[**[**out**](out-idl.md)**\]** arguments, **\[**[**in**](in.md), **out\]** arguments, and the return value.

## Examples


```C++
#include <windows.h>

void __RPC_API midl_user_free(void __RPC_FAR * p) 
{ 
    free(p); 
}
```



## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers)
</dt> <dt>

[Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**midl\_user\_allocate**](/windows/desktop/Rpc/the-midl-user-allocate-function)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 