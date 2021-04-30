---
description: The Microsoft Media Foundation MPEG-2 audio encoder is a Media Foundation transform that encodes mono or stereo audio to MPEG-1 audio (ISO/IEC 11172-3) or MPEG-2 audio (ISO/IEC 13818-3).
ms.assetid: EBEFED1F-D0B8-4C7E-B1FB-CDE3BDFD99AA
title: MPEG-2 Audio Encoder
ms.topic: reference
ms.date: 05/31/2018
---

# MPEG-2 Audio Encoder

The Microsoft Media Foundation MPEG-2 audio encoder is a [Media Foundation transform](media-foundation-transforms.md) that encodes mono or stereo audio to MPEG-1 audio (ISO/IEC 11172-3) or MPEG-2 audio (ISO/IEC 13818-3).

The encoder supports Layer 1 and Layer 2 audio. It does not support MPEG-Layer 3 (MP3) audio. For MPEG-2, the encoder supports the Low Sampling Frequencies (LSF) portion of MPEG-2 audio. It does not support the multichannel extensions. The MFT outputs an MPEG elementary stream. It cannot generate packetized elementary streams, program streams, or transport streams.

## Class Identifier

The class identifier (CLSID) of the MEPG-2 audio encoder is **CLSID\_CMPEG2AudioEncoderMFT**, defined in the header file wmcodecdsp.h.

## Output Types

The output type must be set first, before the input type. The following table lists the required and optional attributes for the output media type.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Remarks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mf-mt-major-type-attribute.md">MF_MT_MAJOR_TYPE</a></td>
<td>Major type.</td>
<td>Required. Must be <strong>MFMediaType_Audio</strong>.</td>
</tr>
<tr class="even">
<td><a href="mf-mt-subtype-attribute.md">MF_MT_SUBTYPE</a></td>
<td>Audio subtype.</td>
<td>Required. Must be <strong>MFAudioFormat_MPEG</strong>. This subtype is used for both MPEG-1 and MPEG-2 audio.</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-samples-per-second-attribute.md">MF_MT_AUDIO_SAMPLES_PER_SECOND</a></td>
<td>Samples per second.</td>
<td>Required. The following values are supported for both MPEG-1 and MPEG-2:
<ul>
<li>32000</li>
<li>44100</li>
<li>48000</li>
</ul>
In addition, the following values are supported for MPEG-2 LSF: <br/>
<ul>
<li>16000</li>
<li>22050</li>
<li>24000</li>
</ul></td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-num-channels-attribute.md">MF_MT_AUDIO_NUM_CHANNELS</a></td>
<td>Number of channels.</td>
<td>Required. Must be either 1 (mono) or 2 (stereo).</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-channel-mask-attribute.md">MF_MT_AUDIO_CHANNEL_MASK</a></td>
<td>Specifies the assignment of audio channels to speaker positions.</td>
<td>Optional. If set, the value must be 0x3 for stereo (front left and right channels) or 0x4 for mono (front center channel).</td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-avg-bytes-per-second-attribute.md">MF_MT_AUDIO_AVG_BYTES_PER_SECOND</a></td>
<td>Bit rate of the encoded MPEG stream, in bytes per second.</td>
<td>Optional.<br/> The ISO/IEC 11172-3 and ISO/IEC 13818-3 (LSF) specifications define several bit rates, depending on the sampling rate, the number of channels, and the audio layer (1 or 2). <br/> The encoder defaults to Layer 2 audio. If the <a href="mf-mt-audio-avg-bytes-per-second-attribute.md">MF_MT_AUDIO_AVG_BYTES_PER_SECOND</a> attribute is not set, the encoder uses the following default bit rates:<br/>
<ul>
<li>MPEG-1 stereo: 224,000 bits per second (bps) = 28,000 bytes per second.</li>
<li>MPEG-1 mono: 192,000 bps = 24,000 bytes per second.</li>
<li>MPEG-2 LSF, mono or stereo: 160,000 bps = 20,000 bytes per second.</li>
</ul>
This attribute can be set to other values. If the value is not valid according to MPEG specifications, the MFT will reject the media type.<br/> You can also set the bit rate by using the <a href="/windows/desktop/api/strmif/nn-strmif-icodecapi"><strong>ICodecAPI</strong></a> interface. See Remarks for more information.<br/></td>
</tr>
</tbody>
</table>



 

If the optional attributes are not set, the encoder adds them to the media type after the type is set.

## Input Types

The following table lists the required and optional attributes for the input media type.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Remarks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mf-mt-major-type-attribute.md">MF_MT_MAJOR_TYPE</a></td>
<td>Major type.</td>
<td>Required. Must be <strong>MFMediaType_Audio</strong>.</td>
</tr>
<tr class="even">
<td><a href="mf-mt-subtype-attribute.md">MF_MT_SUBTYPE</a></td>
<td>Audio subtype.</td>
<td>Required. Must be <strong>MFAudioFormat_PCM</strong> or <strong>MFAudioFormat_Float</strong>.</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-bits-per-sample-attribute.md">MF_MT_AUDIO_BITS_PER_SAMPLE</a></td>
<td>Number of bits per audio sample.</td>
<td>Required. The value must be 16 if the subtype is <strong>MFAudioFormat_PCM</strong>, or 32 if the subtype is <strong>MFAudioFormat_Float</strong>.</td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-samples-per-second-attribute.md">MF_MT_AUDIO_SAMPLES_PER_SECOND</a></td>
<td>Samples per second.</td>
<td>Required. Must match the output type.</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-num-channels-attribute.md">MF_MT_AUDIO_NUM_CHANNELS</a></td>
<td>Number of channels.</td>
<td>Required. Must match the output type.</td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-block-alignment-attribute.md">MF_MT_AUDIO_BLOCK_ALIGNMENT</a></td>
<td>Block alignment, in bytes.</td>
<td>Required. Calculate the value as follows:
<ul>
<li><strong>MFAudioFormat_PCM</strong>: Number of channels × 2.</li>
<li><strong>MFAudioFormat_Float</strong>: Number of channels × 4.</li>
</ul></td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-avg-bytes-per-second-attribute.md">MF_MT_AUDIO_AVG_BYTES_PER_SECOND</a></td>
<td>Bit rate of the encoded AC3 stream, in bytes per second.</td>
<td>Required. Must equal block alignment × samples per second.</td>
</tr>
<tr class="even">
<td><a href="mf-mt-audio-channel-mask-attribute.md">MF_MT_AUDIO_CHANNEL_MASK</a></td>
<td>Specifies the assignment of audio channels to speaker positions.</td>
<td>Optional. If set, the value must match the output type.</td>
</tr>
<tr class="odd">
<td><a href="mf-mt-audio-valid-bits-per-sample-attribute.md">MF_MT_AUDIO_VALID_BITS_PER_SAMPLE</a></td>
<td>Number of valid bits of audio data in each audio sample.</td>
<td>Optional. If set, the value must be identical to <a href="mf-mt-audio-bits-per-sample-attribute.md">MF_MT_AUDIO_BITS_PER_SAMPLE</a>.</td>
</tr>
</tbody>
</table>



 

The encoder does not support sample-rate conversion or stereo/mono conversion. If the optional attributes are not set, the encoder adds them to the media type after the type is set.

## Codec Properties

The encoder supports the following properties through the [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface.



| Property                                                                                | Description                                                                                      | Default value                                                                                                                                                          |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CODECAPI\_AVEncCommonMeanBitRate](../directshow/avenccommonmeanbitrate-property.md)               | Specifies the average encoded bit rate, in bits per second.                                      | As described for the [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute in the output media type.                      |
| [CODECAPI\_AVEncMPACodingMode](../directshow/avencmpacodingmode-property.md)                       | Specifies the MPEG audio encoding mode.                                                          | Stereo for 2-channel audio, or single channel for 1-channel audio.<br/> For 2-channel audio, the encoder also supports dual channel and joint stereo.<br/> |
| [CODECAPI\_AVEncMPACopyright](../directshow/avencmpacopyright-property.md)                         | Specifies whether to set the copyright bit in the MPEG audio stream.                             | No copyright.                                                                                                                                                          |
| [CODECAPI\_AVEncMPAEmphasisType](../directshow/avencmpaemphasistype-property.md)                   | Specifies the type of de-emphasis filter that should be used when the encoded stream is decoded. | No emphasis specified.                                                                                                                                                 |
| [AVEncMPAEnableRedundancyProtection](../directshow/avencmpaenableredundancyprotection-property.md) | Specifies whether to add a cyclic redundancy check (CRC) to the frame header.                    | A CRC checksum is written to the bit stream.                                                                                                                           |
| [CODECAPI\_AVEncMPALayer](../directshow/avencmpalayer-property.md)                                 | Specifies the MPEG audio layer.                                                                  | Layer 2 audio.                                                                                                                                                         |
| [CODECAPI\_AVEncMPAOriginalBitstream](../directshow/avencmpaoriginalbitstream-property.md)         | Specifies whether to set for the original bit in the MPEG audio stream.                          | "Original" bit is off.                                                                                                                                                 |
| [CODECAPI\_AVEncMPAPrivateUserBit](../directshow/avencmpaprivateuserbit-property.md)               | Specifies whether to set for the private user bit in the MPEG audio stream.                      | Private user bit is off.                                                                                                                                               |



 

To get a pointer to the [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface, call [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the MFT.

The MFT implements the following [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) methods:

-   [**GetParameterRange**](/windows/win32/api/strmif/nf-strmif-icodecapi-getparameterrange)
-   [**GetParameterValues**](/windows/win32/api/strmif/nf-strmif-icodecapi-getparametervalues)
-   [**GetValue**](/windows/win32/api/strmif/nf-strmif-icodecapi-getvalue)
-   [**IsModifiable**](/windows/win32/api/strmif/nf-strmif-icodecapi-ismodifiable)
-   [**IsSupported**](/windows/win32/api/strmif/nf-strmif-icodecapi-issupported)
-   [**SetValue**](/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue)

All other [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) methods return **E\_NOTIMPL**.

## Remarks

Each MPEG audio frame contains either 384 (Layer 1) or 1152 (Layer 2) audio samples per channel. However, each input buffer to the encoder may contain any number of PCM samples. The size of each input buffer must be a multiple of the block alignment. The encoder caches input samples until it has enough for an MPEG audio frame.

Each output buffer contains one raw MPEG frame. The size of each output buffer depends on the bit rate and the sample rate.

### Configuring the Encoder

To change any of the default settings on the encoder, perform the following steps:

1.  Create an instance of the encoder MFT.
2.  Call [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) to get the list of the preferred output types. The encoder enumerates all sample rates for both mono and stereo. Select one of these media types, based on the sample rate and number of channels. The [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute indicates the default bit rate, in bytes per second.
3.  Optional: You can override the default bit rate by setting a new value for [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) on the output media type. Valid bit rates depend on the sample rate, number of channels, and audio layer.
    > [!Note]  
    > At this point in the configuration process, the encoder defaults to Layer 2 audio and will only accept Layer 2 bit rates. You will be able to switch the encoder to Layer 1 in a later step (see step 7). In that case, leave the default bit rate for now; you can change it again in step 8.

     

4.  Call [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) to set the output media type. If you set your own value for [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) and the MFT rejects the output media type, it is likely because you specified an invalid bit rate.
5.  Call [**IMFTransform::GetInputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputavailabletype) to enumerate the input media type. Because the sample rate and number of channels must be identical to the output type, only two options are enumerated: 32-bit floating-point PCM input and 16-bit integer PCM input. Select one of these.
6.  Call [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) to set the input media type.
7.  Optional: To encode Layer 1 audio, set the [CODECAPI\_AVEncMPALayer](../directshow/avencmpalayer-property.md) property to **eAVEncMPALayer\_1**.
8.  Optional: To change the bit rate, set the [CODECAPI\_ AVEncCommonMeanBitRate](../directshow/avenccommonmeanbitrate-property.md) property. The bit rate must be one of the valid bit rates listed in the MPEG-1 or MPEG-2 LSF specifications. Alternatively, you can call [**ICodecAPI::GetParameterValues**](/windows/win32/api/strmif/nf-strmif-icodecapi-getparametervalues) to get a list of valid bit rates, based on the current settings.
9.  Optional: With 2-channel audio, you can set the [CODECAPI\_ AVEncMPACodingMode](../directshow/avencmpacodingmode-property.md) property to change the coding mode to dual channel or joint stereo. You can call [**ICodecAPI::GetParameterRange**](/windows/win32/api/strmif/nf-strmif-icodecapi-getparameterrange) to get the valid options. (For 1-channel audio, the only option is mono.)
10. Optional: Set any of the other [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) properties listed previously.

It is important to follow the order of these steps. In particular, set the output media type before changing any [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) properties. Also, you must set **ICodecAPI** properties before the MFT receives the first input sample. After the MFT receives input, the codec properties are read-only, and [**ICodecAPI::SetValue**](/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue) returns the value **S\_FALSE**.

### Supported Bit Rates

The encoder supports the following bit rates.



MPEG-1

MPEG-2

Layer 1

Layer 2

Layer 1

Layer 2

32

32\*

32

8

64

48\*

38

16

96

56\*

56

24

128

64

64

32

160

80\*

80

40

192

96

96

48

224

112

112

56

256

128

128

64

288

160

144

80

320

192

160

96

352

224\*\*

176

112

384

256\*\*

192

128

416

230\*\*

224

144

448

384\*\*

256

160



 

<dl> \* Mono only  
\*\* Stereo only  
</dl>

### Example Media Types

Here is an example of the media types that are needed to encode 16-bit integer PCM, 48-kHz stereo audio at the default bit rate.

Output media type:

| Attribute                                                                           | Value                   |
|-------------------------------------------------------------------------------------|-------------------------|
| [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md)                               | **MFMediaType\_Audio**  |
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md)                                      | **MFAudioFormat\_MPEG** |
| [MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND](mf-mt-audio-samples-per-second-attribute.md) | 48000                   |
| [MF\_MT\_AUDIO\_NUM\_CHANNELS](mf-mt-audio-num-channels-attribute.md)              | 2                       |



 

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
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| DLL<br/>                      | <dl> <dt>Msmpeg2enc.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 
