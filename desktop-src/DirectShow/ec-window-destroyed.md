---
description: The video renderer was destroyed or removed from the graph.
ms.assetid: facf35c2-d6a2-4373-bce5-171fd9325116
title: EC_WINDOW_DESTROYED (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC\_WINDOW\_DESTROYED

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The video renderer was destroyed or removed from the graph.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**IUnknown**\*) Pointer to the video renderer's [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

The filter graph manager releases this window as the focus, through the [**IResourceManager**](/windows/desktop/api/Strmif/nn-strmif-iresourcemanager) interface. It does not send the event notification to the application.

## Remarks

The video renderer sends this event when it leaves the filter graph, in its [**IBaseFilter::JoinFilterGraph**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-joinfiltergraph) method. (Sending the event when the filter is destroyed might be too late, because at that point the filter graph manager might also be destroyed.)

This event enables other filters to acquire resources that depend on window focus, such as audio devices.

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

 

 




