---
description: About the Multimedia Streaming Architecture
ms.assetid: 185c7012-968a-4d9c-9baa-4d20f953068b
title: About the Multimedia Streaming Architecture
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Multimedia Streaming Architecture

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

This article describes the architecture of Multimedia Streaming. It contains the following sections.

-   [Advantages of Multimedia Streaming](advantages-of-multimedia-streaming.md)
-   [Multimedia Streaming Object and Interface Hierarchy](multimedia-streaming-object-and-interface-hierarchy.md)
-   [Creating Multimedia Stream Objects and Stream Samples](creating-multimedia-stream-objects-and-stream-samples.md)
-   [Using Multimedia Streams in Applications](using-multimedia-streams-in-applications.md)
-   [Sharing Data Between Streams](sharing-data-between-streams.md)

## Related topics

<dl> <dt>

[Multimedia Streaming](multimedia-streaming.md)
</dt> </dl>

 

 



