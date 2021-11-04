---
description: Media Types
ms.assetid: '690fda6e-dcbd-44dc-968d-cc949126da81'
title: Media Types (Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Media Types (Media Foundation)

A *media type* is a way to describe the format of a media stream. In Media Foundation, media types are represented by the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) interface. Applications use media types to discover the format of a media file or media stream. Objects in the Media Foundation pipeline use media types to negotiate the formats they will deliver or receive.

This section contains the following topics.



| Topic                                                                    | Description                                                                      |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [About Media Types](about-media-types.md)                               | General overview of media types in Media Foundation.                             |
| [Media Type GUIDs](media-type-guids.md)                                 | Lists the defined GUIDs for major types and subtypes.                            |
| [Audio Media Types](audio-media-types.md)                               | How to create media types for audio formats.                                     |
| [Video Media Types](video-media-types.md)                               | How to create media types for video formats.                                     |
| [Complete and Partial Media Types](complete-and-partial-media-types.md) | Describes the difference between complete media types and partial media types.   |
| [Media Type Conversions](media-type-conversions.md)                     | How to convert between Media Foundation media types and older format structures. |
| [Media Type Helper Functions](media-type-helper-functions.md)           | A list of functions that manipulate or get information from a media type.        |
| [Media Type Debugging Code](media-type-debugging-code.md)               | Example code that shows how to view a media type while debugging.                |



 

## Related topics

<dl> <dt>

[Media Foundation Primitives](media-foundation-primitives.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 



