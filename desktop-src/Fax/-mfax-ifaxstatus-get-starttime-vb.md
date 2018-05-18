---
Description: 'Retrieves the StartTime property for the FaxStatus object of a parent FaxPort object. The StartTime property is a number that represents the starting time for an active fax job.'
ms.assetid: 'c9611619-b7b4-486d-b8fa-a8de8a50fae4'
title: 'FaxStatus.StartTime property'
---

# FaxStatus.StartTime property

Retrieves the **StartTime** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **StartTime** property is a number that represents the starting time for an active fax job.

This property is read-only.

## Syntax


```VB
Property StartTime As Date
```



## Property value

A **Date** that receives the time, expressed in UTC, when an active fax job began transmitting a document on the specified port.

For more information about the **Date** data type, see the *Microsoft Visual C++ Programmer's Guide*.

## Remarks

You can use the **StartTime** property of a [FaxStatus](-mfax-faxstatus.md) object in conjunction with the [**ElapsedTime**](-mfax-ifaxstatus-get-elapsedtime-vb.md) property of the object to inform users about the transmission length of a fax job.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxStatus**](-mfax-faxstatus-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxStatus**](-mfax-ifaxstatus.md)
</dt> <dt>

[**ElapsedTime**](-mfax-ifaxstatus-get-elapsedtime-vb.md)
</dt> <dt>

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> <dt>

[**IFaxPort**](-mfax-ifaxport.md)
</dt> </dl>

 

 




