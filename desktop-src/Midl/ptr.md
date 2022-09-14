---
title: ptr attribute
description: The \ ptr\ attribute designates a pointer as a full pointer.
ms.assetid: a1233a25-b651-4a01-8abf-a64dc9ee168e
keywords:
- ptr attribute MIDL
topic_type:
- apiref
api_name:
- ptr
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ptr attribute

The **\[ptr\]** attribute designates a pointer as a full pointer.

``` syntax
pointer_default(ptr)

typedef [ ptr [ , type-attribute-list ] ] type-specifier declarator-list; 

typedef [ struct | union ]
{
    [ ptr [ , field-attribute-list ] ] type-specifier declarator-list;
    ...
}

[ ptr [ , function-attribute-list ] ] type-specifier ptr-decl function-name(
    [ [ parameter-attribute-list ] ] type-specifier [standard-declarator]
    , ...);

[[ [ function-attribute-list ] ]] type-specifier [[ptr-decl]] function-name(
    [ ptr [[ , parameter-attribute-list ]] ] type-specifier [[standard-declarator]]
    , ...);
```

## Parameters

<dl> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type. Valid type attributes include **\[**[**handle**](handle.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**, **\[**[**transmit\_as**](transmit-as.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md), or **\[ptr\]**; and the usage attributes **\[**[**context\_handle**](context-handle.md)**\]**, **\[**[**string**](string.md)**\]**, and **\[**[**ignore**](ignore.md)**\]**. Separate multiple attributes with commas.

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

Specifies zero or more field attributes that apply to the structure or union member or function parameter. Valid field attributes include **\[**[**first\_is**](first-is.md)**\]**, **\[**[**last\_is**](last-is.md)**\]**, **\[**[**length\_is**](length-is.md)**\]**, **\[**[**max\_is**](max-is.md)**\]**, **\[**[**size\_is**](size-is.md)**\]**; the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[**[**context\_handle**](context-handle.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[ptr\]**; and the union attribute **\[**[**switch\_type**](switch-type.md)**\]**. Separate multiple field attributes with commas.

</dd> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**callback**](callback.md)**\]**, **\[**[**local**](local.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[ptr\]**; and the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[**[**context\_handle**](context-handle.md)**\]**.

</dd> <dt>

*ptr-decl* 
</dt> <dd>

Specifies at least one pointer declarator to which the **\[ptr\]** attribute applies. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Consists of zero or more attributes appropriate for the specified parameter type. Parameter attributes can take the directional attributes [**in**](in.md) and [**out**](out-idl.md); the field attributes [**first\_is**](first-is.md), [**last\_is**](last-is.md), [**length\_is**](length-is.md), [**max\_is**](max-is.md), [**size\_is**](size-is.md), and [**switch\_type**](switch-type.md); the pointer attribute [**ref**](ref.md), [**unique**](unique.md), or **\[ptr\]**; and the usage attributes [**context\_handle**](context-handle.md) and [**string**](string.md). The usage attribute [**ignore**](ignore.md) cannot be used as a parameter attribute. Separate multiple attributes with commas.

</dd> </dl>

## Remarks

The full pointer designated by the **\[ptr\]** attribute approaches the full functionality of the C-language pointer. The full pointer can have the value **NULL** and can change during the call from **NULL** to non-**NULL**. Storage pointed to by full pointers can be reached by other names in the application supporting aliasing and cycles. This functionality requires more overhead during a remote procedure call to identify the data referred to by the pointer, determine whether the value is **NULL**, and to discover if two pointers point to the same data.

Use full pointers for:

-   Remote return values.
-   Double pointers, when the size of an output parameter is not known.
-   **NULL** pointers.

Full (and unique) pointers cannot be used to describe the size of an array or union because these pointers can have the value **NULL**. This restriction by MIDL prevents an error that can result when a **NULL** value is used as the size.

Reference and unique pointers are assumed to cause no aliasing of data. A directed graph obtained by starting from a unique or reference pointer and following only unique or reference pointers contains neither reconvergence nor cycles.

To avoid aliasing, all pointer values should be obtained from an input pointer of the same class of pointer. If more than one pointer points to the same memory location, all such pointers must be full pointers.

In some cases, full and unique pointers can be mixed. A full pointer can be assigned the value of a unique pointer, as long as the assignment does not violate the restrictions on changing the value of a unique pointer. However, when you assign a unique pointer the value of a full pointer, you may cause aliasing.

Mixing full and unique pointers can cause aliasing, as demonstrated in the following example:

``` syntax
typedef struct 
{ 
    [ptr] short * pdata;          // full pointer  
} GRAPH_NODE_TYPE; 
 
typedef struct 
{ 
    [unique] graph_node * left;   // unique pointer  
    [unique] graph_node * right;  // unique pointer 
} TREE_NODE_TYPE; 
 
// application code: 
short a = 5; 
TREE_NODE_TYPE * t; 
GRAPH_NODE_TYPE g, h; 
 
g.pdata = h.pdata = &a; 
t->left = &g; 
t->right = &h; 
// t->left->pdata == t->right->pdata == &a
```

Although "t->left" and "t->right" point to unique memory locations, "t->left->pdata" and "t->right->pdata" are aliased. For this reason, aliasing-support algorithms must follow all pointers (including unique and reference pointers) that may eventually reach a full pointer.

## Examples

``` syntax
pointer_default(ptr) 
 
typedef [ptr, string] unsigned char * MY_STRING_TYPE; 
 
[ptr] char * MyFunction([in, out, unique] long * plNumber);
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

[Interface Definition (IDL) File](interface-definition-idl-file.md)
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

[**pointer\_default**](pointer-default.md)
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
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 