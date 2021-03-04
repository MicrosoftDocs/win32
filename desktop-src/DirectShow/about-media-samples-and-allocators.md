---
description: About Media Samples and Allocators
ms.assetid: d6283bf0-0460-4519-9a56-fd4c78cfaabc
title: About Media Samples and Allocators
ms.topic: article
ms.date: 05/31/2018
---

# About Media Samples and Allocators

Filters deliver data across pin connections. Data moves from the output pin of one filter to the input pin of another filter. The most common way for the output pin to deliver the data is by calling the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method on the input, although a few other mechanisms exist as well.

Depending on the filter, memory for the media data can be allocated in various ways: on the heap, in a DirectDraw surface, using shared GDI memory, or using some other allocation mechanism. The object responsible for allocating the memory is called an *allocator*, which is a COM object that exposes the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

When two pins connect, one of the pins must provide an allocator. DirectShow defines a sequence of method calls that is used to establish which pin provides the allocator. The pins also agree on the number of buffers that the allocator will create, and the size of the buffers.

Before streaming begins, the allocator creates a pool of buffers. During streaming, the upstream filter fills buffers with data and delivers them to the downstream filter. But the upstream filter does not give the downstream filter raw pointers to the buffers. Instead, it uses COM objects called *media samples*, which the allocator creates to manage the buffers. Media samples expose the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface. A media sample contains:

-   a pointer to the underlying buffer
-   a time stamp
-   various flags
-   optionally, a media type

The time stamp defines the presentation time, which the renderer filter uses to schedule rendering. The flags indicate things like whether there was a break in the data since the previous sample. The media type provides a way for filters to change formats mid-stream. Usually, the sample has no media type, which indicates that the format has not changed since the previous sample.

While a filter is using a buffer, it holds reference count on the sample. The allocator uses the reference count to determine when it can re-use the buffer. This prevents a filter from overwriting a buffer that another filter is still using. A sample does not return to the allocator's pool of available samples until every filter has released it.

For more information, see the following topics:

-   The topic [Samples and Allocators](samples-and-allocators.md) provides a more detailed description of how allocators work.
-   The topic [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md) gives a general overview of data flow in DirectShow.

The following topics are intended for developers who are writing their own custom filters:

-   [Data Flow for Filter Developers](data-flow-for-filter-developers.md)
-   [Threads and Critical Sections](threads-and-critical-sections.md)

## Related topics

<dl> <dt>

[The Filter Graph and Its Components](the-filter-graph-and-its-components.md)
</dt> </dl>

 

 



