---
description: MPEG-2 Splitter
ms.assetid: 06704a5a-e7ae-4187-ae36-32512d951aaf
title: MPEG-2 Splitter
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-2 Splitter

Starting in Microsoft® Windows® XP, the MPEG-2 Splitter filter is deprecated. Use the [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) instead.

On earlier platforms, use the MPEG-2 Splitter for MPEG-2 program streams delivered in pull mode that contain at least one of the following stream types: MPEG-2 video; MPEG-2 audio; AC3 audio encoded as defined for DVD video; or PCM audio encoded as defined for DVD video. This filter parses the streams, creates an output pin for each stream, and outputs the compressed MPEG audio or video packets to an MPEG-2 decoder filter.

For program and transport streams delivered in push-mode, use the [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md), on all platforms.

> [!Note]  
> The MPEG-2 Splitter does not support frame-accurate seeking.

 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, <strong>ISpecifyPropertyPages</strong>, <a href="/previous-versions/windows/desktop/api/Amparse/nn-amparse-iamparse"><strong>IAMParse</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iamstreamselect"><strong>IAMStreamSelect</strong></a></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td><ul>
<li>MEDIATYPE_Stream, MEDIASUBTYPE_MPEG2_PROGRAM</li>
<li>MEDIATYPE_Stream, MEDIASUBTYPE_MPEG1_Video</li>
<li>MEDIATYPE_Stream, MEDIASUBTYPE_NULL</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Depends on the stream type. See <a href="mpeg-2-splitter-media-types.md">MPEG-2 Splitter Media Types</a></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_MMSPLITTER</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>mpg2splt.ax</td>
</tr>
<tr class="odd">
<td><a href="merit.md">Merit</a></td>
<td>MERIT_NORMAL + 1</td>
</tr>
<tr class="even">
<td><a href="filter-categories.md">Filter Category</a></td>
<td>CLSID_AudioInputDeviceCategory</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Using the MPEG-2 Splitter](using-the-mpeg-2-splitter.md)
</dt> </dl>

 

 



