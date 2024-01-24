---
description: External Device Interfaces for DV Camcorders
ms.assetid: 001321c5-70c7-4baa-ba5a-1e424ca0d647
title: External Device Interfaces for DV Camcorders
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External Device Interfaces for DV Camcorders

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [WDM Video Capture](wdm-video-capture-filter.md) filter exposes three interfaces for controlling a camcorder.



| Label | Value |
|------------------------------------------------|-------------------------------------------------|
| [**IAMExtDevice**](/windows/desktop/api/Strmif/nn-strmif-iamextdevice)           | The base interface for external device control. |
| [**IAMExtTransport**](/windows/desktop/api/Strmif/nn-strmif-iamexttransport)     | Controls the VCR functions.                     |
| [**IAMTimecodeReader**](/windows/desktop/api/Strmif/nn-strmif-iamtimecodereader) | Reads timecode from the device.                 |



 

> [!Note]  
> To use these interfaces with the MSDV camcorder driver, include the header file XPrtDefs.h in your project.

 

After you select a capture device and create an instance of the capture filter, query the filter for these interfaces. The following example declares a custom structure that holds the interface pointers, along with Boolean values that specify the availability of each interface:


```C++
struct _MyDevCap
{
    IAMExtDevice       *pDevice;
    IAMExtTransport    *pTransport;
    IAMTimecodeReader  *pTimecode;
    BOOL                bHasDevice;
    BOOL                bHasTransport;
    BOOL                bHasTimecode;
} MyDevCap;

HRESULT hr;
IBaseFilter *pDVCam;  // Pointer to the capture filter.

// Create an instance of the capture filter (not shown).

hr = pDVCam->QueryInterface(IID_IAMExtDevice, (void **)&MyDevCap.pDevice);
MyDevCap.bHasDevice = (SUCCEEDED(hr));

hr = pDVCam->QueryInterface(IID_IAMExtTransport, (void **)&MyDevCap.pTransport);
MyDevCap.bHasTransport = (SUCCEEDED(hr));

hr = pDVCam->QueryInterface(IID_IAMTimecodeReader, (void **)&MyDevCap.pTimecode);
MyDevCap.bHasTimecode = (SUCCEEDED(hr));
```



## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 



