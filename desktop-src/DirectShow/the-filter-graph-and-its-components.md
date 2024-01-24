---
description: The Filter Graph and Its Components
ms.assetid: 3747bfcd-1e4a-404c-a493-26d3c20bab21
title: The Filter Graph and Its Components
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The Filter Graph and Its Components

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article describes the major components of DirectShow. It is intended as an introduction for application developers and for developers writing custom DirectShow filters. Application developers can usually ignore many of the low-level details of DirectShow. However, it is still a good idea to read this section, to have a general understanding of the DirectShow architecture.

This article contains the following sections:

-   [About DirectShow Filters](about-directshow-filters.md)
-   [About the Filter Graph Manager](about-the-filter-graph-manager.md)
-   [About Media Types](about-media-types.md)
-   [About Media Samples and Allocators](about-media-samples-and-allocators.md)
-   [How Hardware Devices Participate in the Filter Graph](how-hardware-devices-participate-in-the-filter-graph.md)

 

 



