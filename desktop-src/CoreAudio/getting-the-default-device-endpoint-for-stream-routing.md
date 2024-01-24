---
description: In Windows 7, high-level platform APIs that use Core Audio APIs such as Media Foundation, DirectSound, and Wave APIs, implement the stream routing feature by handling stream switching from an existing device to a new default audio endpoint.
ms.assetid: 4f36710c-c5a8-4f31-9b77-5253475c0715
title: Getting the Device Endpoint for Stream Routing
ms.topic: article
ms.date: 05/31/2018
---

# Getting the Device Endpoint for Stream Routing

In Windows 7, high-level platform APIs that use Core Audio APIs such as Media Foundation, DirectSound, and Wave APIs, implement the stream routing feature by handling stream switching from an existing device to a new default audio endpoint. Media applications that use these APIs (for example, an application activating an **IDirectSound** or **IBaseFilter** object on an [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) object) use the stream routing behavior without any modifications to the source.

The high-level APIs implement stream routing for the device endpoint that is obtained through [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint). If an application streams to the default device, the stream routing feature operates as defined. Streams are not switched to the new device if it is retrieved by any other mechanism even if it is the same as the default device.

A media application that uses Core Audio APIs directly (WASAPI client) can provide a custom stream routing implementation for any rendering or capture device. A WASAPI client can replicate the implemetation provided by the high-level APIs by restricting it to streams that are opened on devices that are set as the default device. To get a reference to the default device's endpoint, the client must call [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint). In this call, the client must indicate whether it requires a pointer to the rendering default device or the capture default device by specifying the *dataFlow* parameter. The client must also specify the appropriate role for the endpoint in the **ERole** attribute (**eConsole** or **eCommunications**). Do not use **eMultimedia**.

If the application streams to any other device, the application can get the device by specifying an endpoint ID string (by calling [**IMMDeviceEnumerator::GetDevice**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdevice)).

After the device is identified, the WASAPI client can provide the implementation for stream routing by handling the device and audio session notifications sent for the device. For more information about these notifications, see [Relevant Notifications for Stream Routing](relevant-device-notifications-for-stream-routing.md).

## Related topics

<dl> <dt>

[About MMDevice API](mmdevice-api.md)
</dt> <dt>

[About WASAPI](wasapi.md)
</dt> <dt>

[Stream Routing](stream-routing.md)
</dt> </dl>

 

 



