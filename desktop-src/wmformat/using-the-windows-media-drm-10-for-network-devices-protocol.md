---
title: Using the Windows Media DRM 10 for Network Devices Protocol
description: Using the Windows Media DRM 10 for Network Devices Protocol
ms.assetid: dec88d72-718c-42ab-8d48-eddf906051ef
keywords:
- Windows Media Format SDK,Windows Media DRM 10 for Network Devices
- Windows Media Format SDK,DRM 10 for Network Devices
- Advanced Systems Format (ASF),Windows Media DRM 10 for Network Devices
- ASF (Advanced Systems Format),Windows Media DRM 10 for Network Devices
- Advanced Systems Format (ASF),DRM 10 for Network Devices
- ASF (Advanced Systems Format),DRM 10 for Network Devices
- digital rights management (DRM),Windows Media DRM 10 for Network Devices
- DRM (digital rights management),Windows Media DRM 10 for Network Devices
- digital rights management (DRM),DRM 10 for Network Devices
- DRM (digital rights management),DRM 10 for Network Devices
- Windows Media DRM 10 for Network Devices,protocols
- DRM 10 for Network Devices,protocols
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Windows Media DRM 10 for Network Devices Protocol

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK provides some features to support the secure network device protocol, Windows Media DRM 10 for Network Devices. This protocol defines the messages sent between a digital media playback device, such as a set-top video player, and the computer that serves data to the device. The media data sent between server and device is encrypted to protect it from interception.

The communication between your application and devices that support Windows Media DRM 10 for Network Devices can use whatever networking protocols you prefer. The Windows Media Format SDK does not provide any objects that perform the network communications for you. Instead, the objects of this SDK process some Windows Media DRM 10 for Network Devices messages after your application has received them.

The features that support Windows Media DRM 10 for Network Devices are device registration, proximity detection, and converting DRM-protected files. These features are described in the following sections.



| Section                                                                                                                                                                          | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Device Registration](device-registration.md)                                                                                                                                   | Describes how to process registration request messages from devices.                                                                       |
| [Performing Proximity Detection](performing-proximity-detection.md)                                                                                                             | Describes the proximity detection process.                                                                                                 |
| [Converting a DRM-Protected File to a Windows Media DRM 10 for Network Devices Stream](converting-a-drm-protected-file-to-a-windows-media-drm-10-for-network-devices-stream.md) | Describes how to convert a DRM-protected file to a stream that can be sent to a device that uses Windows Media DRM 10 for Network Devices. |



 

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




