---
description: Media Foundation Attributes for ASF Header Objects
ms.assetid: 82d2bdeb-4ccf-4713-980e-59bddc7d9b6a
title: Media Foundation Attributes for ASF Header Objects
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation Attributes for ASF Header Objects

The top-level ASF Header Object for a file contains several ASF sub-header objects. The ContentInfo object stores information from all of these Header Objects and exposes certain values to an application through attributes.

## File Properties Object

This header object is present in all ASF files. These fields describe the file-level attributes of the entire presentation. The following table lists the fields in the File Properties Object and the corresponding presentation descriptor attributes.



| File Properties Object field | Presentation descriptor attribute                                                                            | Description                                                                                    |
|------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| File ID                      | [**MF\_PD\_ASF\_FILEPROPERTIES\_FILE\_ID**](mf-pd-asf-fileproperties-file-id-attribute.md)                  | Unique identifier for this file.                                                               |
| File Size                    | [**MF\_PD\_TOTAL\_FILE\_SIZE**](mf-pd-total-file-size-attribute.md)                                         | Size of the file, in bytes.                                                                    |
| Creation Date                | [**MF\_PD\_ASF\_FILEPROPERTIES\_CREATION\_TIME**](mf-pd-asf-fileproperties-creation-time-attribute.md)      | The file creation date and time.                                                               |
| Data Packets Count           | [**MF\_PD\_ASF\_FILEPROPERTIES\_PACKETS**](mf-pd-asf-fileproperties-packets-attribute.md)                   | Number of data packets in the ASF Data Object.                                                 |
| Play Duration                | [**MF\_PD\_ASF\_FILEPROPERTIES\_PLAY\_DURATION**](mf-pd-asf-fileproperties-play-duration-attribute.md)      | Time required to play the file, in 100-nanosecond units. This value includes the preroll time. |
| Send Duration                | [**MF\_PD\_ASF\_FILEPROPERTIES\_SEND\_DURATION**](mf-pd-asf-fileproperties-send-duration-attribute.md)      | Time required to send the file, in 100-nanosecond units.                                       |
| Preroll                      | [**MF\_PD\_ASF\_FILEPROPERTIES\_PREROLL**](mf-pd-asf-fileproperties-preroll-attribute.md)                   | Length of time to buffer data before the playing the file, in 100-nanosecond units.            |
| Flags                        | [**MF\_PD\_ASF\_FILEPROPERTIES\_FLAGS**](mf-pd-asf-fileproperties-flags-attribute.md)                       | Flags indicating whether the file is broadcast or seekable.                                    |
| Minimum Data Packet Size     | [**MF\_PD\_ASF\_FILEPROPERTIES\_MIN\_PACKET\_SIZE**](mf-pd-asf-fileproperties-min-packet-size-attribute.md) | Minimum size of the data packets in the file, in bytes.                                        |
| Maximum Data Packet Size     | [**MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_PACKET\_SIZE**](mf-pd-asf-fileproperties-max-packet-size-attribute.md) | Maximum size of the data packets in the file, in bytes.                                        |
| Maximum Bitrate              | [**MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_BITRATE**](mf-pd-asf-fileproperties-max-bitrate-attribute.md)          | Maximum instantaneous bit rate, in bits per second.                                            |



 

## Stream Properties Object

This header object describes the properties of the streams in the ASF file. In Media Foundation, this is managed by the profile object and the stream configuration object. For more information, see [Creating and Configuring ASF Streams](creating-and-configuring-asf-streams.md).

## Codec List Object

If this header object is present, the [**MF\_PD\_ASF\_CODECLIST**](mf-pd-asf-codeclist-attribute.md) attribute provides a list of codecs that were used to encode the streams within the ASF file. Each stream should have its codec information in this object.

## Script Command Object

If this header object is present, it specifies a list of script commands that are supported in the ASF file. A script command consists of a command type, a command name, and a presentation time. The command type and command name are wide-character strings. These commands can be used to notify the client to perform an action at a certain point in the presentation. For example, an application can use the command type "FILENAME" to play a continuous sequence of ASF files.

To get the list of script commands, get the [**MF\_PD\_ASF\_SCRIPT**](mf-pd-asf-script-attribute.md) attribute from the presentation descriptor. An application should retrieve all of the script commands before starting playback.

## Marker Object

A marker is a bookmark within an ASF file. An application can use markers to seek to various points within the content. Each marker consists of a marker name, the associated presentation time, and the offset from the start of the file. The [**MF\_PD\_ASF\_MARKER**](mf-pd-asf-marker-attribute.md) attribute provides a list of markers that are available for the file.

## Stream Bitrate Properties Object

This header stores the average bit rate of each stream present in the ASF file. This value is stored on the stream descriptor for the stream in the [**MF\_SD\_ASF\_STREAMBITRATES\_BITRATE**](mf-sd-asf-streambitrates-bitrate-attribute.md) attribute.

## Content Encryption Object

This header object is present if the content provider has protected the content by using Microsoft Digital Rights Management. The following table lists the fields in the Content Encryption Object and the corresponding presentation descriptor attributes:



| Content Encryption Object field | Presentation descriptor attribute                                                                         | Description                                                                                        |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Secret Data                     | [**MF\_PD\_ASF\_CONTENTENCRYPTION\_SECRET\_DATA**](mf-pd-asf-contentencryption-secret-data-attribute.md) | Byte array containing secret data.                                                                 |
| Protection Type                 | [**MF\_PD\_ASF\_CONTENTENCRYPTION\_TYPE**](mf-pd-asf-contentencryption-type-attribute.md)                | Null-terminated string that has value "DRM".                                                       |
| Key ID                          | [**MF\_PD\_ASF\_CONTENTENCRYPTION\_KEYID**](mf-pd-asf-contentencryption-keyid-attribute.md)              | Null-terminated string that describes the key identifier.                                          |
| License URL                     | [**MF\_PD\_ASF\_CONTENTENCRYPTION\_LICENSE\_URL**](mf-pd-asf-contentencryption-license-url-attribute.md) | Null-terminated string that contains the URL from which to acquire the license to use the content. |



 

## Extended Content Encryption Object

This header object is present if the content provider has protected the content by using the Windows Media Rights Manager 7 SDK. The [**MF\_PD\_ASF\_CONTENTENCRYPTION\_LICENSE\_URL**](mf-pd-asf-contentencryption-license-url-attribute.md) attribute provides a byte array that corresponds to the Data field of the header object. This field is required to use the content.

## Extended Stream Properties Object

This header is part of the Header Extension Object. The Extended Stream Properties Object provides properties of the stream that are not defined in the Stream Properties Object. These properties are used mainly to determine the "leaky bucket" parameters, which are used by the decoder. These properties are also used by the encoder when compressing data. This is managed by the profile object and the stream configuration object. For more information, see [Creating and Configuring ASF Streams](creating-and-configuring-asf-streams.md).

The following table lists the Extended Stream Properties Object fields and the corresponding stream descriptor attributes.



| Extended Stream Properties field | Stream descriptor attribute                                                                                | Description                                                                                                              |
|----------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Data Bitrate                     | [**MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_DATA\_BITRATE**](mf-sd-asf-extstrmprop-avg-data-bitrate-attribute.md)   | Average data rate, in bits per second.                                                                                   |
| Buffer Size                      | [**MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_BUFFERSIZE**](mf-sd-asf-extstrmprop-avg-buffersize-attribute.md)        | Leaky bucket size. Value is the number of milliseconds of data that can fit in the buffer at the average data rate.      |
| Alternate Data Bitrate           | [**MF\_SD\_ASF\_EXTSTRMPROP\_MAX\_DATA\_BITRATE**](mf-sd-asf-extstrmprop-max-data-bitrate-attribute.md)   | Peak data rate, in bites per second. The peak data rate is used for streams with a variable bit rate.                    |
| Alternate Buffer Size            | [**MF\_SD\_ASF\_EXTSTRMPROP\_MAX\_BUFFERSIZE**](mf-sd-asf-extstrmprop-max-buffersize-attribute.md)        | Maximum leaky bucket size. Value is the number of milliseconds of data that can fit in the buffer at the peak data rate. |
| Stream Language ID               | [**MF\_SD\_ASF\_EXTSTRMPROP\_LANGUAGE\_ID\_INDEX**](mf-sd-asf-extstrmprop-language-id-index-attribute.md) | The language that the stream uses, specified as an index into the list of languages in the Language List Object.         |



 

## Language List Object

This header object is part of the Header Extension Object. If present, the [**MF\_PD\_ASF\_LANGLIST**](mf-pd-asf-langlist-attribute.md) attribute provides a list of language identifiers that are supported in the file. The identifiers are compliant with RFC 1766 for specifying languages.

## Mutual Exclusion Object

This header specifies groups of streams and their properties, only one of which will be delivered at a time. For more information, see [Using Mutual Exclusion for ASF Streams](using-mutual-exclusion-for-asf-streams.md).

## Related topics

<dl> <dt>

[ASF ContentInfo Object](asf-contentinfo-object.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 



