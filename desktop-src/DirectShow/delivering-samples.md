---
description: Delivering Samples
ms.assetid: 31aabb6d-dec6-41fa-b24d-35a77b67bc4a
title: Delivering Samples
ms.topic: article
ms.date: 05/31/2018
---

# Delivering Samples

This article describes how a filter delivers a sample. It describes both the push model, using [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) methods, and the pull model, using [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader).

**Push Model: Delivering a Sample**

The output pin delivers a sample by calling the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method or the [**IMemInputPin::ReceiveMultiple**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivemultiple) method, which is equivalent but delivers an array of samples. The input pin can block inside **Receive** (or **ReceiveMultiple**). If the pin might block, its [**IMemInputPin::ReceiveCanBlock**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivecanblock) method should return S\_OK. If the pin guarantees never to block, **ReceiveCanBlock** should return S\_FALSE. The S\_OK return value does not mean that **Receive** always blocks, just that it might.

Although **Receive** can block to wait for a resource to become available, it should not block to wait for more data from the upstream filter. Doing so can cause a deadlock where the upstream filter waits for the downstream filter to release the sample, which never happens because the downstream filter is waiting on the upstream filter. If a filter has multiple input pins, however, one pin can wait for another pin to receive data. For example, the [AVI Mux](avi-mux-filter.md) filter does this so that it can interleave audio and video data.

A pin might reject a sample for a number of reasons:

-   The pin is flushing (see [Flushing](flushing.md)).
-   The pin is not connected.
-   The filter is stopped.
-   Some other error occurred.

The **Receive** method should return S\_FALSE in the first case, and a failure code in the other cases. The upstream filter should stop sending samples when the return code is anything other than S\_OK.

You can consider the first three cases to be "expected" failures, in the sense that the filter was in the wrong state to receive samples. An unexpected failure would be one that causes the pin to reject a sample even though the pin is in a receiving state. If an error of this type occurs, the pin should send an end-of-stream notification downstream, and send an [**EC\_ERRORABORT**](ec-errorabort.md) event to the Filter Graph Manager.

In the DirectShow base classes, the [**CBaseInputPin::CheckStreaming**](cbaseinputpin-checkstreaming.md) method checks for the general failure cases—flushing, stopped, and so forth. The derived class will need to check for failures that are specific to the filter. In case of an error, the [**CBaseInputPin::Receive**](cbaseinputpin-receive.md) method sends the end-of-stream notification and the EC\_ERRORABORT event.

**Pull Model: Requesting a Sample**

In the **IAsyncReader** interface, the input pin requests samples from the output pin by calling one of the following methods:

-   [**IAsyncReader::Request**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-request)
-   [**IAsyncReader::SyncRead**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-syncread)
-   [**IAsyncReader::SyncReadAligned**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-syncreadaligned)

The **Request** method is asynchronous; the input pin calls [**IAsyncReader::WaitForNext**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-waitfornext) to wait for the request to complete. The other two methods are synchronous.

**When to Deliver Data**

A filter always delivers samples while it is in the running state. In most cases, a filter also delivers samples while paused. This enables the graph to cue up the data so that playback starts immediately when **Run** is called (see [Filter States](filter-states.md)). If your filter does not deliver data while paused, the filter's **IMediaFilter::GetState** method should return VFW\_S\_CANT\_CUE in the paused state. This return code signals the filter graph not to wait for data from your filter before it completes the pause transition. Otherwise, the **Pause** method will block indefinitely. For example code, see [**CBaseFilter::GetState**](cbasefilter-getstate.md).

Here are some examples of when a filter might need to return VFW\_S\_CANT\_CUE:

-   Live sources, such as capture filters, should not send data while paused. See [Producing Data in a Capture Filter](producing-data-in-a-capture-filter.md).
-   A splitter filter might or might not send data while paused, depending on the implementation. If the filter uses separate threads to queue data on each output pin, then it can send data while paused. But if the filter uses a single thread for every output pin, the first pin might block the thread when it calls **Receive**, which will prevent the other pins from sending data. In that case, you should return VFW\_S\_CANT\_CUE.
-   A filter might deliver data sporadically. For example, it might parse a custom data stream and filter out some packets while delivering others. In that case, the filter may not be guaranteed to deliver data while paused.

A source filter (using the push model) or a parser filter (using the push/pull model) creates one or more streaming threads, which deliver samples as quickly as possible. Downstream filters, such as decoders and transforms, typically send data only when **Receive** is called on their input pins.

## Related topics

<dl> <dt>

[Receiving and Delivering Samples](receiving-and-delivering-samples.md)
</dt> </dl>

 

 



