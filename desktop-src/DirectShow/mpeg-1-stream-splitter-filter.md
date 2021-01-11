---
description: MPEG-1 Stream Splitter Filter
ms.assetid: abadf37f-2876-496d-90e7-77c3475a0064
title: MPEG-1 Stream Splitter Filter
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-1 Stream Splitter Filter

This filter splits an MPEG-1 system stream into its component audio and video streams.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><a href="/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent"><strong>IAMMediaContent</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iamstreamselect"><strong>IAMStreamSelect</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Major type: MEDIATYPE_Stream<br/> Subtypes:<br/>
<ul>
<li>MEDIASUBTYPE_MPEG1System</li>
<li>MEDIASUBTYPE_MPEG1VideoCD</li>
<li>MEDIASUBTYPE_Audio</li>
<li>MEDIASUBTYPE_Video</li>
</ul>
See <a href="mpeg-1-media-types.md"><strong>MPEG-1 Media Types</strong></a><br/></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Major type: MEDIATYPE_Audio or MEDIATYPE_Video<br/> Subtype: MEDIASUBTYPE_MPEG1Payload or MEDIASUBTYPE_MPEG1Packet<br/> See <a href="mpeg-1-media-types.md"><strong>MPEG-1 Media Types</strong></a><br/></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_MPEG1Splitter</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>No property page</td>
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



 

## Remarks

This file supports pull mode via [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) only; it does not support push mode.

Because MPEG-1 content is not indexed, seeking can be very approximate. It is usually good for a fixed bitrate MPEG-1 system stream (which is usually hardware generated for video CD).

The filter supports the [**IAMMediaContent**](/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent) interface for retrieving ID3 metadata.

Not all MPEG samples have time stamps. The lack of a time stamp on an MPEG sample is not an error. For filter developers, this means that you should not return an error code from your input pin's **Receive** method if [**IMediaSample::GetTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-gettime) fails. If **Receive** returns any value other than S\_OK, it will cause the splitter to stop sending samples.

If the file contains a video stream, the MPEG-1 Stream Splitter supports seeking by frame number. To enable frame-based seeking, call [**IMediaSeeking::SetTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-settimeformat) on the [Filter Graph Manager](filter-graph-manager.md) with the value **TIME\_FORMAT\_FRAME**.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




