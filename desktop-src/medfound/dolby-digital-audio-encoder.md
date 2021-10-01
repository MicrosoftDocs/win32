---
description: The Dolby audio encoder is a Media Foundation transform (MFT) that encodes mono or stereo audio to Dolby Digital, also called Dolby AC-3.
ms.assetid: CBC31132-046C-4CD7-9DBA-20A9C666FB43
title: Dolby Digital Audio Encoder
ms.topic: reference
ms.date: 05/31/2018
---

# Dolby Digital Audio Encoder

The Dolby audio encoder is a [Media Foundation transform](media-foundation-transforms.md) (MFT) that encodes mono or stereo audio to Dolby Digital, also called Dolby AC-3. The encoder does not support multi-channel input, such as the 5.1 channel configuration.

> [!IMPORTANT]
> For versions of Windows prior to Windows 8, the Microsoft implementation of the Dolby Digital technology is restricted under terms of the Dolby Digital licensing program to use by Microsoft applications.

 

For more information about Dolby Digital audio, refer to Advanced Television Systems Committee (ATSC) document *Digital Audio Compression Standard (AC-3, E-AC-3) Revision B*.

## Class Identifier

The class identifier (CLSID) of the Dolby audio encoder is **CLSID\_CMSDolbyDigitalEncMFT**, defined in the header file wmcodecdsp.h.

## Output Types

The output type must be set first, before the input type. The following table lists the required and optional attributes for the output media type.




| Attribute | Description | Remarks | 
|-----------|-------------|---------|
| <a href="mf-mt-major-type-attribute.md">MF_MT_MAJOR_TYPE</a> | Major type. | Required. Must be <strong>MFMediaType_Audio</strong>. | 
| <a href="mf-mt-subtype-attribute.md">MF_MT_SUBTYPE</a> | Audio subtype. | Required. Must be <strong>MFAudioFormat_Dolby_AC3</strong>. | 
| <a href="mf-mt-audio-samples-per-second-attribute.md">MF_MT_AUDIO_SAMPLES_PER_SECOND</a> | Samples per second. | Required. The following values are supported:<ul><li>32000</li><li>44100</li><li>48000</li></ul> | 
| <a href="mf-mt-audio-num-channels-attribute.md">MF_MT_AUDIO_NUM_CHANNELS</a> | Number of channels. | Required. Must be either 1 (mono) or 2 (stereo). | 
| <a href="mf-mt-audio-channel-mask-attribute.md">MF_MT_AUDIO_CHANNEL_MASK</a> | Specifies the assignment of audio channels to speaker positions. | Optional. If set, the value must be 0x3 for stereo (front left and right channels) or 0x4 for mono (front center channel). | 
| <a href="mf-mt-audio-avg-bytes-per-second-attribute.md">MF_MT_AUDIO_AVG_BYTES_PER_SECOND</a> | Bit rate of the encoded AC-3 stream, in bytes per second. | Optional. See Remarks for valid values. If this attribute is not set, the encoder uses a default bit rate, as described in Remarks. | 




 

If the optional attributes are not set, the encoder adds them to the media type after the type is set.

## Input Types

The following table lists the required and optional attributes for the input media type.




| Attribute | Description | Remarks | 
|-----------|-------------|---------|
| <a href="mf-mt-major-type-attribute.md">MF_MT_MAJOR_TYPE</a> | Major type. | Required. Must be <strong>MFMediaType_Audio</strong>. | 
| <a href="mf-mt-subtype-attribute.md">MF_MT_SUBTYPE</a> | Audio subtype. | Required. Must be <strong>MFAudioFormat_PCM</strong> or <strong>MFAudioFormat_Float</strong>. | 
| <a href="mf-mt-audio-bits-per-sample-attribute.md">MF_MT_AUDIO_BITS_PER_SAMPLE</a> | Number of bits per audio sample. | Required. The value must be 16 if the subtype is <strong>MFAudioFormat_PCM</strong>, or 32 if the subtype is <strong>MFAudioFormat_Float</strong>. | 
| <a href="mf-mt-audio-samples-per-second-attribute.md">MF_MT_AUDIO_SAMPLES_PER_SECOND</a> | Samples per second. | Required. Must match the output type. | 
| <a href="mf-mt-audio-num-channels-attribute.md">MF_MT_AUDIO_NUM_CHANNELS</a> | Number of channels. | Required. Must match the output type. | 
| <a href="mf-mt-audio-block-alignment-attribute.md">MF_MT_AUDIO_BLOCK_ALIGNMENT</a> | Block alignment, in bytes. | Required. Calculate the value as follows:<ul><li><strong>MFAudioFormat_PCM</strong>: Number of channels × 2.</li><li><strong>MFAudioFormat_Float</strong>: Number of channels × 4.</li></ul> | 
| <a href="mf-mt-audio-avg-bytes-per-second-attribute.md">MF_MT_AUDIO_AVG_BYTES_PER_SECOND</a> | Bit rate of the encoded AC3 stream, in bytes per second. | Required. Must equal block alignment × samples per second. | 
| <a href="mf-mt-audio-channel-mask-attribute.md">MF_MT_AUDIO_CHANNEL_MASK</a> | Specifies the assignment of audio channels to speaker positions. | Optional. If set, the value must match the output type. | 
| <a href="mf-mt-audio-valid-bits-per-sample-attribute.md">MF_MT_AUDIO_VALID_BITS_PER_SAMPLE</a> | Number of valid bits of audio data in each audio sample. | Optional. If set, the value must be identical to <a href="mf-mt-audio-bits-per-sample-attribute.md">MF_MT_AUDIO_BITS_PER_SAMPLE</a>. | 




 

The encoder does not support sample-rate conversion or stereo/mono conversion.

## Remarks

Each Dolby AC-3 audio frame contains 1536 audio samples per channel. However, each input buffer to the encoder may contain any number of PCM samples. The size of each input buffer must be a multiple of the block alignment. The encoder caches input samples until it has enough for 1536 audio samples per channel; at which point the encoder outputs one AC-3 frame.

Each output buffer contains one raw AC-3 frame. The duration is equivalent to the duration of 1536 PCM samples at the current sampling rate (32 msec) at 48 kHz sample rate, 34.83 msec at 44.1 kHz, and 48 msec at 32 kHz). The size of each output buffer depends on the bit rate and the sample rate.

To specify the encoding bit rate, set the [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute in the output type. The following table shows the relation between encoding bit rate and MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND.



| Bit rate (kbps) | [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) | Remarks                                                 |
|-----------------|------------------------------------------------------------------------------------------|---------------------------------------------------------|
| 64              | 8000                                                                                     | Mono only.                                              |
| 80              | 10000                                                                                    | Mono only.                                              |
| 96              | 12000                                                                                    | Mono only.                                              |
| 112             | 14000                                                                                    | Mono only.                                              |
| 128             | 16000                                                                                    | Mono or stereo.                                         |
| 160             | 20000                                                                                    | Mono or stereo.                                         |
| 192             | 24000                                                                                    | Mono or stereo. This is the default setting for mono.   |
| 224             | 28000                                                                                    | Mono or stereo.                                         |
| 256             | 32000                                                                                    | Mono or stereo. This is the default setting for stereo. |
| 320             | 40000                                                                                    | Stereo only.                                            |
| 384             | 48000                                                                                    | Stereo only.                                            |
| 448             | 56000                                                                                    | Stereo only.                                            |



 

The default encoding bit rate is set at 256 kbps for stereo and 192 kbps for mono. The default settings are reflected in the media types returned by the encoder's [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) method.

### Example Media Types

Here is an example of the media types that are needed to encode 16-bit integer PCM, 48-kHz stereo audio at the default bit rate of 256 kbps.

Output media type:

| Attribute                                                                           | Value                         |
|-------------------------------------------------------------------------------------|-------------------------------|
| [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md)                               | **MFMediaType\_Audio**        |
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md)                                      | **MFAudioFormat\_Dolby\_AC3** |
| [MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND](mf-mt-audio-samples-per-second-attribute.md) | 48000                         |
| [MF\_MT\_AUDIO\_NUM\_CHANNELS](mf-mt-audio-num-channels-attribute.md)              | 2                             |



 

Input media type:

| Attribute                                                                                | Value                  |
|------------------------------------------------------------------------------------------|------------------------|
| [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md)                                    | **MFMediaType\_Audio** |
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md)                                           | **MFAudioFormat\_PCM** |
| [MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE](mf-mt-audio-bits-per-sample-attribute.md)            | 16                     |
| [MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND](mf-mt-audio-samples-per-second-attribute.md)      | 48000                  |
| [MF\_MT\_AUDIO\_NUM\_CHANNELS](mf-mt-audio-num-channels-attribute.md)                   | 2                      |
| [MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT](mf-mt-audio-block-alignment-attribute.md)             | 4                      |
| [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) | 192000                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                       |
| Minimum supported server<br/> | None supported<br/>                                                               |
| DLL<br/>                      | <dl> <dt>Msac3enc.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 




