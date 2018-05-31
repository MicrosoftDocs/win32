---
Description: Retrieves the SubmittedTime property for the FaxStatus object of a parent FaxPort object. The SubmittedTime property is a number that represents the time the user submitted the active fax job.
ms.assetid: 0ee824af-f946-4fbd-9724-9e143a27fc54
title: FaxStatus.SubmittedTime property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.SubmittedTime property

Retrieves the **SubmittedTime** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **SubmittedTime** property is a number that represents the time the user submitted the active fax job.

This property is read-only.

## Syntax


```VB
Property SubmittedTime As Date
```



## Property value

A **Date** that receives the time, expressed in UTC, when the user submitted an outbound fax job on the specified port. Note that the **SubmittedTime** property is valid only if the [**Send**](-mfax-ifaxstatus-get-send-vb.md) property is equal to **True**.

## Remarks

You can use the **SubmittedTime** property of a [FaxStatus](-mfax-faxstatus.md) object in conjunction with the [**StartTime**](-mfax-ifaxstatus-get-starttime-vb.md) property of the object to provide users with information about a fax job.

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

[**Send**](-mfax-ifaxstatus-get-send-vb.md)
</dt> <dt>

[**StartTime**](-mfax-ifaxstatus-get-starttime-vb.md)
</dt> <dt>

[**IFaxPorts**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxports)
</dt> <dt>

[**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport)
</dt> </dl>

 

 




