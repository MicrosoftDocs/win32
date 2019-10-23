---
title: switch_type attribute
description: The \ switch\_type\ attribute identifies the type of the variable used as the union discriminant. The switch type can be an integer, character, Boolean, or enumeration type.
ms.assetid: e4c6d33b-d4db-42b7-9d18-fd14bf1fb530
keywords:
- switch_type attribute MIDL
topic_type:
- apiref
api_name:
- switch_type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# switch\_type attribute

The **\[switch\_type\]** attribute identifies the type of the variable used as the union discriminant. The switch type can be an integer, character, Boolean, or enumeration type.

``` syntax
switch_type(switch-type-specifier)
```

## Parameters

<dl> <dt>

*switch-type-specifier* 
</dt> <dd>

Specifies an [**int**](int.md), [**char**](char-idl.md), [**Boolean**](boolean.md), or [**enum**](enum.md) type, or an identifier of such a type.

</dd> </dl>

## Remarks

While the **\[switch\_type\]** attribute identifies the variable type, the **\[**[**switch\_is**](switch-is.md)**\]** attribute specifies the name of the parameter that is the union discriminant. The **\[switch\_type\]** attribute applies to parameters or members of structures or unions.

The union and its discriminant must be specified at the same logical level. When the union is a parameter, the union discriminant must be another parameter. When the union is a field of a structure, the discriminant must be another field of the structure at the same level as the union field.

## Examples

``` syntax
typedef [switch_type(short)] union _WILLIE_UNION_TYPE 
{ 
    [case(24)] 
        float fMays; 
    [case(25)] 
        double dMcCovey; 
    [default] 
        ; 
} WILLIE_UNION_TYPE; 
 
typedef struct _WINNER_TYPE 
{ 
    [switch_is(sUniformNumber)] WILLIE_UNION_TYPE w; 
    short sUniformNumber; 
} WINNER_TYPE;
```

## See also

<dl> <dt>

[**Boolean**](boolean.md)
</dt> <dt>

[**char**](char-idl.md)
</dt> <dt>

[Encapsulated Unions](encapsulated-unions.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**int**](int.md)
</dt> <dt>

[Nonencapsulated Unions](nonencapsulated-unions.md)
</dt> <dt>

[**switch\_is**](switch-is.md)
</dt> <dt>

[**union**](union.md)
</dt> </dl>

 

 




