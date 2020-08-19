---
title: out attribute
description: The \ out\ attribute identifies pointer parameters that are returned from the called procedure to the calling procedure (from the server to the client).
ms.assetid: f92ef78a-321b-460e-a18a-b63a5e199ad0
keywords:
- out attribute MIDL
topic_type:
- apiref
api_name:
- out
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# out attribute

The \[**out**\] attribute identifies pointer parameters that are returned from the called procedure to the calling procedure (from the server to the client).

``` syntax
[ [function-attribute-list] ] type-specifier [pointer-declarator] function-name(
    [ out [ , parameter-attribute-list ] ] type-specifier [declarator]
    , ...
);
```

## Parameters

<dl> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are \[[**callback**](callback.md)\], \[[**local**](local.md)\]; the pointer attribute \[[**ref**](ref.md)\], \[[**unique**](unique.md)\], or \[[**ptr**](ptr.md)\]; and the usage attributes \[[**string**](string.md)\], \[[**ignore**](ignore.md)\], and \[[**context\_handle**](context-handle.md)\].

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base\_type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), or [**enum**](enum.md) type or type identifier. An optional storage specification can precede *type-specifier*.

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

Specifies zero or more attributes appropriate for a specified parameter type. Parameter attributes with the \[**out**\] attribute can also take the directional attribute \[**out**\]; the field attributes \[[**first\_is**](first-is.md)\], \[[**last\_is**](last-is.md)\], \[[**length\_is**](length-is.md)\], \[[**max\_is**](max-is.md)\], \[[**size\_is**](size-is.md)\], and \[[**switch\_type**](switch-type.md)\]; the pointer attribute \[[**ref**](ref.md)\], \[[**unique**](unique.md)\], or \[[**ptr**](ptr.md)\]; and the usage attributes \[[**context\_handle**](context-handle.md)\] and \[[**string**](string.md)\]. The usage attribute \[[**ignore**](ignore.md)\] cannot be used as a parameter attribute. Separate multiple attributes with commas.

</dd> <dt>

*declarator* 
</dt> <dd>

Specifies the standard declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The parameter declarator in the function declarator, such as the parameter name, is optional.

</dd> </dl>

## Remarks

The \[**out**\] attribute indicates that a parameter that acts as a pointer and its associated data in memory are to be passed back from the called procedure to the calling procedure.

The \[**out**\] attribute must be a pointer. DCE IDL compilers require the presence of an explicit \* as a pointer declarator in the parameter declaration. Microsoft IDL offers an extension that drops this requirement and allows an array or a previously defined pointer type.

A related attribute, \[[**in**](in.md)\], indicates that the parameter is passed from the calling procedure to the called procedure. The \[**in**\] and \[**out**\] attributes specify the direction in which the parameters are passed. A parameter can be defined as \[**in**\]-only, \[**out**\]-only, or \[**in**, **out**\].

An \[**out**\]-only parameter is assumed to be undefined when the remote procedure is called and memory for the object is allocated by the server. Since top-level pointer/parameters must always point to valid storage, and therefore cannot be **NULL**, \[**out**\] cannot be applied to top-level \[[**unique**](unique.md)\] or \[[**ptr**](ptr.md)\] pointers. Parameters that are \[**unique**\] or \[**ptr**\] pointers must be either \[[**in**](in.md)\] or \[**in**, **out**\] parameters.

## Examples

``` syntax
HRESULT MyFunction([out] short * pcount);
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
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

[**ignore**](ignore.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**last\_is**](last-is.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**switch\_type**](switch-type.md)
</dt> <dt>

[**union**](union.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 