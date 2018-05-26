---
Description: Filter States
ms.assetid: 97418307-eb50-4c8e-b03b-a2cd08139bdc
title: Filter States
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Filter States

Filters have three possible states: stopped, paused, and running. The purpose of the paused state is to cue data in the graph, so that a run command responds immediately. The Filter Graph Manager controls all state transitions. When an application calls [**IMediaControl::Run**](/windows/win32/Control/nf-control-imediacontrol-run?branch=master), [**IMediaControl::Pause**](/windows/win32/Control/nf-control-imediacontrol-pause?branch=master), or [**IMediaControl::Stop**](/windows/win32/Control/nf-control-imediacontrol-stop?branch=master), the Filter Graph Manager calls the corresponding [**IMediaFilter**](/windows/win32/Strmif/nn-strmif-imediafilter?branch=master) method on all of the filters. Transitions between stopped and running always go through the paused state, so if the application calls **Run** on a stopped graph, the Filter Graph Manager pauses the graph before running it.

For most filters, the running and paused states are identical. Consider the following filter graph:

Source &gt; Transform &gt; Renderer

Assume for now that the source filter is not a live capture source. When the source filter pauses, it creates a thread that generates new data and writes it into media samples as quickly as possible. The thread "pushes" the samples downstream by calling [**IMemInputPin::Receive**](/windows/win32/Strmif/nf-strmif-imeminputpin-receive?branch=master) on the transform filter's input pin. The transform filter receives the samples on the source filter's thread. It may use a worker thread to deliver the samples to the renderer, but typically it delivers them on the same thread. While the renderer is paused, it waits to receive a sample. After it receives one, it blocks and holds that sample indefinitely. If it is a video renderer, it displays the sample as a poster image, repainting the image as necessary.

At this point, the stream is fully cued and ready for rendering. If the graph remains paused, samples will "pile up" in the graph behind the first sample, until every filter is blocked in [**Receive**](/windows/win32/Strmif/nf-strmif-imeminputpin-receive?branch=master) or [**IMemAllocator::GetBuffer**](/windows/win32/Strmif/nf-strmif-imemallocator-getbuffer?branch=master). No data is lost, though. Once the source thread is unblocked, it simply resumes from the point where it blocked.

The source filter and the transform filter ignore the transition from paused to running—they simply continue to process data as fast as possible. But when the renderer runs, it starts rendering samples. First it renders the sample it held while it was paused. Then, each time it receives a new sample, it calculates the sample's presentation time. (For details, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).) The renderer holds each sample until the presentation time, at which point it renders the sample. While it waits for the presentation time, it either blocks in the [**Receive**](/windows/win32/Strmif/nf-strmif-imeminputpin-receive?branch=master) method, or receives new samples on a worker thread with a queue. Filters upstream from the renderer are not involved in scheduling.

Live sources, such as capture devices, are an exception to this general architecture. With a live source, it is not appropriate to cue any data in advance. The application might pause the graph and then wait for a long time before running it. The graph should not render "stale" samples. Therefore, a live source produces no samples while paused, only while running. To signal this fact to the Filter Graph Manager, the source filter's [**IMediaFilter::GetState**](/windows/win32/Strmif/nf-strmif-imediafilter-getstate?branch=master) method returns VFW\_S\_CANT\_CUE. This return code indicates that the filter has switched to the paused state, even though the renderer did not receive any data.

When a filter stops, it rejects any more samples delivered to it. Source filters shut down their streaming threads, and other filters shut down any worker threads they may have created. Pins decommit their allocators.

### State Transitions

The Filter Graph Manager carries out all state transitions in upstream order, starting from the renderer and working backward to the source filter. This ordering is necessary to prevent samples from being dropped and to prevent the graph from deadlocking. The most crucial state transitions are between paused and stopped:

-   Stopped to paused: As each filter pauses, it becomes ready to receive samples from the next filter. The source filter is the last to pause. It creates the streaming thread and begins delivering samples. Because all of the downstream filters are paused, no filter rejects any samples. The Filter Graph Manager does not complete the transition until every renderer in the graph has received a sample (with the exception of live sources, as described earlier).
-   Paused to stopped: When a filter stops, it releases any samples that it holds, which unblocks any upstream filters waiting in [**GetBuffer**](/windows/win32/Strmif/nf-strmif-imemallocator-getbuffer?branch=master). If the filter is waiting for a resource inside the [**Receive**](/windows/win32/Strmif/nf-strmif-imeminputpin-receive?branch=master) method, it stops waiting and returns from **Receive**, which unblocks the calling filter. Therefore, when the Filter Graph Manager stops the next upstream filter, that filter is not blocked in either **GetBuffer** or **Receive**, and can respond to the stop command. The upstream filter might deliver a few extra samples before it gets the stop command, but the downstream filter simply rejects them, because it already stopped.

## Related topics

<dl> <dt>

[Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md)
</dt> </dl>

 

 



