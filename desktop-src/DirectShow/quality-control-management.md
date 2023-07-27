---
description: Quality-Control Management
ms.assetid: b1def588-6c9c-4853-a69b-1ba5df8b5ba2
title: Quality-Control Management
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Quality-Control Management

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Quality control is a mechanism for adjusting the rate of data flow through the filter graph in response to run-time performance. If a renderer filter is receiving too much data or too little data, it can send a *quality message*. The quality message requests an adjustment in the data rate. By default, quality messages travel upstream from the renderer until they reach a filter that can respond (if any). An application can also implement a custom quality manager. In that case, the renderer passes quality messages directly to the application's quality manager.

This article contains the following topics.

-   [Quality Messages](quality-messages.md)
-   [Default Quality Control](default-quality-control.md)

## Related topics

<dl> <dt>

[Data Flow for Filter Developers](data-flow-for-filter-developers.md)
</dt> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



