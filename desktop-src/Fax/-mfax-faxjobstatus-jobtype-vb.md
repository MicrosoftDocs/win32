---
Description: The JobType property describes the type of fax job; for example, the job can be a receive job, a send job, or a routing job.
ms.assetid: 9d117f34-73c8-4505-81d0-f95e74821c43
title: FaxJobStatus.JobType property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.JobType property

The **JobType** property describes the type of fax job; for example, the job can be a receive job, a send job, or a routing job.

This property is read-only.

## Syntax


```VB
Property JobType As Integer
```



## Property value

A variable of type [**FAX\_JOB\_TYPE\_ENUM**](-mfax-fax-job-type-enum.md) that receives the job type. For more information, see **FAX\_JOB\_TYPE\_ENUM**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-registering-for-fax-events.md)
</dt> <dt>

[**FaxJobStatus**](-mfax-faxjobstatus.md)
</dt> <dt>

[**IFaxJobStatus**](-mfax-faxjobstatus-cpp.md)
</dt> </dl>

 

 




