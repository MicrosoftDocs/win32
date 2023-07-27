---
description: Audio Capture Filter
ms.assetid: 'f76d5c82-33b2-4579-9420-8f97eca53ede'
title: Audio Capture Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Capture Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Audio Capture filter represents an audio capture device. It has one capture output pin and several input pins (one for each type of input on the card, such as Line In, Mic, CD, and MIDI).

This filter can work with more than one hardware device, so calling CoCreateInstance to create the filter does not work. Instead, use the [System Device Enumerator](system-device-enumerator.md). The System Device Enumerator returns a unique moniker for each device. The moniker's friendly name corresponds to the name of the device. (This is the name that appears in GraphEdit.) For more information, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md).



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMAudioInputMixer**](/windows/desktop/api/Strmif/nn-strmif-iamaudioinputmixer), [**IAMFilterMiscFlags**](/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags), [**IAMResourceControl**](/windows/desktop/api/Strmif/nn-strmif-iamresourcecontrol), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), IPersistPropertyBag, ISpecifyPropertyPages                                                               |
| Input Pin Media Types                    | MEDIATYPE\_AnalogAudio, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                         |
| Input Pin Interfaces                     | [**IAMAudioInputMixer**](/windows/desktop/api/Strmif/nn-strmif-iamaudioinputmixer), [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                                                                                                                           |
| Output Pin Media Types                   | MEDIATYPE\_Audio, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                               |
| Output Pin Interfaces                    | [**IAMBufferNegotiation**](/windows/desktop/api/Strmif/nn-strmif-iambuffernegotiation), [**IAMPushSource**](/windows/desktop/api/Strmif/nn-strmif-iampushsource), [**IAMStreamConfig**](/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig), [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol), [**IKsPropertySet**](ikspropertyset.md), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) |
| Filter CLSID                             | Not applicable                                                                                                                                                                                                                                                                                     |
| Property Page CLSID                      | CLSID\_AudioInputMixerProperties                                                                                                                                                                                                                                                                   |
| Executable                               | qcap.dll                                                                                                                                                                                                                                                                                           |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                                                                                                                                                                |
| [Filter Category](filter-categories.md) | CLSID\_AudioInputDeviceCategory                                                                                                                                                                                                                                                                    |



 

## Remarks

The input pins represent physical hardware connections and are never connected to other filters in DirectShow.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Audio Capture](audio-capture.md)
</dt> </dl>

 

 



