---
description: The graph is dropping samples, for quality control.
ms.assetid: a21fe766-58a5-4851-a282-883374287e18
title: EC_QUALITY_CHANGE (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_QUALITY\_CHANGE

The graph is dropping samples, for quality control.

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

None.

## Remarks

A filter sends this event if it drops samples in response to a quality control message. It sends the event only when it adjusts the quality level, not for each sample that it drops. For more information, see [Quality-Control Management](quality-control-management.md).

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

 

 




