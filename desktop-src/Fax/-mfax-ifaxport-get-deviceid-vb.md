---
Description: The DeviceId property is a number representing the permanent line identifier for the fax port.
ms.assetid: f7720dda-3635-4a23-9dc4-09cac4b6aa17
title: FaxPort.DeviceId property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxPort.DeviceId property

The **DeviceId** property is a number representing the permanent line identifier for the fax port.

This property is read-only.

## Syntax


```VB
Property DeviceId As Long
```



## Property value

A **Long** that receives the permanent line identifier for the fax port.

## Remarks

A fax client application can use the **DeviceId** property to uniquely identify a fax port. A fax client can call the [**Name**](-mfax-ifaxport-get-name-vb.md) property to retrieve the user-friendly name for the fax port. Note, however, that it is possible for multiple fax ports to have the same user-friendly name.

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

[**IFaxPort**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxport?branch=master)
</dt> <dt>

[**IFaxPorts**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxports?branch=master)
</dt> <dt>

[**Name**](-mfax-ifaxport-get-name-vb.md)
</dt> </dl>

 

 




