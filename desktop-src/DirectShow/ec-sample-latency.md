---
description: Specifies how far behind schedule a component is for processing samples.
ms.assetid: 8bd202fb-3015-41a2-ad14-862f64cb252f
title: EC_SAMPLE_LATENCY (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_SAMPLE\_LATENCY

Specifies how far behind schedule a component is for processing samples.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**const REFERENCE\_TIME**\*) How far behind the component is, in 100-nanosecond units. If this value is positive, the component is behind schedule. If this value is negative, the component is ahead of schedule.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

None.

## Remarks

A custom presenter for the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) filter can send this message to the EVR, to notify the EVR whether the presenter is behind schedule or ahead of schedule.

The simplest way to calculate *lParam1* is: *QPC now*   *QPC target*, where *QPC now* is the clock time now, and *QPC target* is the presentation time.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[How to Write an EVR Presenter](/windows/desktop/medfound/how-to-write-an-evr-presenter)
</dt> </dl>

 

