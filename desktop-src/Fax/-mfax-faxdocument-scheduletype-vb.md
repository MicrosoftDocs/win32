---
Description: 'The ScheduleType property indicates when to schedule the fax job; for example, you can specify that the fax service send the fax immediately, at a specified time, or during a predefined discount period.'
ms.assetid: 'e65030e2-850a-40e2-9a5f-f205c896e86d'
title: 'FaxDocument.ScheduleType property'
---

# FaxDocument.ScheduleType property

The **ScheduleType** property indicates when to schedule the fax job; for example, you can specify that the fax service send the fax immediately, at a specified time, or during a predefined discount period.

This property is read/write.

## Syntax


```VB
Property ScheduleType As Integer
```



## Property value

A variable of type [**FAX\_SCHEDULE\_TYPE\_ENUM**](-mfax-fax-schedule-type-enum.md) that specifies or receives the schedule type. For possible values, see **FAX\_SCHEDULE\_TYPE\_ENUM**.

## Remarks

By default, **ScheduleType** is set to 0, indicating that the fax will be sent as soon as the device is available.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](-mfax-faxdocument-cpp.md)
</dt> </dl>

 

 




