---
description: Supported Formats in DirectShow
ms.assetid: cd8af779-2fb5-4724-a838-5d0c8244f0d3
title: Supported Formats in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Supported Formats in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow is an open architecture, which means that it can support any format as long as there are filters to parse and decode it. The filters provided by Microsoft, either as redistributables through DirectShow or as Windows operating system components, provide default support for the following file and compression formats.

File types:



| File Type                                                                                        | More Information                                                                                                                  |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Advanced Systems Format (ASF), including Windows Media Audio (WMA) and Windows Media Video (WMV) | [WM ASF Reader Filter](about-the-wm-asf-reader-filter.md)<br/> [WM ASF Writer Filter](wm-asf-writer-filter.md)<br/> |
| AIFF                                                                                             | [WAVE Parser Filter](wave-parser-filter.md)                                                                                      |
| AU                                                                                               | [WAVE Parser Filter](wave-parser-filter.md)                                                                                      |
| Audio-Video Interleaved (AVI)                                                                    | [AVI Mux Filter](avi-mux-filter.md)<br/> [AVI Splitter Filter](avi-splitter-filter.md)<br/>                         |
| MIDI                                                                                             | [MIDI Parser Filter](midi-parser-filter.md)<br/> [**MIDI Renderer Filter**](midi-renderer-filter.md)<br/>           |
| SND                                                                                              |                                                                                                                                   |
| WAV                                                                                              | [WAVE Parser Filter](wave-parser-filter.md)                                                                                      |



 

Compression formats:



| Format                                        | More Information                                                                                                                                                                                                                                |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AAC                                           | [**Microsoft MPEG-1/DD/AAC Audio Decoder**](microsoft-mpeg-1-dd-audio-decoder.md)                                                                                                                                                              |
| Cinepak                                       |                                                                                                                                                                                                                                                 |
| Digital Video (DV)                            | [DV Video Decoder Filter](dv-video-decoder-filter.md)<br/> [DV Video Encoder Filter](dv-video-encoder-filter.md)<br/>                                                                                                             |
| H.264                                         | [**Microsoft MPEG-2 Video Decoder**](microsoft-mpeg-2-video-decoder.md)                                                                                                                                                                        |
| ISO MPEG-4 video version 1.0                  |                                                                                                                                                                                                                                                 |
| Microsoft MPEG-4 version 3                    |                                                                                                                                                                                                                                                 |
| MJPEG                                         | [MJPEG Compressor Filter](mjpeg-compressor-filter.md)<br/> [MJPEG Decompressor Filter](mjpeg-decompressor-filter.md)<br/>                                                                                                         |
| MPEG Audio Layer-3 (MP3) (decompression only) |                                                                                                                                                                                                                                                 |
| MPEG-1 layer I and layer II audio             | [**Microsoft MPEG-1/DD/AAC Audio Decoder**](microsoft-mpeg-1-dd-audio-decoder.md)<br/> [MPEG-1 Audio Decoder Filter](mpeg-1-audio-decoder-filter.md)<br/>                                                                         |
| MPEG-1 video                                  | [MPEG-1 Video Decoder Filter](mpeg-1-video-decoder-filter.md)<br/> [**Microsoft MPEG-2 Video Decoder**](microsoft-mpeg-2-video-decoder.md)<br/>                                                                                   |
| MPEG-2 audio                                  | [**Microsoft MPEG-2 Audio Encoder**](microsoft-mpeg-2-audio-encoder.md)<br/> [**Microsoft MPEG-2 Encoder**](microsoft-mpeg-2-encoder.md)<br/>                                                                                     |
| MPEG-2 video                                  | [**Microsoft MPEG-2 Encoder**](microsoft-mpeg-2-encoder.md)<br/> [**Microsoft MPEG-2 Video Decoder**](microsoft-mpeg-2-video-decoder.md)<br/> [**Microsoft MPEG-2 Video Encoder**](microsoft-mpeg-2-video-encoder.md)<br/> |



 

For information on the availability of particular third-party codecs for redistribution with DirectShow applications, contact the codec manufacturer.

 

 




