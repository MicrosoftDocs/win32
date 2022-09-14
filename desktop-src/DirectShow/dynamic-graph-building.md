---
description: Dynamic Graph Building
ms.assetid: 13fed430-979b-40f7-91ba-aff2d811bd92
title: Dynamic Graph Building
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Graph Building

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

 

 



