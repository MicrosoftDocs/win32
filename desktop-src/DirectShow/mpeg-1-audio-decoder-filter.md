---
description: MPEG-1 Audio Decoder Filter
ms.assetid: 2f695ac6-7d4b-41a8-b4c5-83fb9d20ab9d
title: MPEG-1 Audio Decoder Filter
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-1 Audio Decoder Filter

Decodes MPEG-1 Layer I and Layer II audio to PCM.




| Label | Value |
|--------|-------|
| Filter Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, <strong>ISpecifyPropertyPages</strong> | 
| Input Pin Media Types | MEDIATYPE_Audio, FORMAT_WaveFormatEx<br /> The following subtypes are valid:<br /><ul><li>MEDIASUBTYPE_MPEG1Packet</li><li>MEDIASUBTYPE_MPEG1Payload</li><li>MEDIASUBTYPE_MPEG1AudioPayload</li><li>GUID_NULL</li></ul> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | MEDIATYPE_Audio, MEDIASUBTYPE_PCM | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_CMpegAudioCodec | 
| Property Page CLSID | CLSID_MpegAudioDecoderPropertyPage | 
| Executable | quartz.dll | 
| <a href="merit.md">Merit</a> | 0x03680001 | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




