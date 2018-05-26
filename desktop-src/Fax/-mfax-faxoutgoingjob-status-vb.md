---
Description: The Status property is a number that indicates the current status of an outbound fax job in the job queue.
ms.assetid: b1c31f68-dc4a-4cab-9e1b-3a9767f3ae38
title: FaxOutgoingJob.Status property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJob.Status property

The **Status** property is a number that indicates the current status of an outbound fax job in the job queue.

This property is read-only.

## Syntax


```VB
Property Status As Integer
```



## Property value

Value from the [**FAX\_JOB\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_status_enum?branch=master) enumeration that specifies the current status of an outbound fax job in the job queue.

## Remarks

For more information, see [**FAX\_JOB\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_job_status_enum?branch=master).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingjob?branch=master)
</dt> </dl>

 

 




