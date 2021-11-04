---
description: The Windows Media Audio decoder decodes audio streams that were encoded by the Windows Media Audio Encoder.
ms.assetid: 2d8e4a97-34a7-4eee-9567-7ae98fa282b9
title: Windows Media Audio Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Audio Decoder

The Windows Media Audio decoder decodes audio streams that were encoded by the [**Windows Media Audio Encoder**](windowsmediaaudioencoder.md). The encoder and decoder support three categories of encoded audio: Windows Media Audio Standard, Windows Media Audio Professional, and Windows Media Audio Lossless.

## Class Identifier

The class identifier (CLSID) for the Windows Media Audio decoder is represented by the constant **CLSID\_CWMADecMediaObject**. You can create an instance of the audio decoder by calling **CoCreateInstance**.

## Input Formats

The following table shows the audio format tags that represent the input categories supported by the Windows Media Audio decoder. For information about how to set the input and output types for the decoder, see [Configuring Audio Decoding](configuringaudiodecoding.md).



| Format tag constant             | Format tag value | Audio format                     |
|---------------------------------|------------------|----------------------------------|
| WAVE\_FORMAT\_WMAUDIO2          | 0x0161           | Windows Media Audio Standard     |
| WAVE\_FORMAT\_WMAUDIO3          | 0x0162           | Windows Media Audio Professional |
| WAVE\_FORMAT\_WMAUDIO\_LOSSLESS | 0x0163           | Windows Media Audio Lossless     |



 

## Output Formats

The following table shows the audio format tags that represent the output types supported by the **Windows Media Audio Decoder**. For information about how to set the input and output types for the decoder, see [Configuring Audio Encoding](configuringaudioencoding.md).



| Format tag constant       | Format tag value | Audio format                                          |
|---------------------------|------------------|-------------------------------------------------------|
| WAVE\_FORMAT\_PCM         | 0x0001           | PCM format                                            |
| WAVE\_FORMAT\_IEEE\_FLOAT | 0x0003           | IEEE floating point                                   |
| WAVE\_FORMAT\_EXTENSIBLE  | 0xFFFE           | PCM/IEEE format in **WAVEFORMATEXTENSIBLE** structure |



 

## Interfaces

An audio decoder object exposes the **IMediaObject** interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the **IMFTransform** interface so that the object can be used as a Media Foundation Transform (MFT).

A Windows Media Audio decoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which an audio decoder behaves as a DMO or an MFT.



| Operating system | Decoder behavior                                                                                                                                                                      |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP       | A Windows Media Audio decoder always behaves as a DMO.                                                                                                                                |
| Windows Vista    | By default, a Windows Media Audio decoder behaves as a DMO. If you obtain an **IMFTransform** interface or an **IPropertyStore** interface on an audio decoder, it behaves as an MFT. |
| Windows 7        | By default, a Windows Media Audio decoder behaves as a DMO. If you obtain an **IMFTransform** interface on an audio decoder, it behaves as an MFT.                                    |



 

## Properties

The Windows Media Audio decoder supports the following properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mfpkey-decoder-maxnumpcmsampleswithpaddedsilenceproperty.md"><strong>MFPKEY_Decoder_MaxNumPCMSamplesWithPaddedSilence</strong></a></td>
<td>Specifies the maximum number of additional PCM samples that might be returned at the end of decoding a file.<br/> <dl> Windows Vista and later.<br />
Standard, Professional, Lossless.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmadec-drcmodeproperty.md"><strong>MFPKEY_WMADEC_DRCMODE</strong></a></td>
<td>Specifies the dynamic-range control mode that the audio decoder will use.<br/> <dl> Windows XP and later.<br />
Standard, Professional, Lossless.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmadec-folddown-matrixproperty.md"><strong>MFPKEY_WMADEC_FOLDDOWN_MATRIX</strong></a></td>
<td>Specifies the author-supplied fold-down coefficients for decoding multichannel audio for fewer channels than the encoded stream contains. <br/> <dl> Windows XP and later.<br />
Professional<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmadec-hiresoutputproperty.md"><strong>MFPKEY_WMADEC_HIRESOUTPUT</strong></a></td>
<td>Specifies whether the audio decoder should deliver high-resolution output.<br/> <dl> Windows XP and later.<br />
Professional, Lossless.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmadec-ltrtoutputproperty.md"><strong>MFPKEY_WMADEC_LTRTOUTPUT</strong></a></td>
<td>Specifies whether the audio decoder should perform Lt-Rt fold down.<br/> <dl> Windows Vista and later.<br />
Professional.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmadec-spkrcfgproperty.md"><strong>MFPKEY_WMADEC_SPKRCFG</strong></a></td>
<td>Specifies the speaker configuration on the client computer.<br/> <dl> Windows XP and later.<br />
Professional.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmadrc-avgrefproperty.md"><strong>MFPKEY_WMADRC_AVGREF</strong></a></td>
<td>Specifies the average volume level of audio content.<br/> <dl> Windows XP and later.<br />
Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmadrc-avgtargetproperty.md"><strong>MFPKEY_WMADRC_AVGTARGET</strong></a></td>
<td>Specifies the desired average volume level of output audio content.<br/> <dl> Windows XP and later.<br />
Professional, Lossless.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmadrc-peakrefproperty.md"><strong>MFPKEY_WMADRC_PEAKREF</strong></a></td>
<td>Specifies the highest volume level occurring in audio content.<br/> <dl> Windows XP and later.<br />
Professional, Lossless.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmadrc-peaktargetproperty.md"><strong>MFPKEY_WMADRC_PEAKTARGET</strong></a></td>
<td>Specifies the desired maximum volume level of output audio content.<br/> <dl> Windows XP and later.<br />
Professional, Lossless.<br />
Write-only.<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmadmod.dll</dt> </dl>  |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> </dl>

 

 




