---
Description: Audio Capture Filter
ms.assetid: ff345670-5a75-40d3-a228-8bc22aa76708
title: Audio Capture Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Capture Filter

The Audio Capture filter represents an audio capture device. It has one capture output pin and several input pins (one for each type of input on the card, such as Line In, Mic, CD, and MIDI).

This filter can work with more than one hardware device, so calling CoCreateInstance to create the filter does not work. Instead, use the [System Device Enumerator](system-device-enumerator.md). The System Device Enumerator returns a unique moniker for each device. The moniker's friendly name corresponds to the name of the device. (This is the name that appears in GraphEdit.) For more information, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md).



|                                          |                                                                                                                                                                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMAudioInputMixer**](/windows/win32/Strmif/nn-strmif-iamaudioinputmixer?branch=master), [**IAMFilterMiscFlags**](/windows/win32/Strmif/nn-strmif-iamfiltermiscflags?branch=master), [**IAMResourceControl**](/windows/win32/Strmif/nn-strmif-iamresourcecontrol?branch=master), [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), IPersistPropertyBag, ISpecifyPropertyPages                                                               |
| Input Pin Media Types                    | MEDIATYPE\_AnalogAudio, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                         |
| Input Pin Interfaces                     | [**IAMAudioInputMixer**](/windows/win32/Strmif/nn-strmif-iamaudioinputmixer?branch=master), [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                                                                                           |
| Output Pin Media Types                   | MEDIATYPE\_Audio, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                               |
| Output Pin Interfaces                    | [**IAMBufferNegotiation**](/windows/win32/Strmif/nn-strmif-iambuffernegotiation?branch=master), [**IAMPushSource**](/windows/win32/Strmif/nn-strmif-iampushsource?branch=master), [**IAMStreamConfig**](/windows/win32/Strmif/nn-strmif-iamstreamconfig?branch=master), [**IAMStreamControl**](/windows/win32/Strmif/nn-strmif-iamstreamcontrol?branch=master), [**IKsPropertySet**](ikspropertyset.md), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) |
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

 

 



