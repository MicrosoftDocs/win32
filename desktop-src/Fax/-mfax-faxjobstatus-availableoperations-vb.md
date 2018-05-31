---
Description: The AvailableOperations property indicates the combination of valid operations that you can perform on the fax job, given its current status.
ms.assetid: 4c7c1e98-c77b-47f4-9717-063e0e5a60a8
title: FaxJobStatus.AvailableOperations property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.AvailableOperations property

The **AvailableOperations** property indicates the combination of valid operations that you can perform on the fax job, given its current status.

This property is read-only.

## Syntax


```VB
Property AvailableOperations As Integer
```



## Property value

A variable of type [**FAX\_JOB\_OPERATIONS\_ENUM**](-mfax-fax-job-operations-enum.md) that receives a bitwise combination of the operations that you can currently perform on the fax job. This is because some operations are mutually exclusive; for example, you cannot pause a job that has already been paused. For more information, see **FAX\_JOB\_OPERATIONS\_ENUM**.

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

 

 




