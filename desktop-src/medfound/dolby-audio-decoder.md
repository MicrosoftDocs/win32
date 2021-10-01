---
description: The Dolby audio decoder is an MFT that decodes Dolby Digital (AC-3) and Dolby Digital Plus.
ms.assetid: A968914A-E4C5-4472-8776-C73F5910089A
title: Dolby Audio Decoder
ms.topic: reference
ms.date: 05/31/2018
---

# Dolby Audio Decoder

The Dolby audio decoder is a [Media Foundation transform](media-foundation-transforms.md) (MFT) that decodes the following stream types:

-   Dolby Digital, also called Dolby AC-3
-   Dolby Digital Plus, also called Enhanced AC-3 (E-AC-3)

> [!IMPORTANT]
> For versions of Windows prior to Windows 8, the Microsoft implementation of the Dolby Digital technology is restricted under terms of the Dolby Digital licensing program to use by Microsoft applications.

 

For more information about these formats, refer to Advanced Television Systems Committee (ATSC) document *Digital Audio Compression Standard (AC-3, E-AC-3) Revision B*.

The decoder can also convert a Dolby Digital Plus stream to Dolby Digital format for AC-3 S/PIDF output, or format a Dolby Digital Plus stream for HDMI digital output.

## Class Identifier

The class identifier (CLSID) of the Dolby audio decoder is **CLSID\_CMSDDPlusDecMFT**, defined in the header file wmcodecdsp.h.

## Input Types

The Dolby audio decoder supports the following input subtypes.



| Subtype                                 | Description                                                                                                                                                 | Header       |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **MEDIASUBTYPE\_DOLBY\_AC3**            | Dolby Digital audio.                                                                                                                                        | mfapi.h      |
| **MEDIASUBTYPE\_DVM**                   | Dolby Digital audio; see [**Audio Subtypes**](../directshow/audio-subtypes.md). This subtype can be used interchangeably with **MEDIASUBTYPE\_DOLBY\_AC3**.<br/> | wmcodecdsp.h |
| **MFAudioFormat\_Dolby\_Digital\_Plus** | Dolby Digital Plus audio.                                                                                                                                   | mfapi.h      |



 

The following table lists the requires and optional attributes for the input media type.




| Attribute | Description | Remarks | 
|-----------|-------------|---------|
| <a href="mf-mt-major-type-attribute.md">MF_MT_MAJOR_TYPE</a> | Major type. | Required. Must be <strong>MFMediaType_Audio</strong>. | 
| <a href="mf-mt-subtype-attribute.md">MF_MT_SUBTYPE</a> | Audio subtype. | Required. See the previous table for details. | 
| <a href="mf-mt-audio-samples-per-second-attribute.md">MF_MT_AUDIO_SAMPLES_PER_SECOND</a> | Sample rate, in samples per second. | Optional. Valid values are: 48000, 44100, 32000, 24000, 22050, and 16000. If this attribute is not set, the default value is 48000. <br /><blockquote>[!Note]<br />Dolby AC-3 streams are limited to the three highest rates in this list.</blockquote><br /> | 
| <a href="mf-mt-audio-num-channels-attribute.md">MF_MT_AUDIO_NUM_CHANNELS</a> | Number of channels, including the low frequency (LFE) channel, if present. | Optional. Valid values are in the range 1 (mono) to 8 (7.1 channel configuration). If this attribute is not set, the default value is 2 (stereo). | 
| <a href="mf-mt-audio-channel-mask-attribute.md">MF_MT_AUDIO_CHANNEL_MASK</a> | Specifies the assignment of audio channels to speaker positions. | Optional. If specified, the value must be consistent with the number of audio channels. If the attribute is not set, the decoder uses a default channel mask, based on the number of channels. | 




 

The following table lists the supported Dolby channel configurations.




| Channel configuration | Number of channels | Channel masks | 
|-----------------------|--------------------|---------------|
| 1/0 (mono) | 1 | 0x4 (<strong>SPEAKER_FRONT_CENTER</strong>) | 
| 2/0 (stereo) or 1+1 (dual mono) | 2 | 0x3 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong>) | 
| 3/0 | 3 | 0x7 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | SPEAKER_FRONT_CENTER) | 
| 2/1 | 3 | 0x103 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_BACK_CENTER</strong>) | 
| 3/1 | 4 | 0x107 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_FRONT_CENTER</strong> | <strong>SPEAKER_BACK_CENTER</strong>) | 
| 2/2 | 4 | 0x33 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_BACK_LEFT</strong> | <strong>SPEAKER_BACK_RIGHT</strong>)<br /> or<br /> 0x603 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_SIDE_LEFT</strong> | <strong>SPEAKER_SIDE_RIGHT</strong>) <br /> | 
| 3/2 | 5 | 0x37 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_FRONT_CENTER</strong> | <strong>SPEAKER_BACK_LEFT</strong> | <strong>SPEAKER_BACK_RIGHT</strong>)<br /> or<br /> 0x607 (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_FRONT_CENTER</strong> | <strong>SPEAKER_SIDE_LEFT</strong> | <strong>SPEAKER_SIDE_RIGHT</strong>) <br /> | 
| 3/2 + LFE | 6 | 0x3F (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_FRONT_CENTER</strong> | <strong>SPEAKER_LOW_FREQUENCY</strong> | <strong>SPEAKER_BACK_LEFT</strong> | <strong>SPEAKER_BACK_RIGHT</strong>)<br /> or<br /> 0x60F (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_FRONT_CENTER</strong> | <strong>SPEAKER_LOW_FREQUENCY</strong> | <strong>SPEAKER_SIDE_LEFT</strong> | <strong>SPEAKER_SIDE_RIGHT</strong>)<br /> | 
| 3/2/2 + LFE<blockquote>[!Note]<br />Dolby Digital Plus only.</blockquote><br /><br /> | 8 | 0x63F (<strong>SPEAKER_FRONT_LEFT</strong> | <strong>SPEAKER_FRONT_RIGHT</strong> | <strong>SPEAKER_FRONT_CENTER</strong> | <strong>SPEAKER_LOW_FREQUENCY</strong> | <strong>SPEAKER_BACK_LEFT</strong> | <strong>SPEAKER_BACK_RIGHT</strong> | SPEAKER_SIDE_LEFT | SPEAKER_SIDE_RIGHT) | 




 

In addition, channel configurations 1/0, 2/0, 3/0, 2/1, 3/1, and 2/2 may also appear with an LFE channel.

## Output Types

The Dolby audio decoder supports the following output subtypes.



| Subtype                                                   | Description                                                                                                                               | Header    |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **MFAudioFormat\_Dolby\_AC3\_SPDIF**                      | Dolby AC-3 audio formatted for S/PDIF digital output.                                                                                     | mfapi.h   |
| **KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_DIGITAL\_PLUS** | Dolby Digital Plus audio formatted for HDMI digital output.                                                                               | ksmedia.h |
| **MFAudioFormat\_Float**                                  | IEEE 32-bit floating-point PCM audio<br/> **Windows 10**: stereo, 5.1, 7.1<br/> **Previous versions**: stereo, 5.1<br/> | mfapi.h   |
| **MFAudioFormat\_PCM**                                    | 16-bit PCM audio<br/> **Windows 10**: stereo, 5.1, 7.1<br/> **Previous versions**: stereo, 5.1<br/>                     | mfapi.h   |



 

The following table lists the required and optional attributes for the output media type.




| Attribute | Description | Remarks | 
|-----------|-------------|---------|
| <a href="mf-mt-major-type-attribute.md">MF_MT_MAJOR_TYPE</a> | Major type. | Required. Must be <strong>MFMediaType_Audio</strong>. | 
| <a href="mf-mt-subtype-attribute.md">MF_MT_SUBTYPE</a> | Audio subtype. | Required. See the previous table for details. | 
| <a href="mf-mt-audio-samples-per-second-attribute.md">MF_MT_AUDIO_SAMPLES_PER_SECOND</a> | Sample rate, in samples per second. | Required. Valid values are: 48000, 44100, 32000, 24000, 22050, and 16000. The output sample rate must be identical to the input sample rate. The decoder cannot change the sampling rate of the stream. | 
| <a href="mf-mt-audio-num-channels-attribute.md">MF_MT_AUDIO_NUM_CHANNELS</a> | Number of channels, including the low frequency (LFE) channel, if present. | Required for PCM output. <br /> Not needed for digital output. <br /> If the input type is mono, stereo, or dual-mono (all without LFE channel), the only valid value is 2, for stereo output. Otherwise, the value can be: <br /><ul><li>2 for stereo downmix</li><li>6 for 5.1 channel configurations</li><li>8 for 7.1 channel configurations</li></ul> | 
| <a href="mf-mt-audio-channel-mask-attribute.md">MF_MT_AUDIO_CHANNEL_MASK</a> | Specifies the assignment of audio channels to speaker positions. | Required for PCM output if the number of channels is greater than 2. The value must be:<br /><ul><li>0x3 for stereo output</li><li>0x3F for 5.1 channel output</li><li>0x63F for 7.1 channel output</li></ul>Not needed for digital output. <br /> | 
| <a href="mf-mt-audio-bits-per-sample-attribute.md">MF_MT_AUDIO_BITS_PER_SAMPLE</a> | Number of bits per audio sample. | Required for PCM output. The value must be 32 for <strong>MFAudioFormat_Float</strong>, and 16 for <strong>MFAudioFormat_PCM</strong>.<br /> Not needed for digital output.<br /> | 
| <a href="mf-mt-audio-valid-bits-per-sample-attribute.md">MF_MT_AUDIO_VALID_BITS_PER_SAMPLE</a> | Number of valid bits of audio data in each audio sample. | Optional for PCM output. If set, the value must be identical to <a href="mf-mt-audio-bits-per-sample-attribute.md">MF_MT_AUDIO_BITS_PER_SAMPLE</a>.<br /> Not needed for the digital output subtypes.<br /> | 
| <a href="mf-mt-audio-block-alignment-attribute.md">MF_MT_AUDIO_BLOCK_ALIGNMENT</a> | Block alignment, in bytes. | Optional for PCM output. Not needed for digital output. | 
| <a href="mf-mt-audio-avg-bytes-per-second-attribute.md">MF_MT_AUDIO_AVG_BYTES_PER_SECOND</a> | Average number of bytes per second. | Optional for PCM output. Not needed for digital output. | 




 

## Transform Attributes

The Dolby audio decoder implements the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method. The application can use this method to get or set the following attributes.



| Attribute                                                                                | Description                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CODECAPI\_AVDecAudioDualMono](../directshow/avdecaudiodualmono-property.md)                        | Specifies whether a 2-channel Dolby audio stream is encoded as stereo or dual-mono. Before the first Dolby frame is decoded, the value is **eAVDecAudioDualMono\_UnSpecified**. After decoding begins, the value reflects the most recent Dolby frame.<br/> Read-only. <br/> |
| [CODECAPI\_AVDecAudioDualMonoReproMode](../directshow/avdecaudiodualmonorepromode-property.md)      | Specifies how the decoder reproduces dual-mono audio. The default value is **eAVDecAudioDualMonoReproMode\_LEFT\_MONO**. The application can set this property at any time.<br/> Read/write.<br/>                                                                            |
| [CODECAPI\_AVDecCommonMeanBitRate](../directshow/avdeccommonmeanbitrate.md)                         | For Dolby Digital (AC-3) streams, specifies the bit rate of the input stream in bits per second. For Dolby Digital Plus (E-AC3), the value is always zero.<br/> Read only.<br/>                                                                                              |
| [CODECAPI\_AVDecDDDynamicRangeScaleHigh](../directshow/avdecdddynamicrangescalehigh-property.md)    | The high-level cut when the decoder performs dynamic range control.<br/> Read/write.<br/>                                                                                                                                                                                    |
| [CODECAPI\_AVDecDDDynamicRangeScaleLow](../directshow/avdecdddynamicrangescalelow-property.md)      | The low-level boost when the decoder performs dynamic range control.<br/> Read/write.<br/>                                                                                                                                                                                   |
| [CODECAPI\_AVDecDDOperationalMode](../directshow/avdecddoperationalmode-property.md)                | The compression control mode.<br/> Read/write.<br/>                                                                                                                                                                                                                          |
| [CODECAPI\_AVDecDDStereoDownMixMode](codecapi-avdecddstereodownmixmode.md)              | The type of stereo downmix. This property applies when the input is a multichannel stream and the output is a stereo stream.<br/> Read/write.<br/>                                                                                                                           |
| [MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE](mft-support-dynamic-format-change-attribute.md) | This attribute returns **FALSE**, indicating that the decoder must be drained before a new input type is set.<br/> Read/write.<br/>                                                                                                                                          |



 

## Remarks

The decoder accepts only raw Dolby streams, as defined by A/52B. Payloads such as Packetized Elementary Streams (PES) are not supported. For Dolby Digital Plus, the decoder decodes up to 5.1 channels. On Windows 10, 7.1 channel streams are decoded without downmix. On previous OS versions, if the stream is 7.1 channels, only the 5.1 channel downmix will be decoded. If the stream is Dolby Digital Plus with more than one independent substream, only independent substream 0 is decoded. The decoder skips other independent substreams. In addition, the decoder skips all dependent substreams. The decoder supports decryption and decoding of streams that are protected by Digital Rights Management (DRM) technology.

If the input media type has a channel configuration other than mono, stereo, or dual-mono (all without LFE channel), the decoder provides two options for the output channel configurations:

-   8-channel output (7.1 channel configuration)
-   6-channel output (5.1 channel configuration)
-   Stereo downmix

If stereo downmix is selected, the type of downmix can be set on the MFT by using the [CODECAPI\_AVDecDDStereoDownMixMode](codecapi-avdecddstereodownmixmode.md) property.

If the output type is **MFAudioFormat\_Dolby\_AC3\_SPDIF**, each output buffer contains 6,144 bytes. The buffer starts with an 8-byte S/PDIF header, followed by a compressed AC-3 frame, followed by zero padding to 6,144 bytes.

If the output type is **KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_DIGITAL\_PLUS**, each output buffer contains 24,576 bytes. The buffer starts with an 8-byte S/PDIF header, followed by 1–6 compressed Dolby Digital Plus frames corresponding to 1,536 PCM samples, followed by zero padding to 24,576 bytes. For HDMI output, only independent substream 0 is packed.

The decoder MFT is registered with the flag **MFT\_ENUM\_FLAG\_FIELDOFUSE**, which indicates that the MFT that must be unlocked by the application before use. For more information, see [Field of Use Restrictions](field-of-use-restrictions.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | None supported<br/>                                                                  |
| DLL<br/>                      | <dl> <dt>Msauddecmft.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 
