---
title: wchar_t attribute
description: The wchar\_t keyword designates a wide-character type.
ms.assetid: e21b2587-909a-4e2b-8c6d-6cc570bf509f
keywords:
- wchar_t attribute MIDL
topic_type:
- apiref
api_name:
- wchar_t
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# wchar\_t attribute

The **wchar\_t** keyword designates a wide-character type.

``` syntax
wchar_t identifier-name;
```

## Parameters

<dl> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

The **wchar\_t** type is a 16-bit integer which represents a UTF-16 code unit.

The underlying type of **wchar\_t** is determined by the C or C++ compiler.
For C++, you can choose the underlying type with the
[/Zc:wchar_t](/cpp/build/reference/zc-wchar-t-wchar-t-is-native-type)
compiler option.

The MIDL compiler allows redefinition of **wchar\_t**, but only if it is defined as an unsigned short.
If you do redefine **wchar\_t** in this way, then you must use the
[/Zc:wchar_t-](/cpp/build/reference/zc-wchar-t-wchar-t-is-native-type)
compiler option when compiling as C++ to avoid a C++ type redefinition conflict for **wchar\_t**.
Redefining **wchar\_t** is supported only for compatibility reasons and is not recommended.

The wide-character type is one of the predefined types of MIDL. The wide-character type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function return type specifier and as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

The **\[string\]** attribute can be applied to a pointer or array of type **wchar\_t**.

Use the **L** character before a character or a string constant to designate the wide character type constant.

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**char**](char-idl.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**short**](short.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> </dl>

 

 




