---
title: struct attribute
description: The struct keyword is used in a structure type specifier.
ms.assetid: 89e18f0e-185a-408e-812d-3d11f228b473
keywords:
- struct attribute MIDL
topic_type:
- apiref
api_name:
- struct
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# struct attribute

The **struct** keyword is used in a structure type specifier.

``` syntax
struct [[ struct-tag ]] 
{
  [[ [ field-attribute-list ] ]] type-specifier declarator-list;
    ...
};
```

## Parameters

<dl> <dt>

*struct-tag* 
</dt> <dd>

Specifies an optional tag for the structure.

</dd> <dt>

*field-attribute-list* 
</dt> <dd>

Specifies zero or more field attributes that apply to the structure member. Valid field attributes include **\[**[**first\_is**](first-is.md)**\]**, **\[**[**last\_is**](last-is.md)**\]**, **\[**[**length\_is**](length-is.md)**\]**, **\[**[**max\_is**](max-is.md)**\]**, and **\[**[**size\_is**](size-is.md)**\]**; the usage attributes **\[**[**string**](string.md)**\]** and **\[**[**ignore**](ignore.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the union attribute **\[**[**switch\_type**](switch-type.md)**\]**. Separate multiple field attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base type](midl-base-types.md), **struct**, [**union**](union.md), or [**enum**](enum.md) type or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*declarator-list* 
</dt> <dd>

Specifies one or more standard C declarators, such as identifiers, pointer declarators, and array declarators. (Function declarators and bit-field declarations are not allowed in structures that are transmitted in remote procedure calls. These declarators are allowed in structures that are not transmitted.) Separate multiple declarators with commas.

</dd> </dl>

## Remarks

The IDL structure type specifier, **struct**, differs from the standard C type specifier in the following ways:

-   Each structure member can be associated with optional field attributes that describe characteristics of that structure member for the purposes of a remote procedure call.
-   Bit fields and function declarators are not allowed in structures that are used in remote procedure calls. These standard C declarator constructs can be used only if the structure is not transmitted on the network.

The shape of structures must be the same across platforms to ensure interconnectivity.

## Examples

``` syntax
typedef struct _PITCHER_RECORD_TYPE 
{ 
    short flag; 
    [switch_is(flag)] union PITCHER_STATISTICS_TYPE p; 
} PITCHER_RECORD_TYPE;
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

[**/c\_ext**](-c-ext.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[**first\_is**](first-is.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**ignore**](ignore.md)
</dt> <dt>

[**last\_is**](last-is.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**switch\_type**](switch-type.md)
</dt> <dt>

[**union**](union.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 