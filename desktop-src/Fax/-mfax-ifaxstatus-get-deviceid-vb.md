---
Description: Retrieves the DeviceId property for the FaxStatus object of a parent FaxPort object. The DeviceId property is a number representing the permanent line identifier for the fax port.
ms.assetid: 14139556-eac3-41b8-9fc9-cb1eb6ffca8f
title: FaxStatus.DeviceId property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.DeviceId property

Retrieves the **DeviceId** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DeviceId** property is a number representing the permanent line identifier for the fax port.

This property is read-only.

## Syntax


```VB
Property DeviceId As Long
```



## Property value

A **Long** that receives the permanent line identifier for the fax port.

## Remarks

It is possible for multiple fax ports to have the same user-friendly name. You can use the **DeviceId** property to uniquely identify a fax port, and thereby associate a [FaxStatus](-mfax-faxstatus.md) object with a [FaxPort](-mfax-faxport.md) object.

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

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> <dt>

[**IFaxPort**](-mfax-ifaxport.md)
</dt> </dl>

 

 




