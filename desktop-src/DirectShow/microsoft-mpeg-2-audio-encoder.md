---
description: The Microsoft MPEG-2 Audio Encoder filter encodes MPEG-1 audio layers I and II, including support for the MPEG-2 Low Sampling Frequency (LSF) extensions.
ms.assetid: a36e838b-8b11-4851-9dd2-efd9fe070770
title: Microsoft MPEG-2 Audio Encoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Microsoft MPEG-2 Audio Encoder

The Microsoft MPEG-2 Audio Encoder filter encodes MPEG-1 audio layers I and II, including support for the MPEG-2 Low Sampling Frequency (LSF) extensions.

To encode and multiplex audio/video streams, use the [**Microsoft MPEG-2 Encoder**](microsoft-mpeg-2-encoder.md) filter, which encapsulates the functions of both this filter and the [**Microsoft MPEG-2 Video Encoder**](microsoft-mpeg-2-video-encoder.md) filter.

> [!Note]  
> This filter is not supported on IA-64-based platforms.

 



Filter Information

Filter Interfaces

[**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)<br/> [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)<br/> **IEncoderAPI**<br/> [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)<br/> [**IVideoEncoder**](/windows/win32/api/strmif/nn-strmif-ivideoencoder)<br/>

Input Pin Media Types

**MEDIATYPE\_Audio**, **MEDIASUBTYPE\_PCM**

Input Pin Interfaces

[**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/>

Output Pin Media Types

**MEDIATYPE\_Audio**, **MEDIASUBTYPE\_MPEG2\_AUDIO**<br/> **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG2\_AUDIO**<br/> **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG2\_PROGRAM**<br/> **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG2\_TRANSPORT**<br/>

Output Pin Interfaces

[**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/>

Filter CLSID

**CLSID\_CMPEG2EncoderAudioDS** (declared in wmcodecdsp.h)

Executable

msmpeg2enc.dll

[Merit](merit.md)

**MERIT\_DO\_NOT\_USE**

[Filter Category](filter-categories.md)

**CLSID\_LegacyAmFilterCategory**



 

## Remarks

The MPEG-2 Audio Encoder can produce the following kinds of output:

-   Audio elementary stream
-   Audio in an MPEG-2 program stream
-   Audio in an MPEG-2 transport stream

It supports MPEG-1 layers I and II and MPEG-2 low sampling frequency (LSF) extensions

Input samples must 16 bits per sample, with an audio sampling rate of 48, 44.1, 32, 22.05, or 16 KHz. The encoder cannot resample the audio stream; the encoded audio has the same sample rate as the input.

Input samples must be mono or stereo. The encoded audio has the number of channels as the input.

### Limitations

The encoder does not support the following:

-   MPEG layer III audio bitstreams.
-   MPEG-2 multi-channel extension bitstreams.
-   MPEG-4 AAC bitstreams.
-   MPEG-2 non-backward compatible (NBC) bitstreams.
-   Generation of packetized elementary stream (PES) packets.
-   Dolby Digital encoding.

### Codec Properties

The filter supports the following properties through [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi):

-   [**AVAudioChannelCount**](avaudiochannelcount-property.md)
-   [**AVAudioSampleRate**](avaudiosamplerate-property.md)
-   [**AVEncAudioIntervalToEncode**](avencaudiointervaltoencode-property.md)
-   [**AVEncCommonFormatConstraint**](avenccommonformatconstraint-property.md)
-   [**AVEncCommonMeanBitRate**](avenccommonmeanbitrate-property.md)
-   [**AVEncMPACodingMode**](avencmpacodingmode-property.md)
-   [**AVEncMPACopyright**](avencmpacopyright-property.md)
-   [**AVEncMPAEmphasisType**](avencmpaemphasistype-property.md)
-   [**AVEncMPAEnableRedundancyProtection**](avencmpaenableredundancyprotection-property.md)
-   [**AVEncMPALayer**](avencmpalayer-property.md)
-   [**AVEncMPAOriginalBitstream**](avencmpaoriginalbitstream-property.md)
-   [**AVEncMPAPrivateUserBit**](avencmpaprivateuserbit-property.md)

> [!Note]  
> An earlier version of the documentation incorrectly listed some additional properties that are not supported.

 

For backward compatibility, the filter supports the following property through the **IEncoderAPI** interface:



| Property                 | Description                                                                      |
|--------------------------|----------------------------------------------------------------------------------|
| **ENCAPIPARAM\_BITRATE** | Equivalent to [**AVEncCommonMeanBitRate**](avenccommonmeanbitrate-property.md). |



 

It is recommended to set properties in the following order:

1.  [**AVEncCommonFormatConstraint**](avenccommonformatconstraint-property.md)
2.  [**AVEncMPALayer**](avencmpalayer-property.md)
3.  [**AVEncCommonMeanBitRate**](avenccommonmeanbitrate-property.md)
4.  [**AVEncMPACodingMode**](avencmpacodingmode-property.md)

Set the remaining properties in any order.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Home Premium, Windows Vista Ultimate, Windows 7 Home Premium, Windows 7 Professional, Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                                     |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl>                                                                                       |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[**MPEG-2 Demultiplexer Media Types**](mpeg-2-demultiplexer-media-types.md)
</dt> </dl>

 

 
