---
description: Filter States
ms.assetid: 97418307-eb50-4c8e-b03b-a2cd08139bdc
title: Filter States
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Filter States

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Filters have three possible states: stopped, paused, and running. The purpose of the paused state is to cue data in the graph, so that a run command responds immediately. The Filter Graph Manager controls all state transitions. When an application calls [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run), [**IMediaControl::Pause**](/windows/desktop/api/Control/nf-control-imediacontrol-pause), or [**IMediaControl::Stop**](/windows/desktop/api/Control/nf-control-imediacontrol-stop), the Filter Graph Manager calls the corresponding [**IMediaFilter**](/windows/desktop/api/Strmif/nn-strmif-imediafilter) method on all of the filters. Transitions between stopped and running always go through the paused state, so if the application calls **Run** on a stopped graph, the Filter Graph Manager pauses the graph before running it.

For most filters, the running and paused states are identical. Consider the following filter graph:

Source > Transform > Renderer

Assume for now that the source filter is not a live capture source. When the source filter pauses, it creates a thread that generates new data and writes it into media samples as quickly as possible. The thread "pushes" the samples downstream by calling [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) on the transform filter's input pin. The transform filter receives the samples on the source filter's thread. It may use a worker thread to deliver the samples to the renderer, but typically it delivers them on the same thread. While the renderer is paused, it waits to receive a sample. After it receives one, it blocks and holds that sample indefinitely. If it is a video renderer, it displays the sample as a poster image, repainting the image as necessary.

At this point, the stream is fully cued and ready for rendering. If the graph remains paused, samples will "pile up" in the graph behind the first sample, until every filter is blocked in [**Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) or [**IMemAllocator::GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer). No data is lost, though. Once the source thread is unblocked, it simply resumes from the point where it blocked.

The source filter and the transform filter ignore the transition from paused to running—they simply continue to process data as fast as possible. But when the renderer runs, it starts rendering samples. First it renders the sample it held while it was paused. Then, each time it receives a new sample, it calculates the sample's presentation time. (For details, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).) The renderer holds each sample until the presentation time, at which point it renders the sample. While it waits for the presentation time, it either blocks in the [**Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method, or receives new samples on a worker thread with a queue. Filters upstream from the renderer are not involved in scheduling.

Live sources, such as capture devices, are an exception to this general architecture. With a live source, it is not appropriate to cue any data in advance. The application might pause the graph and then wait for a long time before running it. The graph should not render "stale" samples. Therefore, a live source produces no samples while paused, only while running. To signal this fact to the Filter Graph Manager, the source filter's [**IMediaFilter::GetState**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-getstate) method returns VFW\_S\_CANT\_CUE. This return code indicates that the filter has switched to the paused state, even though the renderer did not receive any data.

When a filter stops, it rejects any more samples delivered to it. Source filters shut down their streaming threads, and other filters shut down any worker threads they may have created. Pins decommit their allocators.

### State Transitions

The Filter Graph Manager carries out all state transitions in upstream order, starting from the renderer and working backward to the source filter. This ordering is necessary to prevent samples from being dropped and to prevent the graph from deadlocking. The most crucial state transitions are between paused and stopped:

-   Stopped to paused: As each filter pauses, it becomes ready to receive samples from the next filter. The source filter is the last to pause. It creates the streaming thread and begins delivering samples. Because all of the downstream filters are paused, no filter rejects any samples. The Filter Graph Manager does not complete the transition until every renderer in the graph has received a sample (with the exception of live sources, as described earlier).
-   Paused to stopped: When a filter stops, it releases any samples that it holds, which unblocks any upstream filters waiting in [**GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer). If the filter is waiting for a resource inside the [**Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method, it stops waiting and returns from **Receive**, which unblocks the calling filter. Therefore, when the Filter Graph Manager stops the next upstream filter, that filter is not blocked in either **GetBuffer** or **Receive**, and can respond to the stop command. The upstream filter might deliver a few extra samples before it gets the stop command, but the downstream filter simply rejects them, because it already stopped.

## Related topics

<dl> <dt>

[Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md)
</dt> </dl>

 

 



