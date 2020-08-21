---
title: aggregatable attribute
description: The \ aggregatable\ attribute indicates that the class supports aggregation.
ms.assetid: 3b680692-fbf7-4aeb-b11a-c3a87ddaea67
keywords:
- aggregatable attribute MIDL
topic_type:
- apiref
api_name:
- aggregatable
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# aggregatable attribute

The **\[aggregatable\]** attribute indicates that the class supports aggregation.

``` syntax
[
   coclass-attribute-list,
   aggregatable
]
coclass coclass-name
{
   coclass-interface-list
}
```

## Parameters

<dl> <dt>

*coclass-attribute-list* 
</dt> <dd>

Other attributes that apply to the class.

</dd> <dt>

*coclass-name* 
</dt> <dd>

The name of the class.

</dd> <dt>

*coclass-interface-list* 
</dt> <dd>

A list of interfaces for the class.

</dd> </dl>

## Remarks

Use the **\[aggregatable\]** attribute on a [**coclass**](coclass.md) statement to let users know that the class supports aggregations. That is, the class allows its interfaces to be exposed by a container class as if these interfaces were the container's own interfaces.

The typeflag representation for this attribute is TYPEFLAG\_FAGGREGATABLE.

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
    aggregatable
]
coclass Form
{
    [default] interface IForm;
    [default, source] interface IFormEvents;
}
```

## See also

<dl> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> </dl>

 

 