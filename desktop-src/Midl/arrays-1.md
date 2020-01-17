---
title: arrays attribute
description: Arrays are homogenous collections of data accessed by an index or element number.
ms.assetid: 375fb795-8f18-45b7-898c-99f1273746d8
keywords:
- arrays attribute MIDL
topic_type:
- apiref
api_name:
- arrays
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# arrays attribute

Arrays are homogenous collections of data accessed by an index or element number.

``` syntax
typedef [ [type-attr-list] ] type-specifier [pointer-decl] array-declarator;

typedef [ [type-attr-list] ] struct [ tag ] 
{
    [ [ field-attribute-list ] ] type-specifier [pointer-decl] array-declarator;
    ...
};

typedef [ [type-attr-list] ] union [ tag ] 
{
    [ case (limited-expression [ , ... ] ) ]
  [ [ field-attribute-list ] ] type-specifier [pointer-decl] array-declarator;
  [ [ default ]
  [ [ field-attribute-list ] ] type-specifier [pointer-decl] array-declarator;
  ]
};

[[ [function-attribute-list] ]] type-specifier [[pointer-decl]] function-name(
        [[ [param-attr-list] ]] type-specifier [[pointer-decl]] array-declarator
        , ...);
```

## Parameters

<dl> <dt>

*type-attr-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the type. Valid type attributes include [**\[handle\]**](handle.md), [**\[switch\_type\]**](switch-type.md), [**\[transmit\_as\]**](transmit-as.md); the pointer attribute [**\[ref\]**](ref.md), [**\[unique\]**](unique.md), or [**\[ptr\]**](ptr.md); and the usage attributes [**\[context\_handle\]**](context-handle.md), [**\[string\]**](string.md), and [**\[ignore\]**](ignore.md). Separate multiple attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies the type identifier, base type, [**struct**](struct.md), [**union**](union.md), or [**enum**](enum.md) type. The type specification can include an optional storage specification.

</dd> <dt>

*pointer-decl* 
</dt> <dd>

Specifies zero or more pointer declarators. A pointer declarator is the same as the pointer declarator used in C, constructed from the **\*** designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*array-declarator* 
</dt> <dd>

Specifies the name of the array, followed by one of the following constructs for each dimension of the array: "**\[ \]**", "**\[\*\]**", "**\[***const1***\]**", or "**\[***lower...upper***\]**" where *lower* and *upper* are constant values that represent the lower and upper bounds. The constant *lower* must evaluate to zero.

</dd> <dt>

*tag* 
</dt> <dd>

Specifies an optional tag for the structure or union.

</dd> <dt>

*field-attribute-list* 
</dt> <dd>

Specifies zero or more field attributes that apply to the structure, union member, or function parameter. Valid field attributes include [**\[first\_is\]**](first-is.md), [**\[last\_is\]**](last-is.md), [**\[length\_is\]**](length-is.md), [**\[max\_is\]**](max-is.md), [**\[size\_is\]**](size-is.md); the usage attributes [**\[string\]**](string.md), and [**\[ignore\]**](ignore.md); the pointer attributes [**\[ref\]**](ref.md), [**\[unique\]**](unique.md), and [**\[ptr\]**](ptr.md); and the union attribute [**\[switch\_type\]**](switch-type.md). Separate multiple field attributes with commas. Note that of the attributes listed above, **\[first\_is\]**, **\[last\_is\]**, and [**\[ignore\]**](ignore.md) are not valid for unions.

</dd> <dt>

*limited-expression* 
</dt> <dd>

Specifies a C-language expression. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow increment and decrement operators.

</dd> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are [**\[callback\]**](callback.md), [**\[local\]**](local.md); the pointer attribute [**\[ref\]**](ref.md), [**\[unique\]**](unique.md), or [**\[ptr\]**](ptr.md); and the usage attributes [**\[string\]**](string.md), and [**\[context\_handle\]**](context-handle.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*param-attr-list* 
</dt> <dd>

Specifies the directional attributes and one or more optional field attributes that apply to the array parameter. Valid field attributes include [**\[max\_is\]**](max-is.md), [**\[size\_is\]**](size-is.md), [**\[length\_is\]**](length-is.md), [**\[first\_is\]**](first-is.md), and [**\[last\_is\]**](last-is.md).

</dd> </dl>

## Remarks

Arrays in MIDL use a style similar to but not exactly the same as C and C++. For more information, see [MIDL Arrays](midl-arrays.md).

## See also

<dl> <dt>

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
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 




