---
description: Signals that a DVD menu button has been automatically activated per instructions on the disc. This occurs when a menu times out and the disc has specified a button to be automatically activated.
ms.assetid: ecd79c2a-1717-473d-b111-2b1db2ca4cc1
title: EC_DVD_BUTTON_AUTO_ACTIVATED (Dvdevcode.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_BUTTON_AUTO_ACTIVATED
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
---

# EC\_DVD\_BUTTON\_AUTO\_ACTIVATED

Signals that a DVD menu button has been automatically activated per instructions on the disc. This occurs when a menu times out and the disc has specified a button to be automatically activated.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the button that was activated.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

This event is raised in all domains.

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

 

 




