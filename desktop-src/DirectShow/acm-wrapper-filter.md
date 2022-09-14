---
description: ACM Wrapper Filter
ms.assetid: f3cd8e90-8949-482a-8ada-47711f6c935f
title: ACM Wrapper Filter
ms.topic: article
ms.date: 05/31/2018
---

# ACM Wrapper Filter

The ACM Wrapper filter enables Audio Compression Manager (ACM) codecs to join a filter graph. It can act either as a decompression filter or as a compression filter.

As a decompression filter, the ACM Wrapper appears in the "DirectShow Filters" category (CLSID\_LegacyAmFilterCategory) and has a merit of MERIT\_NORMAL. The connection media type on the input pin determines which codec the filter uses. Typically, the application does not need to add the filter to the filter graph; it is pulled in automatically by the Filter Graph Manager when needed. Decompression is only to PCM audio.

As a compression filter, the ACM Wrapper appears in the "Audio Compressors" category (CLSID\_AudioCompressorCategory) and has a merit of MERIT\_DO\_NOT\_USE. Each codec appears as a separate instance. For compression, you cannot directly create the filter with CoCreateInstance. Instead, you must use the system device enumerator. For more information, see [Using the System Device Enumerator](using-the-system-device-enumerator.md).




| Label | Value |
|--------|-------|
| Filter interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, IPersist, IPersistPropertyBag | 
| Input pin media types | MEDIATYPE_Audio, MEDIASUBTYPE_NULL, FORMAT_WaveFormatEx | 
| Input pin interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output pin media types | MEDIATYPE_Audio, MEDIASUBTYPE_PCM, FORMAT_WaveFormatEx.Any combination of the following are possible:<br /><ul><li>Samples per second (kHz): 44.1, 22.05, 11.025, or 8.0.</li><li>Channels: Stereo or mono.</li><li>Bits per sample: 8 or 16.</li></ul> | 
| Output pin interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig"><strong>IAMStreamConfig</strong></a>, <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_ACMWrapper | 
| Property Page CLSID | No property page. | 
| Executable | Quartz.dll | 
| <a href="merit.md">Merit</a> | MERIT_NORMAL or MERIT_DO_NOT_USE | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory or CLSID_AudioCompressorCategory | 




 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




