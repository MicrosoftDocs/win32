---
description: Specifies the decoder’s “operating point”, the scalability layer that the decoder should be operating at when it supports spatial or temporal scalability.
title: MFT_DECODER_OPERATING_POINT attribute (Mftransform.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFT\_DECODER\_OPERATING\_POINT attribute

Specifies the decoder’s “operating point”, the scalability layer that the decoder should be operating at when it supports spatial or temporal scalability.

## Data type

**UINT32**

## Remarks

The term “operating point” comes from the [AV1 specification](https://aomediacodec.github.io/av1-spec/av1-spec.pdf), but can apply generally to layering methods of a variety of video codecs.  The definition of the layer varies depending on the video format. For video formats that support both spatial and temporal scalability, a given operating point may allow for both spatial and temporal scalability – those features are not necessarily exclusive. Generally, the higher the layer, the more frames are output by the decoder.  This is useful when an app knows that it cannot support layers beyond a certain value. For example, higher layers may be too CPU intensive or use a higher resolution than is required by the app. Specifying this value allows the decoder to save resources by not decoding unwanted layers in the bitstream.

There is no upper bound on this value.  If the value is higher than the highest coded layer in the bitstream, then all layers are emitted.  This attribute should be set on the decoder’s MFT attribute store that can be obtained by invoking [IMFTransform::GetAttributes](/windows/win32/api/mftransform/nf-mftransform-imftransform-getattributes).  

By default, this value is 0xffffffff to emit all layers.


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

 

 




