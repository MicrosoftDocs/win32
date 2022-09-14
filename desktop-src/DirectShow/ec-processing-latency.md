---
description: Indicates the amount of time that a component is taking to process each sample.
ms.assetid: 84f81ee1-76d8-46fb-86ef-2500f8f4ef36
title: EC_PROCESSING_LATENCY (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_PROCESSING\_LATENCY

Indicates the amount of time that a component is taking to process each sample.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**const REFERENCE\_TIME**\*) The amount of time to process each sample, in 100-nanosecond units.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

None.

## Remarks

A presenter for the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) filter can send this message to the EVR to notify the EVR about the presenter's processing latency.

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

 

 




