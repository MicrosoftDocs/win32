---
description: Audio Subtype GUIDs
ms.assetid: c38a1194-e2d8-42ca-8581-4054171f6f44
title: Audio Subtype GUIDs
ms.topic: reference
ms.date: 05/31/2018
---

# Audio Subtype GUIDs

The following audio subtype GUIDs are defined. To specify the subtype, set the [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md) attribute on the media type. Except where noted, these constants are defined in the header file mfapi.h.

When these subtypes are used, set the [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md) attribute to **MFMediaType\_Audio**.




| GUID | Description | Format Tag (FOURCC) | 
|------|-------------|---------------------|
| **MEDIASUBTYPE_RAW_AAC1** | Advanced Audio Coding (AAC).<br /> This subtype is used for AAC contained in an AVI file with an audio format tag equal to 0x00FF. <br /> For more information, see <a href="aac-decoder.md">**AAC Decoder**</a>.<br /> Defined in wmcodecdsp.h<br /> | WAVE_FORMAT_RAW_AAC1 (0x00FF) | 
| **MFAudioFormat_AAC** | Advanced Audio Coding (AAC).<br> **Note:** Equivalent to MEDIASUBTYPE_MPEG_HEAAC, defined in wmcodecdsp.h.<br> The stream can contain raw AAC data or AAC data in an Audio Data Transport Stream (ADTS) stream.<br> For more information, see:<br>- [**AAC Decoder**](aac-decoder.md)<br>- [MPEG-4 File Source](mpeg-4-file-source.md)<br> | WAVE_FORMAT_MPEG_HEAAC (0x1610) | 
| **MFAudioFormat_ADTS** | Not used. | WAVE_FORMAT_MPEG_ADTS_AAC (0x1600) | 
| **MFAudioFormat_ALAC** | Apple Lossless Audio Codec<br /> Supported in Windows 10 and later.<br /> | WAVE_FORMAT_ALAC (0x6C61) | 
| **MFAudioFormat_AMR_NB** | Adaptative Multi-Rate audio<br /> Supported in Windows 8.1 and later.<br /> | WAVE_FORMAT_AMR_NB | 
| **MFAudioFormat_AMR_WB** | Adaptative Multi-Rate Wideband audio<br /> Supported in Windows 8.1 and later.<br /> | WAVE_FORMAT_AMR_WB | 
| **MFAudioFormat_AMR_WP** | Supported in Windows 8.1 and later.<br /> | WAVE_FORMAT_AMR_WP | 
| **MFAudioFormat_Dolby_AC3** | Dolby Digital (AC-3).<br /> Same GUID value as **MEDIASUBTYPE_DOLBY_AC3**, which is defined in ksuuids.h<br /> | None. | 
| **MFAudioFormat_Dolby_AC3_SPDIF** | Dolby AC-3 audio over Sony/Philips Digital Interface (S/PDIF).<br /> This GUID value is identical to the following subtypes:<br /><ul><li>**KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL**, defined in ksmedia.h.</li><li>**MEDIASUBTYPE_DOLBY_AC3_SPDIF**, defined in uuids.h.</li></ul> | WAVE_FORMAT_DOLBY_AC3_SPDIF (0x0092) | 
| **MFAudioFormat_Dolby_DDPlus** | Dolby Digital Plus.<br /> Same GUID value as **MEDIASUBTYPE_DOLBY_DDPLUS**, which is defined in wmcodecdsp.h.<br /> | None | 
| **MFAudioFormat_DRM** | Encrypted audio data used with secure audio path. | WAVE_FORMAT_DRM (0x0009) | 
| **MFAudioFormat_DTS** | Digital Theater Systems (DTS) audio. | WAVE_FORMAT_DTS (0x0008) | 
| **MFAudioFormat_FLAC** | Free Lossless Audio Codec<br /> Supported in Windows 10 and later.<br /> | WAVE_FORMAT_FLAC (0xF1AC) | 
| **MFAudioFormat_Float** | Uncompressed IEEE floating-point audio. | WAVE_FORMAT_IEEE_FLOAT (0x0003) | 
| **MFAudioFormat_Float_SpatialObjects** | Uncompressed IEEE floating-point audio. | None | 
| **MFAudioFormat_IAMF** | [IAMF](https://aomedia.org/specifications/iamf/) audio. | None | 
| **MFAudioFormat_MP3** | MPEG Audio Layer-3 (MP3). | WAVE_FORMAT_MPEGLAYER3 (0x0055) | 
| **MFAudioFormat_MPEG** | MPEG-1 audio payload. | WAVE_FORMAT_MPEG (0x0050) | 
| **MFAudioFormat_MSP1** | Windows Media Audio 9 Voice codec. | WAVE_FORMAT_WMAVOICE9 (0x000A) | 
| **MFAudioFormat_Opus** | Opus<br /> Supported in Windows 10 and later.<br /> | WAVE_FORMAT_OPUS (0x704F) | 
| **MFAudioFormat_PCM** | Uncompressed PCM audio. | WAVE_FORMAT_PCM (1) | 
| **MFAudioFormat_QCELP** | QCELP (Qualcomm Code Excited Linear Prediction) audio. | None | 
| **MFAudioFormat_WMASPDIF** | Windows Media Audio 9 Professional codec over S/PDIF. | WAVE_FORMAT_WMASPDIF (0x0164) | 
| **MFAudioFormat_WMAudio_Lossless** | Windows Media Audio 9 Lossless codec or Windows Media Audio 9.1 codec. | WAVE_FORMAT_WMAUDIO_LOSSLESS (0x0163) | 
| **MFAudioFormat_WMAudioV8** | Windows Media Audio 8 codec, Windows Media Audio 9 codec, or Windows Media Audio 9.1 codec. | WAVE_FORMAT_WMAUDIO2 (0x0161) | 
| **MFAudioFormat_WMAudioV9** | Windows Media Audio 9 Professional codec or Windows Media Audio 9.1 Professional codec. | WAVE_FORMAT_WMAUDIO3 (0x0162) | 




 

The format tags listed in the third column of this table are used in the **WAVEFORMATEX** structure, and are defined in the header file mmreg.h.

Given an audio format tag, you can create an audio subtype GUID as follows:

1.  Start with the value **MFAudioFormat\_Base**, which is defined in mfapi.h.
2.  Replace the first **DWORD** of this GUID with the format tag.

You can use the [**DEFINE\_MEDIATYPE\_GUID**](/windows/desktop/api/mfapi/nf-mfapi-define_mediatype_guid) macro to define a new GUID constant that follows this pattern.

## Related topics

<dl> <dt>

[Audio Media Types](audio-media-types.md)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type GUIDs](media-type-guids.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 




