---
Description: Audio Capture and Rendering Interfaces
ms.assetid: 79b42ffd-703a-4a7c-bb2d-5cfc2fbeb16c
title: Audio Capture and Rendering Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Capture and Rendering Interfaces

These interfaces support audio capture and rendering in DirectShow



| Interface                                              | Description                                                                                                                                               |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAMAudioInputMixer**](/windows/win32/Strmif/nn-strmif-iamaudioinputmixer?branch=master)       | Access the analog inputs on the system's sound card and adjust characteristics, such as mono or stereo, mix level, pan level, loudness, treble, and bass. |
| [**IAMAudioRendererStats**](/windows/win32/Strmif/nn-strmif-iamaudiorendererstats?branch=master) | Get statistical performance information about audio renderering.                                                                                          |
| [**IAMBufferNegotiation**](/windows/win32/Strmif/nn-strmif-iambuffernegotiation?branch=master)   | Control how the audio capture filter allocates buffers.                                                                                                   |
| [**IAMClockSlave**](/windows/win32/Strmif/nn-strmif-iamclockslave?branch=master)                 | Control the tolerance of an audio renderer when it matches rates with another clock.                                                                      |
| [**IAMDirectSound**](/windows/win32/Amaudio/nn-amaudio-iamdirectsound?branch=master)               | Enables an application to specify which window has focus for controlling DirectSound audio playback.                                                      |
| [**IAMResourceControl**](/windows/win32/Strmif/nn-strmif-iamresourcecontrol?branch=master)       | Hold an audio device resource before it is needed.                                                                                                        |
| [**IAMStreamConfig**](/windows/win32/Strmif/nn-strmif-iamstreamconfig?branch=master)             | Query and set the capture filter's output format.                                                                                                         |
| [**IBasicAudio**](/windows/win32/Control/nn-control-ibasicaudio?branch=master)                     | Set audio output volume and balance.                                                                                                                      |



 

## Related topics

<dl> <dt>

[Interfaces](interfaces.md)
</dt> </dl>

 

 



