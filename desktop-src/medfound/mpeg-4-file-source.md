---
description: The MPEG-4 file source parses MP4 and 3GPP files.
ms.assetid: e64c1554-9702-4cc0-98ad-8a33e04ed09d
title: MPEG-4 File Source
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-4 File Source

The MPEG-4 file source parses MP4 and 3GPP files. For more information about the MP4 file format, refer to the following standards documents:

-   ISO/IEC 14496-12: *Information technology -- Coding of audio-visual objects -- Part 12: ISO Base Media File Format*
-   ISO/IEC 14496-14: *Information technology -- Coding of audio-visual objects -- Part 14: MP4 File Format*

> [!Note]  
> (These resources may not be available in some languages and countries.)

 

The MPEG-4 file source does not decode the audio/video data in the file.

This topic contains the following sections:

## File Extensions and MIME Types

The MPEG-4 file source is the default media source for the following file name extensions.



| File extension | Description           |
|----------------|-----------------------|
| .3g2           | 3GPP2                 |
| .3gp           | 3GPP                  |
| .3gp2          | 3GPP2                 |
| .3gpp          | 3GPP                  |
| .m4a           | MPEG-4 audio          |
| .m4v           | MPEG-4 video          |
| .mov           | Apple QuickTime Movie |
| .mp4           | MPEG-4 audio or video |
| .mp4v          | MPEG-4 video          |



 

It is also the default media source for the following MIME types.



| MIME type   | Description  |
|-------------|--------------|
| audio/3gpp  | 3GPP audio   |
| audio/3gpp2 | 3GPP2 audio  |
| audio/mp4   | MPEG-4 audio |
| video/3gpp  | 3GPP video   |
| video/3gpp2 | 3GPP2 video  |
| video/mp4   | MPEG-4 video |



 

## Media Types

MP4 is an extensible container format. The MP4 specification does not define a fixed structure for describing media types in an MP4 container. Instead, it defines an object hierarchy that allows custom structures to be defined for each format. The format description is stored in the sample description ('stsd') box for that stream. The sample description box contains a list of sample entries. For each sample entry, a 4-byte code, similar to a FOURCC, defines the format structure.

This extensibility means the MPEG-4 file source cannot recognize every possible format description. Instead, it takes a two-tiered approach when creating media types for the streams. At a minimum, every media type contains the following attributes.



| Attribute                                                                     | Description                                                    |
|-------------------------------------------------------------------------------|----------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md)                     | Equal to **MFMediaType\_Audio** or **MFMediaType\_Video**.     |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)                            | Specifies the stream subtype.                                  |
| [MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION](mf-mt-mpeg4-sample-description.md)      | Contains the complete sample description box as a binary blob. |
| [MF\_MT\_MPEG4\_CURRENT\_SAMPLE\_ENTRY](mf-mt-mpeg4-current-sample-entry.md) | Specifies the current entry in the sample description box.     |



 

The MPEG-4 file source recognizes some sample entry types. For these entries, it can parse the format structure and create a complete media type, with additional attributes that describe the format details. See [Media Type Attributes](media-type-attributes.md).

The MPEG-4 file source can parse the following sample entries.



| Sample entry code | Major type | Subtype                                                               | Description                                         | Notes                                                                                                                                                                                            |
|-------------------|------------|-----------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 'alaw'            | Audio      | **WAVE\_FORMAT\_ALAW**                                                | A-law coding                                        |                                                                                                                                                                                                  |
| 'jpeg'            | Video      | **MFVideoFormat\_MJPG**                                               | Photo-JPEG stream                                   | The QuickTime container format also supports motion JPEG streams with 'mjpa' or 'mjpb' entries, but the MPEG-4 file source does not provide a complete media type for those types.               |
| 'avc1'            | Video      | **MFVideoFormat\_H264**                                               | H.264 video                                         |                                                                                                                                                                                                  |
| 'mp4a'            | Audio      | **MFAudioFormat\_AAC**<br/> **MFAudioFormat\_MP3**<br/>   | AAC or MP3                                          | The 'mp4a' entry can describe other MPEG audio formats, but the MPEG-4 file source does not parse the format structure.                                                                          |
| 'mp4v'            | Video      | **MFVideoFormat\_M4S2**<br/> **MFVideoFormat\_MP4V**<br/> | MPEG-4 part 2                                       | **MFVideoFormat\_M4S2** is used for MPEG-4 part 2 Simple Profile.<br/> **MFVideoFormat\_MP4V** is used for all other MPEG-4 part 2 profiles, including Advanced Simple Profile.<br/> |
| 'raw '            | Audio      | **MFAudioFormat\_PCM**                                                | 8-bit PCM audio                                     |                                                                                                                                                                                                  |
| 'sowt'            | Audio      | **MFAudioFormat\_PCM**                                                | 16-bit little-endian PCM audio                      |                                                                                                                                                                                                  |
| 'twos'            | Audio      | **MFAudioFormat\_PCM**                                                | 16-bit big-endian PCM audio                         | The MPEG-4 file source converts the audio data to little-endian format.                                                                                                                          |
| 'ulaw'            | Audio      | **WAVE\_FORMAT\_MULAW**                                               | μ-law coding                                        |                                                                                                                                                                                                  |
| 'vc-1'            | Video      | **MFVideoFormat\_WVC1**                                               | VC-1 video                                          |                                                                                                                                                                                                  |
| 'NONE'            | Audio      | **MFAudioFormat\_PCM**                                                | 8-bit or 16-bit big-endian PCM audio                | The MPEG-4 file source converts the audio data to little-endian format.                                                                                                                          |
| 0x00000000        | Audio      | **MFAudioFormat\_PCM**                                                | 8-bit or 16-bit big-endian PCM audio                | The MPEG-4 file source converts the audio data to little-endian format.                                                                                                                          |
| 0x6d730002        | Audio      | **WAVE\_FORMAT\_ADPCM**                                               | Adaptive Differential Pulse Code Modulation (ADPCM) |                                                                                                                                                                                                  |
| 0x6d730011        | Audio      | **WAVE\_FORMAT\_IMA\_ADPCM**                                          | ADPCM                                               |                                                                                                                                                                                                  |



 

For any other codes not shown in the previous table, the MPEG-4 file source sets the subtype as follows:

1.  *subtype* = MFMPEG4Format\_Base
2.  *subtype*.Data1 = sample entry code

For codes not shown in the table, a decoder must use the [MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION](mf-mt-mpeg4-sample-description.md) attribute to parse the sample description box.

For a list of sample entry codes and links to relevant specifications, see the ['MP4' Registration Authority](https://mp4ra.org) website.

## Limitations

The MPEG-4 file source does not support the following features of MP4 files:

-   External tracks.
-   Movie fragments ('moof' or 'mfra' boxes). 'moof' is supported in Windows 8.
-   Streamed presentations. The MPEG-4 file source silently ignores hint tracks.
-   Seeking by SMPTE time code.
-   Compressed ('cmov') atoms.

Only video and audio streams are supported. Any tracks that contain other stream types are silently ignored. Media data must be placed inside 'mdat' atoms.

If Platform Update Supplement for Windows Vista is installed, the MPEG-4 file source is available on Windows Vista, but is accessible on Windows Vista only by using the [Source Reader](source-reader.md).

## Windows 8 updates to MPEG-4 source and sink

-   Rotation read and write support added in Windows 8 MPEG-4 source and sink. This is not supported in the Windows 7 MPEG-4 source and sink.

    MPEG-4 source reads the rotation angle for an active video track as the sum of the rotation angle from ‘mvhd’ and from ‘tkhd’.

    Microsoft MPEG-4 sink writes the rotation angle in ‘tkhd’ but writes 0 degree (identity) matrix in ‘mvhd’. Note, Microsoft MPEG-4 sink only supports single video track.

    IPropertyStore reads the rotation angle for only the first video track as the sum of the rotation angle from ‘mvhd’ and from ‘tkhd’.

    IPropertyStore writes the rotation angle for only the first video track in ‘tkhd’ after the rotation angle is adjusted according to the rotation angle in ‘mvhd’, if it exists.

-   Movie fragments ('moof') is supported in Windows 8 MPEG-4 source and sink, but 'mfra' is not.
-   H.263 is supported in Windows 8 MPEG-4 source.

    MPEG-4 source now maps two fourcc’s of ‘h263’ and ‘s263’ in MPEG-4 file format to the media type of **MFVideoFormat\_H263**.

-   More fourcc support added for MJPEG in Windows 8 MPEG-4 source.

    MPEG-4 source maps foucc of ‘dmb1’ to the media type of **MFVideoFormat\_MJPG**.

-   Furigana metadata support added in Windows 8 MPEG-4 source.

    MPEG-4 source reads Furigana metadata from ’soal’, ‘soar’, ‘soaa’, ‘sonm’, and ‘soco’. IPropertyStore reads Furignana metadata through the set of corresponding PKEYs.

    The following table shows the mapping between the shell canonical name, the property key, and the box/tag ID in MPEG-4 file format.

    

    | Field                                | Property Key                         | Tag/Box ID |
    |--------------------------------------|--------------------------------------|------------|
    | System.Music.AlbumTitleSortOverride  | PKEY\_Music\_AlbumTitleSortOverride  | soal       |
    | System.Music.ArtistSortOverride      | PKEY\_Music\_ArtistSortOverride      | soar       |
    | System.Music.AlbumArtistSortOverride | PKEY\_Music\_AlbumArtistSortOverride | soaa       |
    | System.TitleSortOverride             | PKEY \_TitleSortOverride             | sonm       |
    | System.Music.ComposerSortOverride    | PKEY\_Music\_ComposerSortOverride    | soco       |

    

     

-   Stereo 3D atom support added in Windows 8 MPEG-4 source.

-   AC3 and DD+ support added in Windows 8 MPEG-4 source and sink.
-   Files larger than 4 gigabytes (GB) are supported in Windows 8 MPEG-4 sink for non-fragmental MP4.
-   Scrubbing has been optimized in Windows 8 MPEG-4 source.

    To reduce latency, information for the two nearest key frames for a particular seek position are exposed through [**IMFSeekInfo::GetNearestKeyFrames**](/windows/desktop/api/mfidl/nf-mfidl-imfseekinfo-getnearestkeyframes). Since the key frame does not have dependent frames, it presents the frame after decoding only one frame. Use [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) to obtain this interface through the media source, pipeline, or application.

    Set rate to zero in MPEG-4 source. When the pipeline is in scrubbing mode, the rate is zero.

-   SPS and PPS can be stored in sample data in MPEG-4 sink.

    [MF\_MPEG4SINK\_SPSPPS\_PASSTHROUGH](mf-mpeg4sink-spspps-passthrough.md) attribute on MPEG-4 sink is defined to allow SPS’s and PPS’s to be saved together with input samples (H.264 video data). The produced mp4 clips are play-able by Windows 7 MPEG-4 source and others.

-   SPS and PPS can be extracted from input samples in MPEG-4 sink.

    When SPS and PPS are not set through [MF\_MT\_MPEG\_SEQUENCE\_HEADER](mf-mt-mpeg-sequence-header-attribute.md) on input media type of the MPEG-4 sink, MPEG-4 sink will try to extract SPS and PPS from input samples. MPEG-4 sink ignores any input samples until it finds the first SPS and PPS, because all input samples without SPS and PPS are not decode-able.

-   3D information in AVC configuration record is supported for non-fragmental MP4.
-   NALU length is exposed for H.264 compressed samples to optimize H.264 VLD DXVA decoding.

    MPEG-4 source sets [MF\_NALU\_LENGTH\_SET](mf-nalu-length-set.md) on the output media type of **MFVideoFormat\_H264** or **MFVideoFormat\_h264**. It sets the blob of [MF\_NALU\_LENGTH\_INFORMATION](mf-nalu-length-information.md) on each output sample, with four-byte NALU length for different NALU’s in one compressed sample.

-   Support added for MPEG2 ADTS audio in MP4 source.

## Related topics

<dl> <dt>

[Media Sources and Sinks](media-sources-and-sinks.md)
</dt> <dt>

[MPEG-4 Support in Media Foundation](mpeg-4-support-in-media-foundation.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> </dl>

 

 




