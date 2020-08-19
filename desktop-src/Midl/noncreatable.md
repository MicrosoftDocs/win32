---
title: noncreatable attribute
description: The \ noncreatable\ attribute defines an object that cannot be instantiated by itself.
ms.assetid: 75d7b978-0f82-4e8a-89c2-ffd5b9a691d6
keywords:
- noncreatable attribute MIDL
topic_type:
- apiref
api_name:
- noncreatable
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# noncreatable attribute

The **\[noncreatable\]** attribute defines an object that cannot be instantiated by itself.

``` syntax
[
  coclass-attribute-list, 
    noncreatable
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

Use the **\[noncreatable\]** attribute on a [**coclass**](coclass.md) statement to indicate to users that they cannot create a new object of this class at the top level—that is, by calling **CreateInstance** or **CoCreateInstance**. Instantiation of an object of this class requires a method call to another object. For example, in Microsoft Excel, the "Cell" object is noncreatable and must be obtained from a Microsoft Excel Worksheet object.

Methods that return instances of noncreatable classes should return the exact type of the object, rather than **VARIANT** or **IDispatch**\* types.

### Typeflag Representation:

The absence of TYPEFLAG\_FCANCREATE.

## Examples

``` syntax
[
    uuid(12345678-1234-1234-1234-123456789ABC),
    helpstring("This is MyCOClass"),
    noncreatable
]
coclass MyCoClass
{
    [default] interface IMyClass;
    [default, source] dispinterface IMyClassEvents;
}
```

## See also

<dl> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 