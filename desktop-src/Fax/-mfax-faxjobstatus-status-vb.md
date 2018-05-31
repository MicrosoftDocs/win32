---
Description: The Status property is a number that indicates the current status of fax job in the job queue.
ms.assetid: 4f9eb2dc-a2be-4d40-9f57-26a9bda61826
title: FaxJobStatus.Status property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.Status property

The **Status** property is a number that indicates the current status of fax job in the job queue.

This property is read-only.

## Syntax


```VB
Property Status As Integer
```



## Property value

A variable of type [**FAX\_JOB\_STATUS\_ENUM**](-mfax-fax-job-status-enum.md) that receives the current status of a fax job in the job queue. For more information, see **FAX\_JOB\_STATUS\_ENUM**.

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

 

 




