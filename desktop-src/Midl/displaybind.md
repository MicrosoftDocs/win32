---
title: displaybind attribute
description: The \ displaybind\ attribute indicates a property that should be displayed to the user as bindable.
ms.assetid: 047a58b2-3ae2-437a-992f-a9d1541decbe
keywords:
- displaybind attribute MIDL
topic_type:
- apiref
api_name:
- displaybind
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# displaybind attribute

The **\[displaybind\]** attribute indicates a property that should be displayed to the user as bindable.

``` syntax
[
  [interface-attribute-list]
]
interface | dispinterface interface-name
{
    [bindable, displaybind [ , attribute-list]] returntype function-name(params)
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies an optional list of interface attributes.

</dd> <dt>

*interface-name* 
</dt> <dd>

The name of the interface.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes, separated by commas, that apply to the function-return type.

</dd> <dt>

*returntype* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function to which the **\[displaybind\]** attribute will be applied.

</dd> <dt>

*params* 
</dt> <dd>

Function parameter list.

</dd> </dl>

## Remarks

Properties that have the **\[displaybind\]** attribute must also have the **\[**[**bindable**](bindable.md)**\]** attribute. An object can support data binding but not have this attribute.

### Flags

FUNCFLAG\_FDISPLAYBIND, VARFLAG\_FDISPLAYBIND

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676)
] 
interface MyObject : IUnknown
{
    properties:
    methods:
        [id(1), propget, bindable, defaultbind, 
         displaybind] long Size(void);

        [id(1), propput, bindable, defaultbind, 
         displaybind] HRESULT Size([in]long lSize);
}
```

## See also

<dl> <dt>

[**bindable**](bindable.md)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 