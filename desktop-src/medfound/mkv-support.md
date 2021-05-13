---
description: This section describes the Media Foundation support for Matroska Media Container (MKV) files.
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
- Caption tracks are supported, but are not selected (played) by default.
- If one or more fonts or images are present, captions and images won’t render, although the file will load and play.
- Menu information is not supported and won’t be displayed, but the file will load and play.
- If files with chapters refer to supplemental files, the supplemental files won’t play.
- Thumbnail images are available when browsing for files on USB drives using the file browser.

This set of features should allow playback of most MKV files if they contain supported codecs.
MKV files that contain video and audio tracks encoded with the codecs listed in the following section are supported.

## Supported MKV codecs

### Video

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

Matroska ID: V_THEORA

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_Theora
- Description: Theora
- FourCC or WAV identifiers: theo

Matroska ID: V_MPEG4/ISO/SP

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_MP4V
- Description: MPEG4 ISO simple profile (DivX4)
- FourCC or WAV identifiers: MP4V

Matroska ID: V_MPEG4/ISO/A

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_MP4V
- Description: MPEG4 ISO advanced simple profile (DivX5, XviD, FFMPEG)
- FourCC or WAV identifiers: MP4V


Matroska ID: V_MPEGH/ISO/HEVC 

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_HEVC
- Description: HEVC/H.265
- FourCC or WAV identifiers: 

Matroska ID: V_VP8

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_VP80
- Description: VP8 Codec format
- FourCC or WAV identifiers: VP80

Matroska ID: V_VP9

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_VP90
- Description: VP9 Codec format
- FourCC or WAV identifiers: VP90

Matroska ID: V_MJPEG

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_MJPG
- Description: Motion JPEG
- FourCC or WAV identifiers: MJPG

Matroska ID: V_AV1

- MSFT Media Foundation MF_MT_SUBTYPE: MFVideoFormat_AV1
- Description: AOMedia Video 1
- FourCC or WAV identifiers: AV01

# Audio

Matroska ID: A_AAC

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_AAC
- Description: Advanced Audio Coding (AAC)
- FourCC or WAV identifiers: WAVE_FORMAT_MPEG_HEAAC

Matroska ID: A_AC3

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_Dolby_AC3
- Description: Dolby AC3
- FourCC or WAV identifiers: WAVE_FORMAT_DOLBY_AC3_SPDIF

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

Matroska ID: A_ALAC

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_ALAC
- Description: Apple Lossless Audio Codec
- FourCC or WAV identifiers: 

Matroska ID: A_MPEG/L2

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_MPEG
- Description: MPEG Audio 1, 2 Layer II
- FourCC or WAV identifiers: WAVE_FORMAT_MPEG

Matroska ID: A_DTS

- MSFT Media Foundation MF_MT_SUBTYPE: MEDIASUBTYPE_DTS_HD
- Description: Digital Theatre System
- FourCC or WAV identifiers: WAVE_FORMAT_DTS

Matroska ID: A_OPUS

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_Opus
- Description: Opus
- FourCC or WAV identifiers: WAVE_FORMAT_OPUS

Matroska ID: A_VORBIS

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_Vorbis
- Description: Vorbis
- FourCC or WAV identifiers: 

Matroska ID: A_FLAC

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_FLAC
- Description: Free Lossless Audio Codec
- FourCC or WAV identifiers: WAVE_FORMAT_FLAC

Matroska ID: A_AAC/MAIN

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_AAC
- Description: Advanced Audio Coding (AAC)
- FourCC or WAV identifiers: WAVE_FORMAT_MPEG_HEAAC

Matroska ID: A_EAC3

- MSFT Media Foundation MF_MT_SUBTYPE: MFAudioFormat_Dolby_DDPlus
- Description: Enhanced AC-3
- FourCC or WAV identifiers: 

Matroska ID: A_TRUEHD

- MSFT Media Foundation MF_MT_SUBTYPE: MEDIASUBTYPE_DOLBY_TRUEHD
- Description: Dolby TrueHD
- FourCC or WAV identifiers: 

Matroska ID: A_MS/ACM

- MSFT Media Foundation MF_MT_SUBTYPE: Maps to several WAVE_FORMAT audio types defined in mmreg.h


# Subtitles

Matroska ID: S_TEXT/ASCII

- MSFT Media Foundation MF_MT_SUBTYPE: MFSubtitleFormat_SRT
- Description: ASCII text

Matroska ID: S_TEXT/UTF8

- MSFT Media Foundation MF_MT_SUBTYPE: MFSubtitleFormat_SRT
- Description: UTF-8 Plain Text

Matroska ID: S_TEXT/SSA

- MSFT Media Foundation MF_MT_SUBTYPE: MFSubtitleFormat_SSA
- Description: Subtitles Format

Matroska ID: S_TEXT/ASS

- MSFT Media Foundation MF_MT_SUBTYPE: MFSubtitleFormat_SSA
- Description: Advanced Subtitles Format

Matroska ID: S_VOBSUB

- MSFT Media Foundation MF_MT_SUBTYPE: MFSubtitleFormat_VobSub
- Description: VobSub subtitles

Matroska ID: S_HDMV/PGS

- MSFT Media Foundation MF_MT_SUBTYPE: MFSubtitleFormat_PGS
- Description: HDMV presentation graphics subtitles (PGS)


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

 

 



