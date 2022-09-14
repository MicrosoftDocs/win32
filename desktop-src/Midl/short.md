---
title: short attribute
description: The short keyword designates a 16-bit integer.
ms.assetid: 622464a3-0d79-421a-8742-8a3746fe1533
keywords:
- short attribute MIDL
topic_type:
- apiref
api_name:
- short
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# short attribute

The **short** keyword designates a 16-bit integer.

``` syntax
[[ signed | unsigned ]] short [[ int ]] declarator-list;
```

## Parameters

<dl> <dt>

*declarator-list* 
</dt> <dd>

Specifies one or more standard C declarators, such as identifiers, pointer declarators, and array declarators. (Function declarators and bit-field declarations are not allowed in structures that are transmitted in remote procedure calls. These declarators are allowed in structures that are not transmitted.) Separate multiple declarators with commas.

</dd> </dl>

## Remarks

The **short** keyword can be preceded by either the keyword [**signed**](signed.md) or the keyword [**unsigned**](unsigned.md). The [**int**](int.md) keyword is optional and can be omitted. To the MIDL compiler, a short integer is signed by default and is synonymous with **signed short int**.

The **short** integer type is one of the base types of the IDL language. The **short** integer type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**int**](int.md)
</dt> <dt>

[**long**](long.md)
</dt> <dt>

[**signed**](signed.md)
</dt> <dt>

[**small**](small.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> </dl>

 

 




