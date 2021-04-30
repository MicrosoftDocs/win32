---
description: General Graph-Building Techniques
ms.assetid: 66d93305-175c-4549-b825-2f3d7fd6bf09
title: General Graph-Building Techniques
ms.topic: article
ms.date: 05/31/2018
---

# General Graph-Building Techniques

Every DirectShow application starts by building a filter graph. As you read the overview topics in the DirectShow documentation, you will find that most start by describing what kind of filter graph you need. In some cases, there is a method or a helper object specifically designed for building that type of graph. For example, the [DVD Graph Builder](dvd-graph-builder.md) object builds DVD playback graphs. In other cases, the application must construct the graph by adding filters and connecting them.

This section presents some helper functions that implement basic graph-building operations. They can be used by any DirectShow application that needs to build or modify a filter graph. This section contains the following topics:

-   [Add a Filter by CLSID](add-a-filter-by-clsid.md)
-   [Find an Unconnected Pin on a Filter](find-an-unconnected-pin-on-a-filter.md)
-   [Connect Two Filters](connect-two-filters.md)
-   [Find an Interface on a Filter or Pin](find-an-interface-on-a-filter-or-pin.md)
-   [Find a Filter's Peer](find-a-filters-peer.md)
-   [Remove All the Filters in the Graph](remove-all-the-filters-in-the-graph.md)
-   [Building Graphs with the Capture Graph Builder](building-graphs-with-the-capture-graph-builder.md)

## Related topics

<dl> <dt>

[Basic DirectShow Tasks](basic-directshow-tasks.md)
</dt> <dt>

[Enumerating Devices and Filters](enumerating-devices-and-filters.md)
</dt> <dt>

[Enumerating Objects in a Filter Graph](enumerating-objects-in-a-filter-graph.md)
</dt> <dt>

[Intelligent Connect](intelligent-connect.md)
</dt> </dl>

 

 



