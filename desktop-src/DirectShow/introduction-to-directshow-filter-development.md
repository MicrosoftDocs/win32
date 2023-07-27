---
description: Introduction to DirectShow Filter Development
ms.assetid: d5162ea4-ef37-4993-a82c-782f03b08c64
title: Introduction to DirectShow Filter Development
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Introduction to DirectShow Filter Development

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section gives a brief outline of the tasks involved in developing a custom DirectShow filter. It also provides links to topics that discuss these tasks in greater detail. Before reading this section, read the topics in [About DirectShow](about-directshow.md), which describe the overall DirectShow architecture.

**DirectShow Base Class Library**

The DirectShow SDK includes a set of C++ classes for writing filters. Although they are not required, these classes are the recommended way to write a new filter. To use the base classes, compile them into a static library and link the .lib file to your project, as described in [Building DirectShow Filters](building-directshow-filters.md).

The base class library defines a root class for filters, the [**CBaseFilter**](cbasefilter.md) class. Several other classes derive from **CBaseFilter**, and are specialized for particular kinds of filters. For example, the [**CTransformFilter**](ctransformfilter.md) class is designed for transform filters. To create a new filter, implement a class that inherits from one of the filter classes. For example, your class declaration might be as follows:


```C++
class CMyFilter : public CTransformFilter
{
private:
    /* Declare variables and methods that are specific to your filter.
public:
    /* Override various methods in CTransformFilter */
};
```



For more information about the DirectShow base classes, see the following topics:

-   [DirectShow Base Classes](directshow-base-classes.md)
-   [Building DirectShow Filters](building-directshow-filters.md)

**Creating Pins**

A filter must create one or more pins. The number of pins can be fixed at design time, or the filter can create new pins as needed. Pins generally derive from the [**CBasePin**](cbasepin.md) class, or from a class that inherits **CBasePin**, such as [**CBaseInputPin**](cbaseinputpin.md). The filter's pins should be declared as member variables in the filter class. Some of the filter classes already define the pins, but if your filter inherits directly from **CBaseFilter**, you must declare the pins in your derived class.

**Negotiating Pin Connections**

When the Filter Graph Manager tries to connect two filters, the pins must agree on various things. If they cannot, the connection attempt fails. Generally, pins negotiate the following:

-   Transport. The transport is the mechanism that the filters will use to move media samples from the output pin to the input pin. For example, they can use the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface ("push model") or the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface ("pull model").
-   Media type. Almost all pins use media types to describe the format of the data they will deliver.
-   Allocator. The allocator is the object that creates the buffers that hold the data. The pins must agree which pin will provide the allocator. They must also agree on the size of the buffers, the number of buffers to create, and other buffer properties.

The base classes implement a framework for these negotiations. You must complete the details by overriding various methods in the base class. The set of methods that you must override depends on the class and on the functionality of your filter. For more information, see [How Filters Connect](how-filters-connect.md).

**Processing and Delivering Data**

The primary function of most filters is to process and deliver media data. How that occurs depends on the type of filter:

-   A push source has a worker thread that continuously fills samples with data and delivers them downstream.
-   A pull source waits for its downstream neighbor to request a sample. It responds by writing data into a sample and delivering the sample to the downstream filter. The downstream filter creates the thread that drives the data flow.
-   A transform filter has samples delivered to it by its upstream neighbor. When it receives a sample, it processes the data and delivers it downstream.
-   A renderer filter receives samples from upstream, and schedules them for rendering based on the time stamps.

Other tasks related to streaming include flushing data from the graph, handling the end of the stream, and responding to seek requests. For more information about these issues, see the following topics:

-   [Data Flow for Filter Developers](data-flow-for-filter-developers.md)
-   [Quality-Control Management](quality-control-management.md)
-   [Threads and Critical Sections](threads-and-critical-sections.md)

**Supporting COM**

DirectShow filters are COM objects, typically packaged in DLLs. The base class library implements a framework for supporting COM. It is described in the section [DirectShow and COM](directshow-and-com.md).

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



