---
description: Flushing
ms.assetid: '868218c4-3e1a-4da0-89fa-30a9848da0e8'
title: Flushing
ms.topic: article
ms.date: 05/31/2018
---

# Flushing

While the filter graph is running, arbitrary amounts of data can be moving through the graph. Some of it might be in queues, waiting to be delivered. There are times when the filter graph needs to remove this pending data as quickly as possible and replace it with new data. After a seek command, for example, the source filter generates samples from a new position in the source. To minimize latency, downstream filters should discard any samples that were created before the seek command. The process of discarding samples is called *flushing*. It enables the graph to be more responsive when events alter the normal data flow.

Flushing is handled slightly differently by the pull model than the push model. This article starts by describing the push model; then it describes the differences in the pull model.

Flushing happens in two stages.

-   First, the source filter calls [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) on the downstream filter's input pin. The downstream filter starts rejecting samples from upstream. It also discards any samples it is holding, and sends the **BeginFlush** call downstream to the next filter.
-   When the source filter is ready to send new data, it calls [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) on the input pin. This signals the downstream filter that it can receive new samples. The downstream filter sends the **EndFlush** call to the next filter.

In the **BeginFlush** method, the input pin does the following:

1.  Calls **BeginFlush** on downstream input pins.
2.  Rejects any further calls that stream data, including **Receive** and **EndOfStream**.
3.  Unblocks any upstream filters that are blocked waiting for a sample from the filter's allocator. Some filters decommit their allocators for this purpose.
4.  Exits from any waits that block streaming. For example, renderer filters block when paused. They also block when they are waiting to render a sample at the correct stream time. The filter must unblock, so that samples queued upstream can be delivered and rejected. This step ensures that all upstream filters eventually unblock.

In the **EndFlush** method, the input pin does the following:

1.  Waits for all queued samples to be discarded.
2.  Frees any buffered data. This step can sometimes be performed in the **BeginFlush** method. However, **BeginFlush** is not synchronized with the streaming thread. The filter must not process or buffer any more data between the call to **BeginFlush** and the call to **EndFlush**.
3.  Clears any pending EC\_COMPLETE notifications.
4.  Calls **EndFlush** downstream.

At this point, the filter can accept samples again. All samples are guaranteed to be more recent than the flush.

In the pull model, the parser filter initiates flushing, rather than the source filter. Not only does it call **IPin::BeginFlush** and **IPin::EndFlush** on the downstream filter, it also calls [**IAsyncReader::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-beginflush) and [**IAsyncReader::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-endflush) on the *output* pin of the source filter. If the source filter has pending read requests, it will discard them.

## Related topics

<dl> <dt>

[Flushing Data](flushing-data.md)
</dt> </dl>

 

 



