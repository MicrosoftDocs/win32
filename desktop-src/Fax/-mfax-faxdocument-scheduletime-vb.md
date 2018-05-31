---
Description: The ScheduleTime property indicates the time to submit the fax for processing to the fax service.
ms.assetid: 5c86118c-c20b-4602-b195-a5cfc585ff68
title: FaxDocument.ScheduleTime property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.ScheduleTime property

The **ScheduleTime** property indicates the time to submit the fax for processing to the fax service.

This property is read/write.

## Syntax


```VB
Property ScheduleTime As Date
```



## Property value

A **Date** that specifies or receives the hour and minute, expressed in UTC, when the discount period for transmitting faxes ends. **Date** is an 8-byte floating-point number. For more information about the [DATE](http://msdn.microsoft.com/library/en-us/vccore/html/_core_The_DATE_Type.asp) data type, see the Microsoft Visual C++ Programmer's Guide.

## Remarks

If the time specified has passed, the fax service sends the fax as soon as a device is available. By default, **ScheduleTime** is set to zero, meaning that no time is specified.

Note that the fax service ignores this parameter unless you set the [**ScheduleType**](-mfax-faxdocument-scheduletype-vb.md) property to [****fstSpecific\_TIME****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_schedule_type_enum).

> [!Note]  
> The value of the **ScheduleTime** property must include the date and time for submitting the fax.

 

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

[**IFaxDocument**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdocument)
</dt> </dl>

 

 




