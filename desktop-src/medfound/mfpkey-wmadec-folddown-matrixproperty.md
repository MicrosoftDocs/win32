---
description: Specifies the author-supplied fold-down coefficients for decoding multichannel audio for fewer channels than the encoded stream contains.
ms.assetid: f6737c05-4b39-4209-9985-9402b28cf316
title: MFPKEY_WMADEC_FOLDDOWN_MATRIX Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADEC\_FOLDDOWN\_MATRIX Property

Specifies the author-supplied fold-down coefficients for decoding multichannel audio for fewer channels than the encoded stream contains.

## Constant for IPropertyBag

g\_wszWMACFoldDownXToYChannels

g\_wszWMACFoldXToYChannelsZ

## Data Type

**VT\_ARRAY \| VT\_I4**

## Remarks

An audio decoder can act as a DirectX Media Object (DMO) or as a Media Foundation Transform (MFT). For information on when a decoder acts as a DMO or an MFT, see the individual codec reference pages under [Codec Objects](codecobjects.md).

When you use a decoder as a DMO, the decoder can perform channel fold down, and you can enumerate folded down output media types by calling [**IMediaObject::GetOutputType**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-getoutputtype).

When you use a decoder as an MFT, the decoder by default will not perform any fold down, and will not offer folded down output media types. A decoder acting as an MFT will perform fold down only if custom fold-down coefficients are set using the **MFPKEY\_WMADEC\_FOLDDOWN\_MATRIX** property.

If the **MFPKEY\_WMADEC\_FOLDDOWN\_MATRIX** property is not set on the audio decoder MFT, and you want to perform a fold down, you can use (as an MFT) the Audio Resampler digital signal processor.

The value for this property is a string containing fold-down coefficients in a comma-separated list of integer values. The list must contain a number of integers for each channel in the encoded content equal to the number of channels in the decoded content.

If the coefficient is zero, the value to be used in the string must be "-2147483648";otherwise the value is computed using the equation: 20 \* 65536 \* log10(x).

Coefficients are listed in channel mask order, as defined by the channel mask constants that are included in the mmreg.h header file. Therefore, the first two values in a 6-to-2 channel fold-down represent the portions of the left output channel and the right output channel that are made up of the center left channel in the 6 channel stream.

You should set this property only if author-supplied fold-down values are persisted with the encoded content. Otherwise, let the decoder make its own calculations.

The Windows Media Audio 10 Professional codec currently only supports fold-down to two channels.

If the [MFPKEY\_WMADEC\_SPKRCFG](mfpkey-wmadec-spkrcfgproperty.md) property is set to **DSSPEAKER\_SURROUND**, the codec will ignore author-supplied fold-down coefficients and fold down to a 2-channel signal that can be processed by the matrix decoder of the receiver. This enables surround equipment to deliver four channels. This mode is supported only if the source is 5.1. The codec can only fold 8 channels to 2 channels.

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

 

 
