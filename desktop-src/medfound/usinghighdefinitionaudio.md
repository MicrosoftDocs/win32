---
Description: 'Using High-Definition Audio'
ms.assetid: '5e21943f-363c-4831-bc09-aadf6f4a0ad5'
title: 'Using High-Definition Audio'
---

# Using High-Definition Audio

High-definition audio, in the context of the Windows Media Audio codecs, is any audio type with more than two channels or more than 16 bits per sample. High-definition audio is supported by the Professional and Lossless categories of the [Windows Media Audio Encoder](windowsmediaaudioencoder.md).

Uncompressed high-definition audio types are defined using the [**WAVEFORMATEXTENSIBLE**](dshow.waveformatextensible) structure. **WAVEFORMATEXTENSIBLE** is a structured extension of the [**WAVEFORMATEX**](dshow.waveformatex) structure. When you are using DMOs, the **formattype** member of the [**DMO\_MEDIA\_TYPE**](dshow.dmo_media_type) structure that describes a high-definition audio type must be set to WMCFORMAT\_WaveFormatEx, just as it is for normal audio; there is no special format identifier for **WAVEFORMATEXTENSIBLE**. If a format uses **WAVEFORMATEXTENSIBLE** , you must set the **cbSize** member of the **WAVEFORMATEX** structure to 22.

When using Media Foundation, you can construct the correct media type from a [**WAVEFORMATEXTENSIBLE**](dshow.waveformatextensible) structure by using the function [**MFInitMediaTypeFromWaveFormatEx**](mfinitmediatypefromwaveformatex.md).

The multi-channel output types supported by the Windows Media Audio 10 Professional codec do not use [**WAVEFORMATEXTENSIBLE**](dshow.waveformatextensible), but report the correct number of channels and bits per sample in the [**WAVEFORMATEX**](dshow.waveformatex) structure. As with all audio types describing compressed Windows Media Audio content, there is additional information appended to the **WAVEFORMATEX** structure that is used by the decoder for decompression.

## Decoding High-Definition Audio

To decode high-definition audio, you must set the [MFPKEY\_WMADEC\_HIRESOUTPUT](mfpkey-wmadec-hiresoutputproperty.md) property to VARIANT\_TRUE. If this property is not set, the decoder will deliver stereo content with a maximum of 16 bits per sample, regardless of the compressed format.

> [!Note]  
> High-definition audio is supported only for Windows XP, Windows Vista and later. On earlier versions of Windows, Windows Media Audio content encoded with high definition is rendered as two-channel audio with a maximum of 16 bits per sample.

 

## Related topics

<dl> <dt>

[Working with Audio](workingwithaudio.md)
</dt> </dl>

 

 



