---
Description: The ExtendedStatusCode property specifies a code describing the jobs extended status.
ms.assetid: a044c855-d1ac-434c-83af-5b286cd1a9e9
title: FaxOutgoingJob.ExtendedStatusCode property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJob.ExtendedStatusCode property

The **ExtendedStatusCode** property specifies a code describing the job's extended status.

This property is read-only.

## Syntax


```VB
Property ExtendedStatusCode As Integer
```



## Property value

Value from the [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_extended_status_enum?branch=master) enumeration that specifies the job status.

## Remarks

If an fax service provider (FSP) provides a proprietary status code, the service loads the code string from the FSP, and passes both the string and the original status code to the client. If the FSP provides a status defined in [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_extended_status_enum?branch=master), the service passes only the status code to the client.

A fax client application should check the extended status string first. If the string is not **NULL**/empty, it describes the extended status, and the extended status code is the same code that the FSP passed to the fax service. If the string is **NULL**/Empty, the extended status code is one of those defined in [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_extended_status_enum?branch=master).

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

[**IFaxOutgoingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingjob?branch=master)
</dt> </dl>

 

 




