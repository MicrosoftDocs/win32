---
description: DVD Playback Enhancements in Windows Vista
ms.assetid: b3cf043f-c974-4240-8291-5c717bd8afaa
title: DVD Playback Enhancements in Windows Vista
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Playback Enhancements in Windows Vista

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This sections describes the improvements to DVD playback and navigation in Windows Vista.

**Specifying a Decoder**

In earlier versions of DirectShow, it was difficult to specify a particular MPEG-2 decoder when building a DVD playback graph. Starting in Windows Vista, an application can specify the decoder as follows:

1.  Add the decoder to the graph before calling [**IDvdGraphBuilder::RenderDvdVideoVolume**](/windows/desktop/api/Strmif/nf-strmif-idvdgraphbuilder-renderdvdvideovolume).
2.  Call **RenderDvdVideoVolume** and set the AM\_DVD\_DO\_NOT\_CLEAR flag. The DVD Navigator will give preference to the decoder that you added.

**Support for the Enhanced Video Renderer**

It is recommended that applications written for Windows Vista or later use the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) for video playback. To use the EVR in a DVD playback application, set the AM\_DVD\_EVR\_ONLY flag when you call **RenderDvdVideoVolume**.

To configure the EVR before you build the graph, call [**IDvdGraphBuilder::GetDvdInterface**](/windows/desktop/api/Strmif/nf-strmif-idvdgraphbuilder-getdvdinterface) and query for the **IEVRFilterConfig** or **IMFVideoRenderer** interface. (These interfaces are documented in the Media Foundation SDK documentation.) For more information about configuring the video renderer in a DVD playback graph, see [Building the DVD Filter Graph](building-the-dvd-filter-graph.md).

The DVD Navigator will not use the EVR unless the decoder's [**IAMDecoderCaps::GetDecoderCaps**](/windows/desktop/api/Strmif/nf-strmif-iamdecodercaps-getdecodercaps) method returns the AM\_GETDECODERCAP\_QUERY\_EVR\_SUPPORT flag. This flag is defined to ensure that applications are compatible with existing decoders. If **RenderDvdVideoVolume** fails using the AM\_DVD\_EVR\_ONLY flag, fall back to another video renderer by calling the method again without the flag.

**Smooth Reverse Playback**

The DVD Navigator can now perform smooth reverse playback. In smooth reverse playback, the DVD Navigator sends entire video object units (VOBUs) to the decoder, and the decoder emits the frames in reverse order. This feature requires that the decoders support smooth reverse playback.

When the application sets the playback speed to a negative value, the DVD Navigator queries the decoders for the [**AM\_RATE\_ReverseMaxFullDataRate**](am-rate-reversemaxfulldatarate-property.md) property. The value of this property is the absolute value of the maximum reverse speed x 10000. For example, if the maximum reverse speed is -2.0, the value is 20000.

If the video decoder supports the property, the DVD Navigator uses smooth reverse playback. The audio stream is played in reverse if the audio decoder supports the property; otherwise, the audio stream is muted. If the video decoder does not support the property, or the playback rate exceeds the video decoder's maximum reverse rate, the DVD Navigator switches to *scan mode*. In scan mode, the DVD Navigator sends only I frames to the decoder and drops all B and P frames.

During smooth reverse playback, the DVD Navigator sends complete VOBUs to the decoder. The DVD Navigator sends the VOBUs in reverse order but sends the frames within each VOBU in their normal forward order. At the start of each VOBU, the DVD Navigator sets the AM\_ReverseBlockStart flag on the sample. At the end of the VOBU, the DVD Navigator sends an empty sample with the AM\_ReverseBlockEnd flag. To retrieve these flags, call [**IMediaSample2::GetProperties**](/windows/desktop/api/Strmif/nf-strmif-imediasample2-getproperties) on the sample. The flags are set in the **dwTypeSpecificFlags** member of the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-am_sample2_properties) structure.

The decoder caches the video data until it receives the sample with the AM\_ReverseBlockEnd flag. At that point, the decoder delivers decoded frames in reverse order. For example, if VOBU 1 contains frames 1–4 and VOBU 2 contains frames 5–8, the DVD Navigator will send the frames in this order:

(Block start) F5 F6 F7 F8 (block end) (block start) F1 F2 F3 F4 (block end)

The decoder should process the frames as follows:

1.  Decode VOBU 2.
2.  Output frames: F8 F7 F6 F5
3.  Decode VOBU 1.
4.  Output frames: F4 F3 F2 F1

The DVD Navigator sets the time stamp on the first sample in the VOBU (F1 and F5 in this example), but the time stamp contains the presentation time of the start of the block, so the decoder should apply this time to the last sample in the block (F4 and F8). Presentation times increase during reverse playback.

Typically a VOBU contains up to 42 frames and might contain more than one group of pictures (GOP). To enable the entire VOBU to be decoded, the decoder should cache the decoded I and P frames. VOBUs on DVDs are not closed GOPs, so a B frame within a GOP may require decoding all of the reference frames in the previous GOP. If the decoder does not have enough surfaces to hold all of the decoded frames, it might need to re-decode selected frames.

**Rate Changes**

By default, the DVD Navigator flushes the graph between rate changes. If the decoder supports the [**AM\_RATE\_ResetOnTimeDisc**](am-rate-resetontimedisc-property.md) property, however, the DVD Navigator will not flush the graph, resulting in a smoother transition between playback rates.

The DVD Navigator always time stamps samples for playback at 1x speed, regardless of the actual playback speed. The decoder must scale the time stamps on the decoded samples to match the actual playback speed. (For details, see [**AM\_RATE\_SimpleRateChange Property**](am-rate-simpleratechange-property.md).) As a result, when playing at speeds other than 1x, the time stamps on the decoded frames diverge from those on the encoded frames. Whenever the DVD Navigator sets the AM\_SAMPLE\_TIMEDISCONTINUITY flag on a sample, the decoder should resynchronize its time stamps. In other words, the decoded frame should have the same time stamp as the input frame. To retrieve the AM\_SAMPLE\_TIMEDISCONTINUITY flag, call [**IMediaSample2::GetProperties**](/windows/desktop/api/Strmif/nf-strmif-imediasample2-getproperties) on the sample. The flag is set in the **dwSampleFlags** member of the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-am_sample2_properties) structure.

**Power Management**

In Windows Vista, the DVD Navigator enables the following improvements to power management:

-   Higher timer resolution
-   Larger data cache

**Timer resolution**: Applications can request a minimum timer resolution by calling the **timeBeginPeriod** function. A higher resolution (shorter period) increases the system's responsiveness to periodic events, such as timeouts, but can also increase the frequency of thread context switches.

By default, the reference clock in DirectShow sets the timer resolution to 1 millisecond. At that resolution, the CPU will not enter any power-saving modes. Starting in Windows Vista, the DVD Navigator overrides the reference clock's default behavior by calling [**IReferenceClockTimerControl::SetDefaultTimerResolution**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclocktimercontrol-setdefaulttimerresolution) on the reference clock. This removes the clock's request for a 1-millisecond timer resolution. This might allow the CPU to enter a power-saving mode.

Timer resolution is a global setting; Windows picks the lowest requested value. The Video Mixing Renderer (VMR) filters (VMR-7 and VMR-9) set the timer resolution to 1 millisecond. The EVR typically sets the resolution to a value between 4 and 8 milliseconds, depending on the whether desktop composition is enabled and whether the EVR is in full-screen mode. Other applications might also set the resolution.

**Cache size**: Applications can specify how much data the DVD Navigator caches by setting the DVD\_CacheSizeInMB option in the [**IDvdControl2::SetOption**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-setoption) method. If the application sets this flag to a large value (> 50 MB), the DVD drive may spin down after the initial pre-fetch, depending on the hardware, which can reduce power consumption.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



