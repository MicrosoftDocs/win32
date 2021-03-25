---
description: Sent by the DVD Navigator when it needs to skip frames.
ms.assetid: 252ffbcc-e81a-499d-9dd2-170be01f7ce1
title: EC_SKIP_FRAMES (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_SKIP\_FRAMES

Sent by the DVD Navigator when it needs to skip frames.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Number of frames to skip.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Reserved.

</dd> </dl>

## Default Action

This event is not sent to the application. Applications cannot override the default action of this event.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




