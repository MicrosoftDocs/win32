---
description: 'This filter decodes the following audio formats:'
ms.assetid: 2fd14296-9eed-4e25-b140-6281c707fdb7
title: Microsoft MPEG-1/DD/AAC Audio Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Microsoft MPEG-1/DD/AAC Audio Decoder

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This filter decodes the following audio formats:

-   MPEG-1 audio layers I and II.
-   Backward-compatible MPEG-2 audio, layers I and II (ISO/IEC 13818-3), mono and stereo only.
-   Advanced Audio Coding (AAC) Low Complexity (LC) profile.
-   High-Efficiency AAC (HE-AAC) version 1 and version 2.
-   Pass-through Digital Theater Systems (DTS) for digital output.
-   LPCM, mono and stereo only, with or without PES headers.
-   Dolby Digital.
-   Dolby Digital Plus, including conversion from Dolby Digital Plus to Dolby Digital for digital output.

> [!Note]  
> The Microsoft implementation of the Dolby Digital technology is restricted under terms of the Dolby Digital licensing program to use by Microsoft applications.

 

> [!Note]  
> This filter is not supported on IA-64-based platforms.

 

Decoding of Dolby Digital Plus, AAC, and HE-AAC formats requires Windows 7. Decoding of Dolby Digital or Dolby Digital Plus is not supported on Windows 7 Home Basic or Windows 7 Starter.

In the registry, the friendly name of this filter is "Microsoft DTV-DVD Audio Decoder".



Filter Information

Filter Interfaces

[**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)<br/> [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)<br/>

Input Pin Media Types

In Windows Vista and later, the filter supports the following input types:<br/>

-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_DOLBY\_AC3** (See Note 1.)
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_MPEG1Audio**
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_MPEG1Payload**
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_MPEG2\_AUDIO**
-   **MEDIATYPE\_DVD\_ENCRYPTED\_PACK**, **MEDIASUBTYPE\_DOLBY\_AC3** (See Note 1.)
-   **MEDIATYPE\_DVD\_ENCRYPTED\_PACK**, **MEDIASUBTYPE\_DTS** (See Note 2.)
-   **MEDIATYPE\_DVD\_ENCRYPTED\_PACK**, **MEDIASUBTYPE\_DVD\_LPCM\_AUDIO**
-   **MEDIATYPE\_DVD\_ENCRYPTED\_PACK**, **MEDIASUBTYPE\_MPEG2\_AUDIO**
-   **MEDIATYPE\_MPEG2\_PES**, **MEDIASUBTYPE\_DOLBY\_AC3** (See Note 1.)
-   **MEDIATYPE\_MPEG2\_PES**, **MEDIASUBTYPE\_DTS** (See Note 2.)
-   **MEDIATYPE\_MPEG2\_PES**, **MEDIASUBTYPE\_DVD\_LPCM\_AUDIO**
-   **MEDIATYPE\_MPEG2\_PES**, **MEDIASUBTYPE\_MPEG2\_AUDIO**
-   **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_DOLBY\_AC3** (See Note 1.)
-   **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG1Audio**
-   **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG2\_AUDIO**

Starting in Windows 7, the filter also supports the following input types:<br/>

-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_DOLBY\_DDPLUS** (See Note 1.)
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_DTS2** (See Note 2.)
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_DVD\_LPCM\_AUDIO**
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_DVM** (See Note 1.)
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_MPEG\_ADTS\_AAC**
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_MPEG\_LOAS**
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_MPEG1AudioPayload**
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_RAW\_AAC1**
-   **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_DOLBY\_DDPLUS** (See Note 1.)
-   **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG\_ADTS\_AAC**
-   **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG\_LOAS**

The input type can change dynamically during streaming.<br/> For more information about these media types, see [**Audio Subtypes**](audio-subtypes.md).<br/>

> [!Note]  
> 1. The Microsoft implementation of the Dolby Digital technology is restricted under terms of the Dolby Digital licensing program to use by Microsoft applications.

<br/>

> [!Note]  
> 2. For Digital Theater Systems (DTS) input, only S/PDIF output is supported (DTS over S/PDIF). Audio decoding is not supported.

<br/>

Input Pin Interfaces

[**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)<br/> [**IKsPropertySet**](ikspropertyset.md)<br/> [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/>

Output Pin Media Types

In Windows Vista and later, the filter supports the following output types:<br/>

-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_DOLBY\_AC3\_SPDIF** (same as **KSDATAFORMAT\_SUBTYPE\_IEC61937\_DOLBY\_DIGITAL**)
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_PCM**

Starting in Windows 7, the filter also supports the following output types:<br/>

-   **MEDIATYPE\_Audio**, **KSDATAFORMAT\_SUBTYPE\_IEC61937\_DTS**
-   **MEDIATYPE\_Audio**, **MEDIASUBTYPE\_IEEE\_FLOAT**

Output Pin Interfaces

[**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/>

Filter CLSID

**CLSID\_CMPEG2AudDecoderDS** (declared in wmcodecdsp.h)

Executable

msmpeg2adec.dll

[Merit](merit.md)

**MERIT\_NORMAL** - 1

[Filter Category](filter-categories.md)

**CLSID\_LegacyAmFilterCategory**



 

> [!Note]  
> An earlier version of the documentation stated that this filter can decode "MPEG-2 audio." The filter decodes only backward-compatible MPEG-2 audio.

 

## Remarks

Mono streams are always decoded to stereo.

For streams with a channel configuration of two or more speakers, the decoder does one of the following:

-   Up-mixes to six channels, using the common 5.1 speaker configuration.
-   Downmixes to stereo.

To select between these two options, use the [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi) interface to set the [**AVDecCommonOutputFormat**](avdeccommonoutputformat-property.md) property, before connecting the pins. Alternatively, when the application builds the filter graph, it can set the desired media type on the output pin.

### AAC Decoding

For AAC, the decoder has certain format constraints on the compressed AAC input. These format constraints are the same as the Media Foundation [**AAC Decoder**](../medfound/aac-decoder.md), and are documented in the section "[**Format Constraints**](../medfound/aac-decoder.md)".

The DirectShow decoder also accepts different input types than the Media Foundation decoder. The DirectShow decoder supports the following AAC input types:

-   **MEDIASUBTYPE\_RAW\_AAC1**: Raw AAC, typically found in AVI or Matroska (.MKV) files.
-   **MEDIASUBTYPE\_MPEG\_ADTS\_AAC**: AAC in an Audio Data Transport Stream (ADTS) for streaming.
-   **MEDIASUBTYPE\_MPEG\_LOAS**: Transport stream with a synchronization layer (LOAS) and a multiplex layer (LATM).

The Media Foundation decoder supports the following AAC input types:

-   MFAudioFormat\_AAC (same as **MEDIASUBTYPE\_MPEG\_HEAAC**) for MP4 file playback.
-   **MEDIASUBTYPE\_RAW\_AAC1**.

### Property Sets

The decoder's input pin supports the following property sets through [**IKsPropertySet**](ikspropertyset.md):

-   [**DVD Copy Protection Property Set**](dvd-copy-protection-property-set.md)
-   [**Rate-Change Property Set**](rate-change-property-set.md).

> [!Note]  
> Starting in Windows 7, the decoder supports trick mode through the rate-change property set. It supports playback rates in the range \[0.501 – 2.0\], where 1.0 is normal playback rate, and 2.0 is twice the normal rate.

 

### Codec Properties

The decoder's input pin supports the following properties through [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi):



| Property                                                          | Requires                                                 |
|-------------------------------------------------------------------|----------------------------------------------------------|
| [**AVAudioChannelConfig**](avaudiochannelconfig-property.md)     | Windows Vista                                            |
| [**AVAudioChannelCount**](avaudiochannelcount-property.md)       | Windows Vista                                            |
| [**AVAudioSampleRate**](avaudiosamplerate-property.md)           | Windows Vista                                            |
| [**AVDDSurroundMode**](avddsurroundmode-property.md)             | Windows Vista only; not supported in Windows 7 or later. |
| [**AVDecAudioDualMono**](avdecaudiodualmono-property.md)         | Windows Vista                                            |
| [**AVDecCommonInputFormat**](avdeccommoninputformat-property.md) | Windows Vista                                            |
| [**AVDecCommonMeanBitRate**](avdeccommonmeanbitrate.md)          | Windows 7                                                |



 

The filter supports the following properties through [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi):



| Property                                                                          | Requires      |
|-----------------------------------------------------------------------------------|---------------|
| [**AVDecAACDownmixMode**](avdecaacdownmixmode-property.md)                       | Windows 7     |
| [**AVDecAudioDualMonoReproMode**](avdecaudiodualmonorepromode-property.md)       | Windows Vista |
| [**AVDecCommonOutputFormat**](avdeccommonoutputformat-property.md) (See Note 3.) | Windows Vista |
| [**AVDecDDDynamicRangeScaleHigh**](avdecdddynamicrangescalehigh-property.md)     | Windows Vista |
| [**AVDecDDDynamicRangeScaleLow**](avdecdddynamicrangescalelow-property.md)       | Windows Vista |
| [**AVDecDDOperationalMode**](avdecddoperationalmode-property.md)                 | Windows Vista |
| [**AVDecMmcssClass**](avdecmmcss-property.md)                                    | Windows Vista |
| [**AVDSPLoudnessEqualization**](avdsploudnessequalization-property.md)           | Windows 7     |
| [**AVDSPSpeakerFill**](avdspspeakerfill-property.md)                             | Windows 7     |



 

> [!Note]  
> 3. The [**AVDecCommonOutputFormat**](avdeccommonoutputformat-property.md) property must be set before the decoder's output pin is connected. Otherwise, the change has no effect.

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Home Premium, Windows Vista Ultimate, Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl>        |



## See also

<dl> <dt>

[**Audio Subtypes**](audio-subtypes.md)
</dt> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[**DVD Media Types**](dvd-media-types.md)
</dt> </dl>

 

 
