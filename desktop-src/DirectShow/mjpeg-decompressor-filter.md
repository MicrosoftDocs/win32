---
description: MJPEG Decompressor Filter
ms.assetid: 0862fd8c-7e64-4472-9405-4d8e31e4401f
title: MJPEG Decompressor Filter
ms.topic: article
ms.date: 05/31/2018
---

# MJPEG Decompressor Filter

This filter decodes a video stream from motion JPEG to uncompressed video. Some digital video cameras produce a motion JPEG video stream.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)                                                                                                                 |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_MJPG                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                             |
| Output Pin Media Types                   | MEDIATYPE\_VIDEO, MEDIASUBTYPE\_NULL                                                                                                               |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) |
| Filter CLSID                             | CLSID\_MjpegDec                                                                                                                                    |
| Property Page CLSID                      | No property page                                                                                                                                   |
| Executable                               | quartz.dll                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                                                                                      |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Remarks

This filter is compatible with motion JPEG video that uses the FOURCC code 'MJPG'. It cannot decode other varieties of motion JPEG. For these, you will need to use a third-party decoder filter.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



