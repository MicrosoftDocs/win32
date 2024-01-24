---
description: The Windows Media Audio Voice encoder is optimized for encoding the human voice at high compression ratios. This is the preferred encoder for streams consisting mostly of spoken words.
ms.assetid: b3cfa845-4fe1-405f-88e5-4555398639ef
title: Windows Media Audio Voice Encoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Audio Voice Encoder

The Windows Media Audio Voice encoder is optimized for encoding the human voice at high compression ratios. This is the preferred encoder for streams consisting mostly of spoken words.

## Class Identifier

The class identifier (CLSID) for the Windows Media Audio Voice encoder is represented by the constant **CLSID\_CWMSPEncMediaObject2**. You can create an instance of the voice encoder by calling **CoCreateInstance**.

## Output Formats

Windows Media Audio Voice encoded content is identified by the format tag 0x00A.

## Encoder Properties

The Windows Media Audio Voice encoder supports the following properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mfpkey-wmavoice-enc-bufferwindowproperty.md">MFPKEY_WMAVOICE_ENC_BufferWindow</a></td>
<td>Specifies the buffer window, in milliseconds, used for the voice codec.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmavoice-enc-decoderdelayproperty.md">MFPKEY_WMAVOICE_ENC_DecoderDelay</a></td>
<td>Specifies encoder latency in packet units.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-wmavoice-enc-edlproperty.md">MFPKEY_WMAVOICE_ENC_EDL</a></td>
<td>Specifies the portions of content to be encoded as music by the voice codec.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-wmavoice-enc-musicspeechclassmodeproperty.md">MFPKEY_WMAVOICE_ENC_MusicSpeechClassMode</a></td>
<td>Specifies the mode of the voice codec.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmspdmoe.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Using the Windows Media Audio Voice Codec](usingthewindowsmediaaudio9voicecodec.md)
</dt> </dl>

 

 




