---
Description: The JobType property describes the type of fax job; for example, the job can be a receive job, a send job, or a routing job.
ms.assetid: 53768e23-f93c-4fa7-b16e-23292f5a4380
title: FaxIncomingJob.JobType property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.JobType property

The **JobType** property describes the type of fax job; for example, the job can be a receive job, a send job, or a routing job.

This property is read-only.

## Syntax


```VB
Property JobType As byte
```



## Property value

Value that specifies the fax job type.

<dt>



 (0)


</dt> <dd>

The job is an outbound job.

</dd> <dt>



 (1)


</dt> <dd>

The job is an incoming job (being received through a modem).

</dd> <dt>



 (2)


</dt> <dd>

The incoming job has been received, and is now in routing mode (modem is not used).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-queue.md)
</dt> <dt>

[**FaxIncomingJob**](-mfax-faxincomingjob.md)
</dt> <dt>

[**get\_JobType**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxincomingjob-get_jobtype)
</dt> </dl>

 

 




