---
Description: Sent when the value of a general parameter register (GPRM) changes.
ms.assetid: 3e0c400e-9ea5-458c-9eca-97d66a440590
title: EC\_DVD\_GPRM\_Change
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_DVD\_GPRM\_Change

Sent when the value of a general parameter register (GPRM) changes.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

The zero-based index of the GPRM value that changed.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

The lower 16 bits contains the new GPRM value.

</dd> </dl>

## Remarks

This event is disabled by default. To enable this event, call [**IDvdControl2::SetOption**](/windows/win32/Strmif/nf-strmif-idvdcontrol2-setoption?branch=master) and set the **DVD\_EnableLoggingEvents** option to **TRUE**.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdevcode.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> <dt>

[DVD Event Notification Codes](dvd-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> <dt>

[**IDvdInfo2::GetAllGPRMs**](/windows/win32/Strmif/nf-strmif-idvdinfo2-getallgprms?branch=master)
</dt> </dl>

 

 




