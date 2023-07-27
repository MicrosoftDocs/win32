---
description: Analog Video Crossbar Filter
ms.assetid: 668f6a8b-a4ed-4e4a-956c-a87f165225fa
title: Analog Video Crossbar Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Analog Video Crossbar Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Analog Video Crossbar filter represents a video crossbar on a video capture device that supports the Windows Driver Model (WDM).

This filter is a wrapper filter for crossbars on WDM streaming devices. The filter's friendly name is taken from the device. Each output pin represents a hardware path for analog baseband video. One of the input pins comes from a TV Tuner (the [TV Tuner Filter](tv-tuner-filter.md)). Other input pins support video or audio streams. The filter supports any media subtypes and formats that are supported on the downstream connections.

You cannot directly create this filter with CoCreateInstance. The [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interface automatically adds this filter to the graph as needed.

For more information on wrapper filters and WDM streaming devices, see [How Hardware Devices Participate in the Filter Graph](how-hardware-devices-participate-in-the-filter-graph.md).



| Label | Value |
|------------------------------------------|------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMCrossbar**](/windows/desktop/api/Strmif/nn-strmif-iamcrossbar), ISpecifyPropertyPages, IPersistPropertyBag, IPersistStream |
| Input Pin Media Types                    | MEDIATYPE\_AnalogAudio, MEDIATYPE\_AnalogVideo                                                 |
| Input Pin Interfaces                     | [**IKsPropertySet**](ikspropertyset.md)                                                       |
| Output Pin Media Types                   | MEDIATYPE\_AnalogAudio, MEDIATYPE\_AnalogVideo                                                 |
| Output Pin Interfaces                    | [**IKsPropertySet**](ikspropertyset.md)                                                       |
| Filter CLSID                             | Not applicable                                                                                 |
| Property Page CLSID                      | CLSID\_CrossbarFilterPropertyPage                                                              |
| Executable                               | ksxbar.ax                                                                                      |
| [Merit](merit.md)                       | Driver-dependent.                                                                              |
| [Filter Category](filter-categories.md) | AM\_KSCATEGORY\_CROSSBAR                                                                       |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Working with Crossbars](working-with-crossbars.md)
</dt> </dl>

 

 



