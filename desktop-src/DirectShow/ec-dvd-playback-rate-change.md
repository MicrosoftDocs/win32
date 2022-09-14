---
description: Signals that a rate change in DVD playback has been initiated.
ms.assetid: 2a1e3c21-1623-4e43-8c7b-1a34514442c9
title: EC_DVD_PLAYBACK_RATE_CHANGE (Dvdevcode.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_PLAYBACK_RATE_CHANGE
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
---

# EC\_DVD\_PLAYBACK\_RATE\_CHANGE

Signals that a rate change in DVD playback has been initiated.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

LONG indicating the new playback rate. The value is the actual playback rate multiplied by 10,000, so the playback rate equals 10000.0 / *lParam1*. Values less than zero indicate reverse playback mode, and values greater than zero indicate forward playback mode.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Remarks

This event is raised in the title domain.

Playback *rate* is the inverse of playback *speed*. For example, if playback speed is 2x, the rate is 0.5.

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
</dt> </dl>

 

 




