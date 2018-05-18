---
Description: 'Audio Renderer (WaveOut) Filter'
ms.assetid: 'a3f2776b-974b-4886-82a3-38e00b607a07'
title: 'Audio Renderer (WaveOut) Filter'
---

# Audio Renderer (WaveOut) Filter

This filter uses the waveOut\* API to render waveform audio. However, the [DirectSound Renderer Filter](directsound-renderer-filter.md) provides the same functionality using DirectSound. By default, the Filter Graph Manager uses the DirectSound Renderer instead of this filter. Audio mixing is disabled in the waveOut Audio Renderer, so if you need to mix multiple audio streams during playback, use the DirectSound renderer.

This filter does not check the audio stream's subtype. The [**WAVEFORMAT**](https://msdn.microsoft.com/library/windows/desktop/dd757712) or [**WAVEFORMATEX**](waveformatex.md) structure passed in the format contains the information needed for the connection.

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
<li>[<strong>IAMAudioRendererStats</strong>](iamaudiorendererstats.md)</li>
<li>[<strong>IAMClockSlave</strong>](iamclockslave.md)</li>
<li>[<strong>IAMDirectSound</strong>](iamdirectsound.md)</li>
<li>[<strong>IAMResourceControl</strong>](iamresourcecontrol.md)</li>
<li>[<strong>IBaseFilter</strong>](ibasefilter.md)</li>
<li>[<strong>IBasicAudio</strong>](ibasicaudio.md)</li>
<li>[<strong>IMediaPosition</strong>](imediaposition.md)</li>
<li>[<strong>IMediaSeeking</strong>](imediaseeking.md)</li>
<li>IPersistPropertyBag</li>
<li>IPersistStream</li>
<li>[<strong>IQualityControl</strong>](iqualitycontrol.md)</li>
<li>[<strong>IReferenceClock</strong>](ireferenceclock.md)</li>
</ul></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td><strong>MEDIATYPE_Audio</strong></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><ul>
<li>[<strong>IMemInputPin</strong>](imeminputpin.md)</li>
<li>[<strong>IPin</strong>](ipin.md)</li>
<li>[<strong>IQualityControl</strong>](iqualitycontrol.md)</li>
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

 

 



