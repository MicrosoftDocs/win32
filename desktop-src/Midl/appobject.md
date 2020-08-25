---
title: appobject attribute
description: The \ appobject\ attribute identifies the coclass as an application object, which is associated with a full EXE application.
ms.assetid: f4fcdf55-7431-4d66-8a46-f741c52fbe56
keywords:
- appobject attribute MIDL
topic_type:
- apiref
api_name:
- appobject
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# appobject attribute

The **\[appobject\]** attribute identifies the [**coclass**](coclass.md) as an application object, which is associated with a full EXE application.

``` syntax
[
    uuid(uuid-number), 
    appobject 
  [, coclass-attribute-list]
]
coclass classname 
{ 
    [coclass definition]
}
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**coclass**](coclass.md).

</dd> <dt>

*coclass-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the [**coclass**](coclass.md) statement. Allowable **coclass** attributes are [**\[helpstring\]**](helpstring.md), [**\[helpcontext\]**](helpcontext.md), [**\[licensed\]**](licensed.md), [**\[version\]**](version.md), [**\[control\]**](control.md), and [**\[hidden\]**](hidden.md).

</dd> <dt>

*classname* 
</dt> <dd>

Specifies the name by which the component object is known in the type library.

</dd> <dt>

*coclass definition* 
</dt> <dd>

Specifies statements that make up the [**coclass**](coclass.md) definition.

</dd> </dl>

## Remarks

The **\[appobject\]** attribute also indicates that the functions and properties of the [**coclass**](coclass.md) are globally available in the current type library.

The typeflag representation for this attribute is TYPEFLAG\_FAPPOBJECT

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
    helpstring("Hello Class"),
    appobject
] 
coclass Hello
{
    [default] interface IHello : IUnknown;
    interface IDispatch;
}
```

## See also

<dl> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[**control**](control.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**helpstring**](helpstring.md)
</dt> <dt>

[**helpcontext**](helpcontext.md)
</dt> <dt>

[**hidden**](hidden.md)
</dt> <dt>

[**licensed**](licensed.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[**version**](version.md)
</dt> </dl>

 

 