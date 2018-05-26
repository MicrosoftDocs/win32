---
Description: Color Space Converter Filter
ms.assetid: a6765184-43ce-47b8-9eb1-e15af7e11c93
title: Color Space Converter Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Color Space Converter Filter

This transform filter converts from one RGB color type to another RGB type, such as between 24-bit and 8-bit RGB color. Since this type of conversion is generally handled more efficiently within a video decompressor, the main use of the Color Space Converter is when the stream source consists of uncompressed RGB frames.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)</td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>MEDIATYPE_Video, FORMAT_VideoInfo.<br/> The following subtypes are valid:<br/>
<ul>
<li>MEDIASUBTYPE_RGB8</li>
<li>MEDIASUBTYPE_RGB555</li>
<li>MEDIASUBTYPE_RGB565</li>
<li>MEDIASUBTYPE_RGB24</li>
<li>MEDIASUBTYPE_RGB32</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>MEDIATYPE_Video, FORMAT_VideoInfo.<br/> The following subtypes are valid:<br/>
<ul>
<li>MEDIASUBTYPE_RGB8</li>
<li>MEDIASUBTYPE_RGB555</li>
<li>MEDIASUBTYPE_RGB565</li>
<li>MEDIASUBTYPE_RGB24</li>
<li>MEDIASUBTYPE_RGB32</li>
</ul></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IMediaPosition</strong>](/windows/win32/Control/nn-control-imediaposition?branch=master), [<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_Colour</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>No property page.</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>quartz.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>MERIT_UNLIKELY</td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




