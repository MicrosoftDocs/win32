---
title: coclass attribute
description: The coclass statement provides a listing of the supported interfaces for a component object.
ms.assetid: 2c636327-ad18-4087-b495-d1aa84a07f48
keywords:
- coclass attribute MIDL
topic_type:
- apiref
api_name:
- coclass
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# coclass attribute

The **coclass** statement provides a listing of the supported interfaces for a component object.

``` syntax
[
    coclass-attribute-list
]
coclass classname
{
    [
        interface-attributes
    ] 
    [interface | dispinterface] interfacename 
    {
  . . . 
    }
}
```

## Parameters

<dl> <dt>

*coclass-attribute-list* 
</dt> <dd>

The **\[**[**uuid**](uuid.md)**\]** attribute is required on a **coclass**. This is the same **\[uuid\]** that is registered as a CLSID in the system registration database. The **\[**[**helpstring**](helpstring.md)**\]**, **\[**[**helpcontext**](helpcontext.md)**\]**, **\[**[**licensed**](licensed.md)**\]**, **\[**[**version**](version.md)**\]**, **\[**[**control**](control.md)**\]**, **\[**[**hidden**](hidden.md)**\]**, and **\[**[**appobject**](appobject.md)**\]** attributes are accepted, but not required, before a **coclass** definition.

</dd> <dt>

*classname* 
</dt> <dd>

Name by which the common object is known in the type library.

</dd> <dt>

*interface-attributes* 
</dt> <dd>

Optional attributes for the interface or dispinterface. The **\[**[**source**](source.md)**\]**, **\[**[**default**](default.md)**\]**, and **\[**[**restricted**](restricted.md)**\]** attributes are accepted on an interface or dispinterface within a **coclass**.

</dd> <dt>

*interfacename* 
</dt> <dd>

Either an interface declared with the [**interface**](interface.md) keyword, or a dispinterface declared with the [**dispinterface**](dispinterface.md) keyword.

</dd> </dl>

## Remarks

The Microsoft Component Object Model defines a class as an implementation that allows **QueryInterface** between a set of interfaces.

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676), 
    version(1.0), 
    helpstring("A class"), 
    helpcontext(2481), appobject
] 
coclass myapp 
{ 
    [source] interface IMydocfuncs : IUnknown; 
    dispinterface DMydocfuncs; 
}; 
 
[
    uuid(12345678-1234-1234-1234-123456789ABC)
] 
coclass mycoclass 
{ 
    [restricted] interface iface1; 
    interface iface2; 
}
```

## See also

<dl> <dt>

[**appobject**](appobject.md)
</dt> <dt>

[**control**](control.md)
</dt> <dt>

[**default**](default.md)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[**helpstring**](helpstring.md)
</dt> <dt>

[**helpcontext**](helpcontext.md)
</dt> <dt>

[**hidden**](hidden.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**licensed**](licensed.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**restricted**](restricted.md)
</dt> <dt>

[**source**](source.md)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[**uuid**](uuid.md)
</dt> <dt>

[**version**](version.md)
</dt> </dl>

 

 