---
Description: AVI Draw Filter
ms.assetid: 86cd8e48-7cfa-46e4-b8f4-609b4d09fe80
title: AVI Draw Filter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AVI Draw Filter

The AVI Draw filter is pulled automatically into a playback graph instead of the [AVI Decompressor](avi-decompressor-filter.md) when video is being output to an external NTSC television monitor.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IBaseFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)</td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Major Type: MEDIATYPE_VideoSubtypes:<br/>
<ul>
<li>MEDIASUBTYPE_MJPG</li>
<li>MEDIASUBTYPE_TVMJ</li>
<li>MEDIASUBTYPE_WAKE</li>
<li>MEDIASUBTYPE_CFCC</li>
<li>MEDIASUBTYPE_IJPG</li>
<li>MEDIASUBTYPE_Plum</li>
<li>MEDIASUBTYPE_DVCS</li>
<li>MEDIASUBTYPE_DVSD</li>
<li>MEDIASUBTYPE_MDVF</li>
<li>Format type: FORMAT_VideoInfo</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IMemInputPin</strong>](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin), [<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>MEDIATYPE_Video, MEDIASUBTYPE_NULL</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IMediaPosition</strong>](/windows/desktop/api/Control/nn-control-imediaposition), [<strong>IMediaSeeking</strong>](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [<strong>IOverlayNotify</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlaynotify), [<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin), [<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_AVIDraw</td>
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
<td>MERIT_NORMAL + 100</td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

Since the AVI Draw filter and the [VFW Capture Filter](vfw-capture-filter.md) both connect to the same hardware, they cannot be in the same filter graph.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




