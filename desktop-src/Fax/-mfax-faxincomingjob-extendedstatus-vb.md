---
Description: The ExtendedStatus property is a null-terminated string that describes the jobs extended status.
ms.assetid: 679a6fa2-5499-4720-92cb-16eb76a7465b
title: FaxIncomingJob.ExtendedStatus property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingJob.ExtendedStatus property

The **ExtendedStatus** property is a null-terminated string that describes the job's extended status.

This property is read-only.

## Syntax


```VB
Property ExtendedStatus As String
```



## Property value

A **String** that receives a description of the job's extended status. For more information, see [**FAX\_JOB\_EXTENDED\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_extended_status_enum?branch=master).

## Remarks

The **ExtendedStatus** property can have a value only if the fax service provider (FSP) returns a proprietary status code in the [**ExtendedStatusCode**](-mfax-faxincomingjob-extendedstatuscode.md) property. Otherwise, the **ExtendedStatus** property will contain an empty string.

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

[**IFaxIncomingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingjob?branch=master)
</dt> </dl>

 

 




