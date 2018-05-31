---
Description: The Status property is a number that indicates the current status of an inbound fax job in the job queue.
ms.assetid: fd84a3b4-a7ce-400c-a8a9-8134d7308bef
title: FaxIncomingJob.Status property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.Status property

The **Status** property is a number that indicates the current status of an inbound fax job in the job queue.

This property is read-only.

## Syntax


```VB
Property Status As Long
```



## Property value

A **Long** that receives the current status of an inbound fax job in the job queue. For more information, see [**FAX\_JOB\_STATUS\_ENUM**](-mfax-fax-job-status-enum.md).

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

[**get\_Status**](-mfax-faxincomingjob-status-cpp.md)
</dt> </dl>

 

 




