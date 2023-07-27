---
description: DirectShow Video Capture Filters
ms.assetid: e4d1452d-ceac-4b5c-b9ba-ad4722ecff76
title: DirectShow Video Capture Filters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DirectShow Video Capture Filters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Capture filters in DirectShow have some features that distinguish them from other kinds of filters. Although the [Capture Graph Builder](capture-graph-builder.md) hides many of the details, it is a good idea to read this section, in order to have a general understanding of DirectShow capture graphs.

**Pin Categories**

A capture filter often has two or more output pins that deliver the same kind of data—for example, a preview pin and a capture pin. Therefore, media types are not a good way to distinguish the pins. Instead, the pins are distinguished by their functionality, which is identified using a GUID, called the *pin category*.

For a discussion of how to query pins for their category, see [Working with Pin Categories](working-with-pin-categories.md). For most applications, however, you will not have to query pins directly. Instead, various [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) methods take parameters that specify the pin category on which to operate. The Capture Graph Builder automatically locates the correct pin.

**Preview Pins and Capture Pins**

Some video capture devices have separate output pins for preview and capture. The preview pin is used to render video to the screen, while the capture pin is used to write video to a file.

A preview pin and a capture pin have the following differences:

-   A preview pin drops frames as needed to maintain throughput on the capture pin.
-   Each frame from a capture pin is time-stamped with the stream time when the frame was captured. A preview pin does not time stamp the samples it delivers.

The reason that preview frames do not have time stamps is that the filter graph introduces a small amount of latency into the stream. If the capture time is used as the presentation time, the video renderer treats every sample as being slightly late. This can cause the video renderer to drop frames while it tries to catch up. Removing the time stamps ensures that the renderer presents each sample when it arrives, without dropping frames.

The pin category for preview pins is PIN\_CATEGORY\_PREVIEW. The category for capture pins is PIN\_CATEGORY\_CAPTURE.

**Video Port Pins**

A video port is a hardware connection between a video device (such as an analog TV tuner) and the video card. A video port enables the device to send video data directly to the graphics card. The video is displayed on the screen using a hardware overlay. A video port might be an actual cable that connects two devices on separate cards; or it might be a hard-wired connection on the same card.

The advantage of a video port is that the video goes directly into video memory, without any work by the CPU. However, video ports have some drawbacks:

-   A video port always uses the overlay surface during capture, regardless of whether you want to preview the video.
-   Flipping between frames occurs automatically, which makes it difficult to synchronize the flip with other video operations.

If a capture device uses a video port, the capture filter has a video port pin instead of a preview pin. The pin category for video port pins is PIN\_CATEGORY\_VIDEOPORT.

Every capture filter has at least one capture pin. In addition it might have a preview pin or a video port pin, but never both. Filters can have multiple capture pins and preview pins, each delivering a separate media type. Thus, a single filter could have a video capture pin, a video preview pin, an audio capture pin, and an audio preview pin. (There is nothing equivalent to a video port for audio, however.)

**Upstream WDM Filters**

Windows Driver Model (WDM) devices may require some additional filters upstream from the capture filter. These filters include the following:

-   [TV Tuner Filter](tv-tuner-filter.md). Controls tuning for analog TV tuners.
-   [TV Audio Filter](tv-audio-filter.md). Controls audio settings for analog TV tuners.
-   [Analog Video Crossbar Filter](analog-video-crossbar-filter.md). Routes video and audio signals through the hardware device. For example, a device might have multiple inputs, such as S-Video and composite video. The crossbar filter enables the application to select the input.

Although these are separate filters in DirectShow, they typically represent the same hardware device. Each filter controls a different function of the device. The filters are connected by pins, but no media data moves across the pin connections. Therefore, the pins on these filters do not connect by establishing a media type. Instead, they use GUID values called *mediums*. Medium GUIDs are uniquely defined for a given device minidriver. For example, the TV Tuner filter and the Video Capture filter for the same TV card will both support the same medium, which enables the application to build the graph correctly.

In practice, as long as you are using **ICaptureGraphBuilder2** to build your capture graphs, these filters are added to the graph automatically. For a more detailed discussion, see [WDM Class Driver Filters](wdm-class-driver-filters.md).

## Related topics

<dl> <dt>

[About Video Capture in DirectShow](about-video-capture-in-directshow.md)
</dt> </dl>

 

 



