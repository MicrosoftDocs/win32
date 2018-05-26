---
Description: Indicates the DVD players new domain.
ms.assetid: 4faa46d6-2ba2-44a3-b237-acac3b32f8b1
title: EC\_DVD\_DOMAIN\_CHANGE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_DVD\_DOMAIN\_CHANGE

Indicates the DVD player's new domain.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the new domain. Member of the [**DVD\_DOMAIN**](/windows/win32/strmif/ne-strmif-tagdvd_domain?branch=master) enumerated data type.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Remarks

The DVD player signals this event whenever it changes domains.

This event is raised in all DVD domains.

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

 

 




