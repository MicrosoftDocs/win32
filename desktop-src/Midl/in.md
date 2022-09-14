---
title: in attribute
description: The \ in\ attribute indicates that a parameter is to be passed from the calling procedure to the called procedure.
ms.assetid: 85d5617e-8b73-449a-9627-2c8d5ab2b629
keywords:
- in attribute MIDL
topic_type:
- apiref
api_name:
- in
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# in attribute

The **\[in\]** attribute indicates that a parameter is to be passed from the calling procedure to the called procedure.

``` syntax
[ [function-attribute-list] ] type-specifier [pointer-declarator] function-name(
    [ in [ , parameter-attribute-list ] ] type-specifier [declarator]
    , ...);
```

## Parameters

<dl> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[callback\]**, **\[local\]**, the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**, and the usage attributes **\[string\]**, **\[ignore\]**, and **\[context\_handle\]**.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a **base\_type**, [**struct**](struct.md), [**union**](union.md), or [**enum**](enum.md) type or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*pointer-declarator* 
</dt> <dd>

Specifies zero or more pointer declarators. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Specifies zero or more attributes appropriate for the specified parameter type. Parameter attributes with the **\[in\]** attribute can also take the directional attribute **\[out\]**; the field attributes **\[first\_is\]**, **\[last\_is\]**, **\[length\_is\]**, **\[max\_is\]**, **\[size\_is\]** and **\[switch\_type\]**; the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**; and the usage attributes **\[context\_handle\]** and **\[string\]**. The usage attribute **\[ignore\]** cannot be used as a parameter attribute. Separate multiple attributes with commas.

</dd> <dt>

*declarator* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The parameter declarator in the function declarator, such as the parameter name, is optional.

</dd> </dl>

## Remarks

The **\[in\]** attribute has a converse attribute, **\[**[**out**](out-idl.md)**\]**, which indicates that a parameter is to be returned from the called procedure to the calling procedure. The **\[in\]** and **\[out\]** attributes are known as directional parameter attributes because they specify the direction in which parameters are passed. A parameter can be defined as **\[in\]**, **\[out\]**, or **\[in**, **out\]**.

The **\[in\]** attribute identifies parameters that are marshaled by the client stub for transmission to the server.

The **\[in\]** attribute is applied to a parameter by default when no directional parameter attribute is specified.

## Examples

``` syntax
HRESULT MyFunction([in] short count);
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**midl\_user\_allocate**](/windows/desktop/Rpc/the-midl-user-allocate-function)
</dt> <dt>

[**out**](out-idl.md)
</dt> </dl>

 

 