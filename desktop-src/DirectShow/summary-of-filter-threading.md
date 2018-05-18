---
Description: Summary of Filter Threading
ms.assetid: 'b7e42101-75c9-428d-9dc7-e625242dbc1e'
title: Summary of Filter Threading
---

# Summary of Filter Threading

The following methods are called on the streaming thread:

-   [**IMemInputPin::Receive**](imeminputpin-receive.md)
-   [**IMemInputPin::ReceiveMultiple**](imeminputpin-receivemultiple.md)
-   [**IPin::EndOfStream**](ipin-endofstream.md)
-   [**IPin::NewSegment**](ipin-newsegment.md)
-   [**IMemAllocator::GetBuffer**](imemallocator-getbuffer.md)

The following methods are called on the application thread:

-   State changes: [**IBaseFilter::JoinFilterGraph**](ibasefilter-joinfiltergraph.md), [**IMediaFilter::Pause**](imediafilter-pause.md), [**IMediaFilter::Run**](imediafilter-run.md), [**IMediaFilter::Stop**](imediafilter-stop.md), [**IQualityControl::SetSink**](iqualitycontrol-setsink.md).
-   Reference clock: [**IMediaFilter::GetSyncSource**](imediafilter-getsyncsource.md), [**IMediaFilter::SetSyncSource**](imediafilter-setsyncsource.md).
-   Pin operations: [**IBaseFilter::FindPin**](ibasefilter-findpin.md), [**IPin::Connect**](ipin-connect.md), [**IPin::ConnectedTo**](ipin-connectedto.md), [**IPin::ConnectionMediaType**](ipin-connectionmediatype.md), [**IPin::Disconnect**](ipin-disconnect.md), [**IPin::ReceiveConnection**](ipin-receiveconnection.md).
-   Allocator functions: [**IMemInputPin::GetAllocator**](imeminputpin-getallocator.md), [**IMemInputPin::NotifyAllocator**](imeminputpin-notifyallocator.md).
-   Flushing: [**IPin::BeginFlush**](ipin-beginflush.md), [**IPin::EndFlush**](ipin-endflush.md).

This list is not exhaustive. When you implement a filter, you must consider which methods change the filter state, and which methods perform streaming operations.

 

 



