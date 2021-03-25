---
description: Signals that the DVD player started playback of a new program in the DVD\_DOMAIN\_Title domain.
ms.assetid: c0745615-d527-4d93-9118-30419c6c811e
title: EC_DVD_CHAPTER_START (Dvdevcode.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_CHAPTER_START
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
---

# EC\_DVD\_CHAPTER\_START

Signals that the DVD player started playback of a new program in the DVD\_DOMAIN\_Title domain.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the new chapter (program) number.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Remarks

Only simple linear movies signal this event.

This event is raised in the title domain.

## Requirements



| Requirement | Value |
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

[**DVD\_DOMAIN Enumeration**](/windows/win32/api/strmif/ne-strmif-dvd_domain)
</dt> </dl>

 

 




