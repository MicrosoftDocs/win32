---
description: Using the Video Mixing Renderer
ms.assetid: 3d0fdfac-ec7e-4e02-886b-2039c607dac7
title: Using the Video Mixing Renderer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Video Mixing Renderer

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In terms of both performance and breadth of features, the Video Mixing Renderer (VMR) filter represents the next generation in video rendering on the Windows platform. The VMR replaces the [Overlay Mixer](overlay-mixer-filter.md) and [Video Renderer](video-renderer-filter.md), and adds many new mixing features.

There are two versions of the VMR:

-   The VMR-7, which uses DirectDraw 7 for rendering.
-   The VMR-9, which uses Direct3D 9.

The VMR-7 is available on Windows XP and later, but is not available for redistribution. The VMR-9 is available for redistribution on all platforms supported by DirectX 9. The two VMR filters are very similar in their implementation and the interfaces that they expose.

The VMR-9 has its own CLSID and its own set of interfaces, structures and enumeration types which are not always identical to the corresponding data types for the VMR-7, due to the underlying differences between DirectDraw 7 and Direct3D 9. The VMR-9 interfaces all end with "9", for example **IVMRStreamConfig9**, and the structures and enumeration types all have "VMR9" in their name to distinguish them from the data types used with the VMR-7.

To ensure backward-compatibility, the VMR-9 is not the default renderer on any system. To use the VMR-9, you must explicitly add it to the filter graph using the [**IFilterGraph::AddFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-addfilter) method, and configure it before connecting it to any upstream filters.

This article contains the following sections. Except where noted, the information in these sections applies to both the VMR-7 and the VMR-9 filters.

-   [About the Video Mixing Render](about-the-video-mixing-render.md)
-   [VMR Modes of Operation](vmr-modes-of-operation.md)
-   [Building a VMR-9 Filter Graph](building-a-vmr-9-filter-graph.md)
-   [Using VMR Mixing Mode](using-vmr-mixing-mode.md)
-   [Setting Deinterlace Preferences](setting-deinterlace-preferences.md)
-   [Using the VMR for DirectShow Filter Developers](using-the-vmr-for-directshow-filter-developers.md)
-   [Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)

## Related topics

<dl> <dt>

[Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md)
</dt> <dt>

[Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md)
</dt> </dl>

 

 



