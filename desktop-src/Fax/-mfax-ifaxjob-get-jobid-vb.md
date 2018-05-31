---
Description: The JobId property is a number that uniquely identifies the specified fax job.
ms.assetid: d93e0374-d9c7-457b-bef5-71b5f6c1e320
title: FaxJob.JobId property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.JobId property

The **JobId** property is a number that uniquely identifies the specified fax job.

This property is read-only.

## Syntax


```VB
Property JobId As Long
```



## Property value

A **Long** that receives the unique ID of the fax job.

## Remarks

You can use the **JobId** property to uniquely identify a fax job because it is possible for multiple fax jobs to have the same [**DisplayName**](-mfax-ifaxjob-get-displayname-vb.md) property. Note that the fax job identifier can be different from the identifier of a fax print job.

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

[**IFaxJob**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjob)
</dt> <dt>

[**IFaxJobs**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjobs)
</dt> <dt>

[**DisplayName**](-mfax-ifaxjob-get-displayname-vb.md)
</dt> </dl>

 

 




