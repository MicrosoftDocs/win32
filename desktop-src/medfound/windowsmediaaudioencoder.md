---
Description: 'The Windows Media Audio encoder encodes audio streams. The encoder supports three categories of encoded output: Windows Media Audio Standard, Windows Media Audio Professional, and Windows Media Audio Lossless.'
ms.assetid: 1f6a3a9f-b534-4a6b-b773-0315c759624e
title: Windows Media Audio Encoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Audio Encoder

The Windows Media Audio encoder encodes audio streams. The encoder supports three categories of encoded output: Windows Media Audio Standard, Windows Media Audio Professional, and Windows Media Audio Lossless.

## Class Identifier

The class identifier (CLSID) for the Windows Media Audio Encoder is represented by the constant **CLSID\_CWMAEncMediaObject**. You can create an instance of the audio encoder by calling **CoCreateInstance**.

## Input Formats

The following table shows the audio format tags that represent the input categories supported by the Windows Media Audio encoder. For information about how to set the input and output types for the encoder, see [Configuring Audio Encoding](configuringaudioencoding.md).



| Format tag constant       | Format tag value | Audio format                                          |
|---------------------------|------------------|-------------------------------------------------------|
| WAVE\_FORMAT\_PCM         | 0x0001           | PCM format                                            |
| WAVE\_FORMAT\_IEEE\_FLOAT | 0x0003           | IEEE floating point                                   |
| WAVE\_FORMAT\_EXTENSIBLE  | 0xFFFE           | PCM/IEEE format in **WAVEFORMATEXTENSIBLE** structure |



 

## Output Formats

The following table shows the audio format tags that represent the output categories supported by the Windows Media Audio encoder.



| Format tag constant             | Format tag value | Audio format                     |
|---------------------------------|------------------|----------------------------------|
| WAVE\_FORMAT\_WMAUDIO2          | 0x0161           | Windows Media Audio Standard     |
| WAVE\_FORMAT\_WMAUDIO3          | 0x0162           | Windows Media Audio Professional |
| WAVE\_FORMAT\_WMAUDIO\_LOSSLESS | 0x0163           | Windows Media Audio Lossless     |



 

## Interfaces

An audio endoder object exposes the **IMediaObject** interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the **IMFTransform** interface so that the object can be used as a Media Foundation Transform (MFT).

A Windows Media Audio encoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which an audio encoder behaves as a DMO or an MFT.



| Operating system | Encoder behavior                                                                                                                                                                      |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP       | A Windows Media Audio encoder always behaves as a DMO.                                                                                                                                |
| Windows Vista    | By default, a Windows Media Audio encoder behaves as a DMO. If you obtain an **IMFTransform** interface or an **IPropertyStore** interface on an audio encoder, it behaves as an MFT. |
| Windows 7        | By default, a Windows Media Audio encoder behaves as a DMO. If you obtain an **IMFTransform** interface on an audio encoder, it behaves as an MFT.                                    |



 

## Encoder Properties

The Windows Media Audio encoder supports the following properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mfpkey-avgconstrainedproperty"><strong>MFPKEY_AVGCONSTRAINED</strong></a></td>
<td>Specifies whether the encoder uses average-controllable VBR encoding.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-bmaxproperty"><strong>MFPKEY_BMAX</strong></a></td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its peak bit rate.<br/> <dl> Windows XP and later.<br />
Standard, Professional.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-checkdataconsistency2pproperty"><strong>MFPKEY_CHECKDATACONSISTENCY2P</strong></a></td>
<td>Specifies whether whether the encoder should check for data consistency across passes when performing two-pass VBR encoding. <br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-constraindeclatencyproperty"><strong>MFPKEY_CONSTRAINDECLATENCY</strong></a></td>
<td>Specifies whether the encoder is constrained by a maximum decoder latency requirement.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-constrainenccomplexityproperty"><strong>MFPKEY_CONSTRAINENCCOMPLEXITY</strong></a></td>
<td>Specifies whether the complexity of the encoding algorithm is constrained.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-constrainenclatencyproperty"><strong>MFPKEY_CONSTRAINENCLATENCY</strong></a></td>
<td>Specifies whether the encoder is constrained by a maximum latency requirement.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-constrain-enumerated-vbrqualityproperty"><strong>MFPKEY_CONSTRAIN_ENUMERATED_VBRQUALITY</strong></a></td>
<td>Specifies whether modes enumerated by the encoder are limited to those that meet a quality requirement.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-decodercomplexityprofileproperty"><strong>MFPKEY_DECODERCOMPLEXITYPROFILE</strong></a></td>
<td>Specifies the complexity profile of the encoded content.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-desired-vbrqualityproperty"><strong>MFPKEY_DESIRED_VBRQUALITY</strong></a></td>
<td>Specifies the desired quality level for VBR encoding.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-dyn-allow-noisesubproperty"><strong>MFPKEY_DYN_ALLOW_NOISESUB</strong></a></td>
<td>Specifies whether the encoder uses noise substitution.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-dyn-allow-pcmrangelimitingproperty"><strong>MFPKEY_DYN_ALLOW_PCMRANGELIMITING</strong></a></td>
<td>Specifies whether the encoder uses PCM range limiting.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-dyn-bandtrunc-bwceilproperty"><strong>MFPKEY_DYN_BANDTRUNC_BWCEIL</strong></a></td>
<td>Specifies the maximum coded bandwidth allowed by band truncation in the encoder.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-dyn-bandtrunc-bwfloorproperty"><strong>MFPKEY_DYN_BANDTRUNC_BWFLOOR</strong></a></td>
<td>Specifies the minimum coded bandwidth allowed by band truncation in the encoder.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-dyn-bandtrunc-qceilproperty"><strong>MFPKEY_DYN_BANDTRUNC_QCEIL</strong></a></td>
<td>Specifies the quality at which minimum coded bandwidth is allowed. <br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-dyn-bandtrunc-qfloorproperty"><strong>MFPKEY_DYN_BANDTRUNC_QFLOOR</strong></a></td>
<td>Specifies the quality at which maximum coded bandwidth is allowed.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-dyn-bandtruncationproperty"><strong>MFPKEY_DYN_BANDTRUNCATION</strong></a></td>
<td>Specifies whether the encoder performs band truncation.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-dyn-simplemaskproperty"><strong>MFPKEY_DYN_SIMPLEMASK</strong></a></td>
<td>Specifies whether the encoder uses the style of mask computation performed by version 7 of the Windows Media Audio encoder.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-dyn-stereo-preprocproperty"><strong>MFPKEY_DYN_STEREO_PREPROC</strong></a></td>
<td>Specifies whether the encoder performs stereo image processing. <br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-dyn-vbr-bavgproperty"><strong>MFPKEY_DYN_VBR_BAVG</strong></a></td>
<td>Specifies the buffer window, in milliseconds, for an encoder that is configured to use average-controllable VBR encoding.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-dyn-vbr-ravgproperty"><strong>MFPKEY_DYN_VBR_RAVG</strong></a></td>
<td>Specifies the average bit rate, in bits per second, for an encoder that is configured to use average-controllable VBR encoding.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-enccomplexityproperty"><strong>MFPKEY_ENCCOMPLEXITY</strong></a></td>
<td>Specifies the complexity of the encoding algorithm.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-endofpassproperty"><strong>MFPKEY_ENDOFPASS</strong></a></td>
<td>Specifies the end of an encoding pass.<br/> <dl> Windows XP and later.<br />
Standard, Professional.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-enhanced-wmaproperty"><strong>MFPKEY_ENHANCED_WMA</strong></a></td>
<td>Specifies whether the core encoder uses the &quot;Plus&quot; feature.<br/> <dl> Windows Vista and later.<br />
Professional.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-maxdeclatencymsproperty"><strong>MFPKEY_MAXDECLATENCYMS</strong></a></td>
<td>Specifies the maximum latency for the decoder, in milliseconds.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-maxenclatencymsproperty"><strong>MFPKEY_MAXENCLATENCYMS</strong></a></td>
<td>Specifies the maximum latency for the encoder, in milliseconds.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-most-recently-enumerated-vbrqualityproperty"><strong>MFPKEY_MOST_RECENTLY_ENUMERATED_VBRQUALITY</strong></a></td>
<td>Specifies the VBR quality level of the most recently enumerated output type.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-passesrecommendedproperty"><strong>MFPKEY_PASSESRECOMMENDED</strong></a></td>
<td>Specifies the maximum number of passes supported by the encoder.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-passesusedproperty"><strong>MFPKEY_PASSESUSED</strong></a></td>
<td>Specifies the number of passes that the encoder will use to encode the content.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-peakconstrainedproperty"><strong>MFPKEY_PEAKCONSTRAINED</strong></a></td>
<td>Specifies whether the encoder is constrained by a peak bit rate.<br/> <dl> Windows Vista and later.<br />
Standard, Professional.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-preferred-framesizeproperty"><strong>MFPKEY_PREFERRED_FRAMESIZE</strong></a></td>
<td>Specifies the preferred number of samples per frame.<br/> <dl> Windows Vista and later.<br />
Professional.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-requesting-a-framesizeproperty"><strong>MFPKEY_REQUESTING_A_FRAMESIZE</strong></a></td>
<td>Specifies whether the encoder should use a preferred frame size.<br/> <dl> Windows Vista and later.<br />
Professional.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-rmaxproperty"><strong>MFPKEY_RMAX</strong></a></td>
<td>Specifies the peak bit rate, in bits per second, used for constrained 2-pass variable-bit-rate (VBR) encoding. <br/> <dl> Windows XP and later.<br />
Standard, Professional.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-stat-bavgproperty"><strong>MFPKEY_STAT_BAVG</strong></a></td>
<td>Specifies the average buffer window, in milliseconds, of an encoded stream.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-stat-bmaxproperty"><strong>MFPKEY_STAT_BMAX</strong></a></td>
<td>Specifies the maximum buffer window, in milliseconds, of an encoded stream.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-stat-ravgproperty"><strong>MFPKEY_STAT_RAVG</strong></a></td>
<td>Specifies the average bit rate, in bits per second, of an encoded stream.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-stat-rmaxproperty"><strong>MFPKEY_STAT_RMAX</strong></a></td>
<td>Specifies the maximum bit rate, in bits per second, of an encoded stream.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-vbrenabledproperty"><strong>MFPKEY_VBRENABLED</strong></a></td>
<td>Specifies whether the encoder uses VBR encoding.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wma-elementary-streamproperty"><strong>MFPKEY_WMA_ELEMENTARY_STREAM</strong></a></td>
<td>This property is currently not used by the Windows Media Audio codec.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmadrc-avgrefproperty"><strong>MFPKEY_WMADRC_AVGREF</strong></a></td>
<td>Specifies the average volume level of audio content.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmadrc-peakrefproperty"><strong>MFPKEY_WMADRC_PEAKREF</strong></a></td>
<td>Specifies the highest volume level occurring in audio content.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmaenc-avgbytespersecproperty"><strong>MFPKEY_WMAENC_AVGBYTESPERSEC</strong></a></td>
<td>Specifies the average bytes per second for VBR encoded audio.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmaenc-bufferlesscbrproperty"><strong>MFPKEY_WMAENC_BUFFERLESSCBR</strong></a></td>
<td>Specifies whether the encoder should produce 1 WMA packet per frame.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmaenc-generate-drc-paramsproperty"><strong>MFPKEY_WMAENC_GENERATE_DRC_PARAMS</strong></a></td>
<td>Specifies whether the encoder should generate dynamic range control parameters.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmaenc-origwaveformatproperty"><strong>MFPKEY_WMAENC_ORIGWAVEFORMAT</strong></a></td>
<td>Specifies the <strong>WAVEFORMATEX</strong> structure describing the input audio content.<br/> <dl> Windows XP and later.<br />
Standard, Professional.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmaenc-rtspdifproperty"><strong>MFPKEY_WMAENC_RTSPDIF</strong></a></td>
<td>Specifies whether the encoder should enable real-time S/PDIF encoding .<br/> <dl> Windows Vista and later.<br />
Professional.<br />
Read/write.<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmadmoe.dll</dt> </dl>  |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> </dl>

 

 




