---
Description: DVD Navigator Filter
ms.assetid: '3b2c01a2-d52c-4497-8fc9-d1113e8507e8'
title: DVD Navigator Filter
---

# DVD Navigator Filter

The DVD Navigator filter is the source filter for a DVD-Video playback filter graph. It opens all necessary files in a DVD-Video volume, navigates through the linear DVD-Video .vob files, and parses the resulting MPEG-2 program stream, splitting the stream into three (video, audio, subpicture) output pins.

The DVD Navigator filter also implements the [**IDvdControl2**](idvdcontrol2.md) and [**IDvdInfo2**](idvdinfo2.md) interfaces that enable a DVD playback application to control DVD-Video playback.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IBaseFilter</strong>](ibasefilter.md), [<strong>IDvdControl2</strong>](idvdcontrol2.md), [<strong>IDvdInfo2</strong>](idvdinfo2.md), [<strong>IFileSourceFilter</strong>](ifilesourcefilter.md), <strong>ISpecifyPropertyPages</strong></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>MEDIATYPE_Stream, MEDIASUBTYPE_MPEG2_PROGRAM</td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>Not applicable.</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Base types:<br/>
<ul>
<li>Video: <strong>MEDIATYPE_DVD_ENCRYPTED_PACK</strong>, <strong>MEDIASUBTYPE_MPEG2_VIDEO</strong></li>
<li>Audio: <strong>MEDIATYPE_DVD_ENCRYPTED_PACK</strong>, <strong>MEDIASUBTYPE_DOLBY_AC3</strong></li>
<li>Subpicture: <strong>MEDIATYPE_DVD_ENCRYPTED_PACK</strong>, <strong>MEDIASUBTYPE_DVD_SUBPICTURE</strong></li>
</ul>
Extended types:<br/> Video:<br/>
<ul>
<li><strong>MEDIATYPE_DVD_ENCRYPTED_PACK</strong>, <strong>MEDIASUBTYPE_MPEG2_VIDEO</strong></li>
<li><strong>MEDIATYPE_Video</strong>, <strong>MEDIASUBTYPE_MPEG2_VIDEO</strong></li>
<li><strong>MEDIATYPE_MPEG2_PES</strong>, <strong>MEDIASUBTYPE_MPEG2_VIDEO</strong></li>
</ul>
Audio:<br/>
<ul>
<li><strong>MEDIATYPE_DVD_ENCRYPTED_PACK</strong>, <strong>MEDIASUBTYPE_DOLBY_AC3</strong></li>
<li><strong>MEDIATYPE_Audio</strong>, <strong>MEDIASUBTYPE_DOLBY_AC3</strong></li>
<li><strong>MEDIATYPE_MPEG2_PES</strong>, <strong>MEDIASUBTYPE_DOLBY_AC3</strong></li>
</ul>
Subpicture:<br/>
<ul>
<li><strong>MEDIATYPE_DVD_ENCRYPTED_PACK</strong>, <strong>MEDIASUBTYPE_DVD_SUBPICTURE</strong></li>
<li><strong>MEDIATYPE_Video</strong>, <strong>MEDIASUBTYPE_DVD_SUBPICTURE</strong></li>
<li><strong>MEDIATYPE_MPEG2_PES</strong>, <strong>MEDIASUBTYPE_DVD_SUBPICTURE</strong></li>
</ul>
To enable the extended types, call [<strong>IDvdControl2::SetOption</strong>](idvdcontrol2-setoption.md) and set the <br/></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IPin</strong>](ipin.md), [<strong>IQualityControl</strong>](iqualitycontrol.md)</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_DVDNavigator</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>No property page.</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>qdvd.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>MERIT_DO_NOT_USE</td>
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
</dt> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 




