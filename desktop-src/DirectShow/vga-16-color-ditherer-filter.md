---
description: VGA 16 Color Ditherer Filter
ms.assetid: 0a5f4e92-e703-4487-91b0-15265744004e
title: VGA 16 Color Ditherer Filter
ms.topic: article
ms.date: 05/31/2018
---

# VGA 16 Color Ditherer Filter

The VGA 16 Color Ditherer filter converts from an RGB color type to a 4-bit color display so that AVI and MPEG video streams may be displayed on older 16-color monitors. This filter is inserted in the graph between a decompressor filter and a video renderer filter.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)                                                                                                                 |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_RGB8                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_RGB4                                                                                                               |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) |
| Filter CLSID                             | CLSID\_Dither                                                                                                                                      |
| Property Page CLSID                      | No property page.                                                                                                                                  |
| Executable                               | quartz.dll                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                                    |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



