---
description: Stream routing is the ability of a media application to switch streams between devices with minimal interruption to the playback or the capture session.
ms.assetid: 'fc6efe89-013c-47af-870e-8705fa60c99c'
title: Stream Routing
ms.topic: article
ms.date: 05/31/2018
---

# Stream Routing

*Stream routing* is the ability of a media application to switch streams between devices with minimal interruption to the playback or the capture session.

A computer can have multiple rendering and capture devices. The system lists these devices on the **Sounds** control panel. From this list, a user can set a device to be the default device for each role: playback, recording, or the four communications roles (console render, console capture, communication render, or communication capture). The list of devices may be modified dynamically as some of these devices can be available temporarily, for example a USB headset. When multiple devices are available, the user can change the default to a different device. The user can also change the format of a device (sample rate, bits per sample, and so on) on the **Advanced** tab for the device properties.

Consider a scenario in which a user selects **Speakers** as the default device for rendering audio streams. The user then connects a USB headset, selects the headset as the new default device, and changes the sample rate of the device from 44.1 kHz to 48 kHz. The user wants to play the audio stream on the headset at the new sample rate with minimal interruption to the streaming session.

In this scenario, there are two cases that the media application must handle:

-   The stream must be transferred to the new default device with minimal interruption to playback.
-   The new device must resume playback in the new format (that is, the user can change more than the sample rate).

In Windows Vista, to support this scenario, the media application had to provide the implementation for stream routing. The application was responsible for terminating existing streams and restarting the streams on the new device. If the user changed the default device or its mix format changed, then all of the associated sessions were closed and the application had to handle the recovery.

In Windows 7, an application can seamlessly transfer a stream from an existing default device to a new default audio endpoint. High-level audio API sets such as Media Foundation, DirectSound, and WAVE APIs implement the stream routing feature. Media applications that use these API sets to play or capture a stream from the default device use the default implementation and will not have to modify the application. However, if your media application uses MMDeviceAPI or WASAPI directly, the application needs to provide the stream routing implementation.

> [!Note]  
> MMDeviceAPI and WASAPI are Core Audio API components that an application can use to render or capture a stream on a device. The MMDeviceAPI discovers the new audio endpoint device, and WASAPI manages the flow of audio data between a media application and the audio endpoint device.

 

To implement the stream routing feature, the application must listen for the notifications sent by MMDeviceAPI and WASAPI when:

-   The default device is changed by the user.
-   The existing default device is removed and a new default device is added.
-   The device format is changed.

By handling these notifications, an application can perform the necessary stream management operations while transferring the stream to the new default device. In addition, the application can render or capture existing streams by using the new format specified by the user while a rendering session is active.

This section contains the following topics:

-   [Getting the Device Endpoint for Stream Routing](getting-the-default-device-endpoint-for-stream-routing.md)
-   [Relevant Notifications for Stream Routing](relevant-device-notifications-for-stream-routing.md)
-   [Stream Routing Implementation Considerations](stream-routing-implementation-considerations.md)

The following samples, included in the Windows SDK, demonstrate how an application can handle stream routing notifications.

-   [RenderSharedTimerDriven](rendersharedtimerdriven.md)
-   [RenderSharedEventDriven](rendersharedeventdriven.md)
-   [RenderExclusiveTimerDriven](renderexclusivetimerdriven.md)
-   [RenderExclusiveEventDriven](renderexclusiveeventdriven.md)
-   [CaptureSharedTimerDriven](capturesharedtimerdriven.md)
-   [CaptureSharedEventDriven](capturesharedeventdriven.md)

## Related topics

<dl> <dt>

[Stream Management](stream-management.md)
</dt> <dt>

[About MMDevice API](mmdevice-api.md)
</dt> <dt>

[About WASAPI](wasapi.md)
</dt> </dl>

 

 



