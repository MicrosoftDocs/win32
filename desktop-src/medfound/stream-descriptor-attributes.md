---
description: Stream Descriptor Attributes
ms.assetid: 1364d7c5-67e8-49b6-8038-d6d4ea03fb7d
title: Stream Descriptor Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Stream Descriptor Attributes

## Common Stream Descriptor Attributes

The following attributes apply to stream descriptors.



| Attribute                                                   | Description                                                                           |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**MF\_SD\_LANGUAGE**](mf-sd-language-attribute.md)        | Specifies the language for a stream.                                                  |
| [MF\_SD\_MUTUALLY\_EXCLUSIVE](mf-sd-mutually-exclusive.md) | Specifies whether a stream is mutually exclusive with other streams of the same type. |
| [**MF\_SD\_PROTECTED**](mf-sd-protected-attribute.md)      | Specifies whether a stream contains protected content.                                |
| [MF\_SD\_STREAM\_NAME](mf-sd-stream-name.md)               | Contains the name of a stream.                                                        |



 

## ASF-Specific Stream Descriptor Attributes

The following attributes apply to stream descriptors for Advanced Systems Format (ASF) files.



| Attribute                                                                                                                | Description                                                                                |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_BUFFERSIZE**](mf-sd-asf-extstrmprop-avg-buffersize-attribute.md)                      | Specifies the average buffer size needed for a stream in an ASF file, in bytes.            |
| [**MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_DATA\_BITRATE**](mf-sd-asf-extstrmprop-avg-data-bitrate-attribute.md)                 | Specifies the average data bit rate of a stream in an ASF file, in bits per second.        |
| [**MF\_SD\_ASF\_EXTSTRMPROP\_LANGUAGE\_ID\_INDEX**](mf-sd-asf-extstrmprop-language-id-index-attribute.md)               | Specifies the language used by a stream in an ASF file.                                    |
| [**MF\_SD\_ASF\_EXTSTRMPROP\_MAX\_BUFFERSIZE**](mf-sd-asf-extstrmprop-max-buffersize-attribute.md)                      | Specifies the maximum buffer size needed for a stream in an ASF file, in bytes.            |
| [**MF\_SD\_ASF\_EXTSTRMPROP\_MAX\_DATA\_BITRATE**](mf-sd-asf-extstrmprop-max-data-bitrate-attribute.md)                 | Specifies the maximum data bit rate of a stream in an ASF file, in bits per second         |
| [**MF\_SD\_ASF\_METADATA\_DEVICE\_CONFORMANCE\_TEMPLATE**](mf-sd-asf-metadata-device-conformance-template-attribute.md) | Specifies the device conformance template for a stream in an ASF file, in bits per second. |
| [**MF\_SD\_ASF\_STREAMBITRATES\_BITRATE**](mf-sd-asf-streambitrates-bitrate-attribute.md)                               | Specifies the average bit rate of a stream in an ASF file, in bits per second.             |



 

## SAMI Media Source Stream Descriptor Attributes

The following attribute applies to the stream descriptor for the SAMI media source.



| Attribute                                                       | Description                                                                                                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**MF\_SD\_SAMI\_LANGUAGE**](mf-sd-sami-language-attribute.md) | Contains the Synchronized Accessible Media Interchange (SAMI) language name that is defined for the stream. |



 

## Related topics

<dl> <dt>

[**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 



