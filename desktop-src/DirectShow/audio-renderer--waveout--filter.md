---
Description: Audio Renderer (WaveOut) Filter
ms.assetid: a3f2776b-974b-4886-82a3-38e00b607a07
title: Audio Renderer (WaveOut) Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Renderer (WaveOut) Filter

This filter uses the waveOut\* API to render waveform audio. However, the [DirectSound Renderer Filter](directsound-renderer-filter.md) provides the same functionality using DirectSound. By default, the Filter Graph Manager uses the DirectSound Renderer instead of this filter. Audio mixing is disabled in the waveOut Audio Renderer, so if you need to mix multiple audio streams during playback, use the DirectSound renderer.

This filter does not check the audio stream's subtype. The [**WAVEFORMAT**](https://msdn.microsoft.com/library/windows/desktop/dd757712) or [**WAVEFORMATEX**](/windows/win32/mmreg/?branch=master) structure passed in the format contains the information needed for the connection.

This filter supports a range of sample rates that depends on the audio driver.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><ul>
<li>[<strong>IAMAudioRendererStats</strong>](/windows/win32/Strmif/nn-strmif-iamaudiorendererstats?branch=master)</li>
<li>[<strong>IAMClockSlave</strong>](/windows/win32/Strmif/nn-strmif-iamclockslave?branch=master)</li>
<li>[<strong>IAMDirectSound</strong>](/windows/win32/Amaudio/nn-amaudio-iamdirectsound?branch=master)</li>
<li>[<strong>IAMResourceControl</strong>](/windows/win32/Strmif/nn-strmif-iamresourcecontrol?branch=master)</li>
<li>[<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)</li>
<li>[<strong>IBasicAudio</strong>](/windows/win32/Control/nn-control-ibasicaudio?branch=master)</li>
<li>[<strong>IMediaPosition</strong>](/windows/win32/Control/nn-control-imediaposition?branch=master)</li>
<li>[<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master)</li>
<li>IPersistPropertyBag</li>
<li>IPersistStream</li>
<li>[<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</li>
<li>[<strong>IReferenceClock</strong>](/windows/win32/Strmif/nn-strmif-ireferenceclock?branch=master)</li>
</ul></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td><strong>MEDIATYPE_Audio</strong></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><ul>
<li>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master)</li>
<li>[<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master)</li>
<li>[<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</li>
</ul></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Not applicable.</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>Not applicable.</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td><strong>CLSID_AudioRender</strong></td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td><strong>CLSID_AudioProperties</strong>, <strong>CLSID_AudioRendererAdvancedProperties</strong></td>
</tr>
<tr class="even">
<td>Executable</td>
<td>quartz.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td><strong>CLSID_AudioRendererCategory</strong></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



