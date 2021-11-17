---
description: About the Windows Core Audio APIs
ms.assetid: 657cf75f-3d72-4a5f-ae29-299e826b2b86
title: About the Windows Core Audio APIs
ms.topic: article
ms.date: 05/31/2018
---

# About the Windows Core Audio APIs

This documentation provides information about Core Audio APIs for the Microsoft Windows family of operating systems.

The Core Audio APIs were introduced in Windows Vista. This new set of user-mode audio components provide client applications with improved audio capabilities. These capabilities include the following:

-   Low-latency, glitch-resilient audio streaming.
-   Improved reliability (many audio functions have moved from kernel-mode to user-mode).
-   Improved security (processing of protected audio content takes place in a secure, lower-privilege process).
-   Assignment of particular system-wide roles (console, multimedia, and communications) to individual audio devices.
-   Software abstraction of the audio endpoint devices (for example, speakers, headphones, and microphones) that the user manipulates directly.

The Core Audio APIs have been improved in Windows 7. For more information about the improvements and new features added, see [What's New for Core Audio APIs in Windows 7](what-s-new-for-core-audio-apis-in-windows-7.md).

This documentation describes the Core Audio APIs. These APIs serve as the foundation for the following higher-level APIs:

-   DirectSound
-   DirectMusic
-   Windows multimedia **waveXxx** and **mixerXxx** functions
-   Media Foundation

These higher-level APIs use the Core Audio APIs to share access to audio devices. Media Foundation is new with Windows Vista, whereas DirectSound, DirectMusic, and the **waveXxx** and **mixerXxx** functions are supported in Windows 98, Windows Millennium Edition, and in Windows 2000 and later.

Most audio applications communicate with the higher-level APIs instead of communicating directly with the Core Audio APIs. Some examples of applications that use higher-level APIs are:

-   Media players
-   DVD players
-   Games
-   Business applications, such as Microsoft Office PowerPoint, that play sound files

Typically, these applications communicate with the DirectSound or Media Foundation APIs.

Direct communication with the Core Audio APIs might not be suitable for many general-purpose audio applications. For example, the Core Audio APIs require audio streams to use an audio device's native data formats. However, third-party software developers who are developing the following types of products might require the special capabilities of the Core Audio APIs:

-   Professional audio ("pro audio") applications
-   Real-time communication (RTC) applications
-   Third-party audio APIs

A "pro audio" or RTC application might need direct access to the low-level features of the Core Audio APIs to achieve minimum latency by obtaining exclusive access to audio hardware. A third-party audio API might require direct access to the Core Audio APIs to implement a set of features that might not be entirely supported by any single high-level audio API that is supplied with Windows.

An application that uses a legacy audio API to play or record audio might require additional capabilities that are not supported by the legacy audio API, but that are supported by the Core Audio APIs. In many cases, the application can access these capabilities directly through the Core Audio APIs, which can be used in conjunction with the legacy audio API.

The Core Audio APIs are:

-   [Multimedia Device (MMDevice) API](mmdevice-api.md). Clients use this API to enumerate the audio endpoint devices in the system.
-   [Windows Audio Session API (WASAPI)](wasapi.md). Clients use this API to create and manage audio streams to and from audio endpoint devices.
-   [DeviceTopology API](devicetopology-api.md). Clients use this API to directly access the topological features (for example, volume controls and multiplexers) that lie along the data paths inside hardware devices in audio adapters.
-   [EndpointVolume API](endpointvolume-api.md). Clients use this API to directly access the volume controls on audio endpoint devices. This API is primarily used by applications that manage exclusive-mode audio streams.

These APIs support the user-friendly notion of an endpoint device, which is described in [Audio Endpoint Devices](audio-endpoint-devices.md).

Microsoft does not plan to make the Core Audio APIs that are described here available for use with earlier versions of Windows, including Microsoft Windows Server 2003, Windows XP, Windows Millennium Edition, Windows 2000, and Windows 98.

This overview contains the following topics.



| **Topic**                                                                                      | **Description**                                                                           |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [What's New for Core Audio APIs in Windows 7](what-s-new-for-core-audio-apis-in-windows-7.md) | Summarizes the new features and the improvements to the Core Audio APIs                   |
| [Header Files and System Components](header-files-and-system-components.md)                   | Describes the header files and system components for the Core Audio APIs.                 |
| [SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)       | Lists the samples in the Windows SDK that use the Core Audio APIs.                        |




 

## Related topics

<dl> <dt>

[Core Audio APIs](core-audio-apis-in-windows-vista.md)
</dt> </dl>

 

 



