---
title: byte_count attribute
description: The \ byte\_count\ ACF attribute is a parameter attribute that associates a size, in bytes, with the memory area indicated by the pointer.
ms.assetid: 7e146888-fe7c-461c-8615-70da1e3b12cd
keywords:
- byte_count attribute MIDL
topic_type:
- apiref
api_name:
- byte_count
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# byte\_count attribute

The **\[byte\_count\]** ACF attribute is a parameter attribute that associates a size, in bytes, with the memory area indicated by the pointer.

``` syntax
[ function-attribute-list ] function-name(
    [byte_count(length-variable-name)] parameter-name);
    ...);
```

## Parameters

<dl> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more ACF function attributes.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function defined in the IDL file. The function name is required.

</dd> <dt>

*length-variable-name* 
</dt> <dd>

Specifies the name of the [**\[in\]**](in.md)-only parameter that specifies the size, in bytes, of the memory area referenced by *parameter-name*.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies the name of the [**\[out\]**](out-idl.md)-only pointer parameter defined in the IDL file.

</dd> </dl>

## Remarks

The ACF attribute **\[byte\_count\]** represents a Microsoft extension to DCE IDL. Therefore, this attribute is not available when you use the MIDL compiler switch [**/osf**](-osf.md).

> [!Note]  
> The **\[byte count\]** attribute is no longer supported in NDR64 syntax due to the difficulty in estimating the size required for all [**\[out\]**](out-idl.md) parameters.

 

Memory referenced by the pointer parameter is contiguous and is not allocated or freed by the client stubs. This feature of the **\[byte\_count\]** attribute lets you create a persistent buffer area in client memory that can be reused during more than one call to the remote procedure.

The ability to turn off the client stub memory allocation lets you tune the application for efficiency. For example, the **\[byte\_count\]** attribute can be used by service-provider functions that use Microsoft RPC. When a user application calls the service-provider API and sends a pointer to a buffer, the service provider can pass the buffer pointer on to the remote function. The service provider can reuse the buffer during multiple remote calls without forcing the user to reallocate the memory area.

The memory area can contain complex data structures that consist of multiple pointers. Because the memory area is contiguous, the application does not have to make several calls to individually free each pointer and structure. Instead, it can allocate or free the memory area with one call to the memory allocation or free routine.

The buffer must be an [**\[out\]**](out-idl.md)-only parameter, while the buffer length in bytes must be an [**\[in\]**](in.md)-only parameter.

Specify a buffer that is large enough to contain all the [**\[out\]**](out-idl.md) parameters. Because of hidden padding, use overestimates rather than exact counts. For example, 4-byte pointers are unmarshaled on a 4-byte aligned boundary on 32-bit platforms and 8-byte pointers on an 8-byte boundary on 64-bit platforms. Therefore, the alignment padding the stubs will perform must be accounted for in the space for the buffer. In addition, packing levels used during C-language compilation can vary. Use a byte count value that accounts for additional packing bytes added for the packing level used during C-language compilation. A safe practice that covers both 32 bit platforms and 64 bit platforms is to assume that each object going into the big memory block starts at an address that is a multiple of 8.

## Examples

``` syntax
/* IDL file */ 
HRESULT proc1([in] unsigned long length, 
              [out] struct my_struct * pMyStruct); 
 
/* ACF file */ 
proc1([byte_count(length)] pMyStruct);
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> </dl>

 

 




