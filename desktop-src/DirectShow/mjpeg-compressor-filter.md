---
Description: MJPEG Compressor Filter
ms.assetid: de30a2c4-3e51-4f2b-b3f9-ed78e2d6512d
title: MJPEG Compressor Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MJPEG Compressor Filter

This filter compresses an uncompressed video stream, using motion JPEG compression.



|                                          |                                                                                                                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), **IPersistStream**                                                                                                                                                                                             |
| Input Pin Media Types                    | MEDIATYPE\_VIDEO, MEDIASUBTYPE\_NULL                                                                                                                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                                                                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_MJPG                                                                                                                                                                                                               |
| Output Pin Interfaces                    | [**IAMStreamConfig**](/windows/win32/Strmif/nn-strmif-iamstreamconfig?branch=master), [**IAMVideoCompression**](/windows/win32/Strmif/nn-strmif-iamvideocompression?branch=master), [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) |
| Filter CLSID                             | CLSID\_MJPGEnc                                                                                                                                                                                                                                     |
| Property Page CLSID                      | No property page                                                                                                                                                                                                                                   |
| Executable                               | quartz.dll                                                                                                                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                                                                                                                |
| [Filter Category](filter-categories.md) | CLSID\_VideoCompressorCategory                                                                                                                                                                                                                     |



 

## Remarks

This filter encodes using the media subtype MEDIASUBTYPE\_MJPG, which corresponds to the FOURCC code 'MJPG'.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



