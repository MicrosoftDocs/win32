---
Description: The Priority property is a number representing the transmission priority designated for a specified fax port. Priority determines the relative order in which available fax devices send outgoing transmissions.
ms.assetid: d842d79e-6010-4e37-a250-37ae9ddc675e
title: FaxPort.Priority property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxPort.Priority property

The **Priority** property is a number representing the transmission priority designated for a specified fax port. Priority determines the relative order in which available fax devices send outgoing transmissions.

This property is read/write.

## Syntax


```VB
Property Priority As Long
```



## Property value

A **Long** that specifies or receives the transmission priority for the specified fax port. Valid values for this property are 1 through *n*, where *n* is the value returned by a call to the [**Count**](-mfax-ifaxports-get-count-vb.md) method.

## Remarks

> [!Note]  
> Before setting a value for this property, a fax client application can call the [**CanModify**](-mfax-ifaxport-get-canmodify-vb.md) property to ensure that the client has permission to modify configuration information for the specified fax port.

 

When the fax server initiates an outgoing fax transmission, it chooses the fax port with the highest priority and send capability. If that port is not available, the server selects the next available port that follows in rank order, and so on. When a client application changes the priority for a fax port, the fax service adjusts the priority for the other fax ports attached to the server. The **Priority** property has no effect on incoming transmissions.

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

[**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport)
</dt> <dt>

[**IFaxPorts**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxports)
</dt> </dl>

 

 




