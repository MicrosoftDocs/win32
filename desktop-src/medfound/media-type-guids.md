---
description: Major Media Types
ms.assetid: 1cca3539-a920-4938-93b9-ae41e1c0a287
title: Major Media Types
ms.topic: article
ms.date: 05/31/2018
---

# Major Media Types

In a media type, the *major type* describes the overall category of the data, such as audio or video. The *subtype*, if present, further refines the major type. For example, if the major type is video, the subtype might be 32-bit RGB video. Subtypes also distinguish encoded formats, such as H.264 video, from uncompressed formats.

Major type and subtype are identified by GUIDs and stored in the following attributes:



| Attribute                                             | Description |
|-------------------------------------------------------|-------------|
| [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md) | Major type. |
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md)        | Subtype.    |



 

The following major types are defined.



| Major Type                    | Description                                                                                                                                                | Subtypes                                             |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| **MFMediaType\_Audio**        | Audio.                                                                                                                                                     | [Audio Subtype GUIDs](audio-subtype-guids.md).      |
| **MFMediaType\_Binary**       | Binary stream.                                                                                                                                             | None.                                                |
| **MFMediaType\_FileTransfer** | A stream that contains data files.                                                                                                                         | None.                                                |
| **MFMediaType\_HTML**         | HTML stream.                                                                                                                                               | None.                                                |
| **MFMediaType\_Image**        | Still image stream.                                                                                                                                        | [WIC GUIDs and CLSIDs](../wic/-wic-guids-clsids.md).       |
| **MFMediaType\_Metadata**        | Metadata stream.                                                                                                                                        | None.       |
| **MFMediaType\_Protected**    | Protected media.                                                                                                                                           | The subtype specifies the content protection scheme. |
| **MFMediaType\_Perception**   | Streams from a camera sensor or processing unit that reasons and understands raw video data and provides understanding of the environment or humans in it. | None.                                                |
| **MFMediaType\_SAMI**         | Synchronized Accessible Media Interchange (SAMI) captions.                                                                                                 | None.                                                |
| **MFMediaType\_Script**       | Script stream.                                                                                                                                             | None.                                                |
| **MFMediaType\_Stream**       | Multiplexed stream or elementary stream.                                                                                                                   | [Stream Subtype GUIDs](stream-subtype-guids.md)     |
| **MFMediaType\_Video**        | Video.                                                                                                                                                     | [Video Subtype GUIDs](video-subtype-guids.md).      |



 

Third-party components can define new major types and new subtypes.

## Related topics

<dl> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 
