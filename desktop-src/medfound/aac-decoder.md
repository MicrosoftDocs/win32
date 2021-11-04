---
description: 'The Microsoft Media Foundation AAC decoder is a Media Foundation Transform that decodes the following Advanced Audio Coding (AAC) and High Efficiency AAC (HE-AAC) profiles:'
ms.assetid: 036fb0ee-8165-41a3-b41a-2e9bf035a6a6
title: AAC Decoder
ms.topic: reference
ms.date: 05/31/2018
---

# AAC Decoder

The Microsoft Media Foundation AAC decoder is a [Media Foundation Transform](media-foundation-transforms.md) that decodes the following Advanced Audio Coding (AAC) and High Efficiency AAC (HE-AAC) profiles:

-   MPEG-2 AAC Low Complexity (LC) profile (multichannel).
-   MPEG-4 HE-AAC v1 (multichannel) with AAC-LC core.
-   MPEG-4 HE-AAC v2 (stereo) with AAC-LC core.

The AAC decoder supports both raw AAC streams with no headers and AAC in an audio data transport stream (ADTS).

Starting in Windows 8, the AAC decoder also supports decoding MPEG-4 audio transport streams with a multiplex layer (LATM) and synchronization layer (LOAS). It can also convert an LATM/LOAS stream to ADTS.

## Class Identifier

The class identifier (CLSID) of the AAC encoder is **CLSID\_CMSAACDecMFT**, defined in the header file wmcodecdsp.h.

## Media Types

The AAC decoder supports the following media types.

### Input Types

The AAC decoder supports the following audio subtypes:



| Subtype                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Header       |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **MFAudioFormat_AAC**      | Raw AAC or ADTS AAC.<br/> For this subtype, the media type gives the sample rate and number of channels prior to the application of spectral band replication (SBR) and parametric stereo (PS) tools, if present. The effect of the SBR tool is to double the decoded sample rate relative to the core AAC-LC sample rate. The effect of the PS tool is to decode stereo from a mono-channel core AAC-LC stream.<br/> This subtype is equivalent to **MEDIASUBTYPE_MPEG_HEAAC**, defined in wmcodecdsp.h. See [Audio Subtype GUIDs](audio-subtype-guids.md). <br/> The [MPEG-4 File Source](mpeg-4-file-source.md) and the ADTS Parser output this subtype. <br/> | mfapi.h      |
| **MEDIASUBTYPE_RAW_AAC1** | Raw AAC. <br/> This subtype is used for AAC contained in an AVI file with the audio format tag equal to WAVE_FORMAT_RAW_AAC1 (0x00FF). <br/> For this subtype, the media type gives the sample rate and number of channels after the SBR and PS tools are applied, if present.<br/>                                                                                                                                                                                                                                                                                                                                                                                      | wmcodecdsp.h |



 

To configure the AAC decoder, set the following attributes on the input media type.




| Attribute | Description | Remarks | 
|-----------|-------------|---------|
| <a href="mf-mt-major-type-attribute.md"><strong>MF_MT_MAJOR_TYPE</strong></a> | Major type. | Must be <strong>MFMediaType_Audio</strong>. | 
| <a href="mf-mt-subtype-attribute.md"><strong>MF_MT_SUBTYPE</strong></a> | Audio subtype. | Refer to the previous description for details. | 
| <a href="mf-mt-aac-audio-profile-level-indication.md">MF_MT_AAC_AUDIO_PROFILE_LEVEL_INDICATION</a> | Audio profile and level. <br /> | Optional. Applies only to <strong>MFAudioFormat_AAC</strong>. <br /> The value of this attribute is the <strong>audioProfileLevelIndication</strong> field, as defined by ISO/IEC 14496-3. <br /> If unknown, set to zero or 0xFE ("no audio profile specified").<br /> | 
| <a href="mf-mt-aac-payload-type.md">MF_MT_AAC_PAYLOAD_TYPE</a> | Payload type.<br /> | Applies only to <strong>MFAudioFormat_AAC</strong>. The decoder supports the following payload types: <br /><ul><li>0: Raw AAC. The stream contains raw_data_block() elements only, as defined by MPEG-2.</li><li>1: ADTS. The stream contains an adts_sequence(), as defined by MPEG-2. Only one raw_data_block() per adts_frame() is allowed.</li><li>3: Audio transport stream with a synchronization layer (LOAS) and a multiplex layer (LATM). Of the three types of LOAS, only <strong>AudioSyncStream</strong> is supported. The multiplex layer is <strong>AudioMuxElement</strong>, restricted to one audio program and one layer.</li></ul><a href="mf-mt-aac-payload-type.md">MF_MT_AAC_PAYLOAD_TYPE</a> is optional. If this attribute is not specified, the default value 0 is used, which specifies the stream contains raw_data_block elements only.<br /> | 
| <a href="mf-mt-audio-bits-per-sample-attribute.md"><strong>MF_MT_AUDIO_BITS_PER_SAMPLE</strong></a> | Desired bit depth of the decoded PCM audio. | 
| <a href="mf-mt-audio-channel-mask-attribute.md"><strong>MF_MT_AUDIO_CHANNEL_MASK</strong></a> | Specifies the assignment of audio channels to speaker positions. | Optional. For more information, see <a href="#format-constraints">Format Constraints</a>. | 
| <a href="mf-mt-audio-num-channels-attribute.md"><strong>MF_MT_AUDIO_NUM_CHANNELS</strong></a> | Number of channels, including the low frequency (LFE) channel, if present.<br /> | The interpretation of this value depends on the media subtype, as described previously.<br /> | 
| <a href="mf-mt-audio-samples-per-second-attribute.md"><strong>MF_MT_AUDIO_SAMPLES_PER_SECOND</strong></a> | Sample rate, in samples per second.<br /> | The interpretation of this value depends on the media subtype, as described previously.<br /> | 
| <a href="mf-mt-user-data-attribute.md"><strong>MF_MT_USER_DATA</strong></a> | Additional format information. | The value of this attribute depends on the subtype.<br /><ul><li><strong>MFAudioFormat_AAC</strong>: Contains the portion of the <a href="/windows/desktop/api/mmreg/ns-mmreg-heaacwaveinfo"><strong>HEAACWAVEINFO</strong></a> structure that appears after the <strong>WAVEFORMATEX</strong> structure (that is, after the <strong>wfx</strong> member). This is followed by the AudioSpecificConfig() data, as defined by ISO/IEC 14496-3.</li><li><strong>MEDIASUBTYPE_RAW_AAC1</strong>: Contains the AudioSpecificConfig() data. This data must appear; otherwise, the decoder will reject the media type.</li></ul>The length of the AudioSpecificConfig() data is 2 bytes for AAC-LC or HE-AAC with implicit signaling of SBR/PS. It is more than 2 bytes for HE-AAC with explicit signaling of SBR/PS.<br /> The value of <strong>audioObjectType</strong> as defined in AudioSpecificConfig() must be 2, indicating AAC-LC. The value of <strong>extensionAudioObjectType</strong> must be 5 for SBR or 29 for PS. <br /> | 




 

### Output Types

The decoder supports the following output types:




| Subtype | Description | 
|---------|-------------|
| <strong>MFAudioFormat_Float</strong> | IEEE floating-point audio. | 
| <strong>MFAudioFormat_PCM</strong> | 16-bit PCM audio. | 
| <strong>MFAudioFormat_AAC</strong> | Requires Windows 8. <br /> This output type can be used to convert an AAC stream in the LOAS/LATM format to ADTS format. <br /> To convert an LOAS/LATM stream to an ADTS stream, set the input type to <strong>MFAudioFormat_AAC</strong> with payload type 3 (LOAS). Then set the output type to <strong>MFAudioFormat_AAC</strong> with payload type 1 (ADTS). The decoder will reformat the conainter without decoding the bitstream. <br /><blockquote>[!Note]<br />The decoder does not register <strong>MFAudioFormat_AAC</strong> as an output type. However, if the application sets the input type as described, the <a href="/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype"><strong>IMFTransform::GetOutputAvailableType</strong></a> method returns <strong>MFAudioFormat_AAC</strong> in the list of available output types.</blockquote><br /><br /> | 




 

If the input stream contains more than two channels, the AAC decoder provides two options for the output format:

-   The same channel configuration as the input type.
-   Stereo fold-down.

## Format Constraints

The decoded audio sampling rate must be one of the following, after SBR is applied (if present):

-   8 kHz
-   11.025 kHz
-   12 kHz
-   16 kHz
-   22.05 kHz
-   24 kHz
-   32 kHz
-   44.1 kHz
-   48 kHz

Sampling rates above 48 kHz are not supported.

The decoder supports up to 6 audio channels. For each speaker configuration, the decoder expects the AAC syntactic elements to appear in a certain order. The following table lists the supported speaker configurations. The third column of the table lists the expected syntactic elements and their order, using the following notation:

-   &lt;SCE1&gt;: The single_channel_element (SCE) associated with the front center speaker.
-   &lt;SCE2&gt;: The SCE associated with the back center speaker.
-   &lt;CPE1&gt;: The channel_pair_element (CPE) associated with the front speakers.
-   &lt;CPE2&gt;: The CPE associated with the back (or side) speakers
-   &lt;LFE&gt;: The lfe_channel_element (LFE).

For more information about these syntactic elements, refer to ISO/IEC 13818-7.



| Configuration       | Channel Mask                                                                                                                                                              | AAC Syntactic Elements                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Mono                | **SPEAKER_FRONT_CENTER**                                                                                                                                                | &lt;SCE1&gt;                                    |
| Stereo or dual mono | **SPEAKER_FRONT_LEFT** \| **SPEAKER_FRONT_RIGHT**                                                                                                                     | &lt;CPE1&gt;                                    |
| 2/1                 | **SPEAKER_FRONT_LEFT** \| **SPEAKER_FRONT_RIGHT** \| **SPEAKER_BACK_CENTER**                                                                                        | &lt;CPE1&gt;&lt;SCE1&gt;                        |
| 2/2                 | **SPEAKER_FRONT_LEFT** \| **SPEAKER_FRONT_RIGHT** \| **SPEAKER_BACK_LEFT** \| **SPEAKER_BACK_RIGHT**                                                              | &lt;CPE1&gt;&lt;CPE2&gt;                        |
| 3/0                 | **SPEAKER_FRONT_LEFT** \| **SPEAKER_FRONT_RIGHT** \| **SPEAKER_FRONT_CENTER**                                                                                       | &lt;SCE1&gt;&lt;CPE1&gt;                        |
| 3/1                 | **SPEAKER_FRONT_LEFT** \| **SPEAKER_FRONT_RIGHT** \| **SPEAKER_FRONT_CENTER** \| **SPEAKER_BACK_CENTER**                                                          | &lt;SCE1&gt;&lt;CPE1&gt;&lt;SCE2&gt;            |
| 3/2                 | **SPEAKER_FRONT_LEFT** \| **SPEAKER_FRONT_RIGHT** \| **SPEAKER_FRONT_CENTER** \| **SPEAKER_BACK_LEFT** \| **SPEAKER_BACK_RIGHT**                                | &lt;SCE1&gt;&lt;CPE1&gt;&lt;CPE2&gt;            |
| 3/2 + LFE           | **SPEAKER_FRONT_LEFT** \| **SPEAKER_FRONT_RIGHT** \| **SPEAKER_FRONT_CENTER** \| **SPEAKER_LOW_FREQUENCY** \| **SPEAKER_BACK_LEFT** \| **SPEAKER_BACK_RIGHT** | &lt;SCE1&gt;&lt;CPE1&gt;&lt;CPE2&gt;&lt;LFE&gt; |



 

For raw AAC, each input sample must contain exactly one full AAC compressed frame.

For ADTS, each input sample can contain multiple audio frames, as well as partial frames   that is, frames can span sample boundaries. Each ADTS header must be followed by one AAC frame.

The AAC decoder does not support any of the following:

-   Main profile, Sample-Rate Scalable (SRS) profile, or Long Term Prediction (LTP) profile.
-   Audio data interchange format (ADIF).
-   LATM/LAOS transport streams.
-   Coupling channel elements (CCEs). The decoder will skip audio frames with CCEs.
-   AAC-LC with a 960-sample frame size. Only 1024-sample frames are supported.

## Transform Attributes

The AAC decoder implements the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method. Applications can use this method to get or set the following attributes.




| Attribute | Description | 
|-----------|-------------|
| <a href="/windows/desktop/DirectShow/avdecaudiodualmono-property"><strong>CODECAPI_AVDecAudioDualMono</strong></a> | Specifies whether 2-channel audio is encoded as stereo or dual mono. Treat as read-only. | 
| <a href="/windows/desktop/DirectShow/avdecaudiodualmonorepromode-property"><strong>CODECAPI_AVDecAudioDualMonoReproMode</strong></a> | Specifies how the decoder reproduces dual mono audio. The default value is <strong>eAVDecAudioDualMonoReproMode_LEFT_MONO</strong>: Output Ch1 to the left and right speakers. <br /> Applications can set this property to change the default behavior.<br /> | 
| <a href="mft-support-dynamic-format-change-attribute.md"><strong>MFT_SUPPORT_DYNAMIC_FORMAT_CHANGE</strong></a> | The AAC decoder does not handle dynamic format changes, and must be flushed or drained before a new input media type is set. Treat this attribute as read-only. <br /><blockquote>[!Note]<br />The AAC decoder incorrectly reports a value of <strong>TRUE</strong> for this attribute.</blockquote><br /><br /> In Windows 7, the decoder incorrectly reports a value of <strong>TRUE</strong> for this attribute. In Windows 8, the decoder reports <strong>FALSE</strong>, which is the correct value<br /> | 




 

## Example Media Types

Here is an example of the input media type needed for a 6-channel, 48-kHz AAC-LC stream, using a raw AAC payload:



| Attribute                                                                                      | Value                                                                                |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**MF_MT_MAJOR_TYPE**](mf-mt-major-type-attribute.md)                                      | **MFMediaType_Audio**                                                               |
| [**MF_MT_SUBTYPE**](mf-mt-subtype-attribute.md)                                             | **MFAudioFormat_AAC**                                                               |
| [**MF_MT_AUDIO_SAMPLES_PER_SECOND**](mf-mt-audio-samples-per-second-attribute.md)        | 48000                                                                                |
| [**MF_MT_AUDIO_NUM_CHANNELS**](mf-mt-audio-num-channels-attribute.md)                     | 6                                                                                    |
| [MF_MT_AAC_PAYLOAD_TYPE](mf-mt-aac-payload-type.md)                                       | 0                                                                                    |
| [**MF_MT_USER_DATA**](mf-mt-user-data-attribute.md)                                        | {0x00, 0x00, 0x2a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x11, 0xb0} |
| [MF_MT_AAC_AUDIO_PROFILE_LEVEL_INDICATION](mf-mt-aac-audio-profile-level-indication.md) | 0x2a (optional)                                                                      |



 

The first 12 bytes of [**MF_MT_USER_DATA**](mf-mt-user-data-attribute.md) correspond to the following [**HEAACWAVEINFO**](/windows/desktop/api/mmreg/ns-mmreg-heaacwaveinfo) structure members:

-   **wPayloadType** = 0 (raw AAC)
-   **wAudioProfileLevelIndication** = 0x2a (AAC Profile, Level 4)
-   **wStructType** = 0

The last two bytes of [**MF_MT_USER_DATA**](mf-mt-user-data-attribute.md) contain the value of AudioSpecificConfig(), as defined by MPEG-4.

-   AudioSpecificConfig.audioObjectType = 2 (AAC LC) (5 bits)
-   AudioSpecificConfig.samplingFrequencyIndex = 3 (4 bits)
-   AudioSpecificConfig.channelConfiguration = 6 (4 bits)
-   GASpecificConfig.frameLengthFlag = 0 (1 bit)
-   GASpecificConfig.dependsOnCoreCoder = 0 (1 bit)
-   GASpecificConfig.extensionFlag = 0 (1 bit)

Given this input type, use the following output media type to get 6-channel, 32-bit floating point PCM audio from the decoder:



| Attribute                                                                                    | Value                    |
|----------------------------------------------------------------------------------------------|--------------------------|
| [**MF_MT_MAJOR_TYPE**](mf-mt-major-type-attribute.md)                                    | **MFMediaType_Audio**   |
| [**MF_MT_SUBTYPE**](mf-mt-subtype-attribute.md)                                           | **MFAudioFormat_Float** |
| [**MF_MT_AUDIO_BITS_PER_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md)            | 32                       |
| [**MF_MT_AUDIO_SAMPLES_PER_SECOND**](mf-mt-audio-samples-per-second-attribute.md)      | 48000                    |
| [**MF_MT_AUDIO_NUM_CHANNELS**](mf-mt-audio-num-channels-attribute.md)                   | 6                        |
| [**MF_MT_AUDIO_AVG_BYTES_PER_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) | 1152000 (optional)       |
| [**MF_MT_AUDIO_BLOCK_ALIGNMENT**](mf-mt-audio-block-alignment-attribute.md)             | 24 (optional)            |
| [**MF_MT_AUDIO_CHANNEL_MASK**](mf-mt-audio-channel-mask-attribute.md)                   | 0x3f (optional)          |



 

If Platform Update Supplement for Windows Vista is installed, the AAC audio decoder is available on Windows Vista, but is accessible on Windows Vista only by using the [Source Reader](source-reader.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                                                                                                     |
| DLL<br/>                      | <dl> <dt>Msmpeg2adec.dll on Windows 7; </dt> <dt>MSAudDecMFT.dll on Windows 8</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[AAC Media Types](aac-media-types.md)
</dt> <dt>

[Audio Media Types](audio-media-types.md)
</dt> <dt>

[**Microsoft MPEG-1/DD/AAC Audio Decoder**](/windows/desktop/DirectShow/microsoft-mpeg-1-dd-audio-decoder)
</dt> <dt>

[MPEG-4 Support in Media Foundation](mpeg-4-support-in-media-foundation.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> </dl>
