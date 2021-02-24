---
description: This topic describes how to specify the format of an Advanced Audio Coding (AAC) stream in Media Foundation.
ms.assetid: 82218bc5-6660-4253-b50c-b6d9f30be3d5
title: AAC Media Types
ms.topic: article
ms.date: 05/31/2018
---

# AAC Media Types

This topic describes how to specify the format of an Advanced Audio Coding (AAC) stream in Media Foundation.

Two subtypes are defined for AAC audio:



| Subtype                     | Description          | Header       |
|-----------------------------|----------------------|--------------|
| **MFAudioFormat\_AAC**      | Raw AAC or ADTS AAC. | mfapi.h      |
| **MEDIASUBTYPE\_RAW\_AAC1** | Raw AAC.             | wmcodecdsp.h |



 

<dl> <dt>

<span id="MFAudioFormat_AAC"></span><span id="mfaudioformat_aac"></span><span id="MFAUDIOFORMAT_AAC"></span>MFAudioFormat\_AAC
</dt> <dd>

For this subtype, the media type gives the sample rate and number of channels prior to the application of spectral band replication (SBR) and parametric stereo (PS) tools, if present. The effect of the SBR tool is to double the decoded sample rate relative to the core AAC-LC sample rate. The effect of the PS tool is to decode stereo from a mono-channel core AAC-LC stream.

This subtype is equivalent to **MEDIASUBTYPE\_MPEG\_HEAAC**, defined in wmcodecdsp.h. See [Audio Subtype GUIDs](audio-subtype-guids.md).

</dd> <dt>

<span id="MEDIASUBTYPE_RAW_AAC1"></span><span id="mediasubtype_raw_aac1"></span>MEDIASUBTYPE\_RAW\_AAC1
</dt> <dd>

This subtype is used for AAC contained in an AVI file with the audio format tag equal to WAVE\_FORMAT\_RAW\_AAC1 (0x00FF).

For this subtype, the media type gives the sample rate and number of channels after the SBR and PS tools are applied, if present.

</dd> </dl>

The following media type attributes apply to AAC audio.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mf-mt-major-type-attribute.md"><strong>MF_MT_MAJOR_TYPE</strong></a></td>
<td>Major type. Must be <strong>MFMediaType_Audio</strong>.</td>
</tr>
<tr class="even">
<td><a href="mf-mt-subtype-attribute.md"><strong>MF_MT_SUBTYPE</strong></a></td>
<td>Audio subtype. Refer to the previous description for details.</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-aac-audio-profile-level-indication.md">MF_MT_AAC_AUDIO_PROFILE_LEVEL_INDICATION</a></td>
<td>Audio profile and level. <br/> The value of this attribute is the <strong>audioProfileLevelIndication</strong> field, as defined by ISO/IEC 14496-3.<br/> If unknown, set to zero or 0xFE (&quot;no audio profile specified&quot;).<br/></td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-avg-bytes-per-second-attribute.md"><strong>MF_MT_AUDIO_AVG_BYTES_PER_SECOND</strong></a></td>
<td>Bit rate of the encoded AAC stream, in bytes per second.</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-aac-payload-type.md">MF_MT_AAC_PAYLOAD_TYPE</a></td>
<td>Payload type.<br/> Applies only to <strong>MFAudioFormat_AAC</strong>.<br/> <a href="mf-mt-aac-payload-type.md">MF_MT_AAC_PAYLOAD_TYPE</a> is optional. If this attribute is not specified, the default value 0 is used, which specifies the stream contains raw_data_block elements only.<br/></td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-bits-per-sample-attribute.md"><strong>MF_MT_AUDIO_BITS_PER_SAMPLE</strong></a></td>
<td>Bit depth of the decoded PCM audio.</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-channel-mask-attribute.md"><strong>MF_MT_AUDIO_CHANNEL_MASK</strong></a></td>
<td>Assignment of audio channels to speaker positions.</td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-num-channels-attribute.md"><strong>MF_MT_AUDIO_NUM_CHANNELS</strong></a></td>
<td>Number of channels, including the low frequency (LFE) channel, if present.<br/> The interpretation of this value depends on the media subtype, as described previously.<br/></td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-samples-per-second-attribute.md"><strong>MF_MT_AUDIO_SAMPLES_PER_SECOND</strong></a></td>
<td>Sample rate, in samples per second.<br/> The interpretation of this value depends on the media subtype, as described previously.<br/></td>
</tr>
<tr class="even">
<td><a href="mf-mt-user-data-attribute.md"><strong>MF_MT_USER_DATA</strong></a></td>
<td>The value of this attribute depends on the subtype:<br/>
<ul>
<li><strong>MFAudioFormat_AAC</strong>: Contains the portion of the <a href="/windows/desktop/api/mmreg/ns-mmreg-heaacwaveinfo"><strong>HEAACWAVEINFO</strong></a> structure that appears after the <strong>WAVEFORMATEX</strong> structure (that is, after the <strong>wfx</strong> member). This is followed by the AudioSpecificConfig() data, as defined by ISO/IEC 14496-3.</li>
<li><strong>MEDIASUBTYPE_RAW_AAC1</strong>: Contains the AudioSpecificConfig() data.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Audio Media Types](audio-media-types.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[MPEG-4 Support in Media Foundation](mpeg-4-support-in-media-foundation.md)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> </dl>

 

