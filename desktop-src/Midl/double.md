---
title: double attribute
description: The double keyword designates a 64-bit floating-point number.
ms.assetid: a235e9c5-90b3-4fa4-9154-06511abcccd0
keywords:
- double attribute MIDL
topic_type:
- apiref
api_name:
- double
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# double attribute

The **double** keyword designates a 64-bit floating-point number.

``` syntax
double identifier-name;
```

## Parameters

<dl> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

The **double** type is one of the base types of the interface definition language (IDL). This type can appear as a type specifier in [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

The **double** type cannot appear in [**const**](const.md) declarations.

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[**float**](float.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




