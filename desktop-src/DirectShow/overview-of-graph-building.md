---
description: Overview of Graph Building
ms.assetid: 5753f06c-ecfd-48d7-a8e9-768b798e9279
title: Overview of Graph Building
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Graph Building

To create a filter graph, begin by creating an instance of the Filter Graph Manager:


```C++
IGraphBuilder* pIGB;
HRESULT hr = CoCreateInstance(CLSID_FilterGraph,
    NULL, CLSCTX_INPROC_SERVER, IID_IGraphBuilder,
    (void **)&pIGB);
```



The Filter Graph Manager supports the following graph-building methods:

-   [**IFilterGraph::ConnectDirect**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-connectdirect) tries to make a direct connection between two pins. If the pins cannot connect, the method fails.
-   [**IGraphBuilder::Connect**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-connect) connects two pins. If possible, it makes a direct connection. Otherwise, it uses intermediate filters to complete the connection.
-   [**IGraphBuilder::Render**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-render) starts from an output pin and builds the rest of the graph. This methods adds filters as needed, working downstream, until it reaches a renderer filter.
-   [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) builds a complete file-playback graph.
-   [**IFilterGraph::AddFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-addfilter) adds a filter to the graph. It does not connect the filter. You must create the filter before calling this method, either by calling **CoCreateInstance** or by using the Filter Mapper or System Device Enumerator.

These methods provide three basic approaches to building the graph:

1.  The Filter Graph Manager builds the entire graph.
2.  The Filter Graph Manager builds part of the graph.
3.  The application builds the entire graph.

**The Filter Graph Manager Builds the Entire Graph**

If you simply want to play a file that is authored in a recognized format, such as AVI, MPEG, WAV, or MP3, use the **RenderFile** method. The article [How To Play a File](how-to-play-a-file.md) shows how to do this.

The **RenderFile** method starts by looking in the registry for a source filter that can parse the file. It uses the protocol (such as " `https://` " in the URL), the file extension, or pre-defined byte patterns in the file to determine the source filter. For details, see [Registering a Custom File Type](registering-a-custom-file-type.md).

To build the rest of the graph, the Filter Graph Manager uses an iterative process wherein it takes the media types that a filter supports on its output pins, and searches the registry for filters that will accept that media type as input. It uses several criteria to narrow the search and prioritize filters:

-   The *filter category* identifies the general functionality of the filter.
-   The media type describes what kind of data the filter can accept as input or deliver as output.
-   The *merit* determines the order in which filters are tried. If two filters in the same filter category both support the same input types, the Filter Graph Manager selects the one with the highest merit value. Some filters are purposely given a low merit value because they are designed for specialized purposes and should only be added to the graph by the application.

The Filter Graph Manager uses the [Filter Mapper](filter-mapper.md) object to search the registry.

As each filter is added, the Filter Graph Manager tries to connect it to the previous filter's output pin. The filters negotiate to determine whether they can connect, and if so, what media type to use for the connection. If the new filter cannot connect, the Filter Graph Manager discards it and tries another filter. This process continues until every stream is rendered.

**The Filter Graph Manager Builds Part of the Graph**

To do something beyond simply playing a file, your application must perform at least some of the graph building work. For example, a video capture application must select a capture source filter and add it to the graph. If you are writing data to an AVI file, you must add the AVI Mux and File Writer filters to the graph. However, it is often possible to let the Filter Graph Manager complete the graph. For example, you can render a pin for preview by calling the **Render** method.

**The Application Builds the Entire Graph**

In some scenarios, your application may need to build the graph by adding and connecting each filter. In this case, you probably know specifically which filters should be added to the graph. With this approach, the application adds each filter by calling **AddFilter**, enumerates the pins on the filters, and connects them by calling either **Connect** or **ConnectDirect**.

## Related topics

<dl> <dt>

[Building Graphs with the Capture Graph Builder](building-graphs-with-the-capture-graph-builder.md)
</dt> <dt>

[Enumerating Devices and Filters](enumerating-devices-and-filters.md)
</dt> <dt>

[Enumerating Objects in a Filter Graph](enumerating-objects-in-a-filter-graph.md)
</dt> <dt>

[General Graph-Building Techniques](general-graph-building-techniques.md)
</dt> <dt>

[Building the Filter Graph](building-the-filter-graph.md)
</dt> </dl>

 

 



