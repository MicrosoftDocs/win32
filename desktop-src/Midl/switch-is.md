---
title: switch_is attribute
description: The \ switch\_is\ attribute specifies the expression or identifier acting as the union discriminant that selects the union member.
ms.assetid: 93552bdf-6a14-47ce-877e-32ed976bb895
keywords:
- switch_is attribute MIDL
topic_type:
- apiref
api_name:
- switch_is
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# switch\_is attribute

The **\[switch\_is\]** attribute specifies the expression or identifier acting as the union discriminant that selects the union member.

``` syntax
typedef struct [[ struct-tag ]] 
{
    [ switch_is(limited-expr) [[ , field-attr-list ]] ] union-type-specifier declarator;
    ...
}

[[ [function-attribute-list] ]] type-specifier [[pointer-declarator]] function-name(
    [ switch_is(limited-expr) [[ , param-attr-list ]] ] union-type [[declarator]]
    , ...);
```

## Parameters

<dl> <dt>

*struct-tag* 
</dt> <dd>

Specifies an optional tag for a structure.

</dd> <dt>

*limited-expr* 
</dt> <dd>

Specifies a C-language expression supported by MIDL. Almost all C-language expressions are supported. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow pre- and post-increment and pre- and post-decrement operators.

</dd> <dt>

*field-attr-list* 
</dt> <dd>

Specifies zero or more field attributes that apply to a union member. Valid field attributes include **\[**[**first\_is**](first-is.md)**\]**, **\[**[**last\_is**](last-is.md)**\]**, **\[**[**length\_is**](length-is.md)**\]**, **\[**[**max\_is**](max-is.md)**\]**, **\[**[**size\_is**](size-is.md)**\]**; the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[**[**context\_handle**](context-handle.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and for members that are themselves unions, the union attribute **\[**[**switch\_type**](switch-type.md)**\]**. Separate multiple field attributes with commas.

</dd> <dt>

*union-type-specifier* 
</dt> <dd>

Specifies the [**union**](union.md) type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*declarator and declarator-list* 
</dt> <dd>

Specifies a standard C declarator, such as an identifier, pointer declarator, and array declarator. (Function declarators and bit-field declarations are not allowed in unions that are transmitted in remote procedure calls. These declarators are allowed in unions that are not transmitted.) Separate multiple declarators with commas.

</dd> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**callback**](callback.md)**\]**, **\[**[**local**](local.md)**\]**; the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**; and the usage attributes **\[string\]**, **\[ignore\]**, and **\[context\_handle\]**.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), [**enum**](enum.md) type, or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*pointer-declarator* 
</dt> <dd>

Specifies zero or more pointer declarators. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*param-attr-list* 
</dt> <dd>

Specifies zero or more attributes appropriate for the specified parameter type. Parameter attributes can take the directional attributes **\[in\]** and **\[out\]**, the field attributes **\[first\_is\]**, **\[last\_is\]**, **\[length\_is\]**, **\[max\_is\]**, **\[size\_is\]**, and **\[switch\_type\]**; the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**; and the usage attributes **\[context\_handle\]** and **\[string\]**. The usage attribute **\[ignore\]** cannot be used as a parameter attribute. Separate multiple attributes with commas.

</dd> <dt>

*union-type* 
</dt> <dd>

Identifies the [**union**](union.md) type specifier.

</dd> </dl>

## Remarks

The discriminant associated with the **\[switch\_is\]** attribute must be defined at the same logical level as the union:

-   When the union is a parameter, the union discriminant must be another parameter.
-   When the union is a field of a structure, the discriminant must be another field of the same structure.

The sequence in a structure or a function parameter list is not significant. The union can either precede or follow the discriminant.

The **\[switch\_is\]** attribute can appear as a field attribute or as a parameter attribute.

## Examples

``` syntax
typedef [switch_type(short)] union _WILLIE_UNION_TYPE 
{ 
    [case(24)] 
        float fMays; 
    [case(25)] 
        double dMcCovey; 
    [default] 
        ; 
} WILLIE_UNION_TYPE; 
 
typedef struct _WINNER_TYPE 
{ 
    [switch_is(sUniformNumber)] WILLIE_UNION_TYPE w; 
    short sUniformNumber; 
} WINNER_TYPE;
```

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**callback**](callback.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[Encapsulated Unions](encapsulated-unions.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[**first\_is**](first-is.md)
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

[Nonencapsulated Unions](nonencapsulated-unions.md)
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

 

 




