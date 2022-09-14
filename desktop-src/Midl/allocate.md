---
title: allocate attribute
description: The \ allocate\ ACF attribute lets you customize memory allocation and deallocation for a type defined in the IDL file.
ms.assetid: 1956b11f-bafa-41c3-9025-5fcbb890d1a2
keywords:
- allocate attribute MIDL
topic_type:
- apiref
api_name:
- allocate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# allocate attribute

The **\[allocate\]** ACF attribute lets you customize memory allocation and deallocation for a type defined in the IDL file.

``` syntax
typedef [allocate (allocate-option-list) [, type-attribute-list] ] type-name;
```

## Parameters

<dl> <dt>

*allocate-option-list* 
</dt> <dd>

Specifies one or more memory-allocation options. Select one of either **single\_node** or **all\_nodes**, or one of either **free** or **dont\_free**, or one from each pair. When you specify more than one option, separate the options with commas.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies other optional ACF-type attributes. When you specify more than one type attribute, separate the options with commas.

</dd> <dt>

*type-name* 
</dt> <dd>

Specifies a type defined in the IDL file.

</dd> </dl>

## Remarks

The **\[allocate\]** attribute has the following valid options.



| Option           | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| **all\_nodes**   | Makes one call to allocate and free memory for all nodes.             |
| **single\_node** | Makes many individual calls to allocate and free each node of memory. |
| **free**         | Frees memory on return from the server stub.                          |
| **dont\_free**   | Does not free memory on return from the server stub.                  |



 

By default, the stubs may allocate storage for data referenced by a unique or full pointer by calling [**midl\_user\_allocate**](midl-user-allocate-1.md) and [**midl\_user\_free**](midl-user-free-1.md) individually for each pointer.

You can optimize the speed of your application by specifying the option **all\_nodes**. This option directs the stub to compute the size of all memory referenced through the pointer of the specified type and to make a single call to [**midl\_user\_allocate**](midl-user-allocate-1.md). The stub releases the memory by making one call to [**midl\_user\_free**](midl-user-free-1.md).

The **dont\_free** option directs the MIDL compiler to generate a server stub that does not call [**midl\_user\_free**](midl-user-free-1.md) for the specified type. The **dont\_free** option allows the pointer structures to remain accessible to the server application after the remote procedure call has completed and returned to the client.

The **\[allocate\]** attribute will cause any **\[in, out\]** parameter that is a pointer to a type qualified with the **all\_nodes** option to reallocate memory when the data is unmarshaled. It is the responsibility of the application to free the memory allocated previously for this parameter. For example:

``` syntax
typedef struct thistype 
{ 
    [string] char * PTHISTYPE;  
} * PTHISTYPE
HRESULT proc1 ( [in,out] PTHISTYPE * ppthistype);
```

The data type PTHISTYPE will be reallocated in the [**\[out\]**](out-idl.md) direction by the stub before unmarshaling. Therefore, the application must free the memory it previously allocated for this parameter's data, or a memory leak will occur.

## Examples

``` syntax
/* ACF file */ 
typedef [allocate(all_nodes, dont_free)] PTYPE1; 
typedef [allocate(all_nodes)] PTYPE2; 
typedef [allocate(dont_free)] PTYPE3;
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**midl\_user\_allocate**](midl-user-allocate-1.md)
</dt> <dt>

[**midl\_user\_free**](midl-user-free-1.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




