---
Description: Audio Capture Filter
ms.assetid: 'ff345670-5a75-40d3-a228-8bc22aa76708'
title: Audio Capture Filter
---

# Audio Capture Filter

The Audio Capture filter represents an audio capture device. It has one capture output pin and several input pins (one for each type of input on the card, such as Line In, Mic, CD, and MIDI).

This filter can work with more than one hardware device, so calling CoCreateInstance to create the filter does not work. Instead, use the [System Device Enumerator](system-device-enumerator.md). The System Device Enumerator returns a unique moniker for each device. The moniker's friendly name corresponds to the name of the device. (This is the name that appears in GraphEdit.) For more information, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md).



|                                          |                                                                                                                                                                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMAudioInputMixer**](iamaudioinputmixer.md), [**IAMFilterMiscFlags**](iamfiltermiscflags.md), [**IAMResourceControl**](iamresourcecontrol.md), [**IBaseFilter**](ibasefilter.md), IPersistPropertyBag, ISpecifyPropertyPages                                                               |
| Input Pin Media Types                    | MEDIATYPE\_AnalogAudio, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                         |
| Input Pin Interfaces                     | [**IAMAudioInputMixer**](iamaudioinputmixer.md), [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                                                                                                                           |
| Output Pin Media Types                   | MEDIATYPE\_Audio, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                               |
| Output Pin Interfaces                    | [**IAMBufferNegotiation**](iambuffernegotiation.md), [**IAMPushSource**](iampushsource.md), [**IAMStreamConfig**](iamstreamconfig.md), [**IAMStreamControl**](iamstreamcontrol.md), [**IKsPropertySet**](ikspropertyset.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md) |
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

 

 



