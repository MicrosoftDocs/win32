---
description: Specifies the degree to which the codec should reduce the effective color range of the video.
ms.assetid: 7227957b-59c9-4dd9-ad2b-a383e888cd46
title: MFPKEY_RANGEREDUX Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_RANGEREDUX Property

Specifies the degree to which the codec should reduce the effective color range of the video.

## Constant for IPropertyBag

g\_wszWMVCRangeRedux

## Data Type

VT\_I4

## Default Value

0

## Remarks

Range reduction specifies the degree to which the codec should reduce luma and chroma range of the video. Reducing range reduces the size of encoded video frames but also reduces the color detail of the video.

Range reduction consists of reduction during encoding and expansion during decoding. It is possible to make the expansion factors different than the reduction factors, but this is not recommended in most scenarios where range remapping is useful.

Range reduction and expansion is performed separately on luma and chroma channels. Reducing range can be an efficient way to reduce the complexity of low bit-rate video without sacrificing image detail. Setting all four values to 8 reduces the amount of luma and chroma information by half, leaving more bits to be directed to preserving image detail.

The codec can choose to automatically use range reduction when encoding video at very low bit-rates. Setting all four values to 0 completely disables range reduction even in low bit-rate scenarios.

Reducing the color range reduces the encoded size of video frames but can introduce blurriness in the decoded frames.

If this property is not set, the codec determines whether to use range reduction at encoding time. Typically this option is selected by the codec only at low bit rates.

The value of this property is a combination of four components, separated by zeros, formatted as 0x0M0m0N0n, where:

-   M is the encoding range reduction factor for the Y component.
-   m is the decoding range expansion factor for the Y component (usually the same as M).
-   N is the encoding range reduction factor for the UV component.
-   n is the decoding range expansion factor for the UV component (usually the same as N).

Each factor is a digit from 0 to 8, where 0 is no reduction or expansion and 8 is the maximum reduction or expansion.

If you set the value to 0x00000000, range reduction is completely disabled.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




