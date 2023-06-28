---
description: VGA 16 Color Ditherer Filter
ms.assetid: 0a5f4e92-e703-4487-91b0-15265744004e
title: VGA 16 Color Ditherer Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VGA 16 Color Ditherer Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 



