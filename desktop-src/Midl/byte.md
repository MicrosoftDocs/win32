---
title: byte attribute
description: The byte keyword specifies an 8-bit data item.
ms.assetid: d6401e05-5498-4d66-8f70-2c794ed26527
keywords:
- byte attribute MIDL
topic_type:
- apiref
api_name:
- byte
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# byte attribute

The **byte** keyword specifies an 8-bit data item.

``` syntax
byte identifier-name;
```

## Parameters

<dl> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

A **byte** data item does not undergo any conversion for transmission on the network as a [**char**](char-idl.md) type might.

The **byte** type is one of the base types of the interface definition language (IDL). The **byte** type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

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

[**typedef**](typedef.md)
</dt> </dl>

 

 




