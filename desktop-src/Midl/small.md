---
title: small attribute
description: The small keyword designates an 8-bit integer number.
ms.assetid: 368e8836-1baa-4547-a62b-f34ac38bbdb2
keywords:
- small attribute MIDL
topic_type:
- apiref
api_name:
- small
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# small attribute

The **small** keyword designates an 8-bit integer number.

``` syntax
small identifier-name;
```

## Parameters

<dl> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

The **small** keyword can be preceded by either the keyword [**signed**](signed.md) or the keyword [**unsigned**](unsigned.md). The [**int**](int.md) keyword is optional and can be omitted. To the MIDL compiler, a small integer is **signed** by default and is synonymous with **signed small int**.

The **small** integer type is one of the base types of the IDL language. The **small** integer type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function return–type specifier and as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

The sign of the **small** type can be modified by the MIDL compiler switch [**/char**](-char.md). To avoid confusion, specify the sign of the integer type with the keywords [**signed**](signed.md) and [**unsigned**](unsigned.md).

## See also

<dl> <dt>

[**/char**](-char.md)
</dt> <dt>

[**const**](const.md)
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

[**unsigned**](unsigned.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




