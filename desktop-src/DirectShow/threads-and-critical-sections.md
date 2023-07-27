---
description: Threads and Critical Sections
ms.assetid: e55acb06-03f4-4191-bffe-3196f41ef2c7
title: Threads and Critical Sections
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Threads and Critical Sections

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes threading in DirectShow filters, and the steps you should take to avoid crashes or deadlocks in a custom filter.

The examples in this section use pseudocode to illustrate the code you will need to write. They assume that a custom filter is using classes derived from the DirectShow base classes, as follows:

-   CMyInputPin: Derived from [**CBaseInputPin**](cbaseinputpin.md).
-   CMyOutputPin: Derived from [**CBaseOutputPin**](cbaseoutputpin.md).
-   CMyFilter: Derived from [**CBaseFilter**](cbasefilter.md).
-   CMyInputAllocator: The input pin's allocator, derived from [**CMemAllocator**](cmemallocator.md). Not every filter needs a custom allocator. For many filters, the **CMemAllocator** class is sufficient.

This section contains the following topics.

-   [The Streaming and Application Threads](the-streaming-and-application-threads.md)
-   [Pausing](pausing.md)
-   [Receiving and Delivering Samples](receiving-and-delivering-samples.md)
-   [Delivering the End of Stream](delivering-the-end-of-stream.md)
-   [Flushing Data](flushing-data.md)
-   [Stopping](stopping.md)
-   [Getting Buffers](getting-buffers.md)
-   [Streaming Threads and the Filter Graph Manager](streaming-threads-and-the-filter-graph-manager.md)
-   [Summary of Filter Threading](summary-of-filter-threading.md)

## Related topics

<dl> <dt>

[Data Flow for Filter Developers](data-flow-for-filter-developers.md)
</dt> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



