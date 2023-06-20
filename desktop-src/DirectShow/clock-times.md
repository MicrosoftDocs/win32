---
description: Clock Times
ms.assetid: ff964f7f-a084-4de3-8b2b-8efb6c9f4a9f
title: Clock Times
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Clock Times

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow defines two related clock times: reference time and stream time.

-   *Reference time* is the absolute time returned by the reference clock. (See [Reference Clocks](reference-clocks.md).)
-   *Stream time* is defined relative to when the graph last started running.
    -   While the graph is running, stream time equals reference time minus start time.
    -   While the graph is paused, stream time remains at the stream time when it was paused.
    -   After a seek operation, stream time resets to zero.
    -   While the graph is stopped, stream time is undefined.

When a media sample has a time stamp *t*, it means the sample should be rendered at stream time *t*. For this reason, stream time is also called *presentation time*.

When an application calls [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run) to run the filter graph, the Filter Graph Manager calls [**IMediaFilter::Run**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-run) on each filter. To compensate for the slight amount of time it takes for the filters to start running, the Filter Graph Manager specifies a start time slightly in the future.

## Related topics

<dl> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> <dt>

[Time Stamps](time-stamps.md)
</dt> </dl>

 

 



