---
description: A filter is requesting that the graph be restarted.
ms.assetid: 58f17338-dd60-4b77-80d3-b6b6a76af9b2
title: EC_NEED_RESTART (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_NEED\_RESTART

A filter is requesting that the graph be restarted.

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

The filter graph manager pauses and restarts the graph. It does not pass the event to the application.

## Remarks

If a filter rejects a sample in the middle of a stream, the upstream pin will stop delivering samples. The filter can restart the stream by sending this event. For example, the audio renderer might lose access to the sound device, because a video window has lost focus. At that point, the audio renderer starts rejecting samples. When it regains access to the sound device, it sends this event to restart the audio stream.

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

 

 




