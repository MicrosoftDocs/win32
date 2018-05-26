---
Description: AVI Decompressor Filter
ms.assetid: 6a9914db-483a-429c-9b26-9451578951c9
title: AVI Decompressor Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVI Decompressor Filter

The AVI Decompressor filter enables Video Compression Manager (VCM) codecs to join a filter graph. The application does not need to add the filter to the filter graph; it is pulled in automatically by the Filter Graph Manager when needed.

When the Filter Graph Manager is building a graph to render an AVI file, it checks the FOURCC in the file's AVI header to determine whether the video stream is compressed. If it is, the Filter Graph Manager adds the AVI Decompressor, which then searches the registry for an installed decompressor that can handle the file.

> [!Note]  
> MPEG decompressors are never implemented as VCM codecs, but only as native DirectShow filters.

 

On its upstream pin the AVI Decompressor typically connects to the [AVI Splitter](avi-splitter-filter.md). On its output pin it typically connects to the [Video Renderer](video-renderer-filter.md) or the [AVI Mux Filter](avi-mux-filter.md).



|                                          |                                                                                                                                                                                                                    |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)                                                                                                                                                                                 |
| Input Pin Media Types                    | Major type: MEDIATYPE\_VideoSubtype: Must correspond to the FOURCC code for the compression type. For more information, see [FOURCC Codes](fourcc-codes.md).<br/> Format type: FORMAT\_VideoInfo<br/> |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_NULL, FORMAT\_VideoInfo                                                                                                                                                            |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                 |
| Filter CLSID                             | CLSID\_AVIDec                                                                                                                                                                                                      |
| Property Page CLSID                      | No property page.                                                                                                                                                                                                  |
| Executable                               | quartz.dll                                                                                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                                                                                                                                                      |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




