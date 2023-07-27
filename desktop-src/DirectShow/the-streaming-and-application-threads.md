---
description: The Streaming and Application Threads
ms.assetid: 954f7abd-fe06-430a-b6f7-d60852826bc9
title: The Streaming and Application Threads
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The Streaming and Application Threads

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Any DirectShow application contains at least two important threads: the application thread, and one or more streaming threads. Samples are delivered on the streaming threads, and state changes happen on the application thread. The main streaming thread is created by a source or parser filter. Other filters might create worker threads that deliver samples, and these are considered streaming threads as well.

Some methods are called on the application thread, while others are called on a streaming thread. For example:

-   Streaming thread(s): [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive), [**IMemInputPin::ReceiveMultiple**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivemultiple), [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream), [**IMemAllocator::GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer).
-   Application thread: [**IMediaFilter::Pause**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-pause), [**IMediaFilter::Run**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-run), [**IMediaFilter::Stop**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-stop), [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions), [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush), [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush).
-   Either: [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment).

Having a separate streaming thread allows data to flow through the graph while the application thread waits for user input. The danger of multiple threads, however, is that a filter may create resources when it pauses (on the application thread), use them inside a streaming method, and destroy them when it stops (also on the application thread). If you are not careful, the streaming thread might try to use the resources after they are destroyed. The solution is to protect resources using critical sections, and synchronize streaming methods with state changes.

A filter needs one critical section to protect the filter state. The [**CBaseFilter**](cbasefilter.md) class has a member variable for this critical section, [**CBaseFilter::m\_pLock**](cbasefilter-m-plock.md). This critical section is called the filter lock. Also, each input pin needs a critical section to protect resources used by the streaming thread. These critical sections are called streaming locks; you must declare them in your derived pin class. It is easiest to use the [**CCritSec**](ccritsec.md) class, which wraps a Windows **CRITICAL\_SECTION** object and can be locked using the [**CAutoLock**](cautolock.md) class. The **CCritSec** class also provides some useful debugging functions. For more information, see [Critical Section Debugging Functions](critical-section-debugging-functions.md).

When a filter stops or flushes, it must synchronize the application thread with the streaming thread. To avoid deadlocking, it must first unblock the streaming thread, which might be blocked for several reasons:

-   It is waiting to get a sample inside the [**IMemAllocator::GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer) method, because all of the allocator's samples are in use.
-   It is waiting for another filter to return from a streaming method, such as **Receive**.
-   It is waiting inside one of its own streaming methods, for some resource to become available.
-   It is a renderer filter waiting for the presentation time of the next sample
-   It is a renderer filter waiting inside the **Receive** method while paused.

Therefore, when the filter stops or flushes, it must do the following:

-   Release any sample it is holding for any reason. Doing so unblocks the **GetBuffer** method.
-   Return from any streaming method as quickly as possible. If a streaming method is waiting for a resource, it must stop waiting immediately.
-   Start rejecting samples in **Receive**, so that the streaming thread does not access any more resources. (The [**CBaseInputPin**](cbaseinputpin.md) class handles this automatically.)
-   The **Stop** method must decommit all of the filter's allocators. (The **CBaseInputPin** class handles this automatically.)

Flushing and stopping both happen on the application thread. A filter stops in response to the [**IMediaControl::Stop**](/windows/desktop/api/Control/nf-control-imediacontrol-stop) method. The Filter Graph Manager issues the stop command in upstream order, starting from the renderers and working backward to the source filters. The stop command happens completely inside the filter's **CBaseFilter::Stop** method. When the method returns, the filter should be in a stopped state.

Flushing typically occurs because of a seek command. A flush command starts from the source or parser filter, and travels downstream. Flushing happens in two stages: The [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method informs a filter to discard all pending and incoming data; the [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) method signals the filter to accept data again. Flushing requires two stages because the **BeginFlush** call is on the application thread, during which the streaming thread continues to deliver data. Therefore, some samples may arrive after the **BeginFlush** call. The filter should discard these. Any samples that arrive after the **EndFlush** call are guaranteed to be new, and should be delivered.

The sections that follow contain code samples showing how to implement the most important filter methods, such as **Pause**, **Receive**, and so forth, in ways that avoid deadlocks and race conditions. Every filter has different requirements, however, so you will need to adapt these examples to your particular filter.

> [!Note]  
> The [**CTransformFilter**](ctransformfilter.md) and [**CTransInPlaceFilter**](ctransinplacefilter.md) base classes handle many of the issues described in this article. If you are writing a transform filter, and your filter does not wait on events inside a streaming method, or hold onto samples outside of **Receive**, then these base classes should be sufficient.

 

 

 



