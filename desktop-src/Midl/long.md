---
title: long attribute
description: The long keyword designates a 32-bit integer.
ms.assetid: 5619e482-e3c3-4898-a70b-afd337d2749a
keywords:
- long attribute MIDL
topic_type:
- apiref
api_name:
- long
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# long attribute

The **long** keyword designates a 32-bit integer.

``` syntax
[ signed | unsigned ] long [ int ] declarator-list;
```

## Parameters

<dl> <dt>

*declarator-list* 
</dt> <dd>

Specifies one or more standard C declarators, such as identifiers, pointer declarators, and array declarators. (Function declarators and bit-field declarations are not allowed in structures that are transmitted in remote procedure calls. These declarators are allowed in structures that are not transmitted.) Separate multiple declarators with commas.

</dd> </dl>

## Remarks

The **long** keyword can be preceded by either the keyword [**signed**](signed.md) or the keyword [**unsigned**](unsigned.md). The [**int**](int.md) keyword is optional and can be omitted. To the MIDL compiler, a long integer is signed by default and is synonymous with **signed long int**. On 32-bit platforms, **long** is synonymous with **int**.

The **long** integer type is one of the base types of the IDL language. The **long** integer type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function return–type specifier and as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

## See also

<dl> <dt>

[**const**](const.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**hyper**](hyper.md)
</dt> <dt>

[**int**](int.md)
</dt> <dt>

[**short**](short.md)
</dt> <dt>

[**signed**](signed.md)
</dt> <dt>

[**small**](small.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> </dl>

 

 




