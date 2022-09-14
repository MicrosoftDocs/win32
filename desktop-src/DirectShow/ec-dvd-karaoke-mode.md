---
description: Indicates that the DVD Navigator has either begun playing or finished playing karaoke data.
ms.assetid: 910bf809-a56a-4d02-9c7e-429769a4ec2b
title: EC_DVD_KARAOKE_MODE (Dvdevcode.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_KARAOKE_MODE
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
---

# EC\_DVD\_KARAOKE\_MODE

Indicates that the [DVD Navigator](data-flow-in-the-dvd-navigator.md) has either begun playing or finished playing karaoke data.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Boolean value. If **TRUE**, a karaoke track is being played. Otherwise, no karaoke track is being played.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

The DVD player signals this event whenever it changes domains.

This event is raised in all DVD domains.

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

 

 




