---
description: Writing Video Renderers
ms.assetid: 61dfff97-86b2-4d75-ac1c-a69b1dbde02a
title: Writing Video Renderers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing Video Renderers

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to write and use video renderers, both full-screen and custom renderers. It discusses how and why to support a full-screen renderer, and how to handle notifications, state changes, and dynamic format changes in a custom renderer.

This section contains the following topics.

-   [Alternative Video Renderers](alternative-video-renderers.md)
-   [Source and Target Rectangles in Video Renderers](source-and-target-rectangles-in-video-renderers.md)

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



