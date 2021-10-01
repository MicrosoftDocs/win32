---
description: SDK Samples That Use the Core Audio APIs
ms.assetid: 4460df28-a77d-4bf5-9dee-5fb69ba2ded6
title: SDK Samples That Use the Core Audio APIs
ms.topic: article
ms.date: 05/31/2018
---

# SDK Samples That Use the Core Audio APIs

The Windows SDK includes the following code samples that demonstrate the use of the Core Audio APIs. The following samples are located in the directory %MSSdk%\\samples\\multimedia\\audio, where %MSSdk% is the root directory of the Windows SDK installation on your computer.




| Sample | Deascription | 
|--------|--------------|
| <a href="aecmicarray.md">AECMicArray</a> | This sample uses the MMDevice, WASAPI, DeviceTopology, and EndpointVolume APIs to capture a high-quality voice stream. TThe sample supports acoustic echo cancellation (AEC) and microphone array processing by using the AEC DMO also called the Voice capture DSP provided by Microsoft . | 
| <a href="capturesharedeventdriven.md">CaptureSharedEventDriven</a> | This sample application uses the Core Audio APIs to capture audio data from an input device, specified by the user and writes it to a uniquely named .WAV file in the current directory. This sample demonstrates event-driven buffering. | 
| <a href="capturesharedtimerdriven.md">CaptureSharedTimerDriven</a> | This sample application uses the Core Audio APIs to capture audio data from an input device, specified by the user and writes it to a uniquely named .WAV file in the current directory. This sample demonstrates timer-driven buffering. | 
| <a href="duckingcapturesample.md">DuckingCaptureSample</a> | This sample application demonstrates opening and closing communication streams and causing ducking events that an application can get to implement stream attenuation. This application implements a chat client that uses Core Audio APIs to read audio data from a communication device and to play it on the output device. | 
| <a href="endpointvolume.md">EndpointVolume</a> | This sample application uses the Core Audio APIs to change the volume of the device, specified by the user. | 
| <a href="osd.md">OSD</a> | This sample uses the MMDevice and EndpointVolume APIs to implement an on-screen display that shows volume changes to the output stream that plays through the default audio-rendering endpoint device. The on-screen display appears when the user adjusts the volume level in the Windows volume-control program, Sndvol.exe, and it disappears after the volume level remains unchanged for a short period. | 
| <a href="renderexclusiveeventdriven.md">RenderExclusiveEventDriven</a> | This sample application uses the Core Audio APIs to render audio data to an output device, specified by the user. This sample demonstrates event-driven buffering for a rendering client in exclusive mode. For an exclusive-mode stream, the client shares the endpoint buffer with the audio device. | 
| <a href="renderexclusivetimerdriven.md">RenderExclusiveTimerDriven</a> | This sample application uses the Core Audio APIs to render audio data to an output device, specified by the user. This sample demonstrates timer-driven buffering for a rendering client in exclusive mode. For an exclusive-mode stream, the client shares the endpoint buffer with the audio device. | 
| <a href="rendersharedeventdriven.md">RenderSharedEventDriven</a> | This sample application uses the Core Audio APIs to render audio data to an output device, specified by the user. This sample demonstrates event-driven buffering for a rendering client in shared mode. For a shared-mode stream, the client shares the endpoint buffer with the audio engine. | 
| <a href="rendersharedtimerdriven.md">RenderSharedTimerDriven</a> | This sample application uses the Core Audio APIs to render audio data to an output device, specified by the user. This sample demonstrates timer-driven buffering for a rendering client in shared mode. For a shared-mode stream, the client shares the endpoint buffer with the audio engine. | 
| WinAudio | This sample uses the MMDevice API and WASAPI to play and capture audio streams. The user interface of this sample application enables users to select audio endpoint devices, to change the volume level of the local audio session, and to play .wav files and microphone input.<blockquote>[!Note]<br />This sample has been deprecated in Windows 7.</blockquote><br /> | 




 

You can download the Windows SDK from the [Microsoft Windows SDK Download Center](https://developer.microsoft.com/windows/downloads/sdk-archive/) website.

## Related topics

<dl> <dt>

[About the Windows Core Audio APIs](about-the-windows-core-audio-apis.md)
</dt> </dl>

 

 




