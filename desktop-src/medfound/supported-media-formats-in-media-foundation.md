---
description: This topic lists the media formats that Microsoft Media Foundation supports natively.
ms.assetid: 69c12a28-4b58-4979-b4d8-ae37efa847fe
title: Supported Media Formats in Media Foundation
ms.topic: article
ms.date: 05/31/2018
---

# Supported Media Formats in Media Foundation

This topic lists the media formats that Microsoft Media Foundation supports natively. Third parties can support additional formats by writing custom plug-ins.

## File Containers



| Format                                           | File Extensions          | Media Source                                 | Media Sink                                   | Requires                                                              |
|--------------------------------------------------|--------------------------|----------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------|
| 3GP                                              | .3g2, .3gp, .3gp2, .3gpp | [MPEG-4 File Source](mpeg-4-file-source.md) | 3GP File Sink                                | Windows 7                                                             |
| Advanced Streaming Format (ASF)                  | .asf, .wma, .wmv         | [ASF Media Source](asf-media-source.md)     | [ASF Media Sink](asf-media-sinks.md)        | Windows Vista                                                         |
| Audio Data Transport Stream (ADTS).              | .aac, .adts              | ADTS File Source                             | None                                         | Windows 7                                                             |
| AVI                                              | .avi                     | AVI File Source                              | None                                         | Windows 7                                                             |
| MP3                                              | .mp3                     | [**MP3 File Source**](mp3-file-source.md)   | MP3 File Sink                                | File source: Windows Vista<br/> File sink: Windows 7<br/> |
| MPEG-4                                           | .m4a, .m4v, .mov, .mp4   | [MPEG-4 File Source](mpeg-4-file-source.md) | [**MPEG-4 File Sink**](mpeg-4-file-sink.md) | Windows 7                                                             |
| Synchronized Accessible Media Interchange (SAMI) | .sami, .smi              | [SAMI Media Source](sami-media-source.md)   | None                                         | Windows Vista                                                         |
| WAVE                                             | .wav                     | AVI File Source                              | None                                         | Windows 7                                                             |



 

## Audio Codecs



| Format                                              | Decoder                                                                                                                                                          | Encoder                                                                                                                                                          | Requires      |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| μ-law Coding                                        | Audio Compression Manager (ACM) μ-law Codec                                                                                                                      | None                                                                                                                                                             | Windows Vista |
| Adaptive Differential Pulse Code Modulation (ADPCM) | ACM ADPCM Codec                                                                                                                                                  | None                                                                                                                                                             | Windows Vista |
| Advanced Audio Coding (AAC)                         | [**AAC Decoder**](aac-decoder.md)                                                                                                                               | [**AAC Encoder**](aac-encoder.md)                                                                                                                               | Windows 7     |
| MP3                                                 | [**Windows Media MP3 Decoder**](windows-media-mp3-decoder.md)                                                                                                   | None                                                                                                                                                             | Windows Vista |
| GSM 6.10                                            | ACM GSM 6.10 Codec                                                                                                                                               | None                                                                                                                                                             | Windows Vista |
| Windows Media Audio (WMA)                           | [**Windows Media Audio Decoder**](windowsmediaaudiodecoder.md)<br/> [**Windows Media Audio Voice Decoder**](windowsmediaaudiovoicedecoder.md)<br/> | [**Windows Media Audio Encoder**](windowsmediaaudioencoder.md)<br/> [**Windows Media Audio Voice Encoder**](windowsmediaaudiovoiceencoder.md)<br/> | Windows Vista |



 

> [!Note]  
> Media Foundation provides wrappers for several ACM codecs, listed in the previous table. However, Media Foundation does not support arbitrary ACM codecs.

 

## Video Codecs



| Format                                                                                                         | Decoder                                                                                                                                                                  | Encoder                                                                                                                             | Requires      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------|
| DV Video                                                                                                       | [**DV Video Decoder**](dv-video-decoder.md)                                                                                                                             | None                                                                                                                                | Windows 7     |
| H.264                                                                                                          | [**H.264 Video Decoder**](h-264-video-decoder.md)                                                                                                                       | [**H.264 Video Encoder**](h-264-video-encoder.md)                                                                                  | Windows 7     |
| H.263<br/> (H.264 baseline profile which is compatible to MPEG-4 Pt2 short video header mode)<br/> | [**MPEG-4 Part 2 Video Decoder**](mpeg4part2videodecoder.md)                                                                                                            | None                                                                                                                                | Windows 8     |
| MJPEG                                                                                                          | MJPEG Decoder                                                                                                                                                            | None                                                                                                                                | Windows 7     |
| MPEG-4 Part 2                                                                                                  | [**MPEG-4 Part 2 Video Decoder**](mpeg4part2videodecoder.md)                                                                                                            | None                                                                                                                                | Windows 7     |
| MPEG-4 v1/v2/v3                                                                                                | [**Windows Media MPEG-4 V3 Decoder**](./windowsmediampeg4v3decoder.md)<br/> [**Windows Media MPEG4 V1/V2 Decoder**](windowsmediampeg4decoder.md)<br/>         | None                                                                                                                                | Windows Vista |
| Windows Media Video (WMV)                                                                                      | [**Windows Media Video 9 Decoder**](windowsmediavideo9decoder.md)<br/> [**Windows Media Video 9 Screen Decoder**](windowsmediavideo9screendecoder.md)<br/> | Windows Media Video 9 Encoder<br/> Windows Media Video 9 Screen Encoder<br/> Windows Media Video 7/8 Encoder<br/> | Windows Vista |



 

> [!Note]  
> The "Requires" column lists the minimum operating system needed to uses these codecs within a Media Foundation application. Some of these codecs were introduced prior to Windows Vista as [DirectX Media Objects](../directshow/directx-media-objects.md) (DMOs). If a codec supports DMO functionality, it can be used with [DirectShow](../directshow/directshow.md) or the [Windows Media Format SDK](../wmformat/windows-media-format-11-sdk.md).

 

## Related topics

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> <dt>

[Media Sources and Sinks](media-sources-and-sinks.md)
</dt> </dl>

 

 
