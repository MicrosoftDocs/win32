---
Description: Negotiating Allocators
ms.assetid: 'fe13477c-1a7b-4098-9d0f-c54783102bc9'
title: Negotiating Allocators
---

# Negotiating Allocators

When two pins connect, they need a mechanism for exchanging media data. This mechanism is called the *transport*. In general, the DirectShow architecture is neutral about transports. Two filters can agree to connect using any transport that both support.

The most common transport is the *local memory* transport, in which the media data resides in main memory. Two flavors of local memory transport exist, the *push model* and the *pull model*. In the push model, the source filter pushes data to the downstream filter, using the [**IMemInputPin**](imeminputpin.md) interface on the downstream filter's input pin. In the pull model, the downstream filter requests data from the source filter, using the [**IAsyncReader**](iasyncreader.md) interface on the source filter's output pin. For more information on these two data-flow models, see [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md).

In local memory transport, the object responsible for allocating memory buffers is called the *allocator*. An allocator supports the [**IMemAllocator**](imemallocator.md) interface. Both pins share a single allocator. Either pin can provide an allocator, but the output pin selects which allocator to use.

The output pin also sets the allocator properties, which determine how many buffers are created by the allocator, the size of each buffer, and the memory alignment. The output pin might defer to the input pin for the buffer requirements.

In an **IMemInputPin** connection, allocator negotiation works as follows:

1.  Optionally, the output pin calls [**IMemInputPin::GetAllocatorRequirements**](imeminputpin-getallocatorrequirements.md). This method retrieves the input pin's buffer requirements, such as memory alignment. In general, the output pin should honor the input pin's request, unless there is a good reason not to.
2.  Optionally, the output pin calls [**IMemInputPin::GetAllocator**](imeminputpin-getallocator.md). This method requests an allocator from the input pin. The input pin provides one, or returns an error code.
3.  The output pin selects an allocator. It can use one provided by the input pin, or create its own.
4.  The output pin calls [**IMemAllocator::SetProperties**](imemallocator-setproperties.md) to set the allocator properties. However, the allocator might not honor the requested properties. (For example, this can happen if the input pin provides the allocator.) The allocator returns the actual properties as an output parameter in the **SetProperties** method.
5.  The outpin calls [**IMemInputPin::NotifyAllocator**](imeminputpin-notifyallocator.md) to inform the input pin of the selection.
6.  The input pin should call [**IMemAllocator::GetProperties**](imemallocator-getproperties.md) to verify whether the allocator properties are acceptable.
7.  The output pin is responsible for committing and decommitting the allocator. This occurs when streaming starts and stops.

In an **IAsyncReader** connection, allocator negotiation works as follows:

1.  The input pin calls [**IAsyncReader::RequestAllocator**](iasyncreader-requestallocator.md) on the output pin. The input pin specifies its buffer requirements and, optionally, provides an allocator.
2.  The output pin selects an allocator. It can use the one provided by the input pin, if any, or create its own.
3.  The output pin returns the allocator as an outgoing parameter in the **RequestAllocator** method. The input pin should check the allocator properties.
4.  The input pin is responsible for committing and decommitting the allocator.
5.  At any time during the allocator negoriation process, either pin can fail the connection.
6.  If the output pin uses the input pin's allocator, it can use that allocator only to deliver samples to that input pin. The owning filter must not use the allocator to deliver samples to other pins.

## Related topics

<dl> <dt>

[Providing a Custom Allocator](providing-a-custom-allocator.md)
</dt> </dl>

 

 



