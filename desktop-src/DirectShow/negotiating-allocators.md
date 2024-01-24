---
description: Negotiating Allocators
ms.assetid: fe13477c-1a7b-4098-9d0f-c54783102bc9
title: Negotiating Allocators
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Negotiating Allocators

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When two pins connect, they need a mechanism for exchanging media data. This mechanism is called the *transport*. In general, the DirectShow architecture is neutral about transports. Two filters can agree to connect using any transport that both support.

The most common transport is the *local memory* transport, in which the media data resides in main memory. Two flavors of local memory transport exist, the *push model* and the *pull model*. In the push model, the source filter pushes data to the downstream filter, using the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface on the downstream filter's input pin. In the pull model, the downstream filter requests data from the source filter, using the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface on the source filter's output pin. For more information on these two data-flow models, see [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md).

In local memory transport, the object responsible for allocating memory buffers is called the *allocator*. An allocator supports the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface. Both pins share a single allocator. Either pin can provide an allocator, but the output pin selects which allocator to use.

The output pin also sets the allocator properties, which determine how many buffers are created by the allocator, the size of each buffer, and the memory alignment. The output pin might defer to the input pin for the buffer requirements.

In an **IMemInputPin** connection, allocator negotiation works as follows:

1.  Optionally, the output pin calls [**IMemInputPin::GetAllocatorRequirements**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocatorrequirements). This method retrieves the input pin's buffer requirements, such as memory alignment. In general, the output pin should honor the input pin's request, unless there is a good reason not to.
2.  Optionally, the output pin calls [**IMemInputPin::GetAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocator). This method requests an allocator from the input pin. The input pin provides one, or returns an error code.
3.  The output pin selects an allocator. It can use one provided by the input pin, or create its own.
4.  The output pin calls [**IMemAllocator::SetProperties**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-setproperties) to set the allocator properties. However, the allocator might not honor the requested properties. (For example, this can happen if the input pin provides the allocator.) The allocator returns the actual properties as an output parameter in the **SetProperties** method.
5.  The outpin calls [**IMemInputPin::NotifyAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-notifyallocator) to inform the input pin of the selection.
6.  The input pin should call [**IMemAllocator::GetProperties**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getproperties) to verify whether the allocator properties are acceptable.
7.  The output pin is responsible for committing and decommitting the allocator. This occurs when streaming starts and stops.

In an **IAsyncReader** connection, allocator negotiation works as follows:

1.  The input pin calls [**IAsyncReader::RequestAllocator**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-requestallocator) on the output pin. The input pin specifies its buffer requirements and, optionally, provides an allocator.
2.  The output pin selects an allocator. It can use the one provided by the input pin, if any, or create its own.
3.  The output pin returns the allocator as an outgoing parameter in the **RequestAllocator** method. The input pin should check the allocator properties.
4.  The input pin is responsible for committing and decommitting the allocator.
5.  At any time during the allocator negotiation process, either pin can fail the connection.
6.  If the output pin uses the input pin's allocator, it can use that allocator only to deliver samples to that input pin. The owning filter must not use the allocator to deliver samples to other pins.

## Related topics

<dl> <dt>

[Providing a Custom Allocator](providing-a-custom-allocator.md)
</dt> </dl>

 

 



