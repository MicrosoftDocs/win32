---
title: unique attribute
description: The \ unique\ attribute specifies a unique pointer.
ms.assetid: 0d668148-e65a-478f-9e47-2528d3caa84c
keywords:
- unique attribute MIDL
topic_type:
- apiref
api_name:
- unique
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# unique attribute

The **\[unique\]** attribute specifies a unique pointer.

``` syntax
pointer_default(unique)

typedef [ unique [[ , type-attribute-list ]] ] type-specifier declarator-list; 

typedef struct-or-union-declarator 
{
    [ unique [[ , field-attribute-list ]] ] type-specifier declarator-list;
    ...}

[ unique [[ , function-attribute-list ]] ] type-specifier ptr-decl function-name(
    [[ [ parameter-attribute-list ] ]] type-specifier [[declarator]]
    , ...);

[[ [ function-attribute-list ] ]] type-specifier [[ptr-decl]] function-name(
    [ unique [[ , parameter-attribute-list ]] ] type-specifier [[declarator]]
    , ...);
```

## Parameters

<dl> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type. Valid type attributes include **\[**[**handle**](handle.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**, **\[**[**transmit\_as**](transmit-as.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[unique\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**context\_handle**](context-handle.md)**\]**, **\[**[**string**](string.md)**\]**, and **\[**[**ignore**](ignore.md)**\]**. Separate multiple attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), [**enum**](enum.md) type, or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*declarator and declarator-list* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md)., and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators separated by commas. The parameter-name identifier in the function declarator is optional.

</dd> <dt>

*struct-or-union-declarator* 
</dt> <dd>

Specifies a MIDL [**struct**](struct.md) or [**union**](union.md) declarator.

</dd> <dt>

*field-attribute-list* 
</dt> <dd>

Specifies zero or more field attributes that apply to the structure member, union member, or function parameter. Valid field attributes include **\[**[**first\_is**](first-is.md)**\]**, **\[**[**last\_is**](last-is.md)**\]**, **\[**[**length\_is**](length-is.md)**\]**, **\[**[**max\_is**](max-is.md)**\]**, **\[**[**size\_is**](size-is.md)**\]**; the usage attributes **\[string\]**, **\[ignore\]**, and **\[context\_handle\]**; the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**; and the union attribute **\[switch\_type\]**. Separate multiple field attributes with commas.

</dd> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**callback**](callback.md)**\]**, **\[**[**local**](local.md)**\]**; the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**; and the usage attributes **\[string\]**, **\[ignore\]**, and **\[context\_handle\]**.

</dd> <dt>

*ptr-decl* 
</dt> <dd>

Specifies at least one pointer declarator to which the **\[unique\]** attribute applies. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Consists of zero or more attributes appropriate for the specified parameter type. Parameter attributes can take the directional attributes **\[in\]** and **\[out\]**; the field attributes **\[first\_is\]**, **\[last\_is\]**, **\[length\_is\]**, **\[max\_is\]**, **\[size\_is\]**, and **\[switch\_type\]**; the pointer attribute **\[ref\]**, **unique**, or [**ptr**](ptr.md); and the usage attributes **\[context\_handle\]** and **\[string\]**. The usage attribute **\[ignore\]** cannot be used as a parameter attribute. Separate multiple attributes with commas.

</dd> </dl>

## Remarks

Pointer attributes can be applied as a type attribute; as a field attribute that applies to a structure member, union member, or parameter; or as a function attribute that applies to the function return type. The pointer attribute can also appear with the **\[**[**pointer\_default**](pointer-default.md)**\]** keyword.

A unique pointer has the following characteristics:

-   Can have the value **NULL**.
-   Can change during a call from **NULL** to non-**NULL**, from non-**NULL** to **NULL**, or from one non-**NULL** value to another.
-   Can allocate new memory on the client. When the unique pointer changes from **NULL** to non-**NULL**, data returned from the server is written into new storage.
-   Can use existing memory on the client without allocating new memory. When a unique pointer changes during a call from one non-**NULL** value to another, the pointer is assumed to point to a data object of the same type. Data returned from the server is written into existing storage specified by the value of the unique pointer before the call.
-   Can orphan memory on the client. Memory referenced by a non-**NULL** unique pointer may never be freed if the unique pointer changes to **NULL** during a call and the client does not have another means of dereferencing the storage.
-   Does not cause aliasing. Like storage pointed to by a reference pointer, storage pointed to by a unique pointer cannot be reached from any other name in the function.

The stubs call the user-supplied memory-management functions [**midl\_user\_allocate**](/windows/desktop/Rpc/the-midl-user-allocate-function) and [**midl\_user\_free**](/windows/desktop/Rpc/the-midl-user-free-function) to allocate and deallocate memory required for unique pointers and their referents.

The following restrictions apply to unique pointers:

-   The **\[unique\]** attribute cannot be applied to binding-handle parameters ( [**handle\_t**](handle-t.md)) and context-handle parameters.
-   The **\[unique\]** attribute cannot be applied to **\[**[**out**](out-idl.md)**\]**-only top-level pointer parameters (parameters that have only the **\[out\]** directional attribute).
-   By default, top-level pointers in parameter lists are **\[**[**ref**](ref.md)**\]** pointers. This is true even if the interface specifies **pointer\_default(unique)**. Top-level parameters in parameter lists must be specified with the **\[unique\]** attribute to be a unique pointer.
-   Unique pointers cannot be used to describe the size of an array or union arm because unique pointers can have the value **NULL**. This restriction prevents the error that results if a **NULL** value is used as the array size or the union-arm size.

## Examples

``` syntax
pointer_default(unique) 
 
typedef [unique, string] unsigned char * MY_STRING_TYPE; 
 
[unique] char * MyFunction([in, out, unique] long * plNumber);
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

[**handle\_t**](handle-t.md)
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

[midl\_user\_allocate](/windows/desktop/Rpc/the-midl-user-allocate-function)
</dt> <dt>

[midl\_user\_free](/windows/desktop/Rpc/the-midl-user-free-function)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**pointer\_default**](pointer-default.md)
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

[**transmit\_as**](transmit-as.md)
</dt> <dt>

[**union**](union.md)
</dt> </dl>

 

 