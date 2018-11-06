---
title: Top-Level and Embedded Pointers
description: To understand how pointers and their associated data elements are allocated in Microsoft RPC, you have to differentiate between top-level pointers and embedded pointers.
ms.assetid: 217b9200-827c-4d36-9412-5e65858b8a97
ms.topic: article
ms.date: 05/31/2018
---

# Top-Level and Embedded Pointers

To understand how pointers and their associated data elements are allocated in Microsoft RPC, you have to differentiate between *top-level pointers* and *embedded pointers*. It is also useful to refer to the set of all pointers that are not top-level pointers.

*Top-level pointers* are those that are specified as the names of parameters in function prototypes. Top-level pointers and their referents are always allocated on the server.

*Embedded pointers* are pointers that are embedded in data structures such as arrays, structures, and unions. When embedded pointers only write output to a buffer and are null on input, the server application can change their values to non-null. In this case, the client stubs allocate new memory for this data.

If the embedded pointer is not null on the client before the call, the stubs do not allocate memory on the client on return. Instead, the stubs attempt to write the memory associated with the embedded pointer into the existing memory on the client associated with that pointer, overwriting the data already there.

> [!Note]  
> For data read from or writen to a buffer, and which does not specify the buffer size, output length must be less than or equal to input length. An RPC exception is raised when overflow is detected. For string data, output length is determined by checking length of the input string. Therefore, output strings cannot exceed length of input strings. Best practice guidance is to avoid this by always including a size-specified parameter to indicate size of the buffer.

 

Embedded write-only pointers are discussed in [Combining Pointer and Directional Attributes](combining-pointer-and-directional-attributes.md).

The term *nontop-level pointers* refers to all pointers that are not specified as parameter names in the function prototype, including both embedded pointers and multiple levels of nested pointers.

 

 




