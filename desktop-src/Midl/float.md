---
title: float attribute
description: The float keyword designates a 32-bit floating-point number.
ms.assetid: dfc94378-13a4-4d34-a254-7ff68f4f9d40
keywords:
- float attribute MIDL
topic_type:
- apiref
api_name:
- float
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# float attribute

The **float** keyword designates a 32-bit floating-point number.

``` syntax
float identifier-name;
```

## Parameters

<dl> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

The **float** type is one of the base types of the interface definition language (IDL). The **float** type can appear as a type specifier in [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

The **float** type cannot appear in [**const**](const.md) declarations.

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**double**](double.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




