---
description: QT Decompressor Filter
ms.assetid: d013075f-deab-40ef-8438-4fb09820da3e
title: QT Decompressor Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# QT Decompressor Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

The QT Decompressor filter decompresses Apple® QuickTime® 2.0 video. This format is typically used in older QuickTime files.




| Label | Value |
|--------|-------|
| Filter Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a> | 
| Input Pin Media Types | MEDIATYPE_Video, FORMAT_VideoInfo<br /> The following subtypes are valid:<br /><ul><li>MEDIASUBTYPE_QTRpza</li><li>MEDIASUBTYPE_QTSmc</li><li>MEDIASUBTYPE_QTRle</li><li>MEDIASUBTYPE_QTJpeg</li></ul> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | MEDIATYPE_Video, MEDIASUBTYPE_NULL, FORMAT_VideoInfo | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_QTDec | 
| Property Page CLSID | No property page. | 
| Executable | quartz.dll | 
| <a href="merit.md">Merit</a> | MERIT_NORMAL | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




