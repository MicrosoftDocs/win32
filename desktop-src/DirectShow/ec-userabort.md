---
description: The user has terminated playback.
ms.assetid: 974a9c3e-cfc9-4608-9f98-732aeaa0a752
title: EC_USERABORT (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_USERABORT

The user has terminated playback.

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

None. The application must decide whether to stop the graph.

## Remarks

This event code signals that the user has terminated normal graph playback. For example, video renderers send this event if the user closes the video window.

After sending this event, the filter should reject all samples and not send any [**EC\_REPAINT**](ec-repaint.md) events, until the filter stops and is reset.

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

 

 




