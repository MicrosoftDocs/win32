---
Description: Summary of Filter Threading
ms.assetid: b7e42101-75c9-428d-9dc7-e625242dbc1e
title: Summary of Filter Threading
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Summary of Filter Threading

The following methods are called on the streaming thread:

-   [**IMemInputPin::Receive**](/windows/win32/Strmif/nf-strmif-imeminputpin-receive?branch=master)
-   [**IMemInputPin::ReceiveMultiple**](/windows/win32/Strmif/nf-strmif-imeminputpin-receivemultiple?branch=master)
-   [**IPin::EndOfStream**](/windows/win32/Strmif/nf-strmif-ipin-endofstream?branch=master)
-   [**IPin::NewSegment**](/windows/win32/Strmif/nf-strmif-ipin-newsegment?branch=master)
-   [**IMemAllocator::GetBuffer**](/windows/win32/Strmif/nf-strmif-imemallocator-getbuffer?branch=master)

The following methods are called on the application thread:

-   State changes: [**IBaseFilter::JoinFilterGraph**](/windows/win32/Strmif/nf-strmif-ibasefilter-joinfiltergraph?branch=master), [**IMediaFilter::Pause**](/windows/win32/Strmif/nf-strmif-imediafilter-pause?branch=master), [**IMediaFilter::Run**](/windows/win32/Strmif/nf-strmif-imediafilter-run?branch=master), [**IMediaFilter::Stop**](/windows/win32/Strmif/nf-strmif-imediafilter-stop?branch=master), [**IQualityControl::SetSink**](/windows/win32/Strmif/nf-strmif-iqualitycontrol-setsink?branch=master).
-   Reference clock: [**IMediaFilter::GetSyncSource**](/windows/win32/Strmif/nf-strmif-imediafilter-getsyncsource?branch=master), [**IMediaFilter::SetSyncSource**](/windows/win32/Strmif/nf-strmif-imediafilter-setsyncsource?branch=master).
-   Pin operations: [**IBaseFilter::FindPin**](/windows/win32/Strmif/nf-strmif-ibasefilter-findpin?branch=master), [**IPin::Connect**](/windows/win32/Strmif/nf-strmif-ipin-connect?branch=master), [**IPin::ConnectedTo**](/windows/win32/Strmif/nf-strmif-ipin-connectedto?branch=master), [**IPin::ConnectionMediaType**](/windows/win32/Strmif/nf-strmif-ipin-connectionmediatype?branch=master), [**IPin::Disconnect**](/windows/win32/Strmif/nf-strmif-ipin-disconnect?branch=master), [**IPin::ReceiveConnection**](/windows/win32/Strmif/nf-strmif-ipin-receiveconnection?branch=master).
-   Allocator functions: [**IMemInputPin::GetAllocator**](/windows/win32/Strmif/nf-strmif-imeminputpin-getallocator?branch=master), [**IMemInputPin::NotifyAllocator**](/windows/win32/Strmif/nf-strmif-imeminputpin-notifyallocator?branch=master).
-   Flushing: [**IPin::BeginFlush**](/windows/win32/Strmif/nf-strmif-ipin-beginflush?branch=master), [**IPin::EndFlush**](/windows/win32/Strmif/nf-strmif-ipin-endflush?branch=master).

This list is not exhaustive. When you implement a filter, you must consider which methods change the filter state, and which methods perform streaming operations.

 

 



