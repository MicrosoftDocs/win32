---
Description: The ExtendedStatusCode property specifies a code describing the job's extended status.
ms.assetid: 15333cd3-e71a-451c-ae93-9e217ea0895c
title: FaxIncomingJob.ExtendedStatusCode property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.ExtendedStatusCode property

The **ExtendedStatusCode** property specifies a code describing the job's extended status.

This property is read-only.

## Syntax


```VB
Property ExtendedStatusCode As Long
```



## Property value

A **Long** that receives the extended job status. For more information, see [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_job_extended_status_enum).

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

[**get\_ExtendedStatusCode**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxincomingjob-get_extendedstatuscode)
</dt> </dl>

 

 




