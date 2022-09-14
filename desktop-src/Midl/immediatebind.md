---
title: immediatebind attribute
description: The \ immediatebind\ attribute indicates that the database will be notified immediately of all changes to a property of a data-bound object.
ms.assetid: 1c08ddca-e273-43b3-a8f6-ed7f552e4e0e
keywords:
- immediatebind attribute MIDL
topic_type:
- apiref
api_name:
- immediatebind
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# immediatebind attribute

The **\[immediatebind\]** attribute indicates that the database will be notified immediately of all changes to a property of a data-bound object.

``` syntax
[
    interface-attribute-list
] 
interface | dispinterface interface-name 
{
    [bindable, immediatebind[, optional-attribute-list]] returntype function-name(params)
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes that apply to the interface as a whole.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the [**interface**](interface.md) or [**dispinterface**](dispinterface.md).

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Zero or more function attributes.

</dd> <dt>

*returntype* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function in the IDL file.

</dd> <dt>

*params* 
</dt> <dd>

Zero or more function parameters.

</dd> </dl>

## Remarks

The **\[immediatebind\]** attribute allows controls to differentiate between properties that need to notify the database of every change, and those that do not. For example, every change to a checkbox control should be sent to the underlying database immediately, even if the control has not lost the focus. However, for a listbox control, a change occurs whenever a different selection is highlighted. Notifying the database of a change before the control loses focus would be inefficient and unnecessary. The **\[immediatebind\]** attribute allows you to specify, by setting the ImmediateBind bit, individual properties on a form whose changes should be reported immediately.

Properties that have the **\[immediatebind\]** attribute must also have the **\[**[**bindable**](bindable.md)**\]** attribute.

### Flags

FUNCFLAG\_FIMMEDIATEBIND, VARFLAG\_FIMMEDIATEBIND

## Examples

``` syntax
[
    uuid(12345678-1234-1234-1234-123456789ABC)
] 
interface MyObject : IUnknown
{
    properties:
    methods:
        [id(1), propget, bindable, immediatebind] long Size(void);

        [id(1), propput, bindable, 
         immediatebind] HRESULT Size([in]long lSize);
}
```

## See also

<dl> <dt>

[**bindable**](bindable.md)
</dt> <dt>

[**TYPEFLAGS**](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 