---
Description: DV Muxer Filter
ms.assetid: 4dd57202-f4de-40d9-b720-efaba8a60a7c
title: DV Muxer Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DV Muxer Filter

This filter combines a digital video (DV)—encoded video stream with one or two audio streams to produce an interleaved DV stream. To write the stream to an AVI file, connect this filter to the [AVI Mux](avi-mux-filter.md) filter and connect the *AVI Mux* to the [File Writer](file-writer-filter.md) filter. For more information, see [Digital Video in DirectShow](digital-video-in-directshow.md).



|                                          |                                                                                                                                        |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master)                                                             |
| Input Pin Media Types                    | **Video**: MEDIATYPE\_Video, MEDIASUBTYPE\_dvsd, FORMAT\_VideoInfo**Audio**: MEDIATYPE\_Audio, MEDIASUBTYPE\_PCM, FORMAT\_WaveFormatEx |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                 |
| Output Pin Media Types                   | MEDIATYPE\_Interleaved, MEDIASUBTYPE\_dvsd, FORMAT\_DvInfo                                                                             |
| Output Pin Interfaces                    | [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                       |
| Filter CLSID                             | CLSID\_DVMux                                                                                                                           |
| Property Page CLSID                      | No property page                                                                                                                       |
| Executable                               | qdv.dll                                                                                                                                |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                        |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                          |



 

## Remarks

The DV Muxer can create two audio input pins. It supports the audio formats shown in the following table.



Audio Pin 1

Audio Pin 2

Output Format

Sample Rate (kHz)

Bits/Sample

Channels

Sample Rate

Bits/Sample

Channels

32

16

Mono

Unconnected

SD 2 Channel

32

16

Stereo

Unconnected

SD 4 Channel

44.1 or 48

16

Stereo or Mono

Unconnected

SD 2 Channel

Unconnected

32

16

Stereo or Mono

Disallowed

Unconnected

44.1 or 48

16

Mono

Disallowed

Unconnected

44.1 or 48

16

Stereo

SD 2 Channel

32

16

Mono

32

16

Mono

SD 2 Channel

32

16

Stereo or Mono\*

32

16

Stereo or Mono\*

SD 4 Channel

44.1

16

Mono

44.1

16

Mono

SD 2 Channel

48

16

Mono

48

16

Mono

SD 2 Channel

\* If at least one input pin is stereo.



 

For the purpose of this table, audio pin 1 is defined as the first input pin connected to an audio source, and audio pin 2 is defined as the second input pin connected to an audio source. Once an audio pin is connected, this numbering scheme remains in effect unless both audio pins are disconnected. For example, if you connect both audio pins and then disconnect audio pin 1, the remaining pin is still considered pin 2.

Audio supplied to pin 1 is recorded to the first audio block of the DV frames (CH1), and audio supplied to pin 2 is recorded to the second audio block (CH2). Exception: if the filter has a single stereo input at 44.1 kHz or 48 kHz, the left audio channel is recorded to the first audio block, and the right audio channel is recorded to the second audio block.

For SD 4-channel output: If the input is stereo, the left track is recorded to CHa or CHc, and the right track is recorded to CHb or CHd. If the input is mono, the audio is recorded to CHa or CHc, and CHb and CHd are silent.

By connecting and disconnecting audio pin 1, it is possible to reach a disallowed format. In that case, the filter's [**IMediaFilter::Pause**](/windows/win32/Strmif/nf-strmif-imediafilter-pause?branch=master) method returns VFW\_E\_NOT\_CONNECTED. This limitation prevents a situation in which the first audio block has no audio, but the second audio block does have audio. The second block should have audio only if the first block also has audio.

The DV Muxer does not permit audio inputs with different sampling rates. However, graph-building methods such as [**IGraphBuilder::Connect**](/windows/win32/Strmif/nf-strmif-igraphbuilder-connect?branch=master) will typically add the [ACM Wrapper](acm-wrapper-filter.md) filter, which will convert the second audio stream to match the first stream's sampling rate.

If the audio input is 48 kHz or 32 kHz, the audio output is locked. (It is not possible to lock 44.1-kHz audio.)

If no audio pins are connected, the output contains the audio data from the incoming DV frames. This might be silence, or valid audio data.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> </dl>

 

 



