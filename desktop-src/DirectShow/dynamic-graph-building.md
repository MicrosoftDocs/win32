---
description: Dynamic Graph Building
ms.assetid: 13fed430-979b-40f7-91ba-aff2d811bd92
title: Dynamic Graph Building
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Dynamic Graph Building

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If you need to modify an existing filter graph, you can stop the graph, make the changes, and restart the graph. This is usually the best approach. However, under some circumstances, you might want to alter a graph while it is still running. For example:

-   The application inserts a video effects filter during playback.
-   A source filter switches media types midstream, possibly requiring a new decompression filter.
-   The application adds a new video stream to the graph.

These are all examples of *dynamic graph building*, a term that covers any kind of change to a filter graph while the graph continues to run. Dynamic graph building can be initiated by an application or by a filter in the graph. Three distinct scenarios are possible:

-   [Dynamic Format Changes](dynamic-format-changes.md): A filter can change formats midstream, without the need to remove or replace any filters.
-   [Dynamic Reconnection](dynamic-reconnection.md): Changing the graph by adding or removing filters.
-   [Filter Chains](filter-chains.md): Adding, removing, and controlling chains of filters.

## Related topics

<dl> <dt>

[About DirectShow](about-directshow.md)
</dt> </dl>

 

 



