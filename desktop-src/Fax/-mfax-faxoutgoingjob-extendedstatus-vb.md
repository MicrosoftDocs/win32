---
Description: The ExtendedStatus property is a null-terminated string that describes the jobs extended status.
ms.assetid: 3a642a78-e656-41e0-afb5-b03bcd5fa066
title: FaxOutgoingJob.ExtendedStatus property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJob.ExtendedStatus property

The **ExtendedStatus** property is a null-terminated string that describes the job's extended status.

This property is read-only.

## Syntax


```VB
Property ExtendedStatus As String
```



## Property value

A **String** that receives a description of the job's extended status. For more information, see [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_extended_status_enum?branch=master).

## Remarks

The **ExtendedStatus** property can have a value only if the fax service provider (FSP) returns a proprietary status code in the [**ExtendedStatusCode**](-mfax-faxoutgoingjob-extendedstatuscode-vb.md) property. Otherwise, the **ExtendedStatus** property will contain an empty string. Similarly, an FSP may choose not to provide values for the **ExtendedStatus** property, and the property will thus contain an empty string. This is the case for the T.30 FSP provided with the fax service.

If an FSP provides a proprietary status code, the service loads the code string from the FSP, and passes both the string and the original status code to the client. If the FSP provides a status defined in [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_extended_status_enum?branch=master), the service passes only the status code to the client.

A fax client application should check the extended status string first. If the string is not **NULL**/empty, it describes the extended status, and the extended status code is the same code that the FSP passed to the fax service. If the string is **NULL**/empty, the extended status code is one of those defined in [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_extended_status_enum?branch=master).

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

 

 




