---
Description: The AvailableOperations property indicates the combination of valid operations that you can perform on the fax job, given its current status.
ms.assetid: 04149d5c-e26f-4cef-9ae0-eba2a199ec51
title: FaxIncomingJob.AvailableOperations property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.AvailableOperations property

The **AvailableOperations** property indicates the combination of valid operations that you can perform on the fax job, given its current status.

This property is read-only.

## Syntax


```VB
Property AvailableOperations As Long
```



## Property value

A **Long** that receives a bitwise combination of the operations that you can currently perform on the fax job. Some operations are mutually exclusive. For example, you cannot pause a job that has already been paused. For more information, see [**FAX\_JOB\_OPERATIONS\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_job_operations_enum).

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

[**get\_AvailableOperations**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxincomingjob-get_availableoperations)
</dt> </dl>

 

 




