---
title: int attribute
description: The keyword int specifies a 32-bit signed integer on 32-bit platforms. On 16-bit platforms, the keyword int is an optional keyword that can accompany the keywords small, short, and long.
ms.assetid: ad6ce0ff-e87b-4701-b9d2-a69c34e0339b
keywords:
- int attribute MIDL
topic_type:
- apiref
api_name:
- int
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# int attribute

The keyword **int** specifies a 32-bit signed integer on 32-bit platforms. On 16-bit platforms, the keyword **int** is an optional keyword that can accompany the keywords [**small**](small.md), [**short**](short.md), and [**long**](long.md).

``` syntax
[ signed | unsigned ] integer-modifier [ int ] declarator-list;
```

## Parameters

<dl> <dt>

*integer-modifier* 
</dt> <dd>

Specifies the keyword [**small**](small.md), [**short**](short.md), [**long**](long.md), [**hyper**](hyper.md), [**\_\_int3264**](--int3264.md), or [**\_\_int64**](--int64.md),which selects the size of the integer data. On 16-bit platforms, the size qualifier must be present.

</dd> <dt>

*declarator-list* 
</dt> <dd>

Specifies one or more standard C declarators, such as identifiers, pointer declarators, and array declarators. (Function declarators and bit-field declarations are not allowed in structures that are transmitted in remote procedure calls. These declarators are allowed in structures that are not transmitted.) Separate multiple declarators with commas.

</dd> </dl>

## Remarks

Integer types are among the base types of the interface definition language (IDL). They can appear as type specifiers in [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and as a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

If no integer sign specification is provided, the integer type defaults to [**signed**](signed.md).

DCE IDL compilers do not allow the keyword [**signed**](signed.md) to specify the sign of integer types. Therefore, this feature is not available when you use the MIDL compiler [**/osf**](-osf.md) switch.

Microsoft does not recommend the use of \_\_int3264 for remoting if it can be avoided. Please see the topic on [**\_\_int3264**](--int3264.md) for more information regarding it's use and limitations.

## Examples

``` syntax
signed short int i = 0; 
int j = i; 
typedef struct 
{ 
    small int         i1; 
    short             i2; 
    unsigned long int i3; 
} INTSIZETYPE; 
 
HRESULT MyFunc([in] long int lCount);
```

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[**hyper**](hyper.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**long**](long.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**short**](short.md)
</dt> <dt>

[**signed**](signed.md)
</dt> <dt>

[**small**](small.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**union**](union.md)
</dt> </dl>

 

 




