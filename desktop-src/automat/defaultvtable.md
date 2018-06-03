---
title: defaultvtable
description: Enables an object to have two different source interfaces.
ms.assetid: 610fa54d-94a2-4035-b04d-73b2756d548b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# defaultvtable

Enables an object to have two different source interfaces.

## Allowed on

A member of a coclass.

## Flags

IMPLTYPEFLAG\_FDEFAULTVTABLE. (If this flag is set, then IMPLTYPEFLAG\_FSOURCE is also set.)

## Remarks

The [default](https://msdn.microsoft.com/windows/desktop/50501057-73E9-40CF-BE7C-411F78E3B084) interface is an interface or dispinterface that is the default source interface. If the interface is a:

-   [dual](https://msdn.microsoft.com/windows/desktop/1D39D64C-E23A-4249-A167-4369D5BD2B65) interface, event sinks receive events through [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch).

-   [VTBL](glossary.md) interface, event sinks receive events through VTBL.

-   [dispinterface](https://msdn.microsoft.com/windows/desktop/E8C18AE5-3D9E-4DFF-AA20-B5ACC723EACF), event sinks receive events through [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch).

-   defaultvtable, a default VTBL interface, which cannot be a dispinterface — it must be a dual, VTBL, or interface. If the interface is a dual interface, then event sinks receive events through the VTBL.

An object can have both a default source and a default VTBL source interface with the same interface identifier (IID or GUID). In this case, a sink should advise using IID\_IDISPATCH to receive dispatch events, and use the specific interface identifier to receive VTBL events.

For normal (non-source) interfaces, an object can support a single interface that satisfies consumers who want to use [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch)access as well as VTBL access (a dual interface). Because of the way source interfaces work, it is not possible to use dual interface for source interfaces. The object with the source interface is in control of whether calls are made through **IDispatch** or through the VTBL. The sink does not provide any information about how it wants to receive the events. The only action that object-sourcing events can take would be to use the least common denominator, the **IDispatch** interface. This effectively reduces a dual interface to a dispatch interface with regard to sourcing events.



| Interface                                                                                       | Flag it translates into                                                     |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [default](https://msdn.microsoft.com/windows/desktop/50501057-73E9-40CF-BE7C-411F78E3B084)                                                 | IMPLTYPEFLAG\_FDEFAULT                                                      |
| [default](https://msdn.microsoft.com/windows/desktop/50501057-73E9-40CF-BE7C-411F78E3B084), [source](https://msdn.microsoft.com/windows/desktop/FE2AD42D-90C9-44FE-AE8E-E405111D1D1D) | IMPLTYPEFLAG\_FDEFAULT, IMPLTYPEFLAG\_FSOURCE                               |
| defaultvtable,[source](https://msdn.microsoft.com/windows/desktop/FE2AD42D-90C9-44FE-AE8E-E405111D1D1D)                                    | IMPLTYPEFLAG\_FDEFAULT, IMPLTYPEFLAG\_FDEFAULTVTABLE, IMPLTYPEFLAG\_FSOURCE |



 

## Example


```C++
[  odl, 
   dual,
   uuid(1e196b20-1f3c-1069-996b-00dd010ef676),
   restricted
]
interface IForm: IDispatch
{
   [propget]
   HRESULT Backcolor([out, retval] long *Value);

   [propput]
   HRESULT Backcolor([in] long Value);


   [propget]
   HRESULT Name([out, retval] BSTR *Value);

   [propput]
   HRESULT Name([in] BSTR Value);
}

[  odl, 
   dual,
   uuid(1e196b20-1f3c-1069-996b-00dd010ef767),
   restricted
]
interface IFormEvents: IDispatch
{
   HRESULT Click();
   HRESULT Resize();
}

[uuid(1e196b20-1f3c-1069-996b-00dd010fe676)]
coclass Form
{
   [default] interface IForm;
   [default, source] interface IFormEvents;
   [defaultvtable, source] interface IFormEvents;
}
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




