---
title: boolean attribute
description: The keyword boolean indicates that the expression or constant expression associated with the identifier takes only the values TRUE and FALSE.
ms.assetid: ed3b00a4-880f-4674-9f6d-8f5faf1eea66
keywords:
- boolean attribute MIDL
topic_type:
- apiref
api_name:
- boolean
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# boolean attribute

The keyword **boolean** indicates that the expression or constant expression associated with the identifier takes only the values **TRUE** and **FALSE**.

``` syntax
boolean identifier-name;
```

## Parameters

<dl> <dt>

*identifier-name* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> </dl>

## Remarks

The **boolean** type is one of the base types of the IDL language. The **boolean** type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

> [!Note]  
> The **boolean** base type is not compatible with the [**oleautomation**](oleautomation.md) attribute. Use VARIANT\_BOOL in your Automation-compatible interfaces.

 

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**oleautomation**](oleautomation.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




