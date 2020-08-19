---
title: defaultvtable attribute
description: The \ defaultvtable\ attribute defines an interface as the default Vtable interface.
ms.assetid: 05e50935-c630-4f9e-a7ec-3bb70a9834f1
keywords:
- defaultvtable attribute MIDL
topic_type:
- apiref
api_name:
- defaultvtable
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# defaultvtable attribute

The **\[defaultvtable\]** attribute defines an interface as the default Vtable interface.

``` syntax
[
    coclass-attribute-list, 
    defaultvtable
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

Other attributes that apply to the class. The **\[**[**source**](source.md)**\]** and **\[**[**uuid**](uuid.md)**\]** attributes are required.

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

A default Vtable interface cannot be a dispinterface—it must be a dual or Vtable or interface. If the interface is a dual interface, then sinks can assume that they will receive events through Vtable.

A class can be both a default source interface and a default Vtable source interface as shown in the example. In this case an advise sink should use IID\_IDISPATCH to receive dispatch events and use the interface identifier to receive Vtable events.

### Typeflag Representation

The presence of IMPLTYPEFLAG\_FDEFAULTVTABLE.

## Examples

``` syntax
[
    dual,
    uuid(12345678-1234-1234-1234-123456789ABC),
    restricted
]
interface IForm: IDispatch
{
    [propget] HRESULT Backcolor([out, retval] long *Value);
    [propput] HRESULT Backcolor([in] long Value);
    [propget] HRESULT Name([out, retval] BSTR *Value);
    [propput] HRESULT Name([in] BSTR Value);}

[
    dual,
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
    restricted
]
interface IFormEvents: IDispatch
{
    HRESULT Click();
    HRESULT Resize();}

    [
        uuid(1e123456-1f3c-1069-996b-123456789ABC)
    ]
    coclass Form
    {
        [default] interface IForm;
        [default, defaultvtable, source] interface IFormEvents;
    }
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
</dt> <dt>

[**source**](source.md)
</dt> <dt>

[**uuid**](uuid.md)
</dt> </dl>

 

 