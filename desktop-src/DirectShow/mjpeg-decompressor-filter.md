---
Description: MJPEG Decompressor Filter
ms.assetid: 0862fd8c-7e64-4472-9405-4d8e31e4401f
title: MJPEG Decompressor Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MJPEG Decompressor Filter

This filter decodes a video stream from motion JPEG to uncompressed video. Some digital video cameras produce a motion JPEG video stream.



|                                          |                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)                                                                                                                 |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_MJPG                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                             |
| Output Pin Media Types                   | MEDIATYPE\_VIDEO, MEDIASUBTYPE\_NULL                                                                                                               |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) |
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

 

 



