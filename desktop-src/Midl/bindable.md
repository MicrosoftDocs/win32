---
title: bindable attribute
description: The \ bindable\ attribute indicates that the property supports data binding.
ms.assetid: ba09096d-a2f7-4958-827c-0fba19ded26f
keywords:
- bindable attribute MIDL
topic_type:
- apiref
api_name:
- bindable
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# bindable attribute

The **\[bindable\]** attribute indicates that the property supports data binding.

``` syntax
[
    interface-attribute-list
] 
interface | dispinterface interface-name 
{
    [bindable[, attribute-list]] returntype function-name(params)
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies a list of zero or more IDL attributes that apply to the interface as a whole. When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function prototype for a property or a method in an [**interface**](interface.md) or [**dispinterface**](dispinterface.md). The following attributes are valid: [**\[helpstring\]**](helpstring.md), [**\[helpcontext\]**](helpcontext.md), [**\[string\]**](string.md), [**\[defaultbind\]**](defaultbind.md), [**\[displaybind\]**](displaybind.md), [**\[immediatebind\]**](immediatebind.md), [**\[propget\]**](propget.md), [**\[propput\]**](propput.md), [**\[propputref\]**](propputref.md), and [**\[vararg\]**](vararg.md). If **vararg** is specified, the last parameter must be a safe array of type VARIANT. Separate multiple attributes with commas.

</dd> <dt>

*returntype* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function to which the **\[bindable\]** attribute will be applied.

</dd> <dt>

*params* 
</dt> <dd>

Function parameter list.

</dd> </dl>

## Remarks

By supporting data binding, the **\[bindable\]** attribute allows the client to be notified whenever a property has changed value. (If you want the client to be notified of impending changes to a property, use the [**\[requestedit\]**](requestedit.md) attribute.)

Because the **\[bindable\]** attribute refers to the property as a whole, it must be specified wherever the property is defined. Therefore, you need to specify the attribute on both the property-accessing function and the property-setting function.

### Flags

FUNCFLAG\_FBINDABLE, VARFLAG\_FBINDABLE

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676)
]
dispinterface MyObject 
{ 
    properties: 
    methods: 
        [id(1), propget, bindable, defaultbind, displaybind] long x(); 
        [id(1), propput, bindable, 
        defaultbind, displaybind] HRESULT x(long rhs); 
}
```

## See also

<dl> <dt>

[**defaultbind**](defaultbind.md)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[**displaybind**](displaybind.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**helpstring**](helpstring.md)
</dt> <dt>

[**helpcontext**](helpcontext.md)
</dt> <dt>

[**immediatebind**](immediatebind.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**propget**](propget.md)
</dt> <dt>

[**propput**](propput.md)
</dt> <dt>

[**propputref**](propputref.md)
</dt> <dt>

[**requestedit**](requestedit.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[**vararg**](vararg.md)
</dt> </dl>

 

 