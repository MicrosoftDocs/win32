---
description: Sent when the DVD Navigator processes a DVD navigation command.
ms.assetid: 95e502b6-330f-4bc7-8adc-851913987370
title: EC_DVD_NavigationCommand (Dvdevcode.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_NavigationCommand
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
---

# EC\_DVD\_NavigationCommand

Sent when the [DVD Navigator](dvd-navigator-filter.md) processes a DVD navigation command.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

The lower 32 bits of the raw navigation command.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

The upper 32 bits of the raw navigation command.

</dd> </dl>

## Remarks

This event is disabled by default. To enable this event, call [**IDvdControl2::SetOption**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-setoption) and set the **DVD\_EnableLoggingEvents** option to **TRUE**.

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

 

 




