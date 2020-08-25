---
title: string attribute
description: The \ string\ attribute indicates that the one-dimensional char, wchar\_t, byte (or equivalent) array or the pointer to such an array must be treated as a string.
ms.assetid: 379cd59e-7540-4188-9b5c-6c25a8928999
keywords:
- string attribute MIDL
topic_type:
- apiref
api_name:
- string
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# string attribute

The **\[string\]** attribute indicates that the one-dimensional [**char**](char-idl.md), [**wchar\_t**](wchar-t.md), [**byte**](byte.md) (or equivalent) array or the pointer to such an array must be treated as a string. The string can also be an array (or a pointer to an array) of constructs whose fields are all of the type **byte**.

``` syntax
typedef [ string [[ , type-attribute-list ]] ] type-specifier declarator-list; 

typedef [ struct | union ] 
{
    [ string [[ , field-attribute-list ]] ] type-specifier declarator-list;
    ...
};

[ string [[ , function-attribute-list ]] ] type-specifier ptr-decl function-name(
  [[ [ parameter-attribute-list ] ]] type-specifier [[standard-declarator]]
  , ...);

[[ [ function-attribute-list ] ]] type-specifier [[ptr-decl]] function-name(
    [ string [[ , parameter-attribute-list ]] ] type-specifier [[standard-declarator]]
  , ...);
```

## Parameters

<dl> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to a type. Valid type attributes include **\[**[**handle**](handle.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**, **\[**[**transmit\_as**](transmit-as.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**context\_handle**](context-handle.md)**\]**, **\[string\]**, and **\[**[**ignore**](ignore.md)**\]**. Separate multiple attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base type](midl-base-types.md), [**struct**](struct.md) type, or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*standard-declarator* 
</dt> <dd>

Specifies a standard C declarator, such as an identifier, a pointer declarator, or an array declarator. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md)., and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers).

</dd> <dt>

*declarator-list* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md)., and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators separated by commas. The parameter-name identifier in the function declarator is optional.

</dd> <dt>

*field-attribute-list* 
</dt> <dd>

Specifies zero or more field attributes that apply to the structure, union member, or function parameter. The two valid field attributes are **\[**[**max\_is**](max-is.md)**\]** and **\[**[**size\_is**](size-is.md)**\]**; the usage attributes **\[string\]**, **\[ignore\]**, and **\[context\_handle\]**, the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[unique\]**, or **\[**[**ptr**](ptr.md)**\]**, and the union attribute **\[switch\_type\]**. Separate multiple field attributes with commas.

</dd> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**callback**](callback.md)**\]**, **\[**[**local**](local.md)**\]**; the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**; and the usage attributes **\[string\]**, **\[ignore\]**, and **\[context\_handle\]**.

</dd> <dt>

*ptr-decl* 
</dt> <dd>

Specifies an optional pointer declarator to which the **\[string\]** attribute applies. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Consists of zero or more attributes appropriate for the specified parameter type. Parameter attributes can take the directional attributes **\[in\]** and **\[out\]**; the field attributes **\[**[**max\_is**](max-is.md)**\]** and **\[**[**size\_is**](size-is.md)**\]**; the pointer attribute **\[ref\]**, **\[unique\]**, or **\[ptr\]**; and the usage attributes **\[context\_handle\]** and **\[string\]**. The usage attribute **\[ignore\]** cannot be used as a parameter attribute. Separate multiple attributes with commas.

</dd> </dl>

## Remarks

If the **\[string\]** attribute is used with an array whose bounds are determined at run time, you must also specify a **\[size\_is\]** or **\[max\_is\]** attribute, as in the following example:

``` syntax
/* a string that can hold up to MAX_STRING_LENGTH characters */
typedef [string, max_is(MAX_STRING_LENGTH)] char line[];
```

The **\[string\]** attribute cannot be used with attributes that specify the range of transmitted elements, such as **\[first\_is\]**, **\[last\_is\]**, and **\[length\_is\]**.

When used on multidimensional arrays, the **\[string\]** attribute applies to the rightmost array.

To define a counted string, do not use the **\[string\]** attribute. Use a character array or character-based pointer such as the following:

``` syntax
typedef struct 
{ 
    unsigned short size; 
    unsigned short length; 
    [size_is(size), length_is(length)] char string[*]; 
} counted_string;
```

The **\[string\]** attribute specifies that the stub should use a language-supplied method to determine the length of strings.

When declaring strings in C, you must allocate space for an extra character that marks the end of the string.

## Examples

``` syntax
/* a string type that can hold up to 80 characters */ 
typedef [string] char line[81]; 
 
HRESULT Proc1([in, string] char * pszName);
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**callback**](callback.md)
</dt> <dt>

[**char**](char-idl.md)
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

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**size\_is**](size-is.md)
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
</dt> <dt>

[**wchar\_t**](wchar-t.md)
</dt> </dl>

 

 