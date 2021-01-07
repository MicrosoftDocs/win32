---
description: Presentation Descriptor Attributes
ms.assetid: 2a092a6a-956b-4c1f-955f-529ec08665fe
title: Presentation Descriptor Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Presentation Descriptor Attributes

## Common Presentation Descriptor Attributes

The following attributes can apply to any presentation descriptor.



| Attribute                                                                          | Description                                                                                                                                     |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_PD\_APP\_CONTEXT**](mf-pd-app-context-attribute.md)                        | Contains a pointer to the presentation descriptor from the protected media path (PMP).                                                          |
| [**MF\_PD\_AUDIO\_ENCODING\_BITRATE**](mf-pd-audio-encoding-bitrate-attribute.md) | Specifies the audio encoding bit rate for the presentation, in bits per second.                                                                 |
| [MF\_PD\_AUDIO\_ISVARIABLEBITRATE](mf-pd-audio-isvariablebitrate.md)              | Specifies whether the audio streams in the presentation have a variable bit rate.                                                               |
| [**MF\_PD\_DURATION**](mf-pd-duration-attribute.md)                               | Specifies the duration of a presentation, in 100-nanosecond units.                                                                              |
| [**MF\_PD\_LAST\_MODIFIED\_TIME**](mf-pd-last-modified-time-attribute.md)         | Specifies when a presentation was last modified.                                                                                                |
| [**MF\_PD\_MIME\_TYPE**](mf-pd-mime-type-attribute.md)                            | Specifies the MIME type of the content.                                                                                                         |
| [MF\_PD\_PLAYBACK\_BOUNDARY\_TIME](mf-pd-playback-boundary-time.md)               | The time at which the presentation must begin, relative to the start of the media source.                                                       |
| [MF\_PD\_PLAYBACK\_ELEMENT\_ID](mf-pd-playback-element-id.md)                     | The identifier of the playlist element in the presentation.                                                                                     |
| [**MF\_PD\_PMPHOST\_CONTEXT**](mf-pd-pmphost-context-attribute.md)                | Contains a pointer to the proxy object for the application's presentation descriptor.                                                           |
| [MF\_PD\_PREFERRED\_LANGUAGE](mf-pd-preferred-language.md)                        | Contains the preferred RFC 1766 language of the media source.                                                                                   |
| [**MF\_PD\_SAMI\_STYLELIST**](mf-pd-sami-stylelist-attribute.md)                  | Contains the friendly name of the supported Synchronized Accessible Media Interchange (SAMI) styles. This attribute applies only to SAMI files. |
| [**MF\_PD\_TOTAL\_FILE\_SIZE**](mf-pd-total-file-size-attribute.md)               | Specifies the total size of the source file, in bytes.                                                                                          |
| [**MF\_PD\_VIDEO\_ENCODING\_BITRATE**](mf-pd-video-encoding-bitrate-attribute.md) | Specifies the video encoding bit rate for the presentation, in bits per second.                                                                 |



 

## Presentation Descriptor Attributes for ASF

The following attributes apply to presentation descriptors for Advanced Systems Format (ASF) files.



| Attribute                                                                                                             | Description                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**MF\_PD\_ASF\_CODECLIST**](mf-pd-asf-codeclist-attribute.md)                                                       | Contains information about the codecs used to encode the content in an ASF file.                     |
| [**MF\_PD\_ASF\_CONTENTENCRYPTION\_KEYID**](mf-pd-asf-contentencryption-keyid-attribute.md)                          | Specifies the key identifier for an encrypted ASF file.                                              |
| [**MF\_PD\_ASF\_CONTENTENCRYPTION\_LICENSE\_URL**](mf-pd-asf-contentencryption-license-url-attribute.md)             | Specifies the license acquisition URL for an encrypted ASF file.                                     |
| [**MF\_PD\_ASF\_CONTENTENCRYPTION\_SECRET\_DATA**](mf-pd-asf-contentencryption-secret-data-attribute.md)             | Contains secret data for an encrypted ASF file.                                                      |
| [**MF\_PD\_ASF\_CONTENTENCRYPTION\_TYPE**](mf-pd-asf-contentencryption-type-attribute.md)                            | Specifies the type of protection mechanism used in an ASF file.                                      |
| [**MF\_PD\_ASF\_CONTENTENCRYPTIONEX\_ENCRYPTION\_DATA**](mf-pd-asf-contentencryptionex-encryption-data-attribute.md) | Contains encryption data for an ASF file.                                                            |
| [**MF\_PD\_ASF\_DATA\_LENGTH**](mf-pd-asf-data-length-attribute.md)                                                  | Specifies the size, in bytes, of the data section of an ASF file.                                    |
| [**MF\_PD\_ASF\_DATA\_START\_OFFSET**](mf-pd-asf-data-start-offset-attribute.md)                                     | Specifies the offset, in bytes, from the start of an ASF file to the start of the first data packet. |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_CREATION\_TIME**](mf-pd-asf-fileproperties-creation-time-attribute.md)               | Specifies the date and time when an ASF file was initially created.                                  |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_FILE\_ID**](mf-pd-asf-fileproperties-file-id-attribute.md)                           | Specifies the file identifier of an ASF file.                                                        |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_FLAGS**](mf-pd-asf-fileproperties-flags-attribute.md)                                | Contains miscellaneous flags from an ASF header.                                                     |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_BITRATE**](mf-pd-asf-fileproperties-max-bitrate-attribute.md)                   | Specifies the maximum instantaneous bit rate, in bits per second, for an ASF file.                   |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_PACKET\_SIZE**](mf-pd-asf-fileproperties-max-packet-size-attribute.md)          | Specifies the maximum packet size, in bytes, for an ASF file                                         |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_MIN\_PACKET\_SIZE**](mf-pd-asf-fileproperties-min-packet-size-attribute.md)          | Specifies the minimum packet size, in bytes, for an ASF file.                                        |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_PACKETS**](mf-pd-asf-fileproperties-packets-attribute.md)                            | Specifies the number of packets in the data section of an ASF file.                                  |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_PLAY\_DURATION**](mf-pd-asf-fileproperties-play-duration-attribute.md)               | Specifies the time needed to play an ASF file, in 100-nanosecond units.                              |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_PREROLL**](mf-pd-asf-fileproperties-preroll-attribute.md)                            | Specifies the amount of time to buffer data before starting to play an ASF file, in milliseconds.    |
| [**MF\_PD\_ASF\_FILEPROPERTIES\_SEND\_DURATION**](mf-pd-asf-fileproperties-send-duration-attribute.md)               | Specifies the time needed to send an ASF file, in 100-nanosecond units.                              |
| [**MF\_PD\_ASF\_INFO\_HAS\_AUDIO**](mf-pd-asf-info-has-audio-attribute.md)                                           | Specifies whether an ASF file contains at least one audio stream.                                    |
| [**MF\_PD\_ASF\_INFO\_HAS\_NON\_AUDIO\_VIDEO**](mf-pd-asf-info-has-non-audio-video-attribute.md)                     | Specifies whether an ASF file contains any non-audio, non-video streams.                             |
| [**MF\_PD\_ASF\_INFO\_HAS\_VIDEO**](mf-pd-asf-info-has-video-attribute.md)                                           | Specifies whether an ASF file contains at least one video stream.                                    |
| [**MF\_PD\_ASF\_LANGLIST**](mf-pd-asf-langlist-attribute.md)                                                         | Specifies the list of languages used in an ASF file.                                                 |
| [MF\_PD\_ASF\_LANGLIST\_LEGACYORDER](mf-pd-asf-langlist-legacyorder.md)                                              | Contains a list of RFC 1766 languages used in the current presentation.                              |
| [**MF\_PD\_ASF\_MARKER**](mf-pd-asf-marker-attribute.md)                                                             | Specifies the markers in an ASF file.                                                                |
| [**MF\_PD\_ASF\_METADATA\_IS\_VBR**](mf-pd-asf-metadata-is-vbr-attribute.md)                                         | Specifies whether an ASF file uses variable bit rate (VBR) encoding.                                 |
| [**MF\_PD\_ASF\_METADATA\_LEAKY\_BUCKET\_PAIRS**](mf-pd-asf-metadata-leaky-bucket-pairs-attribute.md)                | Describes the buffering requirements for a VBR ASF file.                                             |
| [**MF\_PD\_ASF\_METADATA\_V8\_BUFFERAVERAGE**](mf-pd-asf-metadata-v8-bufferaverage-attribute.md)                     | Specifies the average buffer size needed for a VBR ASF file.                                         |
| [**MF\_PD\_ASF\_METADATA\_V8\_VBRPEAK**](mf-pd-asf-metadata-v8-vbrpeak-attribute.md)                                 | Specifies the highest momentary bit rate in a VBR ASF file.                                          |
| [**MF\_PD\_ASF\_SCRIPT**](mf-pd-asf-script-attribute.md)                                                             | Specifies the script commands in an ASF file.                                                        |



 

## Related topics

<dl> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> </dl>

 

 



