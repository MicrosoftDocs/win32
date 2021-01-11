---
description: QuickTime Movie Parser Filter
ms.assetid: 9537dd7b-9aeb-4e73-a31d-86053874ef13
title: QuickTime Movie Parser Filter
ms.topic: article
ms.date: 05/31/2018
---

# QuickTime Movie Parser Filter

This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

The QuickTime Movie Parser filter splits Apple® QuickTime® data into audio and video streams. It supports QuickTime 2.0 and earlier. The input pin connects to a source filter such as the [Async File Source](file-source--async--filter.md) filter or the [URL File Source](file-source--url--filter.md) filter. The Parser uses the [AVI Decompressor](avi-decompressor-filter.md) or [QT Decompressor](qt-decompressor-filter.md) filter to decompress QuickTime files. The filter creates one output pin for the video stream and one output pin for the audio stream.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><a href="/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent"><strong>IAMMediaContent</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>MEDIATYPE_Stream, MEDIASUBTYPE_QTMovie;</td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td><ul>
<li>MEDIATYPE_Video, MEDIASUBTYPE_NULL, FORMAT_VideoInfo</li>
<li>MEDIATYPE_Audio, MEDIASUBTYPE_NULL, FORMAT_WaveFormatEx</li>
</ul></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td><a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_QuickTimeParser</td>
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

 

 



