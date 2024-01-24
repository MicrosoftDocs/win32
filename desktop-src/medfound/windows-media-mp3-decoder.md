---
description: The Windows Media MP3 decoder decodes audio files that have been encoded in the following formats.
ms.assetid: 817bbc2d-b3d5-49b4-84e4-bc8dc232a8ea
title: Windows Media MP3 Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media MP3 Decoder

The Windows Media MP3 decoder decodes audio files that have been encoded in the following formats.

-   ISO/IEC 11172-3 (MPEG-1 Audio) Layer 3
-   ISO/IEC 13818-3 (MPEG-2 Audio) Layer 3, low sampling frequency extension

## Class Identifier

The class identifier (CLSID) for the Windows Media MP3 decoder is represented by the constant **CLSID\_CMP3DecMediaObject**. You can create an instance of the MP3 decoder by calling **CoCreateInstance**.

## Interfaces

An MP3 decoder object exposes the **IMediaObject** interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the **IMFTransform** interface so that the object can be used as a Media Foundation Transform (MFT).

A Windows Media MP3 decoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which a Windows Media MP3 decoder behaves as a DMO or an MFT.



| Operating system | Decoder behavior                                                                                                                                                                               |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP       | A Windows Media MP3 decoder always behaves as a DMO.                                                                                                                                           |
| Windows Vista    | By default, a Windows Media MP3 decoder behaves as a DMO. If you obtain an **IMFTransform** interface or an **IPropertyStore** interface on a Windows Media MP3 decoder, it behaves as an MFT. |
| Windows 7        | By default, a Windows Media MP3 decoder behaves as a DMO. If you obtain an **IMFTransform** interface on a Windows Media MP3 decoder, it behaves as an MFT.                                    |



 

## Input Formats

The following table shows the audio format tag that represents the input type supported by the Windows Media MP3 decoder.



| Format tag constant      | Format tag value | Audio format     |
|--------------------------|------------------|------------------|
| WAVE\_FORMAT\_MPEGLAYER3 | 0x55             | ISO MPEG Layer 3 |



 

## Output Formats

The following table shows the audio format tags that represent the output types supported by the Windows Media MP3 decoder.



| Format tag constant       | Format tag value | Audio format                                                                |
|---------------------------|------------------|-----------------------------------------------------------------------------|
| WAVE\_FORMAT\_PCM         | 0x0001           | PCM format (when used as a DMO or an MFT)                                   |
| WAVE\_FORMAT\_IEEE\_FLOAT | 0x0003           | IEEE floating point (when used as an MFT)                                   |
| WAVE\_FORMAT\_EXTENSIBLE  | 0xFFFE           | PCM/IEEE format in **WAVEFORMATEXTENSIBLE** structure (when used as an MFT) |



 

The Windows Media MP3 decoder supports and enumerates the following output media types.

-   An output type that has the same sampling rate and number of channels as the input type.
-   Mono output for stereo input.
-   Output types with bit depths of 8 and 16.
-   Floating point output, if the decoder is behaving as an MFT.

The Windows Media MP3 decoder supports, but does not enumerate, the following output media types.

-   An output type that has half the sampling rate of the input type.
-   An output type that has one fourth the sampling rate of the input type.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Mp3dmod.dll</dt> </dl>  |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> </dl>

 

 




