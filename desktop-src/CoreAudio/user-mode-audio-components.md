---
description: User-Mode Audio Components
ms.assetid: b240b629-5bb6-4b07-95be-8ca5a14a3567
title: User-Mode Audio Components
ms.topic: article
ms.date: 05/31/2018
---

# User-Mode Audio Components

In Windows Vista, the core audio APIs serve as the foundation of the user-mode audio subsystem. The core audio APIs are implemented as a thin layer of user-mode system components that separate user-mode clients from kernel-mode audio drivers and audio hardware. Higher-level audio APIs, such as DirectSound and the Windows multimedia functions, access audio devices through the core audio APIs. In addition, some audio applications communicate directly with the core audio APIs.

The core audio APIs support the user-friendly notion of an audio endpoint device. An audio endpoint device is a software abstraction that represents a physical device that the user manipulates directly. Examples of audio endpoint devices are speakers, headphones, and microphones. For more information, see [Audio Endpoint Devices](audio-endpoint-devices.md).

The following diagram shows the core audio APIs and their relationship to the other user-mode audio components in Windows Vista.

![diagram of user-mode audio-rendering components](images/fig1.jpg)

For simplicity, the preceding diagram shows only an audio-rendering data path to the endpoint device—the diagram does not show an audio-capture data path. The core audio APIs include the [MMDevice API](mmdevice-api.md), [WASAPI](wasapi.md), the [DeviceTopology API](devicetopology-api.md), and the [EndpointVolume API](endpointvolume-api.md), which are implemented in the Audioses.dll and Mmdevapi.dll user-mode system modules.

As shown in the preceding diagram, the core audio APIs provide a foundation for the following higher-level APIs:

-   Media Foundation
-   Windows multimedia **waveXxx** and **mixerXxx** functions
-   DirectSound
-   DirectMusic

DirectSound, the Windows multimedia audio functions, and Media Foundation (through its streaming audio renderer, or SAR, component) communicate directly with the core audio APIs. DirectMusic communicates with the core audio APIs indirectly through DirectSound.

A client of WASAPI passes data to an endpoint device through an *endpoint buffer*. System software and hardware components manage the movement of data from the endpoint buffer to the endpoint device in a manner that is largely transparent to the client. Furthermore, for an endpoint device that plugs into an audio adapter with jack-presence detection, the client can create an endpoint buffer only for an endpoint device that is physically present. For more information about jack-presence detection, see [Audio Endpoint Devices](audio-endpoint-devices.md).

The preceding diagram shows two types of endpoint buffer. If a client of WASAPI opens a stream in *shared mode*, then the client writes audio data to the endpoint buffer and the Windows audio engine reads the data from the buffer. In this mode, the client shares the audio hardware with other applications running in other processes. The audio engine mixes the streams from these applications and plays the resulting mix through the hardware. The audio engine is a user-mode system component (Audiodg.dll) that performs all of its stream-processing operations in software. In contrast, if a client opens a stream in *exclusive mode*, the client has exclusive access to the audio hardware. Typically, only a small number of "pro audio" or RTC applications require exclusive mode. Although the diagram shows both the shared-mode and exclusive-mode streams, only one of these two streams (and its corresponding endpoint buffer) exists, depending on whether the client opens the stream in shared mode or in exclusive mode.

In exclusive mode, the client can choose to open the stream in any audio format that the endpoint device supports. In shared mode, the client must open the stream in the mix format that is currently in use by the audio engine (or a format that is similar to the mix format). The audio engine's input streams and the output mix from the engine are all in this format.

In Windows 7, a new feature called *low-latence mode* has been added for streams in share mode. In this mode, the audio engine runs in pull mode, in which there a significant reduction in latency. This is very useful for communication applications that require low audio stream latency for faster streaming.

Applications that manage low-latency audio streams can use the Multimedia Class Scheduler Service (MMCSS) in Windows Vista to increase the priority of application threads that access endpoint buffers. MMCSS enables audio applications to run at high priority without denying CPU resources to lower-priority applications. MMCSS assigns a priority to a thread based on its task name. For example, Windows Vista supports the task names "Audio" and "Pro Audio" for threads that manage audio streams. By default, the priority of a "Pro Audio" thread is higher than that of an "Audio" thread. For more information about MMCSS, see the Windows SDK documentation.

The core audio APIs support both PCM and non-PCM stream formats. However, the audio engine can mix only PCM streams. Thus, only exclusive-mode streams can have non-PCM formats. For more information, see [Device Formats](device-formats.md).

The audio engine runs in its own protected process, which is separate from the process that the application runs in. To support a shared-mode stream, the Windows audio service (the box labeled "Audio Service" in the preceding diagram) allocates a cross-process endpoint buffer that is accessible to both the application and the audio engine. For exclusive mode, the endpoint buffer resides in memory that is accessible to both the application and the audio hardware.

The Windows audio service is the module that implements Windows audio policy. Audio policy is a set of internal rules that the system applies to the interactions between audio streams from multiple applications that share and compete for use of the same audio hardware. The Windows audio service implements audio policy by setting the control parameters for the audio engine. The duties of the audio service include:

-   Keeping track of the audio devices that the user adds to or removes from the system.
-   Monitoring the roles that are assigned to the audio devices in the system.
-   Managing the audio streams from groups of tasks that produce similar classes of audio content (console, multimedia, and communications).
-   Controlling the volume level of the combined output stream ("submix") for each of the various types of audio content.
-   Informing the audio engine about the processing elements in the data paths for the audio streams.

In some versions of Windows, the Windows audio service is disabled by default and must be explicitly turned on before the system can play audio.

In the example shown in the preceding diagram, the endpoint device is a set of speakers that are plugged into the audio adapter. The client application writes audio data to the endpoint buffer, and the audio engine handles the details of transporting the data from the buffer to the endpoint device.

The box labeled "Audio Driver" in the preceding diagram might be a combination of system-supplied and vendor-supplied driver components. In the case of an audio adapter on a PCI or PCI Express bus, the system supplies the Port Class system driver (Portcls.sys), which implements a set of port drivers for the various audio functions in the adapter, and the hardware vendor supplies an adapter driver that implements a set of miniport drivers to handle device-specific operations for the port drivers. In the case of a High Definition Audio controller and codec on a PCI or PCI Express bus, the system supplies the adapter driver (Hdaudio.sys), and no vendor-supplied driver is needed. In the case of an audio adapter on a USB bus, the system supplies the AVStream class system driver (Ks.sys) plus the USB Audio driver (Usbaudio.sys); again, no vendor-supplied driver is needed.

For simplicity, the preceding diagram shows only rendering streams. However, the core audio APIs support capture streams as well. In shared mode, several clients can share the captured stream from an audio hardware device. In exclusive mode, one client has exclusive access to the captured stream from the device.

## Related topics

<dl> <dt>

[Programming Guide](programming-guide.md)
</dt> </dl>

 

 



