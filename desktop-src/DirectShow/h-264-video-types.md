---
description: H.264 Video Types
ms.assetid: aa3166b2-6b04-44fa-bc9d-c8ff46f99201
title: H.264 Video Types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# H.264 Video Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following media subtypes are defined for H.264 video.



| Subtype                | FOURCC | Description                                                    |
|------------------------|--------|----------------------------------------------------------------|
| **MEDIASUBTYPE\_AVC1** | 'AVC1' | H.264 bitstream without start codes.                           |
| **MEDIASUBTYPE\_H264** | 'H264' | H.264 bitstream with start codes.                              |
| **MEDIASUBTYPE\_h264** | 'h264' | Equivalent to **MEDIASUBTYPE\_H264**, with a different FOURCC. |
| **MEDIASUBTYPE\_X264** | 'X264' | Equivalent to **MEDIASUBTYPE\_H264**, with a different FOURCC. |
| **MEDIASUBTYPE\_x264** | 'x264' | Equivalent to **MEDIASUBTYPE\_H264**, with a different FOURCC. |



 

These subtype GUIDs are declared in wmcodecdsp.h.

The main difference between these media types is the presence of start codes in the bitstream. If the subtype is **MEDIASUBTYPE\_AVC1**, the bitstream does not contain start codes.

### H.264 Bitstream with Start Codes

H.264 bitstreams that are transmitted over the air, or contained in MPEG-2 program or transport streams, or recorded on HD-DVD, are formatted as described in Annex B of ITU-T Rec. H.264. According to this specification, the bitstream consists of a sequence of network abstraction layer units (NALUs), each of which is prefixed with a start code equal to 0x000001 or 0x00000001.

When start codes are present in the bitstream, the following media type is used:



| Label | Value |
|-------------|---------------------------------------------------------------------------------------------------|
| Major type  | **MEDIATYPE\_Video**                                                                              |
| Subtypes    | **MEDIASUBTYPE\_H264**, **MEDIASUBTYPE\_h264**, **MEDIASUBTYPE\_X264**, or **MEDIASUBTYPE\_x264** |
| Format type | **FORMAT\_VideoInfo**, **FORMAT\_VideoInfo2**, **FORMAT\_MPEG2Video**, or **GUID\_NULL**          |



 

If the format type is **GUID\_NULL**, no format structure is present.

When the bitstream contains start codes, any of the format types listed here is sufficient, because the decoder does not require any additional information to parse the stream. The bitstream already contains all of the information needed by the decoder, and the start codes enable the decoder to locate the start of each NALU.

The following subtypes are equivalent:

### H.264 Bitstream Without Start Codes

The MP4 container format stores H.264 data without start codes. Instead, each NALU is prefixed by a length field, which gives the length of the NALU in bytes. The size of the length field can vary, but is typically 1, 2, or 4 bytes.

When start codes are not present in the bitstream, the following media type is used.



| Label | Value |
|-------------|------------------------|
| Major type  | **MEDIATYPE\_Video**   |
| Subtype     | **MEDIASUBTYPE\_AVC1** |
| Format type | **FORMAT\_MPEG2Video** |



 

The format block is an [**MPEG2VIDEOINFO**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-mpeg2videoinfo) structure. This structure should be filled in as follows:

-   **hdr**: A [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) structure that describes the bitstream. No color table is present after the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) portion of the structure, and **biClrUsed** must be zero.
-   **dwStartTimeCode**: Not used. Set to zero.
-   **cbSequenceHeader**: The length of the **dwSequenceHeader** array in bytes.
-   **dwProfile**: Specifies the H.264 profile.
-   **dwLevel**: Specifies the H.264 level.
-   **dwFlags**: The number of bytes used for the length field that appears before each **NALU**. The length field indicates the size of the following NALU in bytes. For example, if **dwFlags** is 4, each NALU is preceded by a 4-byte length field. The valid values are 1, 2, and 4.
-   **dwSequenceHeader**: A byte array that may contain sequence parameter set (SPS) and picture parameter set (PPS) NALUs.

The MP4 container might contain sequence parameter sets (SPS) or picture parameter sets (PPS) as special NAL units in file headers or in a separate stream (distinct from the video stream). When the format is established, the media type can specify SPS and PPS NAL units in the **dwSequenceHeader** array. If **cbSequenceHeader** is greater than zero, **dwSequenceHeader** is the start of a byte array containing SPS and PPS NALUs, delimited by 2-byte length fields, all in network byte order (big-endian). It is possible to have both SPS and PPS, only one of these types, or none. The actual type of each NALU can be determined by examining the **nal\_unit\_type** field of the NALU itself.

When this media type is used, each media sample starts at the beginning of a NALU, and NAL units do not span samples. This enables the decoder to recover from data corruption or dropped samples.

 

 



