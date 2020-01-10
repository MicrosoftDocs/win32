---
title: char attribute
description: The char keyword specifies an 8-bit data item.
ms.assetid: 3c9ba8bb-5aea-4166-acf6-b251377e5384
keywords:
- char attribute MIDL
topic_type:
- apiref
api_name:
- char
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# char attribute

The **char** keyword specifies an 8-bit data item.

``` syntax
char identifier-name;
```

## Parameters

<dl> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

The keyword **char** identifies a data item that has 8 bits. To the MIDL compiler, a **char** is unsigned by default and is synonymous with [**unsigned**](unsigned.md) **char**.

In this version of Microsoft RPC, the character translation tables that convert between ASCII and EBCDIC are built into the run-time libraries and cannot be changed by the user.

The **char** type is one of the base types of the interface definition language (IDL). The **char** type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

DCE IDL compilers do not accept the keyword [**signed**](signed.md) applied to **char** types. Therefore, this feature is not available when you use the MIDL compiler [**/osf**](-osf.md) switch.

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**byte**](byte.md)
</dt> <dt>

[**/char**](-char.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**signed**](signed.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> <dt>

[**wchar\_t**](wchar-t.md)
</dt> </dl>

 

 




