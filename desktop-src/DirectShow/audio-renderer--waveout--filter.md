---
Description: Audio Renderer (WaveOut) Filter
ms.assetid: a3f2776b-974b-4886-82a3-38e00b607a07
title: Audio Renderer (WaveOut) Filter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Audio Renderer (WaveOut) Filter

This filter uses the waveOut\* API to render waveform audio. However, the [DirectSound Renderer Filter](directsound-renderer-filter.md) provides the same functionality using DirectSound. By default, the Filter Graph Manager uses the DirectSound Renderer instead of this filter. Audio mixing is disabled in the waveOut Audio Renderer, so if you need to mix multiple audio streams during playback, use the DirectSound renderer.

This filter does not check the audio stream's subtype. The [**WAVEFORMAT**](https://msdn.microsoft.com/library/windows/desktop/dd757712) or [**WAVEFORMATEX**](https://www.bing.com/search?q=**WAVEFORMATEX**) structure passed in the format contains the information needed for the connection.

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
<li>[<strong>IAMAudioRendererStats</strong>](/windows/desktop/api/Strmif/nn-strmif-iamaudiorendererstats)</li>
<li>[<strong>IAMClockSlave</strong>](/windows/desktop/api/Strmif/nn-strmif-iamclockslave)</li>
<li>[<strong>IAMDirectSound</strong>](/windows/desktop/api/Amaudio/nn-amaudio-iamdirectsound)</li>
<li>[<strong>IAMResourceControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iamresourcecontrol)</li>
<li>[<strong>IBaseFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)</li>
<li>[<strong>IBasicAudio</strong>](/windows/desktop/api/Control/nn-control-ibasicaudio)</li>
<li>[<strong>IMediaPosition</strong>](/windows/desktop/api/Control/nn-control-imediaposition)</li>
<li>[<strong>IMediaSeeking</strong>](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)</li>
<li>IPersistPropertyBag</li>
<li>IPersistStream</li>
<li>[<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)</li>
<li>[<strong>IReferenceClock</strong>](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock)</li>
</ul></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td><strong>MEDIATYPE_Audio</strong></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><ul>
<li>[<strong>IMemInputPin</strong>](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)</li>
<li>[<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin)</li>
<li>[<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)</li>
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

 

 



