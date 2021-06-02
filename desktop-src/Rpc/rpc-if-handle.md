---
title: RPC_IF_HANDLE (Rpcdce.h)
description: The RPC\_IF\_HANDLE data type declares an interface handle.
ms.assetid: a85f3a44-7cdf-421f-a1e4-c67a9dd0c54d
keywords:
- RPC_IF_HANDLE
ms.topic: reference
ms.date: 05/31/2018
---

# RPC\_IF\_HANDLE

The **RPC\_IF\_HANDLE** data type declares an interface handle.


```C++
typedef void __RPC_FAR* RPC_IF_HANDLE;
```



## Remarks

The RPC run-time library uses interface handles to access the interface-specification data structure. The MIDL compiler automatically creates an interface-specification data structure from each IDL file and creates a global variable of type RPC\_IF\_HANDLE for the interface specification.

The MIDL compiler includes an interface handle in each header file generated for the interface. Functions requiring the interface specification as a parameter show a data type of **RPC\_IF\_HANDLE**. The form of each interface handle name is as follows:

-   *if-name*\_ClientIfHandle (for the client)
-   *if-name*\_ServerIfHandle (for the server)

The *if-name* part specifies the interface identifier in the IDL file.

For example:

hello\_ClientIfHandle

hello\_ServerIfHandle

> [!Note]  
> The maximum length of the interface handle name is 31 characters.

 

Because the "\_ClientIfHandle" and "\_ServerIfHandle" parts of the names require 15 characters, the *if-name* element can be no more than 16 characters long.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h (include Rpc.h)</dt> </dl> |



 

 





