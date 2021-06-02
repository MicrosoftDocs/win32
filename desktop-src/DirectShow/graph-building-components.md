---
description: Graph-Building Components
ms.assetid: d803c56c-6fb1-4937-92e7-9ed2db2afc46
title: Graph-Building Components
ms.topic: article
ms.date: 05/31/2018
---

# Graph-Building Components

DirectShow provides several components that can be used to build filter graphs. These include the following:

-   [Filter Graph Manager](filter-graph-manager.md). This object controls the filter graph. It supports the [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder), [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol), and [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) interfaces, among others. All DirectShow applications use this object at some point, although in some cases another object creates the Filter Graph Manager for the application.
-   [Capture Graph Builder](capture-graph-builder.md). This object provides additional methods for building filter graphs. It was originally designed for building graphs that perform video capture (hence the name) but is useful for many other types of custom filter graph. It supports the [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interface.
-   [Filter Mapper](filter-mapper.md) and [System Device Enumerator](system-device-enumerator.md). These objects locate filters that are registered on the user's system, or that represent hardware devices.
-   [DVD Graph Builder](dvd-graph-builder.md). This object builds filter graphs for DVD playback and navigation. It supports the [**IDvdGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder) interface.

### Intelligent Connect

The term "Intelligent Connect" covers a set of algorithms that the Filter Graph Manager uses to build all or part of a filter graph. Whenever the Filter Graph Manager requires additional filters to complete the graph, it does roughly the following:

1.  If there is a filter currently in the graph, with at least one unconnected input pin, the Filter Graph Manager tries to use that filter.
2.  Otherwise, the Filter Graph Manager looks in the registry for filters that can accept the correct media type for the connection. Each filter has a registry value called "Merit," which indicates roughly how likely the filter is to be useful in completing the graph. The Filter Graph Manager tries filters in order of merit value. For each stream type (such as audio, video, or MIDI), the default renderer has a high merit. Decoders also have high merit. Special-purpose filters have low merit.

If the Filter Graph Manager gets stuck, it will back out and try a different combination of filters. You can find the exact details in the topic [Intelligent Connect](intelligent-connect.md).

## Related topics

<dl> <dt>

[Building the Filter Graph](building-the-filter-graph.md)
</dt> </dl>

 

 



