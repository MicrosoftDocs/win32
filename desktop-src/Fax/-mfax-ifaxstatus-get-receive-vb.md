---
Description: Retrieves the Receive property for the FaxStatus object of a parent FaxPort object. The Receive property is a Boolean value that indicates whether a specified fax port is currently receiving a fax.
ms.assetid: 0293b40b-b1ea-45bb-aa0e-6f22d535e7cc
title: FaxStatus.Receive property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.Receive property

Retrieves the **Receive** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Receive** property is a Boolean value that indicates whether a specified fax port is currently receiving a fax.

This property is read-only.

## Syntax


```VB
Property Receive As Boolean
```



## Property value

A **Boolean** that receives whether the fax port is receiving a fax transmission. If this parameter is equal to **True**, the port is currently receiving a fax.

## Remarks

To determine if a specified port is currently sending a fax, you can call the [**IFaxStatus::get\_Send**](-mfax-ifaxstatus-get-send-vb.md) method.

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
</dt> <dt>

[**Send**](-mfax-ifaxstatus-get-send-vb.md)
</dt> </dl>

 

 




