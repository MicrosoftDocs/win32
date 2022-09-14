---
description: The filter graph is shutting down, prior to being destroyed.
ms.assetid: f1b3fc87-16ec-485b-b659-fc7d975c4a22
title: EC_SHUTTING_DOWN (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_SHUTTING\_DOWN

The filter graph is shutting down, prior to being destroyed.

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

## Default Action

This event is not sent to the application. The filter graph manager sends it to plug-in distributors, to notify them that the graph is shutting down. Applications cannot override the default action of this event.

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

 

 




