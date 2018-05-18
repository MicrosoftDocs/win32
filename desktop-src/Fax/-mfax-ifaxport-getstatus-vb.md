---
Description: 'The GetStatus method creates a FaxStatus object for the parent FaxPort object. The FaxStatus object contains the current status of a fax port.'
ms.assetid: '7874d54b-f8bd-4b36-896c-ae49754055a5'
title: 'FaxPort.GetStatus method'
---

# FaxPort.GetStatus method

The **GetStatus** method creates a [FaxStatus](-mfax-faxstatus.md) object for the parent [FaxPort](-mfax-faxport.md) object. The FaxStatus object contains the current status of a fax port.

## Syntax


```VB
FaxPort.GetStatus( _
  ByRef retVal As IDispatch _
) As Long
```



## Parameters

<dl> <dt>

*retVal* \[out\]
</dt> <dd>

Type: **[IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)\***

Retrieves a [FaxStatus](-mfax-faxstatus.md) object.

</dd> </dl>

## Remarks

The **GetStatus** method retrieves an [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer to a [FaxStatus](-mfax-faxstatus.md) object. A fax client application can also access the [**IFaxStatus**](-mfax-ifaxstatus.md) interface directly by calling the [IUnknown::QueryInterface](http://msdn.microsoft.com/en-us/library/ms682521.aspx) method to retrieve an **IFaxStatus** interface pointer.

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

[**IFaxStatus**](-mfax-ifaxstatus.md)
</dt> </dl>

 

 




