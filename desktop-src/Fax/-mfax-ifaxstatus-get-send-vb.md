---
Description: Retrieves the Send property for the FaxStatus object of a parent FaxPort object. The Send property is a Boolean value that indicates whether a specified fax port is currently sending a fax.
ms.assetid: e7759c8a-a6f3-4e42-9d56-bf93d11d7ad1
title: FaxStatus.Send property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxStatus.Send property

Retrieves the **Send** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Send** property is a Boolean value that indicates whether a specified fax port is currently sending a fax.

This property is read-only.

## Syntax


```VB
Property Send As Boolean
```



## Property value

A **Boolean** that receives whether the fax port is sending a fax transmission. If this parameter is equal to **True**, the port is currently sending a fax.

## Remarks

You can call the [**IFaxStatus::get\_Receive**](-mfax-ifaxstatus-get-receive-vb.md) method to determine if a specified port is currently receiving a fax.

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

[**IFaxStatus**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxstatus?branch=master)
</dt> <dt>

[**Receive**](-mfax-ifaxstatus-get-receive-vb.md)
</dt> <dt>

[**IFaxPorts**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxports?branch=master)
</dt> <dt>

[**IFaxPort**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxport?branch=master)
</dt> </dl>

 

 




