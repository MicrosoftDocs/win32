---
title: hyper attribute
description: The keyword hyper indicates a 64-bit integer that can be declared as either signed or unsigned.
ms.assetid: cadcacc7-8eea-4ce2-b69f-98a1d8bafeaa
keywords:
- hyper attribute MIDL
topic_type:
- apiref
api_name:
- hyper
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# hyper attribute

The keyword **hyper** indicates a 64-bit integer that can be declared as either signed or unsigned.

``` syntax
[ signed | unsigned ] hyper [ int ] declarator-list;
```

## Parameters

<dl> <dt>

*declarator-list* 
</dt> <dd>

Specifies one or more standard C declarators, such as identifiers, pointer declarators, and array declarators. (Function declarators and bit-field declarations are not allowed in structures that are transmitted in remote procedure calls. These declarators are allowed in structures that are not transmitted.) Separate multiple declarators with commas.

</dd> </dl>

## Remarks

The **hyper** type is one of the base types of the interface definition language (IDL). The **hyper** type can appear as a type specifier in [**const**](const.md) declarations, [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

> [!Note]  
> For 16-bit platforms, the MIDL compiler replaces unsigned hyper integers with **MIDL\_uhyper**. This allows interfaces with unsigned hyper integers to be defined on platforms that do not directly support 64-bit integers. **MIDL\_uhyper** is defined in the RPC header files.

 

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




