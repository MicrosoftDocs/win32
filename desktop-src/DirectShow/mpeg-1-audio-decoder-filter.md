---
Description: MPEG-1 Audio Decoder Filter
ms.assetid: 2f695ac6-7d4b-41a8-b4c5-83fb9d20ab9d
title: MPEG-1 Audio Decoder Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MPEG-1 Audio Decoder Filter

Decodes MPEG-1 Layer I and Layer II audio to PCM.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), <strong>ISpecifyPropertyPages</strong></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>MEDIATYPE_Audio, FORMAT_WaveFormatEx<br/> The following subtypes are valid:<br/>
<ul>
<li>MEDIASUBTYPE_MPEG1Packet</li>
<li>MEDIASUBTYPE_MPEG1Payload</li>
<li>MEDIASUBTYPE_MPEG1AudioPayload</li>
<li>GUID_NULL</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>MEDIATYPE_Audio, MEDIASUBTYPE_PCM</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IMediaPosition</strong>](/windows/win32/Control/nn-control-imediaposition?branch=master), [<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_CMpegAudioCodec</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>CLSID_MpegAudioDecoderPropertyPage</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>quartz.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>0x03680001</td>
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

 

 




