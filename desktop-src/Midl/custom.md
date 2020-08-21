---
title: custom attribute
description: The \ custom\ attribute creates a user-defined attribute.
ms.assetid: 63c93eca-c9c1-4c14-9f46-aa78b01d9ff8
keywords:
- custom attribute MIDL
topic_type:
- apiref
api_name:
- custom
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# custom attribute

The **\[custom\]** attribute creates a user-defined attribute.

``` syntax
[custom(attribute-id, attribute-value),attribute-list] element-type element-name
```

## Parameters

<dl> <dt>

*attribute-id* 
</dt> <dd>

The GUID for the custom attribute.

</dd> <dt>

*attribute-value* 
</dt> <dd>

The value that the attribute holds. The value must be one that can be put into a VARIANT type.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Other attributes, such as **\[**[**uuid**](uuid.md)**\]** and **\[**[**helpstring**](helpstring.md)**\]**, that apply to this element.

</dd> <dt>

*element-type* 
</dt> <dd>

The type of element to which the custom attribute applies. This can be a library statement, type information, a variable, a function, or a parameter. You cannot use a custom attribute on a member of a coclass.

</dd> <dt>

*element-name* 
</dt> <dd>

The name of the element.

</dd> </dl>

## Remarks

Use the **\[custom\]** attribute to define your own attribute. For example, you might create a string-valued attribute that gives the ProgID for a class.

To retrieve a custom attribute value call one of the following:

-   ITypeLib2::GetCustData(rguid, pvarVal)
-   ITypeInfo2::GetCustData(rguid, pvarVal)
-   ITypeInfo2::GetFuncCustData(index, rguid, pvarVal)
-   ITypeInfo2::GetVarCustData(index, rguid, pvarval)
-   ITypeInfo2::GetParamCustData(indexFunc, indexParam, rguid, pvarVal)

## See also

<dl> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**helpstring**](helpstring.md)
</dt> <dt>

[**library**](library.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**uuid**](uuid.md)
</dt> </dl>

 

 