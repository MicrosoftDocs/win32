---
description: Multimedia Streaming Sample Code
ms.assetid: 3fe2996b-b4de-40ad-bd02-d850a45f3a2c
title: Multimedia Streaming Sample Code
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Multimedia Streaming Sample Code

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

This article provides sample code that implements the multimedia streaming interfaces. The video streaming sample code demonstrates how to read a file and render it to a primary Microsoft® DirectDraw® surface. For brevity, this code contains no error checking.

The second code sample demonstrates how to use the audio streaming interfaces to stream audio data.

This article contains the following sections.

-   [Video Streaming Sample Code](video-streaming-sample-code.md)
-   [Audio Streaming Sample Code](audio-streaming-sample-code.md)

 

 



