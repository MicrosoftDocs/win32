---
Description: The GetRoutingMethods interface method creates a FaxRoutingMethods object for the parent FaxPort object.
ms.assetid: c919fc6f-227d-428a-8d73-ae5ac600a851
title: FaxPort.GetRoutingMethods method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxPort.GetRoutingMethods method

The **GetRoutingMethods** interface method creates a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object for the parent [FaxPort](-mfax-faxport.md) object. The FaxRoutingMethods object allows enumeration of the fax routing methods associated with a fax port. Fax routing methods are defined by a fax routing extension DLL.

## Syntax


```VB
FaxPort.GetRoutingMethods( _
  ByRef retVal As IDispatch _
) As Long
```



## Parameters

<dl> <dt>

*retVal* \[out\]
</dt> <dd>

Type: **[IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)\***

Retrieves a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object.

</dd> </dl>

## Remarks

The **GetRoutingMethods** interface method retrieves an [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer to a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object. This object is derived from the [FaxPort](-mfax-faxport.md) object specified by the [**IFaxPorts**](-mfax-ifaxports.md) interface.

A fax client application can access the [**IFaxRoutingMethods**](-mfax-ifaxroutingmethods.md) interface directly by calling the [IUnknown::QueryInterface](http://msdn.microsoft.com/en-us/library/ms682521.aspx) method to retrieve an interface pointer.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxPort**](-mfax-faxport-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxPort**](-mfax-ifaxport.md)
</dt> <dt>

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> <dt>

[**IFaxRoutingMethods**](-mfax-ifaxroutingmethods.md)
</dt> </dl>

 

 




