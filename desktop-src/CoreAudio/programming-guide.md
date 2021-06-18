---
description: Learn about the concepts and features of the core audio APIs of Windows Vista and how to use them in application programming.
ms.assetid: 825c7cd7-dc66-47b6-a1b6-d10101daebb3
title: Core Audio Programming Guide
ms.topic: article
ms.date: 05/31/2018
---

# Core Audio Programming Guide

This guide section explains the concepts and features of the core audio APIs of Windows Vista, and describes how to use them in application programming.

This section contains the following topics.



| Topic                                                                                                                      | Description                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [User-Mode Audio Components](user-mode-audio-components.md)                                                               | Through the low-level interfaces in the core audio APIs, a client can access the system components that manage and mix audio streams.                                                                        |
| [Protected User Mode Audio (PUMA)](protected-user-mode-audio--puma-.md)                                                   | Describes the updates to Protected User Mode Audio (PUMA), the user-mode audio engine in the Protected Environment (PE), which provides a safer environment for audio processing and rendering.              |
| [Audio Endpoint Devices](audio-endpoint-devices.md)                                                                       | An audio endpoint device is a software abstraction that enables user-friendly interactions with audio devices such as microphones and speakers.                                                              |
| [Audio Sessions](audio-sessions.md)                                                                                       | An audio session is a software abstraction that enables a client to manage a collection of related audio streams as a single unit.                                                                           |
| [Volume Controls](volume-controls.md)                                                                                     | The system integrates its policy-based volume settings with the user's volume settings in a logical and consistent way.                                                                                      |
| [Stream Management](stream-management.md)                                                                                 | The Windows Audio Session API (WASAPI) provides a client with a complete set of methods for creating and managing audio streams.                                                                             |
| [Device Topologies](device-topologies.md)                                                                                 | The DeviceTopology API enables a client to discover the audio controls that lie along the various data paths in the audio hardware.                                                                          |
| [Using the IKsControl Interface to Access Audio Properties](using-the-ikscontrol-interface-to-access-audio-properties.md) | A specialized audio application might need to use the IKsControl interface to access the properties of an audio adapter.                                                                                     |
| [Interoperability with Legacy Audio APIs](interoperability-with-legacy-audio-apis.md)                                     | Key features of the core audio APIs in Windows Vista can be incorporated into existing applications that use DirectSound, DirectShow, and the Windows multimedia **waveOutXxx** and **waveInXxx** functions. |
| [Spatial Sound](spatial-sound.md)                                                                                         | Provides guidance for using Windows Sonic, Microsoft’s platform-level solution for spatial sound support on Xbox and Windows, enabling both surround and elevation (above or below the listener) audio cues. |



 

## Related topics

<dl> <dt>

[Core Audio APIs](core-audio-apis-in-windows-vista.md)
</dt> </dl>

 

 



