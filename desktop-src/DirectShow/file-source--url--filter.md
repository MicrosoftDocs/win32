---
description: File Source (URL) Filter
ms.assetid: 405fd6ea-aa17-4d11-8f07-067468cb090b
title: File Source (URL) Filter
ms.topic: article
ms.date: 05/31/2018
---

# File Source (URL) Filter

The URL File Source filter is a generic asynchronous source filter that works with any source file that can be identified by a Uniform Resource Locator (URL) and whose media major type is stream. This includes AVI, MOV, MPEG, and WAV files. It requires the downstream filter to be a parser, such as the [MPEG-1 Stream Splitter](mpeg-1-stream-splitter-filter.md), the [AVI Splitter](avi-splitter-filter.md), or the [QuickTime Movie Parser](quicktime-movie-parser-filter.md).



| Label | Value |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMOpenProgress**](/windows/desktop/api/Strmif/nn-strmif-iamopenprogress), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IFileSourceFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter)       |
| Input Pin Media Types                    | Not applicable                                                                                                                       |
| Input Pin Interfaces                     | Not applicable                                                                                                                       |
| Output Pin Media Types                   | MEDIATYPE\_Stream. The subtype depends on the media format. (MEDIASUBTYPE\_NULL if the filter doesn't recognize the format.)         |
| Output Pin Interfaces                    | [**IAMAsyncReaderTimestampScaling**](/windows/desktop/api/Strmif/nn-strmif-iamasyncreadertimestampscaling), [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) |
| Filter CLSID                             | CLSID\_URLReader                                                                                                                     |
| Property Page CLSID                      | No property page                                                                                                                     |
| Executable                               | quartz.dll                                                                                                                           |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                      |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                        |



 

## Remarks

This filter uses URLMon and supports code pages.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



