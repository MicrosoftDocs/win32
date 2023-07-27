---
description: TV Tuner Filter
ms.assetid: a8e101dc-78ab-495f-9086-7b1d1e87c357
title: TV Tuner Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TV Tuner Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The TV Tuner filter selects an analog broadcast or cable channel to be viewed. The single output stream is a hardware path for analog baseband video. This output should connect to the Analog Video Crossbar filter. The input pins include an input for cable and an antenna input.



| Label | Value |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IAMTVTuner**](/windows/desktop/api/Strmif/nn-strmif-iamtvtuner), **ISpecifyPropertyPages**, **IPersistPropertyBag**, **IKsObject**, [**IKsPropertySet**](ikspropertyset.md) |
| Input Pin Media Types                    | Not applicable.                                                                                                                                                                   |
| Input Pin Interfaces                     | Not applicable.                                                                                                                                                                   |
| Output Pin Media Types                   | Video: MEDIATYPE\_AnalogVideo, KSDATAFORMAT\_SUBTYPE\_NONE Audio: MEDIATYPE\_AnalogAudio, MEDIASUBTYPE\_NULL                                                                      |
| Output Pin Interfaces                    | [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)                                                                                                                                                              |
| Filter CLSID                             | CLSID\_TVTunerFilter                                                                                                                                                              |
| Property Page CLSID                      | CLSID\_TVTunerFilterPropertyPage                                                                                                                                                  |
| Executable                               | KSTVTune.ax                                                                                                                                                                       |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                                               |
| [Filter Category](filter-categories.md) | AM\_KSCATEGORY\_TVTUNER                                                                                                                                                           |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



