---
title: defaultbind attribute
description: The \ defaultbind\ attribute indicates the single, bindable property that best represents the object.
ms.assetid: 8cf0922a-3d7c-404d-b4fd-edbd772987bf
keywords:
- defaultbind attribute MIDL
topic_type:
- apiref
api_name:
- defaultbind
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# defaultbind attribute

The **\[defaultbind\]** attribute indicates the single, bindable property that best represents the object.

``` syntax
[
    interface-attribute-list
] 
interface | dispinterface interface-name 
{
    [bindable, defaultbind [, attribute-list]] returntype function-name(params)
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes that apply to the interface as a whole. When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes that apply to the function. When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*returntype* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function to which the **\[defaultbind\]** attribute will be applied.

</dd> <dt>

*params* 
</dt> <dd>

Function parameter list.

</dd> </dl>

## Remarks

Properties that have the **\[defaultbind\]** attribute must also have the **\[**[**bindable**](bindable.md)**\]** attribute. Only one property in an interface or dispinterface can have the **\[defaultbind\]** attribute.

This attribute is used by containers that have a user model involving binding to an object rather than binding to a property of an object. An object can support data binding but not have this attribute.

### Flags

FUNCFLAG\_FDEFAULTBIND, VARFLAG\_FDEFAULTBIND

## Examples

``` syntax
[
    uuid(12345678-1234-1234-1234-123456789ABC)
] 
interface MyObject : IUnknown
{
    properties:
    methods:
        [id(1), propget, bindable, 
         defaultbind, displaybind] long Size(void);

        [id(1), propput, bindable, 
         defaultbind, displaybind] HRESULT Size([in]long lSize);
}
```

## See also

<dl> <dt>

[**bindable**](bindable.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> </dl>

 

 