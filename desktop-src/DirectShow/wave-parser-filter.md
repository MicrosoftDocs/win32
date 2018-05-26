---
Description: WAVE Parser Filter
ms.assetid: 53a9538d-7a79-40bb-9468-d710eb238925
title: WAVE Parser Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WAVE Parser Filter

The WAVE Parser filter parses WAV-format audio data from .wav, .au, or .aif files. The upstream filter must be the [Async File Source](file-source--async--filter.md) filter, [URL File Source](file-source--url--filter.md) filter, or a compatible third-party asynchronous source filter that contains WAV audio data. The output stream is audio data, which you can connect directly to an audio rendering filter or to an intervening audio transform filter.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IAMMediaContent</strong>](/windows/win32/Qnetwork/nn-qnetwork-iammediacontent?branch=master), [<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [<strong>IPersistMediaPropertyBag</strong>](/windows/win32/Strmif/nn-strmif-ipersistmediapropertybag?branch=master)</td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Major type: MEDIATYPE_StreamThe following subtypes are valid:<br/>
<ul>
<li>MEDIASUBTYPE_AIFF</li>
<li>MEDIASUBTYPE_AU</li>
<li>MEDIASUBTYPE_WAVE</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Major type: MEDIATYPE_AudioSubtype: MEDIASUBTYPE_PCM or other compression type. (See [<strong>Audio Subtypes</strong>](audio-subtypes.md).)<br/> Format type: FORMAT_WaveFormatEx<br/></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master)</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>{D51BD5A1-7548-11cf-A520-0080C77EF58A}</td>
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



 

## Remarks

This filter supports the following file types:

-   WAVE (.wav)
-   AIFF and AIFF-C (.aif)
-   AU (.au)

However, it has the following limitations on the audio format:

-   The audio must be 8-bit or 16-bit linear PCM.
-   For AIFF-C files, the audio must be uncompressed, in big-endian byte order (compression type 'NONE').

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




