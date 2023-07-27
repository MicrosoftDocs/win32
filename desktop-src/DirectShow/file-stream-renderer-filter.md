---
description: File Stream Renderer Filter
ms.assetid: e26462bb-e67f-4522-bec2-88378c4ff442
title: File Stream Renderer Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# File Stream Renderer Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The File Stream Renderer filter renders file names that are parsed by the [Multi-File Parser](multi-file-parser-filter.md) filter. For more information, see the documentation for that filter.

The use of this filter is deprecated. To render multiple files within the same filter graph, the application should simply call **RenderFile** or **AddSourceFilter** multiple times.




| Label | Value |
|--------|-------|
| Filter interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a> | 
| Input pin media types | <ul><li>Major type: MEDIATYPE_File</li><li>Subtype: GUID_NULL</li><li>Format type: MEDIATYPE_File</li></ul> | 
| Input pin interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output pin media types | None | 
| Output pin interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-istreambuilder"><strong>IStreamBuilder</strong></a> | 
| Filter CLSID | CLSID_FileRend | 
| Executable | Quartz.dll | 
| <a href="merit.md">Merit</a> | MERIT_UNLIKELY | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Remarks

The filter's CLSID is not defined in Uuids.h. Use this macro in your own header file:


```C++
// {D51BD5A5-7548-11cf-A520-0080C77EF58A}
DEFINE_GUID(CLSID_FileRend,
0xd51bd5A5, 0x7548, 0x11cf, 0xa5, 0x20, 0x0, 0x80, 0xc7, 0x7e, 0xf5, 0x8a);
```



## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



