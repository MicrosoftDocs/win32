---
description: A filter is not receiving enough data.
ms.assetid: c9cdfe46-02bb-4ea9-ac58-7d63e03c26d8
title: EC_STARVATION (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_STARVATION

A filter is not receiving enough data.

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

The event is not sent to the application. If the filter graph is running, the filter graph manager pauses the graph and waits for the pause to complete. Then it runs the graph again. The filter sending the event should not complete its transition to paused until it has enough data to resume. If the filter graph is not running, the filter graph manager ignores this event.

## Remarks

A parser or source filter can send this event if too little data is arriving.

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

 

 




