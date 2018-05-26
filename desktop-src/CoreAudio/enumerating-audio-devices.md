---
Description: Enumerating Audio Devices
ms.assetid: 20110ffc-5eff-4279-abea-53115803b6ee
title: Enumerating Audio Devices
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Audio Devices

The first task of a client audio application is to find a suitable audio device to use. The [MMDevice API](mmdevice-api.md) lets clients discover the [audio endpoint devices](audio-endpoint-devices.md) in the system and determine which devices are suitable for the application to use. This API enables clients to retrieve collections of the available endpoint devices and get the capabilities of each device. Header file Mmdeviceapi.h defines the interfaces in the MMDevice API.

An audio adapter might contain several devices—for example, a wave-rendering device and a wave-capture device. These are adapter devices rather than endpoint devices. As mentioned previously, adapter devices are registered by the Plug and Play manager, in contrast with endpoint devices, which are registered by the endpoint manager. Each adapter device typically supports one or more endpoint devices. A rendering endpoint device (for example, headphones) can receive a stream of audio data from a client application, and a capture endpoint device (for example, a microphone) can send an audio stream to a client application.

Before enumerating the endpoint devices in the system, the client must first call the Windows [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) function to create a device enumerator. A device enumerator is an object with an [**IMMDeviceEnumerator**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator?branch=master) interface. For information about **CoCreateInstance**, see the Windows SDK documentation.

The client calls the [**IMMDeviceEnumerator::EnumAudioEndpoints**](/windows/win32/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-enumaudioendpoints?branch=master) method to create a collection of endpoint objects. Each endpoint object represents an audio endpoint device in the system. In this call, the client specifies whether the collection should contain all of the rendering devices in the system, all of the capture devices, or both.

A device collection is an object with an [**IMMDeviceCollection**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immdevicecollection?branch=master) interface. Each item in a device collection is an endpoint object with at least the following two interfaces:

-   An [**IMMDevice**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immdevice?branch=master) interface. A client obtains a reference to the **IMMDevice** interface of an endpoint object in a device collection by calling the [**IMMDeviceCollection::Item**](/windows/win32/Mmdeviceapi/nf-mmdeviceapi-immdevicecollection-item?branch=master) method.
-   An [**IMMEndpoint**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immendpoint?branch=master) interface. A client obtains a reference to the **IMMEndpoint** interface of an endpoint object by calling the [**IMMDevice::QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) method.

After retrieving a collection of endpoint devices, the client can query the properties of the individual devices in the collection to determine their suitability for use. For a code example that shows how to enumerate endpoint devices and query their properties, see [Device Properties](device-properties.md).

After selecting a suitable device, the client can call the [**IMMDevice::Activate**](/windows/win32/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate?branch=master) method to activate the device-specific interfaces in [WASAPI](wasapi.md), the [DeviceTopology API](devicetopology-api.md), and the [EndpointVolume API](endpointvolume-api.md).

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> </dl>

 

 



