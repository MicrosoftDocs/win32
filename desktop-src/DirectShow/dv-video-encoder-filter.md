---
Description: DV Video Encoder Filter
ms.assetid: 'ac57bd11-de16-4a58-9f4b-da270a57ad08'
title: DV Video Encoder Filter
---

# DV Video Encoder Filter

This filter encodes an uncompressed video stream into digital video (DV). It provides a custom interface, [**IDVEnc**](idvenc.md), for setting the encoding resolution and format.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IAMVideoCompression</strong>](iamvideocompression.md), [<strong>IBaseFilter</strong>](ibasefilter.md), [<strong>IDVEnc</strong>](idvenc.md), [<strong>IDVRGB219</strong>](idvrgb219.md), <strong>IPersistStream</strong>, <strong>ISpecifyPropertyPages</strong></td>
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
<td>[<strong>IMemInputPin</strong>](imeminputpin.md), [<strong>IPin</strong>](ipin.md), [<strong>IQualityControl</strong>](iqualitycontrol.md)</td>
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
<td>[<strong>IMediaPosition</strong>](imediaposition.md), [<strong>IMediaSeeking</strong>](imediaseeking.md), [<strong>IPin</strong>](ipin.md), [<strong>IQualityControl</strong>](iqualitycontrol.md)</td>
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

 

 




