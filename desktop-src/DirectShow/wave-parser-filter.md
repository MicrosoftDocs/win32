---
description: WAVE Parser Filter
ms.assetid: 53a9538d-7a79-40bb-9468-d710eb238925
title: WAVE Parser Filter
ms.topic: article
ms.date: 05/31/2018
---

# WAVE Parser Filter

The WAVE Parser filter parses WAV-format audio data from .wav, .au, or .aif files. The upstream filter must be the [Async File Source](file-source--async--filter.md) filter, [URL File Source](file-source--url--filter.md) filter, or a compatible third-party asynchronous source filter that contains WAV audio data. The output stream is audio data, which you can connect directly to an audio rendering filter or to an intervening audio transform filter.




| 
|
| Filter Interfaces | <a href="/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent"><strong>IAMMediaContent</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipersistmediapropertybag"><strong>IPersistMediaPropertyBag</strong></a> | 
| Input Pin Media Types | Major type: MEDIATYPE_StreamThe following subtypes are valid:<br /><ul><li>MEDIASUBTYPE_AIFF</li><li>MEDIASUBTYPE_AU</li><li>MEDIASUBTYPE_WAVE</li></ul> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | Major type: MEDIATYPE_AudioSubtype: MEDIASUBTYPE_PCM or other compression type. (See <a href="audio-subtypes.md"><strong>Audio Subtypes</strong></a>.)<br /> Format type: FORMAT_WaveFormatEx<br /> | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a> | 
| Filter CLSID | {D51BD5A1-7548-11cf-A520-0080C77EF58A} | 
| Property Page CLSID | No property page. | 
| Executable | quartz.dll | 
| <a href="merit.md">Merit</a> | MERIT_UNLIKELY | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Remarks

This filter supports the following file types:

-   WAVE (.wav)
-   AIFF and AIFF-C (.aif)
-   AU (.au)

However, it has the following limitations on the audio format:

-   The audio must be 8-bit or 16-bit linear PCM.
-   For AIFF-C files, the audio must be uncompressed, in big-endian byte order (compression type 'NONE').

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




