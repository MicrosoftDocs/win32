---
description: This topic describes the difference between complete media types and partial media types.
ms.assetid: 59b3f0b5-f378-41e6-9b49-85a16bb6e008
title: Complete and Partial Media Types
ms.topic: article
ms.date: 05/31/2018
---

# Complete and Partial Media Types

This topic describes the difference between complete media types and partial media types.

## Complete Media Types

A *complete* media type is one that fully defines the format of the media stream. Given a complete media type, a pipeline component can parse the stream data associated with the media type, with no ambiguity.

For uncompressed formats, the following topics define the attributes that are required for a complete media type:

-   Audio: [Uncompressed Audio Media Types](uncompressed-audio-media-types.md)
-   Video: [Uncompressed Video Media Types](uncompressed-video-media-types.md)

For compressed (or *encoded*) streams, the definition of a complete media type is defined by the codec. However, if any uncompressed type attributes are known for the compressed stream, these values should be included in the media type for the compressed stream. For example, if the frame size is known, set the [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md) attribute on the media type, even though technically a compressed stream does not have a frame size.

## Partial Media Types

A *partial* media type lacks one or more of the attributes needed for a complete media type. When enumerating possible media types, a Microsoft Media Foundation component may leave a value unset, to indicate that it can handle any value. For example, a video processor might leave the [**MF\_MT\_FRAME\_RATE**](mf-mt-frame-rate-attribute.md) attribute unset, to indicate that it can handle any frame rate, and will perform a frame-rate conversion if necessary.

If you create a partial media type, you should still include as much information as you know. However, a media type must not include information that is uncertain. It is better for information to be missing than wrong.

At a minimum, a partial media type should include just two attributes: [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) and [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md).

Sometimes Media Foundation components must provide complete media types:

-   Media sources must provide complete output types.
-   Decoders must provide complete output types, after the input type is set. Before the input type is set, a decoder might provide a partial output type.
-   Encoders must provide complete input types, after the output type is set. Before the output type is set, an encoder might provide a partial input type.

## Related topics

<dl> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 



