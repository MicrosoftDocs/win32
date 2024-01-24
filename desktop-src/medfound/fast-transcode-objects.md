---
description: This topic described how to use the transcode API to encode a media file.
ms.assetid: 52b27359-b319-41a0-88e8-d23567420e92
title: Using the Transcode API
ms.topic: article
ms.date: 05/31/2018
---

# Using the Transcode API

This topic described how to use the transcode API to encode a media file.

-   [Overview](#overview)
-   [Creating a Media Source](#creating-a-media-source)
-   [Creating a Transcode Profile](#creating-a-transcode-profile)
    -   [Audio Attributes](#audio-attributes)
    -   [Video Attributes](#video-attributes)
    -   [Container Attributes](#container-attributes)
-   [Creating a Transcode Topology](#creating-a-transcode-topology)
-   [Running the Encoding Session](#running-the-encoding-session)
-   [Related topics](#related-topics)

## Overview

Before using the transcode API, the application must have the following pieces of information:

-   The path or URL to an existing media file that will be re-encoded.
-   The name of the output file.
-   The container type for the output file, such as MP4 or Advanced Streaming Format (ASF).
-   The encoding format. This information includes the media types that describe the encoded audio and video streams.

To use the transcode API, an application performs the following steps.

1.  Create a media source to read the source file.
2.  Create a transcode profile. Add attributes that describe the audio stream, video stream, and file container.
3.  Use the transcode profile to create an encoding topology. (For more information about topologies, see [About Topologies](about-topologies.md).)
4.  Set the topology on the [Media Session](media-session.md).
5.  Start the Media Session and wait for the [MESessionEnded](mesessionended.md) event.

The remainder of this topic describes these steps in more detail.

## Creating a Media Source

A media source is an object that reads and parses the source file. To create a media source, use the [Source Resolver](source-resolver.md). You can find example code in the topic [Using the Source Resolver](using-the-source-resolver.md).

## Creating a Transcode Profile

A *transcode profile* describes the format and settings that are used to encode the output file. The transcode profile contains three sets of attributes:

-   Audio attributes: Describe the target audio format and audio encoder settings.
-   Video attributes: Describe the target video format and video encoder settings.
-   Container attributes: Define the type of file container, as well as some global encoding settings.

To create a transcode profile, call the [**MFCreateTranscodeProfile**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetranscodeprofile) function. This function returns a pointer to the [**IMFTranscodeProfile**](/windows/desktop/api/mfidl/nn-mfidl-imftranscodeprofile) interface. The initial profile object is empty; it contains no attributes. The next step is to add the attributes that define the profile.

### Audio Attributes

To add attributes for the audio stream, call [**IMFTranscodeProfile::SetAudioAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setaudioattributes). These attributes specify how the audio stream is encoded. If the output file will not contain an audio stream, omit these attributes.

Audio attributes fall into two categories:

-   Attributes that specify the format of the encoded stream
-   Attributes that specify other encoding parameters.

Format attributes are simply media-type attributes, as described in the section [Audio Media Types](audio-media-types.md). The exact set of format attributes depends on the encoder. (See [Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md).) Here is a list of typical audio format attributes:



| Format Attribute                                                                         | Description                                                      |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md)                                           | The subtype. See [Audio Subtype GUIDs](audio-subtype-guids.md). |
| [MF\_MT\_AUDIO\_NUM\_CHANNELS](mf-mt-audio-num-channels-attribute.md)                   | The number of audio channels.                                    |
| [MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND](mf-mt-audio-samples-per-second-attribute.md)      | The number of audio samples per second.                          |
| [MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT](mf-mt-audio-block-alignment-attribute.md)             | The block alignment.                                             |
| [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) | The average number of bytes per second (the encoded bit rate).   |



 

The following encoding parameters are defined.



| Encoding Parameter                                                             | Description                                                                |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [MF\_TRANSCODE\_DONOT\_INSERT\_ENCODER](mf-transcode-donot-insert-encoder.md) | Prevents the transcode API from inserting an encoder for the audio stream. |
| [MF\_TRANSCODE\_ENCODINGPROFILE](mf-transcode-encodingprofile.md)             | Specifies the device conformance template. (Applies only to ASF files.)    |
| [MF\_TRANSCODE\_QUALITYVSSPEED](mf-transcode-qualityvsspeed.md)               | Specifies the trade-off between encoding quality and speed.                |



 

You must set the format attributes. The encoding parameters are optional.

One way to find a format that is compatible with the encoder is to call the [**MFTranscodeGetAudioOutputAvailableTypes**](/windows/desktop/api/mfidl/nf-mfidl-mftranscodegetaudiooutputavailabletypes) function. The desired encoder is specified by subtype. The function returns a collection of media types for that encoder. You can select a type from the list and copy the attributes to the profile. For example code that uses this approach, see [Tutorial: Encoding a WMA File](tutorial--converting-an-mp3-file-to-a-wma-file.md).

### Video Attributes

To add attributes for the video stream, call [**IMFTranscodeProfile::SetVideoAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setvideoattributes). These attributes specify how the video stream is encoded. If the output file will not contain a video stream, omit these attributes.

As with audio attributes, the video attributes fall into two categories:

-   Attributes that specify the format of the encoded stream
-   Attributes that specify other encoding parameters.

Format attributes are media-type attributes, as described in the section [Video Media Types](video-media-types.md). Here is a list of typical video format attributes:



| Format Attribute                                                       | Description                                                      |
|------------------------------------------------------------------------|------------------------------------------------------------------|
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md)                         | The subtype. See [Video Subtype GUIDs](video-subtype-guids.md). |
| [MF\_MT\_FRAME\_RATE](mf-mt-frame-rate-attribute.md)                  | The frame rate.                                                  |
| [MF\_MT\_FRAME\_SIZE](mf-mt-frame-size-attribute.md)                  | The frame size.                                                  |
| [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md)            | The average bit rate.                                            |
| [MF\_MT\_PIXEL\_ASPECT\_RATIO](mf-mt-pixel-aspect-ratio-attribute.md) | The pixel aspect ratio.                                          |



 

The following encoding parameters are defined.



| Encoding Parameter                                                             | Description                                                                |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [MF\_TRANSCODE\_DONOT\_INSERT\_ENCODER](mf-transcode-donot-insert-encoder.md) | Prevents the transcode API from inserting an encoder for the video stream. |
| [MF\_TRANSCODE\_ENCODINGPROFILE](mf-transcode-encodingprofile.md)             | Specifies the device conformance template. (Applies only to ASF files.)    |
| [MF\_TRANSCODE\_QUALITYVSSPEED](mf-transcode-qualityvsspeed.md)               | Specifies the trade-off between encoding quality and speed.                |



 

You must set the format attributes. The encoding parameters are optional.

### Container Attributes

Container attributes define file-level characteristics of the output file. To set container attributes, call [**IMFTranscodeProfile::SetContainerAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setcontainerattributes). The following attributes are defined.



| Attribute                                                                          | Description                                                                                                                                            |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MF\_TRANSCODE\_ADJUST\_PROFILE](mf-transcode-adjust-profile.md)                  | Defines the stream settings to use for the transcode topology. You can set the flags to use the input source settings or use custom stream attributes. |
| [MF\_TRANSCODE\_CONTAINERTYPE](mf-transcode-containertype.md)                     | Specifies the file format of the output file, such as MP4 or ASF. Based on this value, the appropriate media sink is added to the topology.            |
| [MF\_TRANSCODE\_SKIP\_METADATA\_TRANSFER](mf-transcode-skip-metadata-transfer.md) | Specifies whether metadata from the source is copied to the output file.                                                                               |
| [MF\_TRANSCODE\_TOPOLOGYMODE](mf-transcode-topologymode.md)                       | Specifies whether hardware-based codecs may be used during transcoding.                                                                                |
| [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md)          | Unlocks a codec that has field-of-use restrictions. For more information, see [Field of Use Restrictions](field-of-use-restrictions.md).              |



 

The [MF\_TRANSCODE\_CONTAINERTYPE](mf-transcode-containertype.md) attribute is required. The other container attributes are optional.

## Creating a Transcode Topology

The transcode topology is a partial topology that contains the media source, the appropriate codecs, and the media sink. To create the transcode topology, call to the [**MFCreateTranscodeTopology**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetranscodetopology) function. This function takes the following parameters as input:

-   A pointer to the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface of the media source.
-   The name of the output file.
-   A pointer to the [**IMFTranscodeProfile**](/windows/desktop/api/mfidl/nn-mfidl-imftranscodeprofile) interface of the transcode profile.

The function returns a pointer to the [**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology) interface.

## Running the Encoding Session

After you create the topology, you are ready to encode the file. You can discard the profile at this point.

1.  Call [**MFCreateMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatemediasession) to create the Media Session.
2.  Call [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) to set the topology on the Media Session.
3.  Call [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) to start the encoding session.
4.  Wait for the [MESessionEnded](mesessionended.md) event.
5.  Call [**IMFMediaSession::Close**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-close) to close the Media Session.
6.  Wait for the [MESessionClosed](mesessionclosed.md) event.
7.  Call [**IMFMediaSource::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown).
8.  Call [**IMFMediaSession::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-shutdown).

Most of the time spent encoding occurs between steps 3 and 4.

## Related topics

<dl> <dt>

[Transcode API](transcode-api.md)
</dt> <dt>

[About the Media Session](about-the-media-session.md)
</dt> </dl>

 

 



