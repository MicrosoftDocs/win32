---
description: The end of a segment was reached.
ms.assetid: 07f141b1-2e96-49e2-9cf7-581690e245b5
title: EC_END_OF_SEGMENT (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_END\_OF\_SEGMENT

The end of a segment was reached.

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

The filter graph manager checks the number of **EC\_END\_OF\_SEGMENT** events against the number of [**EC\_SEGMENT\_STARTED**](ec-segment-started.md) events. If they match, it forwards the **EC\_END\_OF\_SEGMENT** event to the application. Applications cannot override the default action for this event.

## Remarks

This event code supports seamless looping. When a call to the [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions) method includes the AM\_SEEKING\_Segment flag, the source filter sends this event code instead of calling [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream).

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

 

 




