---
description: The Microsoft MPEG Audio Decoder is a synchronous Media Foundation Transform (MFT) that enables decoding MPEG audio elementary stream formats using the Media Foundation (MF) pipeline.
ms.assetid: 29A0491D-CA0D-4909-96F0-5640D5EE77F9
title: MPEG Audio Decoder
ms.topic: reference
ms.date: 05/31/2018
---

# MPEG Audio Decoder

The Microsoft MPEG Audio Decoder is a synchronous [Media Foundation Transform](media-foundation-transforms.md) (MFT) that enables decoding MPEG audio elementary stream formats using the Media Foundation (MF) pipeline.

The decoder supports the following MPEG elementary stream formats.

-   MPEG-1 audio layers I and II (ISO/IEC 11172-3). 2. MPEG-2 backward-compatible, layers I and II (ISO

-   MPEG-2 backward-compatible, layers I and II (ISO/IEC 13818-3), mono and stereo only

## Class Identifier

The class identifier (CLSID) of the MPEG Audio decoder is **CLSID\_MSMPEGAudDecMFT**, defined in the header file wmcodecdsp.h.

## Input Media Types

The MPEG Audio decoder supports the following input media type attributes.



| Attribute                                                                               | Value                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md)                               | **MFMediaType\_Audio**                                                                                                                                                                                                                                                |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)                                      | **MFAudioFormat\_MPEG**                                                                                                                                                                                                                                               |
| [**MF\_MT\_AUDIO\_NUM\_CHANNELS**](mf-mt-audio-num-channels-attribute.md)              | (Optional) Usually 1 for mono or 2 for stereo, but can be up to 6 channels.<br/>                                                                                                                                                                                |
| [**MF\_MT\_AUDIO\_CHANNEL\_MASK**](mf-mt-audio-channel-mask-attribute.md)              | (Optional) Usually 0x4 for mono or 0x3 for stereo, but can also be any one of the channel masks associated with up to 6 channels (3/2/1, 3/2, 3/1, 2/2, 2/1). If present, the channel mask must be consistent with the specified input number of channels.<br/> |
| [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md) | (Optional) One of the following: 16000, 22050, 24000, 32000, 44100, 48000. If specified, the input sampling rate must be one of the valid MPEG sampling rates.<br/>                                                                                             |



 

## Output Media Types

The MPEG Audio decoder will support up to four output media subtypes, in the following order.

<dl> 1. Stereo, floating point.  
2. Stereo, 16-bit PCM.  
3. Mono, floating point (only if the input is mono or dual-mono).  
4. Mono, 16-bit PCM (only if the input is mono or dual-mono).  
</dl>

The decoder always supports stereo output and it is enumerated as the first output media type.

The decoder supports the following output media type attributes.



| Attribute                                                                           | Value                                                                      |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md)                               | **MFMediaType\_Audio**                                                     |
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md)                                      | Either **MFAudioFormat\_PCM** or **MFAudioFormat\_Float**                  |
| [MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE](mf-mt-audio-bits-per-sample-attribute.md)       | 16 or 32                                                                   |
| [MF\_MT\_AUDIO\_NUM\_CHANNELS](mf-mt-audio-num-channels-attribute.md)              | 1 or 2                                                                     |
| [MF\_MT\_AUDIO\_CHANNEL\_MASK](mf-mt-audio-channel-mask-attribute.md)              | 0x4 for mono or 0x3 for stereo                                             |
| [MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND](mf-mt-audio-samples-per-second-attribute.md) | One of the following: 16000, 22050, 24000, 32000, 44100, 48000.<br/> |



 

## Transform Attributes

The MPEG Audio decoder implements the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method. Applications can use this method to get or set the following attributes.



| Attribute                                                                               | Description                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CODECAPI\_AVDecAudioDualMono**](../directshow/avdecaudiodualmono-property.md)                   | Specifies whether 2-channel audio being decoded is dual mono or not. Read-only. Set by the MFT. For more information see [**eAVDecAudioDualMono**](/windows/win32/api/codecapi/ne-codecapi-eavdecaudiodualmono).                                                                                                                               |
| [**CODECAPI\_AVDecAudioDualMonoReproMode**](../directshow/avdecaudiodualmonorepromode-property.md) | Specifies how the decoder reproduces dual mono audio. The default value is **eAVDecAudioDualMonoReproMode\_LEFT\_MONO**.<br/> Read/Write. Applications can set this property to change the default behavior. For more information see [**eAVDecAudioDualMono**](/windows/win32/api/codecapi/ne-codecapi-eavdecaudiodualmono).<br/> |
| [**CODECAPI\_AVEncCommonMeanBitRate**](../directshow/avenccommonmeanbitrate-property.md)           | Specifies the compressed stream bit rate. Read-only. Set by the MFT.                                                                                                                                                                                                                                         |



 

## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 
