---
description: All data from a particular stream has been rendered.
ms.assetid: 46037d53-085d-4fd0-91a0-408702cbfce5
title: EC_COMPLETE (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC\_COMPLETE

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

All data from a particular stream has been rendered.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**HRESULT**) Status of the stream on completion. If no errors occurred during playback, the value is S\_OK.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

(**IUnknown**\*) Zero, or a pointer to the renderer's [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface.

</dd> </dl>

## Default Action

By default, the filter graph manager does not forward this event to the application. However, after all the streams in the graph report **EC\_COMPLETE**, the filter graph manager posts a separate **EC\_COMPLETE** event to the application.

If the default action is disabled for this event, the application receives all of the **EC\_COMPLETE** events from the renderers.

## Remarks

A renderer filter sends this event when it receives an end-of-stream notice. (End-of-stream is signaled through the [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) method.) The filter sends exactly one **EC\_COMPLETE** event for each stream. The filter must process any pending samples before it sends the event. Stopping a renderer resets any end-of-stream state that was cached.

If the renderer is paused, it does not send **EC\_COMPLETE** until the [**IMediaFilter::Run**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-run) method is called. Furthermore, it continues to send **EC\_COMPLETE** events for each transition from pause to run, until the filter is either stopped or flushed.

Filters set the *lParam2* parameter to an [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) pointer. If the default action is enabled, the filter graph manager sets this parameter to zero.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> <dt>

[Alternative Video Renderers](alternative-video-renderers.md)
</dt> </dl>

 

 




