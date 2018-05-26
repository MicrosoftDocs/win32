---
Description: The Status property is a number that indicates the current status of an inbound fax job in the job queue.
ms.assetid: fd84a3b4-a7ce-400c-a8a9-8134d7308bef
title: FaxIncomingJob.Status property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingJob.Status property

The **Status** property is a number that indicates the current status of an inbound fax job in the job queue.

This property is read-only.

## Syntax


```VB
Property Status As Long
```



## Property value

A **Long** that receives the current status of an inbound fax job in the job queue. For more information, see [**FAX\_JOB\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_status_enum?branch=master).

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

[**get\_Status**](/windows/previous-versions/FaxComex/nf-faxcomex-ifaxincomingjob-get_status?branch=master)
</dt> </dl>

 

 




