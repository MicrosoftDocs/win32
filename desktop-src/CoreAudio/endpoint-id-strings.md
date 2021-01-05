---
description: Endpoint ID Strings
ms.assetid: 3c955e2d-daaa-4b77-8ca5-890383bb2d39
title: Endpoint ID Strings
ms.topic: article
ms.date: 05/31/2018
---

# Endpoint ID Strings

In Windows Vista, the system generates endpoint ID strings to identify the [audio endpoint devices](audio-endpoint-devices.md) in the system. An endpoint ID string is a null-terminated wide-character string. The endpoint ID string for a particular audio endpoint device uniquely identifies the device among all audio endpoint devices in the system.

If a system contains two or more identical audio adapter devices, the corresponding audio endpoint devices will have identical friendly names, but each endpoint device will have a unique endpoint ID string. For more information about obtaining the friendly name of an endpoint device, see [Device Properties](device-properties.md).

After obtaining an [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface instance for an audio endpoint device, a client can call the [**IMMDevice::GetId**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-getid) method to obtain the endpoint ID string for the device. A client can use the endpoint ID string to create an instance of the audio endpoint device at a later time or in a different process by calling the [**IMMDeviceEnumerator::GetDevice**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdevice) method.

A client can arrange to receive a notification when the status of any audio endpoint device changes. To receive notifications, the client implements an [**IMMNotificationClient**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immnotificationclient) interface and registers that interface with the MMDevice API. When the status of an endpoint device changes, the MMDevice API calls the appropriate method in the client's [**EDataFlow**](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-edataflow) interface. One of the input parameters to the method is the endpoint ID string that identifies the endpoint device whose status has changed. For more information about **EDataFlow**, see [Device Events](device-events.md).

Legacy audio APIs such as DirectSound and the Windows multimedia functions have their own interfaces for enumerating and identifying audio devices. In Windows Vista, these interfaces have been extended to supply the endpoint ID strings that identify the endpoint devices that underlie the device abstractions presented by the APIs.

During DirectSound device enumeration, DirectSound supplies the endpoint ID string for each device that it enumerates. For more information, see [Audio Events for Legacy Audio Applications](audio-events-for-legacy-audio-applications.md).

To obtain the endpoint ID string for a legacy waveform device, use the [**waveOutMessage**](/previous-versions//dd743865(v=vs.85)) or [**waveInMessage**](/previous-versions//dd743846(v=vs.85)) function to send a DRV\_QUERYFUNCTIONINSTANCEID message to the waveform device driver. For a code example that shows the use of this message, see [Device Roles for Legacy Windows Multimedia Applications](device-roles-for-legacy-windows-multimedia-applications.md).

For more information about using the capabilities of the core audio APIs to enhance applications that use legacy audio APIs, see [Interoperability with Legacy Audio APIs](interoperability-with-legacy-audio-apis.md).

Clients should treat the contents of the endpoint ID string as opaque. That is, clients should not attempt to parse the contents of the string to obtain information about the device. The reason is that the string format is undefined and might change from one implementation of the MMDevice API system module to the next.

The lifetime of an endpoint ID string is tied to the device installation. The endpoint ID string of a device changes if the user upgrades the device driver, or if the user uninstalls the device, and installs it again. However, the endpoint ID string remains unchanged across system restarts, and the endpoint ID string of a USB audio device remains unchanged if the user unplugs the device and plugs it back in.

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> </dl>

 

 
