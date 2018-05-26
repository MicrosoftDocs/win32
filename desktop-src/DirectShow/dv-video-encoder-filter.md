---
Description: DV Video Encoder Filter
ms.assetid: ac57bd11-de16-4a58-9f4b-da270a57ad08
title: DV Video Encoder Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DV Video Encoder Filter

This filter encodes an uncompressed video stream into digital video (DV). It provides a custom interface, [**IDVEnc**](/windows/win32/Strmif/nn-strmif-idvenc?branch=master), for setting the encoding resolution and format.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IAMVideoCompression</strong>](/windows/win32/Strmif/nn-strmif-iamvideocompression?branch=master), [<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [<strong>IDVEnc</strong>](/windows/win32/Strmif/nn-strmif-idvenc?branch=master), [<strong>IDVRGB219</strong>](/windows/win32/Strmif/nn-strmif-idvrgb219?branch=master), <strong>IPersistStream</strong>, <strong>ISpecifyPropertyPages</strong></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td><ul>
<li>Major type: MEDIATYPE_VideoThe following subtypes are valid:<br/>
<ul>
<li>MEDIASUBTYPE_RGB24</li>
<li>MEDIASUBTYPE_RGB565</li>
<li>MEDIASUBTYPE_RGB555</li>
</ul></li>
<li>Format type: FORMAT_VideoInfo</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td><ul>
<li>Major type: MEDIATYPE_Video</li>
<li>Subtype: MEDIASUBTYPE_dvsd</li>
<li>Format type: FORMAT_VideoInfo</li>
</ul></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IMediaPosition</strong>](/windows/win32/Control/nn-control-imediaposition?branch=master), [<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_DVVideoEnc</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>CLSID_DVEncPropertiesPage</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>qdv.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>MERIT_DO_NOT_USE</td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td>CLSID_VideoCompressorCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

For 16-bit video (MEDIASUBTYPE\_RGB555 or MEDIASUBTYPE\_RGB565), the input must be 720 x 480 pixels for NTSC, or 720 x 576 pixels for PAL. For 24-bit video, there are no size constraints on the input.

The output is always 720 x 480 for NTSC or 720 x 576 for PAL; 24-bit video is scaled to fit these dimensions.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> </dl>

 

 




