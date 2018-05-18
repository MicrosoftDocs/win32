---
Description: MJPEG Decompressor Filter
ms.assetid: '0862fd8c-7e64-4472-9405-4d8e31e4401f'
title: MJPEG Decompressor Filter
---

# MJPEG Decompressor Filter

This filter decodes a video stream from motion JPEG to uncompressed video. Some digital video cameras produce a motion JPEG video stream.



|                                          |                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](ibasefilter.md)                                                                                                                 |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_MJPG                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                             |
| Output Pin Media Types                   | MEDIATYPE\_VIDEO, MEDIASUBTYPE\_NULL                                                                                                               |
| Output Pin Interfaces                    | [**IMediaPosition**](imediaposition.md), [**IMediaSeeking**](imediaseeking.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md) |
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

 

 



