---
description: DV Video Encoder Filter
ms.assetid: ac57bd11-de16-4a58-9f4b-da270a57ad08
title: DV Video Encoder Filter
ms.topic: article
ms.date: 05/31/2018
---

# DV Video Encoder Filter

This filter encodes an uncompressed video stream into digital video (DV). It provides a custom interface, [**IDVEnc**](/windows/desktop/api/Strmif/nn-strmif-idvenc), for setting the encoding resolution and format.




| 
|
| Filter Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-iamvideocompression"><strong>IAMVideoCompression</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-idvenc"><strong>IDVEnc</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-idvrgb219"><strong>IDVRGB219</strong></a>, <strong>IPersistStream</strong>, <strong>ISpecifyPropertyPages</strong> | 
| Input Pin Media Types | <ul><li>Major type: MEDIATYPE_VideoThe following subtypes are valid:<br /><ul><li>MEDIASUBTYPE_RGB24</li><li>MEDIASUBTYPE_RGB565</li><li>MEDIASUBTYPE_RGB555</li></ul></li><li>Format type: FORMAT_VideoInfo</li></ul> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | <ul><li>Major type: MEDIATYPE_Video</li><li>Subtype: MEDIASUBTYPE_dvsd</li><li>Format type: FORMAT_VideoInfo</li></ul> | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_DVVideoEnc | 
| Property Page CLSID | CLSID_DVEncPropertiesPage | 
| Executable | qdv.dll | 
| <a href="merit.md">Merit</a> | MERIT_DO_NOT_USE | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_VideoCompressorCategory | 




 

## Remarks

For 16-bit video (MEDIASUBTYPE\_RGB555 or MEDIASUBTYPE\_RGB565), the input must be 720 x 480 pixels for NTSC, or 720 x 576 pixels for PAL. For 24-bit video, there are no size constraints on the input.

The output is always 720 x 480 for NTSC or 720 x 576 for PAL; 24-bit video is scaled to fit these dimensions.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> </dl>

 

 




