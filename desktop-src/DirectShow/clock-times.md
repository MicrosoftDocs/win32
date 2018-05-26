---
Description: Clock Times
ms.assetid: ff964f7f-a084-4de3-8b2b-8efb6c9f4a9f
title: Clock Times
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Clock Times

DirectShow defines two related clock times: reference time and stream time.

-   *Reference time* is the absolute time returned by the reference clock. (See [Reference Clocks](reference-clocks.md).)
-   *Stream time* is defined relative to when the graph last started running.
    -   While the graph is running, stream time equals reference time minus start time.
    -   While the graph is paused, stream time remains at the stream time when it was paused.
    -   After a seek operation, stream time resets to zero.
    -   While the graph is stopped, stream time is undefined.

When a media sample has a time stamp *t*, it means the sample should be rendered at stream time *t*. For this reason, stream time is also called *presentation time*.

When an application calls [**IMediaControl::Run**](/windows/win32/Control/nf-control-imediacontrol-run?branch=master) to run the filter graph, the Filter Graph Manager calls [**IMediaFilter::Run**](/windows/win32/Strmif/nf-strmif-imediafilter-run?branch=master) on each filter. To compensate for the slight amount of time it takes for the filters to start running, the Filter Graph Manager specifies a start time slightly in the future.

## Related topics

<dl> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> <dt>

[Time Stamps](time-stamps.md)
</dt> </dl>

 

 



