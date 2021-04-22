---
description: AVI Decompressor Filter
ms.assetid: 6a9914db-483a-429c-9b26-9451578951c9
title: AVI Decompressor Filter
ms.topic: article
ms.date: 05/31/2018
---

# AVI Decompressor Filter

The AVI Decompressor filter enables Video Compression Manager (VCM) codecs to join a filter graph. The application does not need to add the filter to the filter graph; it is pulled in automatically by the Filter Graph Manager when needed.

When the Filter Graph Manager is building a graph to render an AVI file, it checks the FOURCC in the file's AVI header to determine whether the video stream is compressed. If it is, the Filter Graph Manager adds the AVI Decompressor, which then searches the registry for an installed decompressor that can handle the file.

> [!Note]  
> MPEG decompressors are never implemented as VCM codecs, but only as native DirectShow filters.

 

On its upstream pin the AVI Decompressor typically connects to the [AVI Splitter](avi-splitter-filter.md). On its output pin it typically connects to the [Video Renderer](video-renderer-filter.md) or the [AVI Mux Filter](avi-mux-filter.md).



| Label | Value |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)                                                                                                                                                                                 |
| Input Pin Media Types                    | Major type: MEDIATYPE\_VideoSubtype: Must correspond to the FOURCC code for the compression type. For more information, see [FOURCC Codes](fourcc-codes.md).<br/> Format type: FORMAT\_VideoInfo<br/> |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                                                                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_NULL, FORMAT\_VideoInfo                                                                                                                                                            |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                                                 |
| Filter CLSID                             | CLSID\_AVIDec                                                                                                                                                                                                      |
| Property Page CLSID                      | No property page.                                                                                                                                                                                                  |
| Executable                               | quartz.dll                                                                                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                                                                                                                                                      |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




