---
description: DV Splitter Filter
ms.assetid: 099d1cc7-f0c5-4c50-a1d5-f2defde7e104
title: DV Splitter Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DV Splitter Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This filter splits an interleaved digital video (DV) stream into its component video and audio streams.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IDVSplitter**](/windows/desktop/api/Strmif/nn-strmif-idvsplitter)                                                                             |
| Input Pin Media Types                    | MEDIATYPE\_Interleaved, MEDIASUBTYPE\_dvsd, FORMAT\_DvInfo                                                                                         |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                             |
| Output Pin Media Types                   | **Video**: MEDIATYPE\_Video, FORMAT\_DvInfo<br/> **Audio**: MEDIATYPE\_Audio, MEDIASUBTYPE\_PCM, FORMAT\_WaveFormatEx<br/>             |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) |
| Filter CLSID                             | CLSID\_DVSplitter                                                                                                                                  |
| Property Page CLSID                      | No property page.                                                                                                                                  |
| Executable                               | qdv.dll                                                                                                                                            |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                                                                                      |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Remarks

DV frames contain audio and video in the same frame. The DV Splitter filter extracts the audio data and delivers it as one or two audio streams, from the audio output pins. The original DV frame is delivered from the video output pin, as a video frame. The media type on the video frame is changed from MEDIATYPE\_Interleaved to MEDIATYPE\_Video, but otherwise the data is not modified. The media type is changed to signal that the audio data into the frame should be ignored. The DV Splitter does not set a media time on its output samples; if you are writing a downstream filter that requires the media times, then you can derive the times from the frame count.

Only one output pin at a time exposes the [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) and [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interfaces.

The DV Splitter filter can accept dynamic format changes in the audio stream. However, if the [AVI Mux](avi-mux-filter.md) filter is downstream, it will reject the format change. If this happens, the DV Splitter stops producing an audio stream. This limitation only affects type-2 file capture. For type-1 files, the interleaved stream is not split in the first place. For preview, there is no AVI Mux filter downstream.

If the DV source is a live camera, there is normally no reason for the audio format to change. However, the format might change if you transmit from a VTR tape that contains several heterogeneous sources.

Each DV frame contains metadata, in addition to the audio and video data. This metadata can change from frame to frame. Applications can parse the metadata by examining either the input samples or the video output samples. However, DirectShow does not provide any direct support for parsing DV metadata. Consult IEC 61834-4 for more information.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> </dl>

 

 




