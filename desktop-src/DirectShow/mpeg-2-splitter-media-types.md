---
description: MPEG-2 Splitter Media Types
ms.assetid: d0ff2011-4ee3-4f5e-8bd0-af9f4c6346e8
title: MPEG-2 Splitter Media Types
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-2 Splitter Media Types

The [MPEG-2 Splitter](mpeg-2-splitter.md) filter currently supports audio and video. Dolby AC-3 is supported as a substream as defined by DVD. The filter also supports MPEG-2 audio. The media types depend on whether the MPEG-2 splitter is delivering PES packets or PES payloads.

### Video

For MPEG-2 video, the media types are as follows.



| Label | Value |
|------------------|------------------------------------------|--------------------------------|
|                  | PES output                               | Payload output                 |
| Major Type       | **MEDIATYPE\_MPEG2\_PES**                | **MEDIATYPE\_Video**           |
| Subtype          | **MEDIASUBTYPE\_MPEG2\_VIDEO**           | **MEDIASUBTYPE\_MPEG2\_VIDEO** |
| Format Type      | **FORMAT\_MPEG2Video**                   | **FORMAT\_MPEG2Video**         |
| Format Structure | [**MPEG2VIDEOINFO**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-mpeg2videoinfo) | **MPEG2VIDEOINFO**             |



 

### AC-3 Audio

For AC-3 audio, the media types are as follows.



| Label | Value |
|------------------|--------------------------------------|------------------------------|
|                  | PES output                           | Payload output               |
| Major Type       | MEDIATYPE\_MPEG2\_PES                | **MEDIATYPE\_Audio**         |
| Subtype          | MEDIASUBTYPE\_DOLBY\_AC3             | **MEDIASUBTYPE\_DOLBY\_AC3** |
| Format Type      | FORMAT\_WaveFormatEx                 | **FORMAT\_WaveFormatEx**     |
| Format Structure | [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) | **WAVEFORMATEX**             |



 

The **WAVEFORMATEX** structure's **wFormatTag** member for AC-3 is currently **WAVE\_FORMAT\_UNKNOWN**, but this might change.

### MPEG-2 Audio

For MPEG-2 audio, the media types are as follows.



| Label | Value |
|------------------|-------------------------------|--------------------------------|
|                  | PES output                    | Payload output                 |
| Major Type       | **MEDIATYPE\_MPEG2\_PES**     | **MEDIATYPE\_Audio**           |
| Subtype          | **MEDIASUBTYE\_MPEG2\_AUDIO** | **MEDIASUBTYPE\_MPEG2\_AUDIO** |
| Format Type      | **FORMAT\_WaveFormatEx**      | **FORMAT\_WaveFormatEx**       |
| Format Structure | **WAVEFORMATEX**              | **WAVEFORMATEX**               |



 

The **WAVEFORMATEX** structure's **wFormatTag** member for MPEG-2 Audio is currently **WAVE\_FORMAT\_UNKNOWN**, but this might change.

The MPEG-2 Splitter assumes that streams D0 through DF are used for the multichannel extension stream, as they are for DVD MPEG-2 audio. Therefore, whenever stream C *x* is selected, the splitter forwards the packets for stream D *x* as well.

### LPCM Audio

For LPCM audio, the media types are as follows.



| Label | Value |
|------------------|------------------------------------|------------------------------------|
|                  | PES output                         | Payload output                     |
| Major Type       | **MEDIATYPE\_MPEG2\_PES**          | **MEDIATYPE\_Audio**               |
| Subtype          | **MEDIASUBTYPE\_DVD\_LPCM\_AUDIO** | **MEDIASUBTYPE\_DVD\_LPCM\_AUDIO** |
| Format Type      | **FORMAT\_WaveFormatEx**           | **FORMAT\_WaveFormatEx**           |
| Format Structure | **WAVEFORMATEX**                   | **WAVEFORMATEX**                   |



 

The **WAVEFORMATEX** structure's **wFormatTag** member for LPCM audio is currently **WAVE\_FORMAT\_UNKNOWN**, but this might change.

## Related topics

<dl> <dt>

[MPEG-2 Media Types](mpeg-2-media-types.md)
</dt> </dl>

 

 
