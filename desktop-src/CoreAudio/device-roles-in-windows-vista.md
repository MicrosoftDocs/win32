---
description: Working with Device Roles
ms.assetid: 3b2cb1fe-0f11-4509-a6f3-513d2755cd29
title: Working with Device Roles
ms.topic: article
ms.date: 05/31/2018
---

# Working with Device Roles

The [MMDevice API](mmdevice-api.md) supports device roles. The [**ERole**](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-erole) enumeration defines the device roles that are supported by the MMDevice API.

> [!Note]  
> Although the [MMDevice API](mmdevice-api.md) supports device roles, the user interface in Windows Vista does not implement support for this feature.

 

An application can use MMDevice API to support [device roles](device-roles.md) through the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) and [**IMMNotificationClient::OnDefaultDeviceChanged**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immnotificationclient-ondefaultdevicechanged) methods. However, the user interface in Windows Vista does not support assignment of individual roles to different devices. In Windows Vista, the user interface enables the user to select a default audio device for rendering and a default audio device for capture. When the user selects a default rendering or capture device, the system assigns all three device roles (eConsole, eMultimedia, and eCommunications) to that device. Applications cannot change the roles that are assigned to audio endpoint devices. The operating system allows only the user to assign device roles.

A client can register itself to receive a notification from the MMDevice API each time a change occurs in the assignment of roles to audio endpoint devices. When a role shifts from one device to another, the client can choose whether to continue playing (or recording) its streams through the same device or to switch the streams to another device. By default, the streams continue to play (or be recorded) through the original device. In Windows Vista, to switch the streams to another device, the client must delete the streams on the original device and create replacement streams on the new device. In Windows 7, the client can listen for new notifications to implement a seamless switch without interrupting the playback or the capture session. For more information, see [Stream Routing](stream-routing.md).

If you plan to use Windows Vista to test your application, you can set up a test environment to verify that the application behaves as expected when the user can assign individual device roles to different devices. For more information, send email to uaa@microsoft.com.

## Communication Devices

The Windows 7 user interface has the capability of adding *communications devices*. The **Sound** control panel enables the user to select a default communication device each for rendering and capturing audio stream. By default, when a new device is connected to the computer, the operating system performs automatic role detecting and determines whether the device is suitable for the eCommunication role. By targeting communication devices, you can develop applications that use Core Audio APIs to implement PC-phone communication solutions. For example, a VoIP application might assign its voice input and output streams to the default capture and rendering endpoint devices with the eCommunications role. Like any other stream, a communication application must get a reference to the communication device's endpoint by calling [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint). In this call, the application must specify **eCommunications** in the *Role* parameter. The WASAPI stream operations on a stream, opened on a communication device, are similar to any other audio stream. The communication application can enhance user experience by implementing behaviors such as ducking by handling notifications from the device endpoint. For more information, see [Using a Communication Device](using-the-communication-device.md).

## Automatic Device Role Detection

Consider a scenario in which a computer has a default rendering device, the speakers, and a default capture device, a microphone. The user connects a USB headset to the computer. After the appropriate drivers are installed, the operating system attempts to detect a role to assign for the new audio device.

In Windows 7, the device role detection feature has been improved significantly to determine the appropriate roles suited for audio devices. All audio devices contain a set of configuration settings populated by the device OEM, which help the system decide how to use the device. These settings include information such as the physical location of the audio jack the device type, the jack subtype, and detection capabilities so that the system can determine whether the device is plugged in. By retrieving these values from the device, the operating system determines the role to assign to the device. In this scenario, the system has queried the USB headset device, performed automatic role detection, and decided that the device is best suited to be a communication device.

An application can also get jack information by using the Core Audio APIs. For more information, see [**IKsJackDescription**](/windows/desktop/api/Devicetopology/nn-devicetopology-iksjackdescription) and [**IKsJackDescription2**](/windows/desktop/api/Devicetopology/nn-devicetopology-iksjackdescription2).

## Related topics

<dl> <dt>

[Device Roles](device-roles.md)
</dt> </dl>

 

 



