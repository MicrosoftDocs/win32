---
description: QT Decompressor Filter
ms.assetid: d013075f-deab-40ef-8438-4fb09820da3e
title: QT Decompressor Filter
ms.topic: article
ms.date: 05/31/2018
---

# QT Decompressor Filter

This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

The QT Decompressor filter decompresses Apple® QuickTime® 2.0 video. This format is typically used in older QuickTime files.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>MEDIATYPE_Video, FORMAT_VideoInfo<br/> The following subtypes are valid:<br/>
<ul>
<li>MEDIASUBTYPE_QTRpza</li>
<li>MEDIASUBTYPE_QTSmc</li>
<li>MEDIASUBTYPE_QTRle</li>
<li>MEDIASUBTYPE_QTJpeg</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>MEDIATYPE_Video, MEDIASUBTYPE_NULL, FORMAT_VideoInfo</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td><a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_QTDec</td>
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
<td><a href="merit.md">Merit</a></td>
<td>MERIT_NORMAL</td>
</tr>
<tr class="even">
<td><a href="filter-categories.md">Filter Category</a></td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




