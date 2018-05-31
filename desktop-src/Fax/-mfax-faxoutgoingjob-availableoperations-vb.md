---
Description: The AvailableOperations property indicates the combination of valid operations that you can perform on the fax job, given its current status.
ms.assetid: fedabd5c-1ee1-4ed7-aaa8-06dd818f21f1
title: FaxOutgoingJob.AvailableOperations property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.AvailableOperations property

The **AvailableOperations** property indicates the combination of valid operations that you can perform on the fax job, given its current status.

This property is read-only.

## Syntax


```VB
Property AvailableOperations As Integer
```



## Property value

A value from the [**FAX\_JOB\_OPERATIONS\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_job_operations_enum) enumeration, which specifies a bitwise combination of the operations that you can currently perform on the fax job. This is because some operations are mutually exclusive; for example, you cannot pause a job that has already been paused. For more information, see **FAX\_JOB\_OPERATIONS\_ENUM**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outgoing-jobs.md)
</dt> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob)
</dt> </dl>

 

 




