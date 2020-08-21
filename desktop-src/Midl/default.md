---
title: default attribute
description: The \ default\ attribute Indicates that the interface or dispinterface, defined within a coclass, represents the default programmability interface. This attribute is intended for use by macro languages.
ms.assetid: 66769dff-60a0-4e6e-9357-c4339c0bfa3f
keywords:
- default attribute MIDL
topic_type:
- apiref
api_name:
- default
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# default attribute

The **\[default\]** attribute Indicates that the [**interface**](interface.md) or [**dispinterface**](dispinterface.md), defined within a [**coclass**](coclass.md), represents the default programmability interface. This attribute is intended for use by macro languages.

``` syntax
[
    uuid(uuid-number) 
    [, attribute-list]
] 
coclass coclass-name
{
    [ default [, optional-interface-attribute] ]; 
    interface | dispinterface interface-name;
}
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**coclass**](coclass.md).

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies additional [**coclass**](coclass.md) attributes. Separate multiple attributes with commas.

</dd> <dt>

*coclass-name* 
</dt> <dd>

Specifies the name by which other software components can reference this [**coclass**](coclass.md).

</dd> <dt>

*optional-interface-attribute* 
</dt> <dd>

The **\[**[**source**](source.md)**\]** attribute, which specifies that an interface or dispinterface is outgoing, is the only other attribute that can be used here.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> </dl>

## Remarks

A [**coclass**](coclass.md) may have at most two **\[default\]** members. One represents the outgoing (source) interface or dispinterface, and the other represents the incoming (sink) interface or dispinterface. If the **\[default\]** attribute is not specified for any member of the **coclass** or **cotype**, the first outgoing and incoming members that do not have the **\[**[**restricted**](restricted.md)**\]** attribute are treated as the defaults.

### Flags

IMPLTYPEFLAG\_FDEFAULT

## Examples

``` syntax
[ 
    uuid(12345678-1234-1234-1234-123456789ABC), 
    helpstring("Hello Class"),appobject
]  
coclass Hello
{
    [default] interface IHello:IUnknown;
    interface IDispatch;
};
```

## See also

<dl> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**restricted**](restricted.md)
</dt> <dt>

[**source**](source.md)
</dt> </dl>

 

 