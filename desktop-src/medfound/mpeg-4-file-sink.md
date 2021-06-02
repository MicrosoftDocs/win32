---
description: The MPEG-4 file sink creates MP4 files.
ms.assetid: 069b8e72-d081-466e-ac8d-c3f81c8a6f35
title: MPEG-4 File Sink
ms.topic: reference
ms.date: 05/31/2018
---

# MPEG-4 File Sink

The MPEG-4 file sink creates MP4 files. For more information about the MP4 file format, refer to the following standards documents:

-   ISO/IEC 14496-12: *Information technology -- Coding of audio-visual objects -- Part 12: ISO Base Media File Format*
-   ISO/IEC 14496-14: *Information technology -- Coding of audio-visual objects -- Part 14: MP4 File Format*

> [!Note]  
> (These resources may not be available in some languages and countries.)

 

The MPEG-4 file sink does not encapsulate encoding functionality.

To create the MPEG-4 file sink, call the [**MFCreateMPEG4MediaSink**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatempeg4mediasink) function. The MPEG-4 file sink exposes the following interfaces through **QueryInterface**:

-   [**IMFClockStateSink**](/windows/desktop/api/mfidl/nn-mfidl-imfclockstatesink)
-   [**IMFFinalizableMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imffinalizablemediasink)
-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
-   [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator)
-   [**IMFMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasink)

## Sample Description Box

MP4 is an extensible container format. The MP4 specification does not define a fixed structure for describing media types in an MP4 container. Instead, it defines an object hierarchy that allows custom structures to be defined for each format. The format description is stored in the sample description ('stsd') box for each stream. The sample description box contains a list of sample entries. For each sample entry, a 4-byte code, similar to a FOURCC, defines the format structure.

The MPEG-4 File Sink can generate the sample description box for the following formats:

-   H.264/AVC video
-   AAC audio
-   MP3 audio

For other formats, the sample description box must be provided in the media type for each stream. To specify the sample description box, set the following attributes on the media type:



| Attribute                                                                     | Description                                                                                                                                                   |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION](mf-mt-mpeg4-sample-description.md)      | Contains the sample description box as a binary blob.                                                                                                         |
| [MF\_MT\_MPEG4\_CURRENT\_SAMPLE\_ENTRY](mf-mt-mpeg4-current-sample-entry.md) | Specifies which of the sample entries in the sample description box is currently active. (Optional.)<br/> Currently, the value must be zero.<br/> |



 

In some cases, it is not possible to generate a sample description box until all of the data has been encoded. For example, information such as the average bit rate might not be known ahead of time. In that case, you can update the media type by using the [**IMFMediaTypeHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfmediatypehandler) interface on the MPEG-4 file sink. This must be done before the media sink is finalized.

Typically the media type is created by an upstream encoder. The encoder can generate a new media type during streaming, through a dynamic format change. For more information, see [Dynamic Format Changes](basic-mft-processing-model.md).

## H.264/AVC Video

The MPEG-4 file sink supports the version of the AVC stream that has an elementary video stream, with sequence parameter set (SPS) and picture parameter set (PPS) NALUs contained in the sample description box, as defined in ISO/IEC 14496 part 15 section 5.1. The file sink does not support the alternate method of storing SPS/PPS NALUs as a separate parameter-set elementary stream.

The MPEG-4 file sink can generate the sample description box, but must be provided with the SPS and PPS NALUs. Specify this information in the media type by setting the [**MF\_MT\_MPEG\_SEQUENCE\_HEADER**](mf-mt-mpeg-sequence-header-attribute.md) attribute. The value of the attribute is the H.264 sequence header. The sequence header must consist of the SPS and PPS NALUs delimited by either 3-byte or 4-byte start codes.

Optionally, when you configure the file sink, you can omit the [**MF\_MT\_MPEG\_SEQUENCE\_HEADER**](mf-mt-mpeg-sequence-header-attribute.md) attribute from the initial media type. In that case, you must update the media type later to include the sequence header.

The MPEG-4 file sink has the following requirements for AVC bitstreams:

-   The bitstream must conform to the H.264 Annex B format specification. In particular, NALUs must be delimited with either 3-byte or 4-byte start codes.
-   Media samples must contain all slice and data NALUs that correspond to a single presentation time.
-   When writing B-frames into an MP4 file, you must set both the presentation time stamp and the decode time stamp. If stream has a B frame and the decode timestamp is not set, the MP4 writer will see the frame time going backwards and will drop the frame. 

## AAC Audio

For AAC audio, the MPEG-4 file sink can generate the sample description box for the following subtypes:

-   **MFAudioFormat\_AAC**
-   **MEDIASUBTYPE\_RAW\_AAC1**

For more information about these substypes, see [AAC Media Types](aac-media-types.md).

For the **MFAudioFormat\_AAC** subtype, the media type optionally contains the [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md) attribute. If present, this attribute the portion of the [**HEAACWAVEINFO**](/windows/win32/api/mmreg/ns-mmreg-heaacwaveinfo) structure that appears after the **WAVEFORMATEX** structure (that is, after the **wfx** member). This is followed by the AudioSpecificConfig() data, as defined by ISO/IEC 14496-3. If the **MF\_MT\_USER\_DATA** attribute is not present, the stream is assumed to be AAC Low Complexity (LC) profile, and the MPEG-4 file sink generates a suitable sample description box.

For the **MEDIASUBTYPE\_RAW\_AAC1** subtype, the media sink must contain the [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md) attribute, and the attribute must contain the AudioSpecificConfig() data.

The MPEG-4 file sink creates the MPEG-4 variant of the AAC sample description box, using an 'mp4a' sample entry with objectTypeIndication = 0x40. It does not use MPEG-2 object types.

## MP3 Audio

For MP3 audio, the MPEG-4 file sink can generate the sample description box from a standard audio media type. (See [Audio Media Types](audio-media-types.md).)

The MPEG-4 file sink creates the MPEG-4 variant of the MP3 sample description box, using an 'mp4a' sample entry with objectTypeIndication = 0x6b for MPEG-1 audio.

## Limitations

-   The maximum size of the authored file is 4 GB. In Windows 8, files large than 4 GBGB are supported.
-   The MPEG-4 file sink does not support edit lists ('edts' and 'elst' boxes).

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
-   Files larger than 4 GB are supported in Windows 8 MPEG-4 sink for non-fragmental MP4.
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

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Media Sources and Sinks](media-sources-and-sinks.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> <dt>

[MPEG-4 Support in Media Foundation](mpeg-4-support-in-media-foundation.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> </dl>

 

 
