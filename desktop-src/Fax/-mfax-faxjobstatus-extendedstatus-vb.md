---
Description: The ExtendedStatus property is a null-terminated string that describes the job's extended status.
ms.assetid: f57912d7-6269-4359-af27-e1056caa3c4e
title: FaxJobStatus.ExtendedStatus property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.ExtendedStatus property

The **ExtendedStatus** property is a null-terminated string that describes the job's extended status.

This property is read-only.

## Syntax


```VB
Property ExtendedStatus As String
```



## Property value

A **String** that receives the job's extended status. For more information, see [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](-mfax-fax-job-extended-status-enum.md).

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

 

 




