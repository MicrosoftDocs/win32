---
Description: The ExtendedStatusCode property specifies a code describing the job's extended status.
ms.assetid: c04e6dc4-cf1f-4b9c-89c6-b170cb84296a
title: FaxJobStatus.ExtendedStatusCode property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.ExtendedStatusCode property

The **ExtendedStatusCode** property specifies a code describing the job's extended status.

This property is read-only.

## Syntax


```VB
Property ExtendedStatusCode As Integer
```



## Property value

A variable of type [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_job_extended_status_enum) that receives the extended job status. For more information, see **FAX\_JOB\_EXTENDED\_STATUS\_ENUM**.

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

[**IFaxJobStatus**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxjobstatus)
</dt> </dl>

 

 




