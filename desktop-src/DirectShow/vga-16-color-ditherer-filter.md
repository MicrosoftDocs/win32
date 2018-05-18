---
Description: VGA 16 Color Ditherer Filter
ms.assetid: '0a5f4e92-e703-4487-91b0-15265744004e'
title: VGA 16 Color Ditherer Filter
---

# VGA 16 Color Ditherer Filter

The VGA 16 Color Ditherer filter converts from an RGB color type to a 4-bit color display so that AVI and MPEG video streams may be displayed on older 16-color monitors. This filter is inserted in the graph between a decompressor filter and a video renderer filter.



|                                          |                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](ibasefilter.md)                                                                                                                 |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_RGB8                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_RGB4                                                                                                               |
| Output Pin Interfaces                    | [**IMediaPosition**](imediaposition.md), [**IMediaSeeking**](imediaseeking.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md) |
| Filter CLSID                             | CLSID\_Dither                                                                                                                                      |
| Property Page CLSID                      | No property page.                                                                                                                                  |
| Executable                               | quartz.dll                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                                    |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



