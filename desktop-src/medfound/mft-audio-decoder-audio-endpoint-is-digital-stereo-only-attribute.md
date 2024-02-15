---
description: Specifies whether the audio endpoint device associated with an audio decoder MFT only supports uncompressed stereo signals.
title: MFT_AUDIO_DECODER_AUDIO_ENDPOINT_DIGITAL_STEREO_ONLY attribute (mftransform.h)
ms.topic: reference
ms.date: 01/23/2024
---

# MFT\_AUDIO\_DECODER\_AUDIO\_ENDPOINT\_DIGITAL\_STEREO\_ONLY attribute

Specifies whether the audio endpoint device associated with an audio decoder MFT only supports uncompressed stereo signals.

## Data type

A **UINT32** that should be interpreted as a **BOOL**. The value is non-zero when the audio endpoint is a digital audio endpoint, such as a HDMI endpoint, that only supports uncompressed stereo.

## Remarks

This attribute is set on components via the attribute store obtained from [IMFTransform::GetAttributes](/windows/win32/api/mftransform/nf-mftransform-imftransform-getattributes). This value may not always be present, such as when the decoder is invoked for transcoding scenarios.

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

 

 
