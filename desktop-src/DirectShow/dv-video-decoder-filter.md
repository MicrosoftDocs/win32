---
Description: DV Video Decoder Filter
ms.assetid: aa47010e-8510-475d-836a-cb63deeb3a7b
title: DV Video Decoder Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DV Video Decoder Filter

This filter decodes a digital video (DV) stream into uncompressed video.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [<strong>IDVRGB219</strong>](/windows/win32/Strmif/nn-strmif-idvrgb219?branch=master), [<strong>IIPDVDec</strong>](/windows/win32/Strmif/nn-strmif-iipdvdec?branch=master), <strong>IPersistStream</strong>, <strong>ISpecifyPropertyPages</strong></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td><ul>
<li>MEDIATYPE_Video</li>
<li>MEDIASUBTYPE_dvsd</li>
<li>FORMAT_VideoInfo, FORMAT_DvInfo</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td><strong>Major type</strong>: MEDIATYPE_Video<strong>Subtypes</strong>:<br/>
<ul>
<li>MEDIASUBTYPE_YUY2</li>
<li>MEDIASUBTYPE_UYVY</li>
<li>MEDIASUBTYPE_RGB24</li>
<li>MEDIASUBTYPE_RGB32</li>
<li>MEDIASUBTYPE_ARGB32</li>
<li>MEDIASUBTYPE_RGB565</li>
<li>MEDIASUBTYPE_RGB555</li>
<li>MEDIASUBTYPE_RGB8</li>
<li>MEDIASUBTYPE_Y41P</li>
</ul>
<strong>Format types</strong>:<br/> Format_VideoInfo, Format_VideoInfo2<br/></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IMediaPosition</strong>](/windows/win32/Control/nn-control-imediaposition?branch=master), [<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_DVVideoCodec</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>CLSID_DVDecPropertiesPage</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>qdv.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>MERIT_NORMAL</td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

Use the [**IIPDVDec**](/windows/win32/Strmif/nn-strmif-iipdvdec?branch=master) interface to set the decoding resolution to full, half size, quarter size, or one-eighth size.

**Interlacing**: Earlier versions of the decoder always deinterlace the video. As of DirectX 9.0, the DV Video Decoder can preserve the interlacing. This enables the interlaced video to be deinterlaced by the Video Mixing Renderer (VMR), for improved rendering quality. To use this feature, the downstream filter must support [**VIDEOINFOHEADER2**](/windows/win32/Dvdmedia/ns-dvdmedia-tagvideoinfoheader2?branch=master) formats, indicated by that value Format\_VideoInfo2 in the **formattype** member of the [**AM\_MEDIA\_TYPE**](/windows/win32/strmif/ns-strmif-_ammediatype?branch=master) structure. At full resolution output, the deinterlacing flags (**dwInterlace**) in the **VIDEOINFOHEADER2** structure are set to `AMINTERLACE_IsInterlaced | AMINTERLACE_DisplayModeBobOrWeave`, indicating interlaced fields. At half resolution or lower, **dwInterlace** is set to zero, indicating progressive frames.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> </dl>

 

 




