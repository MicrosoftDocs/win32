---
description: Live Sources
ms.assetid: 571fe5e5-9616-463b-837c-f8dbb8adf1be
title: Live Sources
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Live Sources

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A live source, also called a *push source*, receives data in real time. Examples include video capture and network broadcasts. In general, a live source cannot control the rate at which data arrives.

A filter is considered to be a live source if either of the following are true:

-   The filter returns the AM\_FILTER\_MISC\_FLAGS\_IS\_SOURCE flag from the [**IAMFilterMiscFlags::GetMiscFlags**](/windows/desktop/api/Strmif/nf-strmif-iamfiltermiscflags-getmiscflags) method, AND at least one of its output pins exposes the [**IAMPushSource**](/windows/desktop/api/Strmif/nn-strmif-iampushsource) interface.
-   The filter exposes the [**IKsPropertySet**](ikspropertyset.md) interface and has a capture pin (PIN\_CATEGORY\_CAPTURE). See [Pin Property Set](pin-property-set.md) for more information.

If a live source filter provides a clock, the Filter Graph Manager will prefer that clock when it chooses the graph reference clock. See [Reference Clocks](reference-clocks.md) for more information.

**Latency**

A filter's latency is the amount of time it takes the filter to process a sample. For live sources, the latency is determined by the size of the buffer used to hold samples. For example, suppose the filter graph has a video source with a latency of 33 milliseconds (ms) and an audio source with a latency of 500 ms. Each video frame arrives at the video renderer about 470 ms before the matching audio sample reaches the audio renderer. Unless the graph compensates for the difference, the audio and video will not be synchronized.

Live sources can be synchronized through the [**IAMPushSource**](/windows/desktop/api/Strmif/nn-strmif-iampushsource) interface. The Filter Graph Manager does not synchronize live sources unless the application enables synchronization by calling the [**IAMGraphStreams::SyncUsingStreamOffset**](/windows/desktop/api/Strmif/nf-strmif-iamgraphstreams-syncusingstreamoffset) method. If synchronization is enabled, the Filter Graph Manager queries each source filter for **IAMPushSource**. If the filter supports **IAMPushSource**, the Filter Graph Manager calls [**IAMLatency::GetLatency**](/windows/desktop/api/Strmif/nf-strmif-iamlatency-getlatency) to retrieve the filter's expected latency. (The **IAMPushSource** interface inherits [**IAMLatency**](/windows/desktop/api/Strmif/nn-strmif-iamlatency).) From the combined latency values, the Filter Graph Manager determines the maximum expected latency in the graph. It then calls [**IAMPushSource::SetStreamOffset**](/windows/desktop/api/Strmif/nf-strmif-iampushsource-setstreamoffset) to give each source filter a stream offset, which that filter adds to the time stamps that it generates.

This method is intended primarily for live preview. However, note that a preview pin on a live capture device (such as a camera) does not set time stamps on the samples it delivers. Therefore, to use this method with a live capture device, you must preview from the capture pin. For more information, see [DirectShow Video Capture Filters](directshow-video-capture-filters.md).

Currently the [**IAMPushSource**](/windows/desktop/api/Strmif/nn-strmif-iampushsource) interface is supported by the [VFW Capture](vfw-capture-filter.md) filter and the [Audio Capture](audio-capture-filter.md) filter.

**Rate Matching**

If a renderer filter schedules samples using one reference clock, but the source filter produces them using a different clock, glitches can occur in playback. The renderer might run faster than the source, causing gaps in the data. Or it might run slower than the source, causing samples to "bunch up," until at some point the graph will drop samples. Typically, a live source cannot control its production rate, so instead the renderer should match rates with the source.

Currently, only the audio renderer performs rate matching, because glitches in audio playback are more noticeable than glitches in video. To perform rate-matching, the audio renderer must select something against which it will match rates. It uses the following algorithm:

-   If the graph is not using a reference clock, the audio renderer does not try to match rates. (Whenever the graph has no reference clock, samples are always rendered immediately as they arrive.)
-   Otherwise, if there is a reference clock for the graph, the audio renderer checks whether there is a live source upstream, using the criteria described previously. If not, the audio renderer does not match rates.
-   If there is a live source upstream, and that source exposes the [**IAMPushSource**](/windows/desktop/api/Strmif/nn-strmif-iampushsource) interface on its output pin, the audio renderer calls [**IAMPushSource::GetPushSourceFlags**](/windows/desktop/api/Strmif/nf-strmif-iampushsource-getpushsourceflags). It looks for one of the following flags:
    -   AM\_PUSHSOURCECAPS\_INTERNAL\_RM. This flag means the source filter has its own rate-matching mechanism, so the audio renderer does not match rates.
    -   AM\_PUSHSOURCECAPS\_NOT\_LIVE. This flag means the source filter is not really a live source, even though it exposes the [**IAMPushSource**](/windows/desktop/api/Strmif/nn-strmif-iampushsource) interface. Therefore, the audio renderer does not match rates.
    -   AM\_PUSHSOURCECAPS\_PRIVATE\_CLOCK. This flag means the source filter is using a private clock to generate time stamps. In this case, the audio renderer matches rates against the time stamps. (If the samples have no time stamps, however, the renderer ignores this flag.)
-   If [**GetPushSourceFlags**](/windows/desktop/api/Strmif/nf-strmif-iampushsource-getpushsourceflags) returns no flags (zero), the audio renderer's behavior depends on the graph clock and whether the samples have time stamps:
    -   If the audio renderer is not the graph clock, AND the samples have time stamps, the audio renderer matches rates against the time stamps.
    -   If the samples do not have time stamps, the audio renderer tries to match the rate of incoming audio data.
    -   If the audio renderer is the graph clock, it tries to match the incoming data rate.

The reason for the last case is the following: If the audio renderer is the reference clock, and the source filter is using the same clock to generate time stamps, then the audio renderer cannot match rates against the time stamps. If it did, in effect it would be trying to match rates with itself, which could cause the clock to drift. Therefore, in this case the renderer matches the rate of incoming audio data.

## Related topics

<dl> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



