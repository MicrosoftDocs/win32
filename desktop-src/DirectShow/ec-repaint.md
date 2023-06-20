---
description: A video renderer requires a repaint.
ms.assetid: 2e756dea-366c-4024-8fc8-6feabaef1954
title: EC_REPAINT (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC\_REPAINT

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A video renderer requires a repaint.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**IUnknown**\*) Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface of the video renderer's input pin, or **NULL**.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

The *lParam1* parameter might specify the video renderer's input pin. If so, the filter graph manager finds the output pin connected to that pin and queries it for the [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink) interface. If the output pin supports **IMediaEventSink**, the filter graph manager calls [**IMediaEventSink::Notify**](/windows/desktop/api/Strmif/nf-strmif-imediaeventsink-notify) with the EC\_REPAINT event code. This gives the upstream filter the opportunity to re-send the last sample.

If *lParam1* is **NULL**, or if the pin does not support [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink), or if the [**Notify**](/windows/desktop/api/Strmif/nf-strmif-imediaeventsink-notify) method fails, the filter graph manager handles the EC\_REPAINT event by itself. Its behavior depends on the state of the graph:

-   Running: Ignores the event. (The renderer will receive the next sample in the stream.)
-   Paused: Seeks the graph to its current location, thereby flushing the filter and re-queuing the data.
-   Stopped: Pauses and stops the graph, thereby re-queuing the data.

By default, the filter graph manager does not pass this event to the application.

## Remarks

Video renderers send this message when they receive a [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message and have no data to display.

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

 

