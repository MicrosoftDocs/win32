---
description: Time Stamps
ms.assetid: 445fe6b9-9d5b-45fd-9c9e-8c632c5228ae
title: Time Stamps
ms.topic: article
ms.date: 05/31/2018
---

# Time Stamps

The *time stamp* defines a media sample's start and finish times, measured in stream time. The time stamp is sometimes called the *presentation time*. When reading the rest of this article, it is important to remember that not all formats use time stamps in the same way. For example, not all MPEG samples are time stamped. In MPEG filter graphs, the time stamp is not applied to each frame until they are output from the decoder.

When a renderer filter receives a sample, it schedules rendering based on the time stamp. If the sample arrives late, or has no time stamp, the filter renders the sample immediately. Otherwise, the filter waits until the sample's start time before it renders the sample. (It waits for the start time by calling the [**IReferenceClock::AdviseTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-advisetime) method.)

Source filters and parser filters are responsible for setting the correct time stamps on the samples they process. Use the following guidelines.

-   File playback: The first sample is time stamped with a start time of zero. Subsequent time stamps are determined by the sample length and the playback rate, which itself is determined by the file format. The filter that parses the file is responsible for calculating the correct time stamps (for example, the [AVI Splitter](avi-splitter-filter.md)).
-   Video and audio capture: Every sample is time stamped with a start time equal to the stream time when it was captured, with the following caveats:
    -   Video frames from a preview pin (as opposed to a capture pin) are not time stamped. Because of graph latency, a video frame that is stamped with the capture time will always arrive late at the video renderer. This may cause the renderer to drop frames, in an attempt at quality control. For information about quality control, see [Quality-Control Management](quality-control-management.md).
    -   Audio capture: The audio capture filter uses its own set of buffers, which are separate from those used by the audio driver. The audio driver fills the capture filter's buffers at fixed intervals. The interval depends on the driver, but generally is not more than 10 milliseconds. The time stamps on the audio samples reflect the time when the driver filled the audio capture filter's buffers. These times can be slightly inaccurate, especially if the application is using a very small buffer size. However, the media times will accurately reflect the number audio samples in the buffer.
-   Mux filters: Depending on the output format, a mux filter may need to generate time stamps, or it may not. For example, the AVI file format uses a fixed frame rate with no time stamps, so the [AVI Mux](avi-mux-filter.md) filter assumes that samples are arriving at approximately the right time. If the incoming time stamps show a gap larger than one frame, however, the AVI Mux writes an index entry with size zero, to indicate a dropped frame. On file playback, new time stamps are generated at run time, as described previously.

To set the time stamp on a sample, call the [**IMediaSample::SetTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-settime) method.

**Media Times**

Optionally, the filter can also specify a *media time* for the sample. In a video stream, media time represents the frame number. In an audio stream, media time represents the sample number in the packet. For example, if each packet contains one second of 44.1 kilohertz (kHz) audio, the first packet has a media start time of zero and a media stop time of 44100. In a seekable stream, the media time is always relative to the start time of the stream. For example, suppose you seek to 2 seconds from the start of a 15-fps video stream. The first media sample after the seek has a time stamp of zero but a media time of 30.

Renderer and mux filters can use the media time to determine whether frames or samples have been dropped, by checking for gaps. However, filters are not required to set the media time. To set the media time on a sample, call the [**IMediaSample::SetMediaTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setmediatime) method.

## Related topics

<dl> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



