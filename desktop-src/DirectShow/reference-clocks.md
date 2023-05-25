---
description: Reference Clocks
ms.assetid: 43f1a4d6-dbed-4940-a301-d863ddd34bce
title: Reference Clocks
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reference Clocks

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

One function of the Filter Graph Manager is to synchronize all of the filters in the graph to the same clock, called the *reference clock*.

Any object that exposes the [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock) interface can act as the reference clock. The reference clock might be provided by a DirectShow filter—typically the audio renderer, which has access to a hardware timer. As a fallback, the Filter Graph Manager can use the system time.

Nominally, a reference clock measures time in 100-nanosecond intervals, although the actual accuracy of the clock might be less. To retrieve the clock's current time, call the [**IReferenceClock::GetTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-gettime) method. The clock's baseline—the time from which it starts counting—depends on the implementation, so the value returned by **GetTime** is not inherently meaningful. What matters is the delta from when the graph started running.

Although the accuracy of a reference clock can vary, the times returned by the [**GetTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-gettime) method are guaranteed to increase monotonically. In other words, clock times will never go backward. If a reference clock is generating clock times from a hardware source and the hardware clock jumps backward (for example, if there is an adjustment to the clock), the **GetTime** method should continue to return the last reported time until the hardware clock catches up. For more information, see [**CBaseReferenceClock Class**](cbasereferenceclock.md).

**Default Reference Clock**

The Filter Graph Manager automatically selects a reference clock when the graph runs. It uses the following algorithm to select the clock:

-   If the application has selected a clock (see below), use that clock.
-   If the graph contains a live source filter that supports [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock), use that filter. For the definition of a live source, see [Live Sources](live-sources.md).
-   If the graph does NOT contain any live source filters, use any filter in the graph that supports [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock), starting from the renderers and working upstream. Prefer connected filters over unconnected filters. (If the graph is rendering an audio stream, this step in the algorithm will normally select the audio renderer filter.)
-   If no filter provides a suitable clock, use the [System Reference Clock](system-reference-clock.md), which is based on the system time.

**Setting the Reference Clock**

An application can select a clock by calling the [**IMediaFilter::SetSyncSource**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-setsyncsource) method on the Filter Graph Manager. You should do this only if you have a particular reason to prefer another clock.

You can instruct the Filter Graph Manager not to use a reference clock by calling [**SetSyncSource**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-setsyncsource) with the value **NULL**. For example, you might do this to process samples as quickly as possible. To restore the default reference clock, call the [**IFilterGraph::SetDefaultSyncSource**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-setdefaultsyncsource) method on the Filter Graph Manager.

Whenever the reference clock changes, the Filter Graph Manager notifies each filter by calling its [**IMediaFilter::SetSyncSource**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-setsyncsource) method. Applications should never call this method on filters.

## Related topics

<dl> <dt>

[Setting the Graph Clock](setting-the-graph-clock.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



