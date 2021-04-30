---
description: This section lists the media types used for MPEG-1 data.
ms.assetid: 4ea1cb84-0558-4c4a-9483-1b0f2a8f76f8
title: MPEG-1 Media Types
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-1 Media Types

This section lists the media types used for MPEG-1 data.

## MPEG-1 System Stream



| Label | Value |
|-----------------------|-------------------------------------------------|
| Major type            | MEDIATYPE\_Stream                               |
| Subtype               | MEDIASUBTYPE\_MPEG1System                       |
| Format Type           | FORMAT\_MPEGStreams                             |
| Format Structure      | [**AM\_MPEGSYSTEMTYPE**](/previous-versions/windows/desktop/api/mpegtype/ns-mpegtype-am_mpegsystemtype) |
| Media Sample Contents | Byte stream; no alignment                       |



 

## MPEG-1 System Stream from Video CD



| Label | Value |
|-----------------------|----------------------------|
| Major type            | MEDIATYPE\_Stream          |
| Subtype               | MEDIASUBTYPE\_MPEG1VideoCD |
| Format Type           | GUID\_NULL                 |
| Format Structure      | None                       |
| Media Sample Contents | Byte stream; no alignment. |



 

## MPEG-1 Audio Packet



| Label | Value |
|-----------------------|------------------------------------------------|
| Major type            | MEDIATYPE\_Audio                               |
| Subtype               | MEDIASUBTYPE\_MPEG1Packet                      |
| Format Type           | FORMAT\_WaveFormatEx                           |
| Format Structure      | [**MPEG1WAVEFORMAT**](/windows/desktop/api/mmreg/ns-mmreg-mpeg1waveformat)     |
| Media Sample Contents | Single MPEG-1 packet, including packet header. |



 

## MPEG-1 Audio Payload



| Label | Value |
|-----------------------|--------------------------------------------|
| Major type            | MEDIATYPE\_Audio                           |
| Subtype               | MEDIASUBTYPE\_MPEG1Payload                 |
| Format Type           | FORMAT\_WaveFormatEx                       |
| Format Structure      | [**MPEG1WAVEFORMAT**](/windows/desktop/api/mmreg/ns-mmreg-mpeg1waveformat) |
| Media Sample Contents | Byte-aligned MPEG-1 audio data.            |



 

## MPEG-1 Video Packet



| Label | Value |
|-----------------------|------------------------------------------------|
| Major type            | MEDIATYPE\_Video                               |
| Subtype               | MEDIASUBTYPE\_MPEG1Packet                      |
| Format Type           | FORMAT\_MPEGVideo                              |
| Format Structure      | [**MPEG1VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-mpeg1videoinfo)       |
| Media Sample Contents | Single MPEG-1 packet, including packet header. |



 

## MPEG-1 Video payload



| Label | Value |
|-----------------------|------------------------------------------|
| Major type            | MEDIATYPE\_Video                         |
| Subtype               | MEDIASUBTYPE\_MPEG1Payload               |
| Format Type           | FORMAT\_MPEGVideo                        |
| Format Structure      | [**MPEG1VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-mpeg1videoinfo) |
| Media Sample Contents | Byte-aligned MPEG-1 video data.          |



 

## MPEG-1 Native Video Stream



| Label | Value |
|-----------------------|------------------------------------------------|
| Major type            | MEDIATYPE\_Stream                              |
| Subtype               | MEDIASUBTYPE\_ MPEG1Video                      |
| Format Type           | GUID\_NULL                                     |
| Format Structure      | None                                           |
| Media Sample Contents | Array of video stream bytes (no system layer). |



 

## MPEG-1 Native Audio Stream



| Label | Value |
|-----------------------|------------------------------------------------|
| Major type            | MEDIATYPE\_Stream                              |
| Subtype               | MEDIASUBTYPE\_ MPEG1Audio                      |
| Format Type           | GUID\_NULL                                     |
| Format Structure      | None                                           |
| Media Sample Contents | Array of audio stream bytes (no system layer). |



 

## Remarks

The DirectShow MPEG-1 filters support these types as follows.



| Filter               | Direction | Supported media types                                                                                             |
|----------------------|-----------|-------------------------------------------------------------------------------------------------------------------|
| MPEG-1 Splitter      | Input     | MPEG-1 system streamMPEG-1 system stream from Video CD<br/>                                                 |
| MPEG-1 Splitter      | Output    | MPEG-1 Audio packetMPEG-1 Audio payload<br/> MPEG-1 Video packet<br/> MPEG-1 Video payload<br/> |
| Software Audio Codec | Input     | MPEG-1 Audio packetMPEG-1 Audio payload<br/>                                                                |
| Software Video Codec | Input     | MPEG-1 Video packetMPEG-1 Video payload<br/>                                                                |
| Software Audio Codec | Output    | PCM audio                                                                                                         |
| Software Video Codec | Output    | Uncompressed video (Y41P, YUY2, UYVY, RGB-24, RGB-32, RGB-565, RGB-555, RGB-8)                                    |



 

MPEG-1 Video packet and payload media types contain a complete sequence header so that data can be played from the middle of a file without needing a sequence header to initialize the video playback.

The video sequence header is appended to the video data type for MPEG video so that play can begin from the middle of a stream. The length of this field is up to 140 bytes; it includes the sequence header start code (0x000001B3) at the start, along with any quantization matrices found in the first sequence header encountered.

 

 




