---
Description: 'Indicates that the Navigator has finished playing the segment specified in a call to IDvdControl2::PlayPeriodInTitleAutoStop.'
ms.assetid: '1716eabe-f106-436a-8a6a-ca43cee9341c'
title: 'EC\_DVD\_PLAYPERIOD\_AUTOSTOP'
---

# EC\_DVD\_PLAYPERIOD\_AUTOSTOP

Indicates that the Navigator has finished playing the segment specified in a call to [**IDvdControl2::PlayPeriodInTitleAutoStop**](idvdcontrol2-playperiodintitleautostop.md).

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Zero.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Remarks

This event is raised in the Title domain.

This event is also sent when playback is canceled before the Navigator finishes playing the specified segment.

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

[**IDvdControl2::PlayPeriodInTitleAutoStop**](idvdcontrol2-playperiodintitleautostop.md)
</dt> </dl>

 

 




