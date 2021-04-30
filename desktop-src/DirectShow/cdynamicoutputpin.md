---
description: The CDynamicOutputPin class implements an output pin that supports dynamic reconnections and format changes.
ms.assetid: d2488fba-a653-4b6e-b786-ce95f9e20daa
title: CDynamicOutputPin class (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin class

The `CDynamicOutputPin` class implements an output pin that supports dynamic reconnections and format changes.

This class derives from the [**CBaseOutputPin**](cbaseoutputpin.md) class and implements the [**IPinFlowControl**](/windows/desktop/api/Strmif/nn-strmif-ipinflowcontrol) interface. It supports several operations that are important for dynamic graph building:

-   Dynamic reconnection: The pin can disconnect and reconnect while the filter is still active (paused or running).
-   Dynamic format change: The pin can negotiate a new media type while the filter is still active, without reconnecting.
-   Flow control: The owning filter (or an application) can block data flow from the pin without stopping the filter.

For more information, see [Dynamic Graph Building](dynamic-graph-building.md).

The pin has three possible states: blocked, unblocked, and pending. In the *pending* state, the pin is waiting for some operation to complete on another thread, before the pin switches to the blocked state. While the pin is blocked, the filter cannot deliver data through the pin, or change the pin's connection.

To coordinate among multiple threads, the owning filter must follow certain rules. (For more information about threads in the filter graph, see [Threads and Critical Sections](threads-and-critical-sections.md).) First, the streaming thread must always call the [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) method before it calls any of the following methods:

-   [**CDynamicOutputPin::ChangeOutputFormat**](cdynamicoutputpin-changeoutputformat.md)
-   [**CDynamicOutputPin::ChangeMediaType**](cdynamicoutputpin-changemediatype.md)
-   [**CDynamicOutputPin::DynamicReconnect**](cdynamicoutputpin-dynamicreconnect.md)
-   [**CBaseOutputPin::Deliver**](cbaseoutputpin-deliver.md)
-   [**CBaseOutputPin::DeliverEndOfStream**](cbaseoutputpin-deliverendofstream.md)
-   [**CBaseOutputPin::DeliverNewSegment**](cbaseoutputpin-delivernewsegment.md)
-   [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive)
-   [**IMemInputPin::ReceiveMultiple**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivemultiple)
-   [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream)
-   [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment)

Afterward, it must call the [**CDynamicOutputPin::StopUsingOutputPin**](cdynamicoutputpin-stopusingoutputpin.md) method.

Second, the application thread must not call any of the methods in the previous list. Third, the streaming thread must not call the class methods that block or unblock the pin. These methods are: [**CDynamicOutputPin::Block**](cdynamicoutputpin-block.md), [**CDynamicOutputPin::SynchronousBlockOutputPin**](cdynamicoutputpin-synchronousblockoutputpin.md), [**CDynamicOutputPin::AsynchronousBlockOutputPin**](cdynamicoutputpin-asynchronousblockoutputpin.md), and [**CDynamicOutputPin::UnblockOutputPin**](cdynamicoutputpin-unblockoutputpin.md).

These rules ensure that the application thread cannot block the pin while the streaming thread is using it, and vice versa. After the streaming thread has called **StartUsingOutputPin**, the pin will not block until the streaming thread calls **StopUsingOutputPin**. Conversely, if the pin is blocked, **StartUsingOutputPin** waits until the pin is unblocked.

To avoid forgetting to call **StopUsingOutputPin**, you can use the [**CAutoUsingOutputPin**](cautousingoutputpin-cautousingoutputpin.md) class. It calls **StopUsingOutputPin** automatically when it goes out of scope.

When the owning filter joins or leaveds the filter graph (in its [**IBaseFilter::JoinFilterGraph**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-joinfiltergraph) method), it must call the pin's [**CDynamicOutputPin::SetConfigInfo**](cdynamicoutputpin-setconfiginfo.md) method.



| Protected Member Variables                                                                      | Description                                                                                                                   |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**m\_BlockStateLock**](cdynamicoutputpin-m-blockstatelock.md)                                 | Critical section that protects the blocking state.                                                                            |
| [**m\_hUnblockOutputPinEvent**](cdynamicoutputpin-m-hunblockoutputpinevent.md)                 | Event that is signaled when the pin is not blocked.                                                                           |
| [**m\_hNotifyCallerPinBlockedEvent**](cdynamicoutputpin-m-hnotifycallerpinblockedevent.md)     | Event that is signaled when the pin successfully blocks, or the user cancels a pending block.                                 |
| [**m\_BlockState**](cdynamicoutputpin-m-blockstate.md)                                         | Blocking state.                                                                                                               |
| [**m\_dwBlockCallerThreadID**](cdynamicoutputpin-m-dwblockcallerthreadid.md)                   | The identifier of the thread that last called the [**IPinFlowControl::Block**](/windows/desktop/api/Strmif/nf-strmif-ipinflowcontrol-block) method on this pin. |
| [**m\_dwNumOutstandingOutputPinUsers**](cdynamicoutputpin-m-dwnumoutstandingoutputpinusers.md) | Number of streaming threads using this pin.                                                                                   |
| [**m\_hStopEvent**](cdynamicoutputpin-m-hstopevent.md)                                         | Event that is signaled when the filter stops or the pin flushes data.                                                         |
| [**m\_pGraphConfig**](cdynamicoutputpin-m-pgraphconfig.md)                                     | Pointer to the [**IGraphConfig**](/windows/desktop/api/Strmif/nn-strmif-igraphconfig) interface for performing dynamic reconnections.                           |
| [**m\_bPinUsesReadOnlyAllocator**](cdynamicoutputpin-m-bpinusesreadonlyallocator.md)           | Flag that specifies whether samples from the pin's allocator are read-only.                                                   |
| Protected Methods                                                                               | Description                                                                                                                   |
| [**SynchronousBlockOutputPin**](cdynamicoutputpin-synchronousblockoutputpin.md)                | Blocks the pin; does not return until the pin is blocked.                                                                     |
| [**AsynchronousBlockOutputPin**](cdynamicoutputpin-asynchronousblockoutputpin.md)              | Blocks the pin; might return before the pin is blocked.                                                                       |
| [**UnblockOutputPin**](cdynamicoutputpin-unblockoutputpin.md)                                  | Unblocks the pin.                                                                                                             |
| [**BlockOutputPin**](cdynamicoutputpin-blockoutputpin.md)                                      | Blocks the pin.                                                                                                               |
| [**WaitEvent**](cdynamicoutputpin-waitevent.md)                                                | Waits until the specified event is signaled.                                                                                  |
| Public Methods                                                                                  | Description                                                                                                                   |
| [**CDynamicOutputPin**](cdynamicoutputpin-cdynamicoutputpin.md)                                | Constructor method.                                                                                                           |
| [**~CDynamicOutputPin**](cdynamicoutputpin--cdynamicoutputpin.md)                              | Destructor method.                                                                                                            |
| [**SetConfigInfo**](cdynamicoutputpin-setconfiginfo.md)                                        | Specifies the [**IGraphConfig**](/windows/desktop/api/Strmif/nn-strmif-igraphconfig) pointer and the stop event.                                                |
| [**DeliverBeginFlush**](cdynamicoutputpin-deliverbeginflush.md)                                | Requests the connected input pin to begin a flush operation.                                                                  |
| [**DeliverEndFlush**](cdynamicoutputpin-deliverendflush.md)                                    | Requests the connected input pin to end a flush operation.                                                                    |
| [**Inactive**](cdynamicoutputpin-inactive.md)                                                  | Notifies the pin that the filter has stopped.                                                                                 |
| [**Active**](cdynamicoutputpin-active.md)                                                      | Notifies the pin that the filter is now active.                                                                               |
| [**CompleteConnect**](cdynamicoutputpin-completeconnect.md)                                    | Completes a connection to an input pin. Virtual.                                                                              |
| [**StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md)                            | Obtains access to the pin for a streaming operation. Virtual.                                                                 |
| [**StopUsingOutputPin**](cdynamicoutputpin-stopusingoutputpin.md)                              | Releases access to the pin after a streaming operation. Virtual.                                                              |
| [**StreamingThreadUsingOutputPin**](cdynamicoutputpin-streamingthreadusingoutputpin.md)        | Determines whether any thread is performing a streaming operation on the pin. Virtual.                                        |
| [**ChangeOutputFormat**](cdynamicoutputpin-changeoutputformat.md)                              | Dynamically changes the media type for the connection, and delivers new segment information.                                  |
| [**ChangeMediaType**](cdynamicoutputpin-changemediatype.md)                                    | Dynamically changes the media type for the connection.                                                                        |
| [**DynamicReconnect**](cdynamicoutputpin-dynamicreconnect.md)                                  | Performs a dynamic reconnection with a new media type.                                                                        |
| IPin Methods                                                                                    | Description                                                                                                                   |
| [**Disconnect**](cdynamicoutputpin-disconnect.md)                                              | Breaks the current pin connection.                                                                                            |
| IPinFlowControl Methods                                                                         | Description                                                                                                                   |
| [**Block**](cdynamicoutputpin-block.md)                                                        | Blocks or unblocks the flow of data from the pin.                                                                             |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




