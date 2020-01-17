---
title: enum attribute
description: The keyword enum identifies an enumerated type.
ms.assetid: 1aaa3c36-17f7-42ff-8f4c-66133fcf4a1a
keywords:
- enum attribute MIDL
topic_type:
- apiref
api_name:
- enum
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# enum attribute

The keyword **enum** identifies an enumerated type.

``` syntax
enum [tag ] 
{ 
    identifier [=integer-value ] 
    [ , ... ] 
}
```

## Parameters

<dl> <dt>

*tag* 
</dt> <dd>

Specifies an optional tag for the enumerated type.

</dd> <dt>

*identifier* 
</dt> <dd>

Specifies the particular enumeration.

</dd> <dt>

*integer-value* 
</dt> <dd>

Specifies a constant integer value.

</dd> </dl>

## Remarks

**enum** types can appear as type specifiers in [**typedef**](typedef.md) declarations, general declarations, and function declarators (either as the function-return-type or as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

In the MIDL compiler's default mode, you can assign integer values to enumerators. (This feature is not available when you compile with the [**/osf**](-osf.md) switch.) As with C-language enumerators, enumerator names must be unique, but the enumerator values need not be.

When assignment operators are not provided, identifiers are mapped to consecutive integers from left to right, starting with zero. When assignment operators are provided, assigned values start from the most recently assigned value.

The maximum number of identifiers is 65,535.

Objects of type **enum** are [**int**](int.md) types, and their size is system-dependent. By default, objects of **enum** types are treated as 16-bit objects of type [**unsigned**](unsigned.md) [**short**](short.md) when transmitted over a network. Values outside the range 0 - 32,767 cause the run-time exception RPC\_X\_ENUM\_VALUE\_OUT\_OF\_RANGE. To transmit objects as 32-bit entities, apply the **\[**[**v1\_enum**](v1-enum.md)**\]** attribute to the **enum** typedef.

## Examples

``` syntax
typedef enum {Monday=2, Tuesday, Wednesday, Thursday, Friday} workdays; 
 
typedef enum {Clemens=21, Palmer=22, Ryan=34} pitchers;
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**int**](int.md)
</dt> <dt>

[**short**](short.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> <dt>

[**v1\_enum**](v1-enum.md)
</dt> </dl>

 

 




