---
title: implicit_handle attribute
description: The \ implicit\_handle\ ACF attribute specifies the handle used for functions that do not include an explicit handle as a procedure parameter.
ms.assetid: 09c17473-87b5-4fd6-beb9-3d9b7bc82d8c
keywords:
- implicit_handle attribute MIDL
topic_type:
- apiref
api_name:
- implicit_handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# implicit\_handle attribute

The **\[implicit\_handle\]** ACF attribute specifies the handle used for functions that do not include an explicit handle as a procedure parameter.

``` syntax
implicit_handle(handle-type handle-name)
```

## Parameters

<dl> <dt>

*handle-type* 
</dt> <dd>

Specifies the handle data type, such as the base type [**handle\_t**](handle-t.md) or a user-defined handle type.

</dd> <dt>

*handle-name* 
</dt> <dd>

Specifies the name of the handle.

</dd> </dl>

## Remarks

The handle specified by the **\[implicit\_handle\]** attribute is used in different ways depending on the nature of the procedure. If the procedure is remote, the handle will be used as the binding handle for the remote call. The implicit handle may also be used to establish an initial binding for a function that uses a context handle. If the procedure is a serializing procedure, the handle is used as a serializing handle controlling the operation. In the case of type serialization, the handle is used as the serialization handle for all the serialized types.

The **\[implicit\_handle\]** attribute specifies a global variable that contains a handle used by any function needing implicit handles.

The implicit binding handle type must be either [**handle\_t**](handle-t.md) (or a type based on **handle\_t**) or a user-defined handle type specified with the [**handle**](handle.md) attribute. The implicit serializing handle must be a type based on **handle\_t**.

If the implicit handle type is not defined in the IDL file or in any files included and imported by the IDL file for the MIDL computer, you must supply the file containing the handle-type definition when you compile the stubs. Use the ACF [**include**](include.md) statement to include the file containing the handle-type definition.

The **\[implicit\_handle\]** attribute can occur once, at most. The **\[implicit\_handle\]** attribute can occur only if the [**\[auto\_handle\]**](auto-handle.md) and [**\[explicit\_handle\]**](explicit-handle.md) attributes do not occur.

## Examples

``` syntax
/* ACF file */ 
[
    implicit_handle(handle_t hMyHandle)
] 
interface iface
{ 
    // Attribute configuration statements
}
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**auto\_handle**](auto-handle.md)
</dt> <dt>

[**explicit\_handle**](explicit-handle.md)
</dt> <dt>

[**handle\_t**](handle-t.md)
</dt> <dt>

[**include**](include.md)
</dt> </dl>

 

 




