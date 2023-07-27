---
description: Data Flow in the Filter Graph
ms.assetid: 3fcfd874-39bc-42d2-9fc9-2d8945ffa8e3
title: Data Flow in the Filter Graph
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Data Flow in the Filter Graph

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how media data moves through the filter graph. Usually, you do not need to know these details to write a DirectShow application, although in some situations you may find it helpful. If you are writing a DirectShow filter, you will need to understand this material.

This section contains the following topics:

-   [Overview of Data Flow in DirectShow](overview-of-data-flow-in-directshow.md)
-   [Transports](transports.md)
-   [Samples and Allocators](samples-and-allocators.md)
-   [Filter States](filter-states.md)
-   [Pull Model](pull-model.md)

## Related topics

<dl> <dt>

[Data Flow for Filter Developers](data-flow-for-filter-developers.md)
</dt> </dl>

 

 



