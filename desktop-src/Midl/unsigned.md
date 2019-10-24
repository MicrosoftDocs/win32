---
title: unsigned attribute
description: The unsigned keyword indicates that the most significant bit of an integer variable represents a data bit rather than a signed bit.
ms.assetid: bfcc6bec-895e-45e1-b162-b79651662aa6
keywords:
- unsigned attribute MIDL
topic_type:
- apiref
api_name:
- unsigned
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# unsigned attribute

The **unsigned** keyword indicates that the most significant bit of an integer variable represents a data bit rather than a signed bit.

``` syntax
[[ unsigned ]] type-qualifier [[ int ]]identifier-name;
```

## Parameters

<dl> <dt>

*type-qualifier* 
</dt> <dd>

Can be any of [**char**](char-idl.md), [**wchar\_t**](wchar-t.md), [**long**](long.md), [**int**](int.md), [**short**](short.md), and [**small**](small.md).

</dd> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

This keyword is optional and can be used with any of the character and integer types [**char**](char-idl.md), [**wchar\_t**](wchar-t.md), [**long**](long.md), [**short**](short.md), and [**small**](small.md). You can optionally include the keyword [**int**](int.md) after the type qualifiers **long**, **short**, and **small**.

When you use the MIDL compiler switch [**/char**](-char.md), character and integer types that appear in the IDL file without explicit sign keywords can appear with the [**signed**](signed.md) or **unsigned** keyword in the generated header file. To avoid confusion, specify the sign of the integer and character types.

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**char**](char-idl.md)
</dt> <dt>

[**/char**](-char.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**int**](int.md)
</dt> <dt>

[**long**](long.md)
</dt> <dt>

[**short**](short.md)
</dt> <dt>

[**signed**](signed.md)
</dt> <dt>

[**small**](small.md)
</dt> <dt>

[**wchar\_t**](wchar-t.md)
</dt> </dl>

 

 




