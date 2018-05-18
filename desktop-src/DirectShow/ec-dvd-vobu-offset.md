---
Description: 'Sent when the DVD Navigator parses a PCI packet.'
ms.assetid: 'e2e65007-7c34-4be4-86b9-9491061891e5'
title: 'EC\_DVD\_VOBU\_Offset'
---

# EC\_DVD\_VOBU\_Offset

Sent when the [DVD Navigator](dvd-navigator-filter.md) parses a PCI packet.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

The block offset of the most recent video object unit (VOBU).

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

The current video title set number (VTSN).

</dd> </dl>

## Remarks

This event is disabled by default. To enable this event, call [**IDvdControl2::SetOption**](idvdcontrol2-setoption.md) and set the **DVD\_EnableLoggingEvents** option to **TRUE**.

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
</dt> </dl>

 

 




