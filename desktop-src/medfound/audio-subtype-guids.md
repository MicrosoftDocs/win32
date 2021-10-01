---
description: Audio Subtype GUIDs
ms.assetid: c38a1194-e2d8-42ca-8581-4054171f6f44
title: Audio Subtype GUIDs
ms.topic: article
ms.date: 05/31/2018
---

# Audio Subtype GUIDs

The following audio subtype GUIDs are defined. To specify the subtype, set the [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md) attribute on the media type. Except where noted, these constants are defined in the header file mfapi.h.

When these subtypes are used, set the [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md) attribute to **MFMediaType\_Audio**.




| GUID | Description | Format Tag (FOURCC) | 
|------|-------------|---------------------|
| <strong>MEDIASUBTYPE_RAW_AAC1</strong> | Advanced Audio Coding (AAC).<br /> This subtype is used for AAC contained in an AVI file with an audio format tag equal to 0x00FF. <br /> For more information, see <a href="aac-decoder.md"><strong>AAC Decoder</strong></a>.<br /> Defined in wmcodecdsp.h<br /> | WAVE_FORMAT_RAW_AAC1 (0x00FF) | 
| <strong>MFAudioFormat_AAC</strong> | Advanced Audio Coding (AAC).<br /><blockquote>[!Note]<br />Equivalent to MEDIASUBTYPE_MPEG_HEAAC, defined in wmcodecdsp.h.</blockquote><br /> The stream can contain raw AAC data or AAC data in an Audio Data Transport Stream (ADTS) stream.<br /> For more information, see:<br /><ul><li><a href="aac-decoder.md"><strong>AAC Decoder</strong></a></li><li><a href="mpeg-4-file-source.md">MPEG-4 File Source</a></li></ul> | WAVE_FORMAT_MPEG_HEAAC (0x1610) | 
| <strong>MFAudioFormat_ADTS</strong> | Not used. | WAVE_FORMAT_MPEG_ADTS_AAC (0x1600) | 
| <strong>MFAudioFormat_ALAC</strong> | Apple Lossless Audio Codec<br /> Supported in Windows 10 and later.<br /> | WAVE_FORMAT_ALAC (0x6C61) | 
| <strong>MFAudioFormat_AMR_NB</strong> | Adaptative Multi-Rate audio<br /> Supported in Windows 8.1 and later.<br /> | WAVE_FORMAT_AMR_NB | 
| <strong>MFAudioFormat_AMR_WB</strong> | Adaptative Multi-Rate Wideband audio<br /> Supported in Windows 8.1 and later.<br /> | WAVE_FORMAT_AMR_WB | 
| <strong>MFAudioFormat_AMR_WP</strong> | Supported in Windows 8.1 and later.<br /> | WAVE_FORMAT_AMR_WP | 
| <strong>MFAudioFormat_Dolby_AC3</strong> | Dolby Digital (AC-3).<br /> Same GUID value as <strong>MEDIASUBTYPE_DOLBY_AC3</strong>, which is defined in ksuuids.h<br /> | None. | 
| <strong>MFAudioFormat_Dolby_AC3_SPDIF</strong> | Dolby AC-3 audio over Sony/Philips Digital Interface (S/PDIF).<br /> This GUID value is identical to the following subtypes:<br /><ul><li><strong>KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL</strong>, defined in ksmedia.h.</li><li><strong>MEDIASUBTYPE_DOLBY_AC3_SPDIF</strong>, defined in uuids.h.</li></ul> | WAVE_FORMAT_DOLBY_AC3_SPDIF (0x0092) | 
| <strong>MFAudioFormat_Dolby_DDPlus</strong> | Dolby Digital Plus.<br /> Same GUID value as <strong>MEDIASUBTYPE_DOLBY_DDPLUS</strong>, which is defined in wmcodecdsp.h.<br /> | None | 
| <strong>MFAudioFormat_DRM</strong> | Encrypted audio data used with secure audio path. | WAVE_FORMAT_DRM (0x0009) | 
| <strong>MFAudioFormat_DTS</strong> | Digital Theater Systems (DTS) audio. | WAVE_FORMAT_DTS (0x0008) | 
| <strong>MFAudioFormat_FLAC</strong> | Free Lossless Audio Codec<br /> Supported in Windows 10 and later.<br /> | WAVE_FORMAT_FLAC (0xF1AC) | 
| <strong>MFAudioFormat_Float</strong> | Uncompressed IEEE floating-point audio. | WAVE_FORMAT_IEEE_FLOAT (0x0003) | 
| <strong>MFAudioFormat_Float_SpatialObjects</strong> | Uncompressed IEEE floating-point audio. | None | 
| <strong>MFAudioFormat_MP3</strong> | MPEG Audio Layer-3 (MP3). | WAVE_FORMAT_MPEGLAYER3 (0x0055) | 
| <strong>MFAudioFormat_MPEG</strong> | MPEG-1 audio payload. | WAVE_FORMAT_MPEG (0x0050) | 
| <strong>MFAudioFormat_MSP1</strong> | Windows Media Audio 9 Voice codec. | WAVE_FORMAT_WMAVOICE9 (0x000A) | 
| <strong>MFAudioFormat_Opus</strong> | Opus<br /> Supported in Windows 10 and later.<br /> | WAVE_FORMAT_OPUS (0x704F) | 
| <strong>MFAudioFormat_PCM</strong> | Uncompressed PCM audio. | WAVE_FORMAT_PCM (1) | 
| <strong>MFAudioFormat_QCELP</strong> | QCELP (Qualcomm Code Excited Linear Prediction) audio. | None | 
| <strong>MFAudioFormat_WMASPDIF</strong> | Windows Media Audio 9 Professional codec over S/PDIF. | WAVE_FORMAT_WMASPDIF (0x0164) | 
| <strong>MFAudioFormat_WMAudio_Lossless</strong> | Windows Media Audio 9 Lossless codec or Windows Media Audio 9.1 codec. | WAVE_FORMAT_WMAUDIO_LOSSLESS (0x0163) | 
| <strong>MFAudioFormat_WMAudioV8</strong> | Windows Media Audio 8 codec, Windows Media Audio 9 codec, or Windows Media Audio 9.1 codec. | WAVE_FORMAT_WMAUDIO2 (0x0161) | 
| <strong>MFAudioFormat_WMAudioV9</strong> | Windows Media Audio 9 Professional codec or Windows Media Audio 9.1 Professional codec. | WAVE_FORMAT_WMAUDIO3 (0x0162) | 




 

The format tags listed in the third column of this table are used in the **WAVEFORMATEX** structure, and are defined in the header file mmreg.h.

Given an audio format tag, you can create an audio subtype GUID as follows:

1.  Start with the value **MFAudioFormat\_Base**, which is defined in mfaph.i.
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

 

 




