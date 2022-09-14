---
description: TV Tuner Filter
ms.assetid: a8e101dc-78ab-495f-9086-7b1d1e87c357
title: TV Tuner Filter
ms.topic: article
ms.date: 05/31/2018
---

# TV Tuner Filter

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

 

 



