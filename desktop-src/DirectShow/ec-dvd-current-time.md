---
Description: 'Signals the beginning of every video object unit (VOBU), a video segment which is 0.4 to 1.0 seconds in length.'
ms.assetid: '1f2def2f-3a6b-458b-b564-09b6cf74543c'
title: 'EC\_DVD\_CURRENT\_TIME'
---

# EC\_DVD\_CURRENT\_TIME

Signals the beginning of every video object unit (VOBU), a video segment which is 0.4 to 1.0 seconds in length.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the current playback timecode in a binary coded decimal (BCD) hours, minutes, seconds, frames (HH:MM:SS:FF) format. Member of the [**DVD\_TIMECODE**](dvd-timecode.md) structure.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Boolean (**BOOL**) value indicating the timecode. Zero (0) indicates 25 frames per second while 1 indicates 30 frames per second (nondropped). A value of 2 indicates the playback time cannot be determined.

</dd> </dl>

## Remarks

Only simple linear movies signal this event.

This event is raised in the title domain.

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

 

 




