---
description: Data Flow for Filter Developers
ms.assetid: cc7378c8-e268-4caa-98eb-6dc9c3b5bcad
title: Data Flow for Filter Developers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Data Flow for Filter Developers

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes in detail how data moves through the filter graph. It focuses on local memory transport using the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) or [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface. It is intended for developers who are writing their own custom filters. For a general introduction to how Microsoft DirectShow handles data flow, see [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md).

A lot of data moves through a filter graph. It falls roughly into two categories: media data and control data. In general, media data travels downstream and control data travels upstream. Media data includes the video frames, audio samples, MPEG packets, and so forth that make up a stream, but also includes flush commands, end-of-stream notifications, and other data that travels with the stream. Control data is not part of the media stream. Examples of control data are quality-control requests and seek commands.

This section contains the following articles.

-   [Delivering Samples](delivering-samples.md)
-   [Processing Data](processing-data.md)
-   [End-of-Stream Notifications](end-of-stream-notifications.md)
-   [New Segments](new-segments.md)
-   [Flushing](flushing.md)
-   [Seeking](seeking.md)
-   [Dynamic Format Changes](dynamic-format-changes.md)

## Related topics

<dl> <dt>

[Quality-Control Management](quality-control-management.md)
</dt> <dt>

[Threads and Critical Sections](threads-and-critical-sections.md)
</dt> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



