---
title: uidefault attribute
description: The \ uidefault\ attribute indicates that the type information member is the default member for display in the user interface.
ms.assetid: e789be38-a509-437d-89c9-ebbc830e5ae2
keywords:
- uidefault attribute MIDL
topic_type:
- apiref
api_name:
- uidefault
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# uidefault attribute

The **\[uidefault\]** attribute indicates that the type information member is the default member for display in the user interface.

``` syntax
[method-attribute-list, uidefault]return-type method-name(method-parameter-list)
```

## Parameters

<dl> <dt>

*method-attribute-list* 
</dt> <dd>

Other attributes that apply to the method.

</dd> <dt>

*return-type* 
</dt> <dd>

The type of the data that the method will return when it finishes execution.

</dd> <dt>

*method-name* 
</dt> <dd>

The name of the method.

</dd> <dt>

*method-parameter-list* 
</dt> <dd>

Zero or more parameters for the method.

</dd> </dl>

## Remarks

Applying the **\[uidefault\]** attribute to a member of an interface or a dispinterface tells Visual Basic, at design-time, to automatically display this event or property to the user. This means that when the user double-clicks an object, Visual Basic jumps to the event in the default source interface that has the **\[uidefault\]** attribute. When the user selects an object, Visual Basic's Properties browser displays the property in the default source interface that has this attribute. If no event or property has the **\[uidefault\]** attribute, Visual Basic displays the first event or property listed in the default interface.

### Typeflag Representation

The presence of FUNCFLAG\_FUIDEFAULT or VARFLAG\_FUIDEFAULT

## Examples

``` syntax
[
    dual,
    uuid(12345678-1234-1234-1234-123456789ABC),
    restricted
]
interface IForm: IDispatch
{
    [propget]HRESULT Backcolor([out, retval] long *Value);
    [propput]HRESULT Backcolor([in] long Value);
    [propget, uidefault]HRESULT Name([out, retval] BSTR *Value);
    [propput, uidefault]HRESULT Name([in] BSTR Value);
}
[
    odl,
    dual,
    uuid(87654321-1234-1234-1234-123456789ABC),
    restricted
] 
interface IFormEvents: IDispatch
{
    [uidefault]HRESULT Click();
    HRESULT Resize();
}

[
    uuid(12345678-1234-1234-1234-987654321ABC)
]
coclass Form
{
    [default] interface IForm;
    [default, source] interface IFormEvents;
}
```

## See also

<dl> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> </dl>

 

 