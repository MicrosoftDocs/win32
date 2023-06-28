---
description: QuickTime Movie Parser Filter
ms.assetid: 9537dd7b-9aeb-4e73-a31d-86053874ef13
title: QuickTime Movie Parser Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# QuickTime Movie Parser Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

The QuickTime Movie Parser filter splits Apple® QuickTime® data into audio and video streams. It supports QuickTime 2.0 and earlier. The input pin connects to a source filter such as the [Async File Source](file-source--async--filter.md) filter or the [URL File Source](file-source--url--filter.md) filter. The Parser uses the [AVI Decompressor](avi-decompressor-filter.md) or [QT Decompressor](qt-decompressor-filter.md) filter to decompress QuickTime files. The filter creates one output pin for the video stream and one output pin for the audio stream.




| Label | Value |
|--------|-------|
| Filter Interfaces | <a href="/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent"><strong>IAMMediaContent</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a> | 
| Input Pin Media Types | MEDIATYPE_Stream, MEDIASUBTYPE_QTMovie; | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | <ul><li>MEDIATYPE_Video, MEDIASUBTYPE_NULL, FORMAT_VideoInfo</li><li>MEDIATYPE_Audio, MEDIASUBTYPE_NULL, FORMAT_WaveFormatEx</li></ul> | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_QuickTimeParser | 
| Property Page CLSID | No property page. | 
| Executable | quartz.dll | 
| <a href="merit.md">Merit</a> | MERIT_NORMAL | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



