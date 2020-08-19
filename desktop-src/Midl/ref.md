---
title: ref attribute
description: The \ ref\ attribute identifies a reference pointer. It is used simply to represent a level of indirection.
ms.assetid: db4ff938-0f38-4f77-bb65-f728ffd609e0
keywords:
- ref attribute MIDL
topic_type:
- apiref
api_name:
- ref
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ref attribute

The **\[ref\]** attribute identifies a reference pointer. It is used simply to represent a level of indirection.

``` syntax
pointer_default(ref)

typedef [ ref [[ , type-attribute-list ]] ] type-specifier declarator-list; 

typedef [ struct | union ] 
{
    [ ref [[ , field-attribute-list ]] ] type-specifier declarator-list;
    ...}

[[ [ function-attribute-list ] ]] type-specifier [[ptr-decl]] function-name(
    [ ref [[ , parameter-attribute-list ]] ] type-specifier [[standard-declarator]]
    , ...);
```

## Parameters

<dl> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type. Valid type attributes include **\[**[**handle**](handle.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**, **\[**[**transmit\_as**](transmit-as.md)**\]**; the pointer attributes **\[ref\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**context\_handle**](context-handle.md)**\]**, **\[**[**string**](string.md)**\]**, and **\[**[**ignore**](ignore.md)**\]**. Separate multiple attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), or [**enum**](enum.md) type or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*standard-declarator* 
</dt> <dd>

Specifies a standard C declarator, such as an identifier, a pointer declarator, or an array declarator. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers).

</dd> <dt>

*declarator-list* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators separated by commas. The parameter-name identifier in the function declarator is optional.

</dd> <dt>

*field-attribute-list* 
</dt> <dd>

Specifies zero or more field attributes that apply to the structure, union member, or function parameter. Valid field attributes include **\[**[**first\_is**](first-is.md)**\]**, **\[**[**last\_is**](last-is.md)**\]**, **\[**[**length\_is**](length-is.md)**\]**, **\[**[**max\_is**](max-is.md)**\]**, **\[**[**size\_is**](size-is.md)**\]**; the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[**[**context\_handle**](context-handle.md)**\]**; the pointer attribute **\[ref\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the union attribute **\[**[**switch\_type**](switch-type.md)**\]**. Separate multiple field attributes with commas.

</dd> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**callback**](callback.md)**\]**, **\[**[**local**](local.md)**\]**; the pointer attribute **\[ref\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[**[**context\_handle**](context-handle.md)**\]**.

</dd> <dt>

*ptr-decl* 
</dt> <dd>

Specifies at least one pointer declarator to which the **\[ref\]** attribute applies. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Consists of zero or more attributes appropriate for the specified parameter type. Parameter attributes can take the directional attributes **\[**[**in**](in.md)**\]** and **\[**[**out**](out-idl.md)**\]**; the field attributes **\[**[**first\_is**](first-is.md)**\]**, **\[**[**last\_is**](last-is.md)**\]**, **\[**[**length\_is**](length-is.md)**\]**, **\[**[**max\_is**](max-is.md)**\]**, **\[**[**size\_is**](size-is.md)**\]**, and **\[**[**switch\_type**](switch-type.md)**\]**; the pointer attribute **\[ref\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**context\_handle**](context-handle.md)**\]** and **\[**[**string**](string.md)**\]**. The usage attribute **\[**[**ignore**](ignore.md)**\]** cannot be used as a parameter attribute. Separate multiple attributes with commas.

</dd> </dl>

## Remarks

A pointer attribute can be applied as a type attribute, as a field attribute that applies to a structure member, union member, or parameter; or as a function attribute that applies to the function return type. The pointer attribute can also appear with the **\[**[**pointer\_default**](pointer-default.md)**\]** keyword.

A reference pointer has the following characteristics:

-   Always points to valid storage; never has the value **NULL**. A reference pointer can always be dereferenced.
-   Never changes during a call. A reference pointer always points to the same storage on the client before and after the call.
-   Does not allocate new memory on the client. Data returned from the server is written into existing storage specified by the value of the reference pointer before the call.
-   Does not cause aliasing. Storage pointed to by a reference pointer cannot be reached from any other name in the function.

A reference pointer cannot be used as the type of a pointer returned by a function.

If no attribute is specified for a top-level pointer parameter, it is treated as a reference pointer.

## Examples

``` syntax
[unique] char * GetFirstName( 
    [in, ref] char * pszFullName);
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers)
</dt> <dt>

[Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**callback**](callback.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[**first\_is**](first-is.md)
</dt> <dt>

[**handle**](handle.md)
</dt> <dt>

[**ignore**](ignore.md)
</dt> <dt>

[**last\_is**](last-is.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**switch\_type**](switch-type.md)
</dt> <dt>

[**transmit\_as**](transmit-as.md)
</dt> <dt>

[**union**](union.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 