---
Description: Retrieves the CurrentPage property for the FaxStatus object of a parent FaxPort object. The CurrentPage property is a number that identifies the current page of an active outbound fax job on a specific port.
ms.assetid: 632a8c49-46fa-4736-a273-c6efea5fd0b1
title: FaxStatus.CurrentPage property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.CurrentPage property

Retrieves the **CurrentPage** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **CurrentPage** property is a number that identifies the current page of an active outbound fax job on a specific port.

This property is read-only.

## Syntax


```VB
Property CurrentPage As Long
```



## Property value

A **Long** that receives the page in the fax transmission that the port is currently sending. The page number is relative to 1. This parameter has no meaning for an inbound job.

## Remarks

If the current page is not available, the **IFaxStatus::get\_CurrentPage** method returns zero.

You can use the **CurrentPage** property of a [FaxStatus](-mfax-faxstatus.md) object in conjunction with the [**PageCount**](-mfax-ifaxstatus-get-pagecount-vb.md) property of the object to provide users with a running page count for an outbound fax job. For example, you could inform a user that the fax server is currently transmitting the second page of a four page transmission.

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

[**IFaxStatus**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxstatus)
</dt> <dt>

[**PageCount**](-mfax-ifaxstatus-get-pagecount-vb.md)
</dt> <dt>

[**IFaxPorts**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxports)
</dt> <dt>

[**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport)
</dt> </dl>

 

 




