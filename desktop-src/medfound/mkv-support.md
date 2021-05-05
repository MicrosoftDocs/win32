---
description: This section describes the Media Foundation components that support MPEG-4 formats, including H.264 video, AAC audio, and the MP4 and 3GP file formats.
ms.assetid: a8fa05c6-74b4-408e-8390-9dcbafa012f1
title: Matroska Media Container (MKV) support
ms.topic: article
ms.date: 05/31/2018
---

# Matroska Media Container (MKV) support

This section describes the Media Foundation support for Matroska Media Container (MKV) files.

The MKV format can support multiple video and audio codecs, such as H.264 and AAC audio. In general, containers describe how video and audio data is laid out and what supplementary information is used to describe those A/V streams. Containers can also include data that complements A/V streams, such as the title, languages of the audio streams, subtitle or caption tracks, fonts for those subtitles, images, chapter information, and menus. MKV is a highly flexible format that supports many of these container features. For more info about the MKV format, see [https://matroska.org](https://matroska.org/)


## MKV container feature support
MKV container features are supported on the by Media Foundation in the following ways:
- If one or more video tracks are present, the first track will be played.
- If one or more audio tracks are present, the first track will be played.
- If one or more caption tracks are present, the captions won’t render, but the file will load and play.
- If one or more fonts or images are present, captions and images won’t render, although the file will load and play.
- Menu information is not supported and won’t be displayed, but the file will load and play.
- Chapter information is not supported, but the file will load and play.
- If files with chapters refer to supplemental files, the supplemental files won’t play.
- Thumbnail images are available when browsing for files on USB drives using the file browser.

This set of features should allow playback of most MKV files if they contain supported codecs.
MKV files that contain video and audio tracks encoded with the codecs listed in the following section are supported.

## Supported MKV codecs

Matroska ID: V_MPEG4/ISO/AVC
- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_H264
- Description: H.264 video
- FourCC or WAV identifiers: H264
Matroska ID: V_MPEG2
- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_MPEG2
- Description: MPEG-2 video
Matroska ID: V_MPEG1
- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_MPG1
- Description: MPEG-1 video
- FourCC or WAV identifiers: MPG1
Matroska ID: V_MPEG4/MS/V3
- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_MP43
- Description: Microsoft MPEG 4 codec version 3
- FourCC or WAV identifiers: MP43
Matroska ID: V_MPEG4/ISO/ASP
- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_MP4V
- Description: MPEG-4 part 2 video
- FourCC or WAV identifiers: MP4V
Matroska ID: V_MS/VFW/FOURCC
- Description: Maps to several codecs usually supported in the AVI format that are available on the console.
Matroska ID: A_AAC
- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_AAC
- Description: Advanced Audio Coding (AAC)
- FourCC or WAV identifiers: WAVE_FORMAT_MPEG_HEAAC
Matroska ID: A_AC3
- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_Dolby_AC3
- Description: Dolby Digital (AC-3)
Matroska ID: A_MPEG/L3
- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_MP3
- Description: MPEG Audio Layer-3 (MP3)
- FourCC or WAV identifiers: WAVE_FORMAT_MPEGLAYER3
Matroska ID: A_MPEG/L1
- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_MPEG
- Description: MPEG-1 audio payload
- FourCC or WAV identifiers: WAVE_FORMAT_MPEG
Matroska ID: A_PCM/INT/BIG
- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_PCM
- Description: Uncompressed PCM audio
- FourCC or WAV identifiers: WAVE_FORMAT_PCM
Matroska ID: A_PCM/INT/LIT
- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_PCM
- Description: Uncompressed PCM audio
- FourCC or WAV identifiers: WAVE_FORMAT_PCM
Matroska ID: A_PCM/FLOAT/IEEE
- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_Float
- Description: Uncompressed IEEE floating-point audio
- FourCC or WAV identifiers: WAVE_FORMAT_IEEE_FLOAT


## Technical details regarding codecs

See the following for technical details regarding codecs.

- [Matroska Codec Specs](http://www.matroska.org/technical/specs/codecid/index.html)
- [Audio Subtype GUIDs](audio-subtype-guids.md)
- [Video Subtype GUIDs](video-subtype-guids.md)


## Related topics

<dl> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> <dt>

[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> </dl>

 

 



