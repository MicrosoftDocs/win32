---
description: Enumerating Audio Devices
ms.assetid: 20110ffc-5eff-4279-abea-53115803b6ee
title: Enumerating Audio Devices
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Audio Devices

The first task of a client audio application is to find a suitable audio device to use. The [MMDevice API](mmdevice-api.md) lets clients discover the [audio endpoint devices](audio-endpoint-devices.md) in the system and determine which devices are suitable for the application to use. This API enables clients to retrieve collections of the available endpoint devices and get the capabilities of each device. Header file Mmdeviceapi.h defines the interfaces in the MMDevice API.

An audio adapter might contain several devices—for example, a wave-rendering device and a wave-capture device. These are adapter devices rather than endpoint devices. As mentioned previously, adapter devices are registered by the Plug and Play manager, in contrast with endpoint devices, which are registered by the endpoint manager. Each adapter device typically supports one or more endpoint devices. A rendering endpoint device (for example, headphones) can receive a stream of audio data from a client application, and a capture endpoint device (for example, a microphone) can send an audio stream to a client application.

Before enumerating the endpoint devices in the system, the client must first call the Windows [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function to create a device enumerator. A device enumerator is an object with an [**IMMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) interface. For information about **CoCreateInstance**, see the Windows SDK documentation.

The client calls the [**IMMDeviceEnumerator::EnumAudioEndpoints**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-enumaudioendpoints) method to create a collection of endpoint objects. Each endpoint object represents an audio endpoint device in the system. In this call, the client specifies whether the collection should contain all of the rendering devices in the system, all of the capture devices, or both.

A device collection is an object with an [**IMMDeviceCollection**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevicecollection) interface. Each item in a device collection is an endpoint object with at least the following two interfaces:

-   An [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface. A client obtains a reference to the **IMMDevice** interface of an endpoint object in a device collection by calling the [**IMMDeviceCollection::Item**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevicecollection-item) method.
-   An [**IMMEndpoint**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immendpoint) interface. A client obtains a reference to the **IMMEndpoint** interface of an endpoint object by calling the [**IMMDevice::QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) method.

After retrieving a collection of endpoint devices, the client can query the properties of the individual devices in the collection to determine their suitability for use. For a code example that shows how to enumerate endpoint devices and query their properties, see [Device Properties](device-properties.md).

After selecting a suitable device, the client can call the [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate) method to activate the device-specific interfaces in [WASAPI](wasapi.md), the [DeviceTopology API](devicetopology-api.md), and the [EndpointVolume API](endpointvolume-api.md).

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> </dl>

 

 
