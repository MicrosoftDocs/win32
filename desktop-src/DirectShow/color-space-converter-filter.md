---
description: Color Space Converter Filter
ms.assetid: a6765184-43ce-47b8-9eb1-e15af7e11c93
title: Color Space Converter Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Color Space Converter Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This transform filter converts from one RGB color type to another RGB type, such as between 24-bit and 8-bit RGB color. Since this type of conversion is generally handled more efficiently within a video decompressor, the main use of the Color Space Converter is when the stream source consists of uncompressed RGB frames.




| Label | Value |
|--------|-------|
| Filter Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a> | 
| Input Pin Media Types | MEDIATYPE_Video, FORMAT_VideoInfo.<br /> The following subtypes are valid:<br /><ul><li>MEDIASUBTYPE_RGB8</li><li>MEDIASUBTYPE_RGB555</li><li>MEDIASUBTYPE_RGB565</li><li>MEDIASUBTYPE_RGB24</li><li>MEDIASUBTYPE_RGB32</li></ul> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | MEDIATYPE_Video, FORMAT_VideoInfo.<br /> The following subtypes are valid:<br /><ul><li>MEDIASUBTYPE_RGB8</li><li>MEDIASUBTYPE_RGB555</li><li>MEDIASUBTYPE_RGB565</li><li>MEDIASUBTYPE_RGB24</li><li>MEDIASUBTYPE_RGB32</li></ul> | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_Colour | 
| Property Page CLSID | No property page. | 
| Executable | quartz.dll | 
| <a href="merit.md">Merit</a> | MERIT_UNLIKELY | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




