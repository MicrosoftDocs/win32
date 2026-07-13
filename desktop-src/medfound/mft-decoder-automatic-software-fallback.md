---
description: Specifies whether the decoder MFT should, if possible, not automatically switch to software decoding mode.
title: MFT_DECODER_AUTOMATIC_SOFTWARE_FALLBACK attribute (Mftransform.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFT\_DECODER\_AUTOMATIC\_SOFTWARE\_FALLBACK attribute

Specifies whether the decoder MFT should, if possible, not automatically switch to software decoding mode.

## Data type

**UINT32**

## Remarks

Even if a decoder has been successfully configured to use hardware accelerated decoding, properties of the encoded bitstream may prevent hardware accelerated decoding from being used. In that case, the default behavior is that the decoder will automatically switch to software decoding mode. This attribute can be used to suggest to the decoder that the decoder should report an error instead of switching to software decoding mode.

The attribute value is treated as a boolean. The default value is 1.  When the value is non-zero, the decoder may automatically switch to using software decoding if the bitstream is in a format which is not supported by the accelerator.  When the value is 0, the decoder is being asked to emit an error code instead of switching to software decoding mode.

Note that this value is only a hint to the decoder.  Decoder MFTs are not required to implement this, and the value may be ignored silently.

## Requirements



| Requirement | Value |
|----------------|----------------------------|
| Minimum supported client | Windows 11 version 24H2 |
| Header                   | Mftransform.h |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




