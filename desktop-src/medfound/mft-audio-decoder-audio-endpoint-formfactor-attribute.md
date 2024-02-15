---
description: Specifies the form factor for the audio endpoint device associated with an audio decoder MFT.
title: MFT_AUDIO_DECODER_AUDIO_ENDPOINT_FORMFACTOR attribute (mftransform.h)
ms.topic: reference
ms.date: 01/23/2024
---

# MFT\_AUDIO\_DECODER\_AUDIO\_ENDPOINT\_FORMFACTOR attribute

Specifies the form factor for the audio endpoint device associated with an audio decoder MFT.

## Data type

A **UINT32** that should be interpreted as a value from the [EndpointFormFactor](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-endpointformfactor) enumeration.

## Remarks

This attribute is set on components via the attribute store obtained from [IMFTransform::GetAttributes](/windows/win32/api/mftransform/nf-mftransform-imftransform-getattributes). The default value for this attribute is 10, which corresponds to [UnknownFormFactor](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-endpointformfactor). This value may not always be present, such as when the decoder is invoked for transcoding scenarios.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------|
| Minimum supported client | Windows Version 24H2 |
| Minimum supported server | Windows Server Version 24H2 |
| Header | mftransform.h |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Audio Decoder Attributes](audio-decoder-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt>  </dl>

 

 
