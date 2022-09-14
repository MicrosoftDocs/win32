---
title: switch attribute
description: The switch keyword selects the discriminant for an encapsulated\_union.
ms.assetid: 66179b68-852f-4943-9105-e9fb310f3c2e
keywords:
- switch attribute MIDL
topic_type:
- apiref
api_name:
- switch
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# switch attribute

The **switch** keyword selects the discriminant for an [**encapsulated\_union**](encapsulated-unions.md).

``` syntax
switch (switch-type switch-name)
```

## Parameters

<dl> <dt>

*switch-type* 
</dt> <dd>

Specifies an [**int**](int.md), [**char**](-char.md), [**enum**](enum.md) type, or an identifier that resolves to one of these types.

</dd> <dt>

*switch-name* 
</dt> <dd>

Specifies the name of the variable of type *switch-type* that acts as the union discriminant.

</dd> </dl>

## Examples

``` syntax
typedef union _S1_TYPE switch (long l1) U1_TYPE 
{ 
    case 1024: 
        float f1; 
    case 2048: 
        double d2; 
} S1_TYPE; 
 
/* in generated header file */ 
typedef struct _S1_TYPE 
{ 
    long l1; 
    union 
    { 
        float f1; 
        double d2; 
    } U1_TYPE; 
} S1_TYPE;
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[Nonencapsulated Unions](nonencapsulated-unions.md)
</dt> <dt>

[**switch\_is**](switch-is.md)
</dt> <dt>

[**switch\_type**](switch-type.md)
</dt> <dt>

[**union**](union.md)
</dt> </dl>

 

 




