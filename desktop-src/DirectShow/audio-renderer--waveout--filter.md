---
description: Audio Renderer (WaveOut) Filter
ms.assetid: a3f2776b-974b-4886-82a3-38e00b607a07
title: Audio Renderer (WaveOut) Filter
ms.topic: article
ms.date: 05/31/2018
---

# Audio Renderer (WaveOut) Filter

This filter uses the waveOut\* API to render waveform audio. However, the [DirectSound Renderer Filter](directsound-renderer-filter.md) provides the same functionality using DirectSound. By default, the Filter Graph Manager uses the DirectSound Renderer instead of this filter. Audio mixing is disabled in the waveOut Audio Renderer, so if you need to mix multiple audio streams during playback, use the DirectSound renderer.

This filter does not check the audio stream's subtype. The [**WAVEFORMAT**](/windows/win32/api/mmreg/ns-mmreg-waveformat) or [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure passed in the format contains the information needed for the connection.

This filter supports a range of sample rates that depends on the audio driver.




| 
|
| Filter Interfaces | <ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-iamaudiorendererstats"><strong>IAMAudioRendererStats</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-iamclockslave"><strong>IAMClockSlave</strong></a></li><li><a href="/previous-versions/windows/desktop/api/Amaudio/nn-amaudio-iamdirectsound"><strong>IAMDirectSound</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-iamresourcecontrol"><strong>IAMResourceControl</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></li><li><a href="/windows/desktop/api/Control/nn-control-ibasicaudio"><strong>IBasicAudio</strong></a></li><li><a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a></li><li>IPersistPropertyBag</li><li>IPersistStream</li><li><a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ireferenceclock"><strong>IReferenceClock</strong></a></li></ul> | 
| Input Pin Media Types | <strong>MEDIATYPE_Audio</strong> | 
| Input Pin Interfaces | <ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></li></ul> | 
| Output Pin Media Types | Not applicable. | 
| Output Pin Interfaces | Not applicable. | 
| Filter CLSID | <strong>CLSID_AudioRender</strong> | 
| Property Page CLSID | <strong>CLSID_AudioProperties</strong>, <strong>CLSID_AudioRendererAdvancedProperties</strong> | 
| Executable | quartz.dll | 
| <a href="merit.md">Merit</a> | <strong>MERIT_DO_NOT_USE</strong> | 
| <a href="filter-categories.md">Filter Category</a> | <strong>CLSID_AudioRendererCategory</strong> | 




 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 
