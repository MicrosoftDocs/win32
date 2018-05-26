---
Description: VGA 16 Color Ditherer Filter
ms.assetid: 0a5f4e92-e703-4487-91b0-15265744004e
title: VGA 16 Color Ditherer Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VGA 16 Color Ditherer Filter

The VGA 16 Color Ditherer filter converts from an RGB color type to a 4-bit color display so that AVI and MPEG video streams may be displayed on older 16-color monitors. This filter is inserted in the graph between a decompressor filter and a video renderer filter.



|                                          |                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)                                                                                                                 |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_RGB8                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_RGB4                                                                                                               |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) |
| Filter CLSID                             | CLSID\_Dither                                                                                                                                      |
| Property Page CLSID                      | No property page.                                                                                                                                  |
| Executable                               | quartz.dll                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                                    |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



