---
description: AVI Draw Filter
ms.assetid: 86cd8e48-7cfa-46e4-b8f4-609b4d09fe80
title: AVI Draw Filter
ms.topic: article
ms.date: 05/31/2018
---

# AVI Draw Filter

The AVI Draw filter is pulled automatically into a playback graph instead of the [AVI Decompressor](avi-decompressor-filter.md) when video is being output to an external NTSC television monitor.




| 
|
| Filter Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a> | 
| Input Pin Media Types | Major Type: MEDIATYPE_VideoSubtypes:<br /><ul><li>MEDIASUBTYPE_MJPG</li><li>MEDIASUBTYPE_TVMJ</li><li>MEDIASUBTYPE_WAKE</li><li>MEDIASUBTYPE_CFCC</li><li>MEDIASUBTYPE_IJPG</li><li>MEDIASUBTYPE_Plum</li><li>MEDIASUBTYPE_DVCS</li><li>MEDIASUBTYPE_DVSD</li><li>MEDIASUBTYPE_MDVF</li><li>Format type: FORMAT_VideoInfo</li></ul> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | MEDIATYPE_Video, MEDIASUBTYPE_NULL | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ioverlaynotify"><strong>IOverlayNotify</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_AVIDraw | 
| Property Page CLSID | No property page. | 
| Executable | quartz.dll | 
| <a href="merit.md">Merit</a> | MERIT_NORMAL + 100 | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Remarks

Since the AVI Draw filter and the [VFW Capture Filter](vfw-capture-filter.md) both connect to the same hardware, they cannot be in the same filter graph.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




