---
title: ms_union attribute
description: The keyword \ ms\_union\ is used to control the NDR alignment of nonencapsulated unions.
ms.assetid: 20ac2985-4552-4224-b03b-07378a2c0cdf
keywords:
- ms_union attribute MIDL
topic_type:
- apiref
api_name:
- ms_union
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ms\_union attribute

The keyword \[**ms\_union**\] is used to control the NDR alignment of nonencapsulated unions.

``` syntax
[
    ms_union,
    ...
]
interface interface-name 
{
    ...
}

[ms_union] procedure-type procedure-name(param-list);
```

## Parameters

<dl> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*procedure-type* 
</dt> <dd>

Specifies the return type of the procedure to which the attribute is being applied.

</dd> <dt>

*procedure-name* 
</dt> <dd>

Specifies the name of the procedure.

</dd> <dt>

*param-list* 
</dt> <dd>

Specifies the procedure's parameter list, which may be empty.

</dd> </dl>

## Remarks

Never use this switch or attribute with new interfaces. This is a backward compatibility feature only.The MIDL compiler in this version of Microsoft RPC mirrors the behavior of the OSF DCE IDL compiler for nonencapsulated unions. However, because earlier versions of the MIDL compiler did not do so, the [**/ms\_union**](-ms-union.md) switch provides compatibility with interfaces built on previous versions of the MIDL compiler.

The **ms\_union** feature can be used as an IDL interface attribute, an IDL type attribute, or as a command-line switch ( [**/ms\_union**](-ms-union.md)).

## Examples

``` syntax
[ms_union] long procedure (...);
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**/ms\_union**](-ms-union.md)
</dt> </dl>

 

 




