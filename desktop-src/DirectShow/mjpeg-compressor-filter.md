---
Description: MJPEG Compressor Filter
ms.assetid: 'de30a2c4-3e51-4f2b-b3f9-ed78e2d6512d'
title: MJPEG Compressor Filter
---

# MJPEG Compressor Filter

This filter compresses an uncompressed video stream, using motion JPEG compression.



|                                          |                                                                                                                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](ibasefilter.md), **IPersistStream**                                                                                                                                                                                             |
| Input Pin Media Types                    | MEDIATYPE\_VIDEO, MEDIASUBTYPE\_NULL                                                                                                                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                                                                                                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_MJPG                                                                                                                                                                                                               |
| Output Pin Interfaces                    | [**IAMStreamConfig**](iamstreamconfig.md), [**IAMVideoCompression**](iamvideocompression.md), [**IMediaPosition**](imediaposition.md), [**IMediaSeeking**](imediaseeking.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md) |
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

 

 



