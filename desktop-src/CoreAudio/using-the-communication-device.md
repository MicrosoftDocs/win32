---
description: In Windows 7, the Windows multimedia control panel, Mmsys.cpl, provides a new Communications tab.
ms.assetid: bec2127d-fb82-436d-beee-d43e8fef5c35
title: Using a Communication Device
ms.topic: article
ms.date: 05/31/2018
---

# Using a Communication Device

In Windows 7, the Windows multimedia control panel, Mmsys.cpl, provides a new **Communications** tab. This tab contains options that enables a user to set options that defines how the system manages a *communication device*. A communication device is used primarily for placing or receiving telephone calls on the computer. For a computer that has only one rendering device (speaker) and one capture device (microphone), these audio devices also act as the default communication devices. When a user connects a new device, such as a USB headset, the system performs automatic device role detection by looking up the configuration settings that are populated by the OEM. If the system determines a device to be best suited for communication purposes, the system assigns the **eCommunications** role to the device. For these devices, the Windows 7 Mmsys.cpl provides the option **Default Communication Device** that enables a user to select a communication device each for audio rendering (**Playback** tab) and audio capturing (**Recording** tab). The system performs automatic role detection but does not set a particular device to be used for communications. This must be done by the user. The new **eCommunications** role lets an application distinguish between a device that is chosen by the user for handling phone calls and a device to be used as a multimedia device (music playback). For example, if the user has a headset and a speaker connected to the computer, the system assigns the **eConsole** role to the speaker and the **eCommunications** role to the headset. After the user selects the headset to be used as the communication device, to develop a communication application, you can target the headset specifically for rendering an audio stream. An application the user cannot change the device role assigned by the system. For more information about device roles, see [Device Roles](device-roles.md).

Communication applications, such as VoIP and Unified Communication applications, place and receive phone calls through a computer. For example, a VoIP application might assign a stream that contains the ring-in notification to the endpoint of a communication device set for rendering audio streams. In addition, the application might open the voice input and output streams on the capture and rendering endpoint devices that are set as communication devices.

To integrate communication capabilities into your applications, you can use:

-   [MMDevice API](mmdevice-api.md)—to get a reference to the endpoint of the communication device.
-   [WASAPI](wasapi.md)—to render and capture audio streams through the communication device. The operating system considers the stream opened on a communication device to be a *communication stream*.

The communication application enumerates devices and provides stream management for a communication stream (rendering or capture) stream in the same manner as it would manage a non-communication stream by using the Core Audio APIs.

One of the features that you can integrate in your communication application is *ducking* or *stream attenuation*. This behavior defines what must happen to other sounds when a communication stream is opened, such as when a phone call is received on the communication device. The system might mute or lower the audio volume of the non-communication stream depending on the user's choice. The audio system generates ducking events when a communication stream is opened or closed for rendering or capturing streams. By default, the operating system provides a default ducking experience. A media application can replace the default behavior and handle these events itself to provide a customized ducking experience.

The following sections describe how to use Core Audio APIs to provide a custom ducking experience.

-   [Default Ducking Experience](stream-attenuation.md)
-   [Disabling the Default Ducking Experience](disabling-the-ducking-experience.md)
-   [Providing a Custom Ducking Behavior](providing-a-custom-ducking-experience.md)
-   [Implementation Considerations for Ducking Notifications](handling-audio-ducking-events-from-communication-devices.md)
-   [Getting Ducking Events](getting-ducking-events-from-a-communication-device.md)

### Getting a Reference to the Communication Device Endpoint

To use the communication device, a direct WASAPI client must enumerate the devices by using the device enumerator. Get a reference to the endpoint of the default communication device by calling [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint). In this call, the application must specify **eCommunications** in the *Role* parameter to restrict the device enumeration to communication devices. After you get a reference to the device endpoint for the device, you can activate the services that are scoped for the endpoint by calling [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate). For example, you can pass the **IID\_IAudioClient** service identifier to activate an audio client object and use it for stream management, the **IID\_IAudioEndpointVolume** identifier to get access to the volume controls of the communication device endpoint, or the **IID\_IAudioSessionManager** identifier to activate the session manager that enables you to interact with the policy engine of the endpoint. For information about stream operations, see [Stream Management](stream-management.md).

By using the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) reference, you can also access the property store for the device endpoint. These property values, such as device friendly name and manufacturer name, are populated by the OEM and enable an application to determine the characteristics of a communication device. For more information, see [Device Properties](device-properties.md).

The following example code gets a reference to the endpoint of the default communication device for rendering an audio stream.


```C++
IMMDevice *defaultDevice = NULL;

hr = CoCreateInstance(__uuidof(MMDeviceEnumerator), NULL,
            CLSCTX_INPROC_SERVER, 
            __uuidof(IMMDeviceEnumerator), 
            (LPVOID *)&deviceEnumerator);

hr = deviceEnumerator->GetDefaultAudioEndpoint(eRender, 
            eCommunications, &defaultDevice);
```



## Related topics

<dl> <dt>

[Stream Management](stream-management.md)
</dt> </dl>

 

 



