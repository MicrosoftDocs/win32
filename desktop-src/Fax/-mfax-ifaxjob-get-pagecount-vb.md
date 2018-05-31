---
Description: The PageCount property is a number that represents the total number of pages in a fax transmission. The PageCount property applies only to outgoing fax transmissions.
ms.assetid: 705b8555-fde5-4e11-b580-6ec84c3d1bc9
title: FaxJob.PageCount property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.PageCount property

The **PageCount** property is a number that represents the total number of pages in a fax transmission. The **PageCount** property applies only to outgoing fax transmissions.

This property is read-only.

## Syntax


```VB
Property PageCount As Long
```



## Property value

A **Long** that receives the total page count for the specified outbound fax job.

## Remarks

The total page count is only available for faxes where [**Type**](-mfax-ifaxjob-get-type-vb.md) returns JT\_SEND. If the page count is not available, **PageCount** returns zero.

The total page count is only available for faxes that have a [**Type**](-mfax-ifaxjob-get-type-vb.md) property equal to JT\_SEND. If the page count is not available, the **PageCount** property is zero.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxJob**](-mfax-faxjob-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxJob**](-mfax-ifaxjob.md)
</dt> <dt>

[**IFaxJobs**](-mfax-ifaxjobs.md)
</dt> <dt>

[**Type**](-mfax-ifaxjob-get-type-vb.md)
</dt> </dl>

 

 




