---
description: External Device Control Interfaces
ms.assetid: edc10466-7852-4530-9ce7-b9dd36726745
title: External Device Control Interfaces
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External Device Control Interfaces

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These interfaces support application control over external devices, such as DV camcorders.



| Interface                                            | Description                                                                             |
|------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**IAMCameraControl**](/windows/desktop/api/Strmif/nn-strmif-iamcameracontrol)         | Control a camera.                                                                       |
| [**IAMExtDevice**](/windows/desktop/api/Strmif/nn-strmif-iamextdevice)                 | Control an external device such as a VCR or camcorder.                                  |
| [**IAMExtTransport**](/windows/desktop/api/Strmif/nn-strmif-iamexttransport)           | Control VCR transport functions, such as play, pause, record, fast-forward, and rewind. |
| [**IAMTimecodeDisplay**](/windows/desktop/api/Strmif/nn-strmif-iamtimecodedisplay)     | Set properties on a device that displays SMPTE timecode.                                |
| [**IAMTimecodeGenerator**](/windows/desktop/api/Strmif/nn-strmif-iamtimecodegenerator) | Set properties on a device that generates SMPTE timecode.                               |
| [**IAMTimecodeReader**](/windows/desktop/api/Strmif/nn-strmif-iamtimecodereader)       | Read SMPTE timecode from an external device.                                            |



 

## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 



