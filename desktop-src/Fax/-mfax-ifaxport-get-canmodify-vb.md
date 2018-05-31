---
Description: The CanModify property is a Boolean value that indicates whether the user has permission to modify configuration information for the fax port.
ms.assetid: c88c2855-51cd-404e-a89f-cc42f456f51c
title: FaxPort.CanModify property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxPort.CanModify property

The **CanModify** property is a Boolean value that indicates whether the user has permission to modify configuration information for the fax port.

This property is read-only.

## Syntax


```VB
Property CanModify As String
```



## Property value

A **String** that receives whether configuration information can be modified for the fax port. If this parameter is equal to TRUE, the user can modify the configuration for the fax port.

## Remarks

To ensure that the client has permission to modify the specified fax port, a fax client application can call the **CanModify** property before calling any method that begins with **IFaxPort::put\_**. For more information, see [Fax Device Management](-mfax-fax-device-management.md).

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
</dt> </dl>

 

 




