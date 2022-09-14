---
description: Using the MPEG-2 Splitter
ms.assetid: a08e079c-41be-475a-9e88-ee46d17fe938
title: Using the MPEG-2 Splitter
ms.topic: article
ms.date: 05/31/2018
---

# Using the MPEG-2 Splitter

> [!Note]  
> Starting in Microsoft® Windows® XP, the MPEG-2 Splitter filter is deprecated. Use the [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) instead.

 

The MPEG-2 Splitter filter supports pull-mode playback of MPEG-2 program streams that contain at least one of the following stream types.

-   MPEG-2 video
-   MPEG-2 audio
-   Dolby AC-3 audio encoded as defined for DVD-Video
-   LPCM (Linear Pulse Code Modulated) audio encoded as defined for DVD-Video

For a list of media types that the MPEG-2 Splitter supports, see [MPEG-2 Splitter Media Types](mpeg-2-splitter-media-types.md).

The MPEG-2 Splitter does not parse transport streams. Use the MPEG-2 Demultiplexer filter for transport streams (push mode only).

**Time Stamps**

When playing back MPEG-2 program streams, the MPEG-2 Splitter filter treats the first system clock reference it encounters as the time origin of any stream. This differs from the [MPEG-1 Stream Splitter](mpeg-1-stream-splitter-filter.md), which uses presentation time stamps. The [**IAMParse::GetParseTime**](/previous-versions/windows/desktop/api/Amparse/nf-amparse-iamparse-getparsetime) method returns the (possibly estimated) stream system clock time for the data it has processed.

If the MPEG-2 splitter filter encounters an input sample with the discontinuity property set (the discontinuity property can be set by using [**IMediaSample::SetDiscontinuity**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setdiscontinuity) or [**IMediaSample2::SetProperties**](/windows/desktop/api/Strmif/nf-strmif-imediasample2-setproperties)), it skips data until it finds the first pack in the data and adjusts its time stamps so that the system clock reference (SCR) for that pack is considered identical to the SCR time before the discontinuity. If the SCR clock appears either to jump backward or to jump forward by more than a second, then (in line with the MPEG-2 program stream specification), this is also treated as a clock discontinuity and the apparent clock discrepancy is subtracted from the time stamps passed to downstream filters.

**Stream Selection**

When playing back the MPEG-2 program stream, the first video stream and first audio stream found traversing the program stream are chosen. Up to one audio and one video output pin are supported. Through the [**IAMStreamSelect**](/windows/desktop/api/Strmif/nn-strmif-iamstreamselect) interface, different streams of the same type can be selected up to the number specified by the audio limit in the system header. For MPEG-2 audio, it is currently assumed the streams form a contiguous range starting at stream 0xC0.

**Supported Interfaces**

The MPEG-2 splitter filter supports the following interfaces.

-   [**IAMParse**](/previous-versions/windows/desktop/api/Amparse/nn-amparse-iamparse). MPEG-2 program stream only.
-   [**IAMStreamSelect**](/windows/desktop/api/Strmif/nn-strmif-iamstreamselect). MPEG-2 program stream only, audio streams only.
-   [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking). Includes byte mode seeking.

## Related topics

<dl> <dt>

[MPEG-2 Support in DirectShow](mpeg-2-support-in-directshow.md)
</dt> </dl>

 

 



