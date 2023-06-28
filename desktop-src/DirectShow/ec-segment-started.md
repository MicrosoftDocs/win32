---
description: A new segment has started.
ms.assetid: 9742436a-e233-4641-a0d5-aa240cde5f28
title: EC_SEGMENT_STARTED (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC\_SEGMENT\_STARTED

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A new segment has started.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**const** **REFERENCE\_TIME**\*) Pointer to a **REFERENCE\_TIME** value that specifies the accumulated stream time since the start of the segment, in 100-nanosecond units.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

(**DWORD**) Segment number (zero-based).

</dd> </dl>

## Default Action

This event is not sent to the application. Applications cannot override the default action for this event.

## Remarks

If a filter will send an [**EC\_END\_OF\_SEGMENT**](ec-end-of-segment.md) at the end of a segment, it sends this event at the start of the segment. The filter graph manager uses this event notification to compute how many EC\_END\_OF\_SEGMENT notifications it should expect at the end of the segment.

By default, filters do not send [**EC\_END\_OF\_SEGMENT**](ec-end-of-segment.md) events at the end of segments, and therefore should not send this event. For more information, see [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions).

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

 

 




