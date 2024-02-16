---
description: Specifies the identifier for the audio endpoint device associated with an audio decoder MFT.
title: MFT_AUDIO_DECODER_AUDIO_ENDPOINT_ID attribute (mftransform.h)
ms.topic: reference
ms.date: 01/23/2024
---

# MFT\_AUDIO\_DECODER\_AUDIO\_ENDPOINT\_ID attribute

Specifies the identifier for the audio endpoint device associated with an audio decoder MFT.

## Data type

Wide-character string

## Remarks

If set on the transform to a nonzero value, this attribute indicates that the data from this audio decoder transform will be rendered on the audio endpoint device specified by the null-terminated wide-character string. This value may not always be present, such as when the decoder is invoked for transcoding scenarios.

An example usage scenario for this attribute is an audio decoder MFT using the attribute value in a call [ActivateAudioInterfaceAsync](/windows/win32/api/mmdeviceapi/nf-mmdeviceapi-activateaudiointerfaceasync) to obtain information about which spatial audio format is enabled on the audio endpoint.

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

[**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt>  </dl>

 

 
