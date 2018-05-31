---
Description: Specifies the schedule type that was used for the transmission.
ms.assetid: c587aba4-aff6-4a19-90c5-aefb55df2fbb
title: FaxOutgoingJob.ScheduleType property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.ScheduleType property

Specifies the schedule type that was used for the transmission.

This property is read-only.

## Syntax


```VB
Property ScheduleType As Integer
```



## Property value

A variable of type [**FAX\_SCHEDULE\_TYPE\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_schedule_type_enum) that receives a value that specifies the schedule type.

## Remarks

This property can indicate the following: the fax should be transmitted right away, that it should be sent at a specified time, or that it should be sent during a period of discounted rates.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob2)
</dt> </dl>

 

 




