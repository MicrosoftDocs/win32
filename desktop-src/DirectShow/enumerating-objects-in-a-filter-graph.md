---
description: Enumerating Objects in a Filter Graph
ms.assetid: 04a3dbc8-33c4-4b70-930e-686be2f8301f
title: Enumerating Objects in a Filter Graph
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Enumerating Objects in a Filter Graph

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

An application might need to locate a particular filter in the filter graph, or even a particular pin on a filter. For example, it might use an interface that a particular filter exposes. Or, it might construct a specialized filter graph and need to call methods on individual pins to connect the filters. For this purpose, DirectShow provides several methods for enumerating objects in a filter graph.

The enumerators discussed in this section follow the standard form used by COM enumeration interfaces. For more information, see the "IEnumXXXX" topic in the Platform SDK. For information on enumerating filters that are registered on the user's computer, but aren't yet in the filter graph, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md).

This article contains the following topics:

-   [Enumerating Filters](enumerating-filters.md)
-   [Enumerating Pins](enumerating-pins.md)
-   [Enumerating Media Types](enumerating-media-types.md)

## Related topics

<dl> <dt>

[Basic DirectShow Tasks](basic-directshow-tasks.md)
</dt> </dl>

 

 



