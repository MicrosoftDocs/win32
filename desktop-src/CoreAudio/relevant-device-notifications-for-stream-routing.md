---
description: In Windows 7, high-level platform APIs that use Core Audio APIs, such as Media Foundation, DirectSound, and Wave APIs, implement the stream routing feature by handling stream switching from an existing device to a new default audio endpoint.
ms.assetid: caf831bb-b8de-467f-bdb4-f9f8991dc7a8
title: Relevant Notifications for Stream Routing
ms.topic: article
ms.date: 05/31/2018
---

# Relevant Notifications for Stream Routing

In Windows 7, high-level platform APIs that use Core Audio APIs, such as Media Foundation, DirectSound, and Wave APIs, implement the stream routing feature by handling stream switching from an existing device to a new default audio endpoint. Media applications that use these APIs use the stream routing behavior without any modifications to the source. Direct WASAPI clients can use the notifications sent by Core Audio components and implement the stream routing feature.

To implement the stream routing feature, a client must listen for two types of events: device change notifications and session disconnect notifications. In the implementation provided by the high-level APIs, these events are sent for default device endpoints created by calling [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint). For more information, see [Getting the Device Endpoint for Stream Routing](getting-the-default-device-endpoint-for-stream-routing.md).

The Core Audio component MMDeviceAPI delivers notification callbacks when audio devices are added, removed, or modified. The format and audio session changes are reported as events through WASAPI.

## Device Change Notifications

MMDeviceAPI raises events when audio devices are added, removed, or modified. If the client is to provide stream routing functionality, it must implement the [**IMMNotificationClient**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immnotificationclient) interface and register its implementation with MMDeviceAPI.

To get device change notifications, the client must perform the following tasks:

-   Implement the [**IMMNotificationClient**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immnotificationclient) interface to handle device change notifications sent by MMDeviceAPI.
-   Register the [**IMMNotificationClient**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immnotificationclient) implementation with MMDeviceAPI by calling the [**IMMDeviceEnumerator::RegisterEndpointNotificationCallback**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-registerendpointnotificationcallback) method.

After the client's implementation of these interfaces is registered, the client receives notifications in the form of callbacks through the methods of these interfaces. [**IMMNotificationClient**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immnotificationclient) methods are called by MMDeviceAPI when it raises endpoint-level events (endpoint state changes, new endpoint arrivals, endpoint deletions, default endpoint changes, and endpoint property changes).

If the client wants to provide stream routing for the default device, the client must implement the device change behavior when it receives the notification through the [**IMMNotificationClient::OnDefaultDeviceChanged**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immnotificationclient-ondefaultdevicechanged) callback.

## Audio Session Change Notifications

Audio session changes and format changes are reported as audio session events through WASAPI. A WASAPI client implements the [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) interface and registers the implementation with WASAPI.

To get audio session change notifications, the client must perform the following tasks:

-   Implement the [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) interface to handle format change notifications sent by WASAPI.
-   Register the [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) implementation with WASAPI by calling the [**IAudioSessionControl::RegisterAudioSessionNotification**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessioncontrol-registeraudiosessionnotification) method.

[**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) methods are called by WASAPI when audio session changes occur. These events are raised when the session's display name, icon path, volume, grouping parameter, or state changes.

To implement the stream routing feature, the client must wait for the session-disconnect notification. When an audio session is disconnected or a device's format is changed, WASAPI sends the client notifications in the form of callbacks through [**IAudioSessionEvents::OnSessionDisconnected**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessionevents-onsessiondisconnected). With the disconnection notification, WASAPI also sends a value that indicates why the session was disconnected. This can occur for several reasons, such as the device was removed, the server stopped, and so on. For the complete list of reasons, see the **AudioSessionDisconnectReason** enumeration defined in AudioPolicy.h. If the default device changes, the client must wait for the notifications (if they have not already been received) that are accompanied with a **DisconnectReasonDeviceRemoval** value. In response to such notifications, the client might reopen the stream on the new default device.

Because all of these operations are asychronous, the order in which the application receives notifications cannnot be predicted. However, typically, the application receives **AudioSessionDisconnect** value before the default device change notification.

### Format Change Notifications

Audio format changes occur when the format of the stream changes. This can occur when the user selects a new format in the **Sound** control panel or the new default device supports a new format (for example, HDMI or certain professional audio interfaces with a manual sample-rate adjustment). To notify the client about these types of format changes, WASAPI sends a session notification by the registered implementation of [**IAudioSessionEvents::OnSessionDisconnected**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessionevents-onsessiondisconnected) with a disconnect reason of **DisconnectReasonFormatChanged**. The client can handle the notification by reopening the stream in the new format.

## Related topics

<dl> <dt>

[About MMDevice API](mmdevice-api.md)
</dt> <dt>

[About WASAPI](wasapi.md)
</dt> <dt>

[Stream Routing](stream-routing.md)
</dt> </dl>

 

 



