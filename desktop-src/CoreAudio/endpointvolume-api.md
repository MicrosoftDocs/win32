---
description: EndpointVolume API
ms.assetid: 1fe1cd57-a0a4-4e08-ab52-3b6e66d14e79
title: EndpointVolume API
ms.topic: article
ms.date: 05/31/2018
---

# EndpointVolume API

The EndpointVolume API enables specialized clients to control and monitor the volume levels of [audio endpoint devices](audio-endpoint-devices.md). A client obtains references to the interfaces in the EndpointVolume API by obtaining the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface of an audio endpoint device and calling the [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate) method.

Header file Endpointvolume.h defines the interfaces in the EndpointVolume API.

Audio applications that use the [MMDevice API](mmdevice-api.md) and [WASAPI](wasapi.md) typically use the [**ISimpleAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-isimpleaudiovolume) interface to control volume levels on a per-session basis. Only two types of audio applications require the use of the EndpointVolume API. These application types are:

-   Applications that manage the master volume levels of audio endpoint devices, similar to the Windows volume-control program, Sndvol.exe.
-   Professional audio ("pro audio") applications that require exclusive-mode access to audio endpoint devices.

Inappropriate use of the EndpointVolume API can interfere with Windows audio policy and disrupt the user's system volume settings.

If an audio endpoint device implements hardware volume and mute controls, the EndpointVolume API uses those controls to manage the device volume. Otherwise, the EndpointVolume API implements the controls in software, transparently to the client.

If a device has hardware volume and mute controls, changes made to the device's volume and mute settings through the EndpointVolume API affect the volume level in both shared mode and exclusive mode. If a device lacks hardware volume and mute controls, changes made to the software volume and mute controls through the EndpointVolume API affect the volume level in shared mode, but not in exclusive mode. In exclusive mode, the client and the device exchange audio data directly, bypassing the software controls.

For applications that must manage hardware volume and mute controls, the EndpointVolume API offers two potential advantages over the [DeviceTopology API](devicetopology-api.md).

First, a number of audio adapter devices lack hardware volume controls. If a device lacks a hardware volume control, the [**IAudioEndpointVolume**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface in the EndpointVolume API automatically implements a software volume control on the stream to or from that device. For a client of the EndpointVolume API, the result is the same whether the volume control is implemented in hardware by the device or in software by the EndpointVolume API interface.

Second, even if the adapter device does implement hardware volume controls, an application that uses the DeviceTopology API to implement a topology-traversal algorithm might fail to find the control that it is looking for. Typically, such an application is designed to traverse the hardware topology of a particular device or set of related devices. The application risks failing if it attempts to traverse the topology of a device that it has not been specifically designed for or tested with.

Only specialized applications that must access hardware functions other than volume and mute controls require the use of the DeviceTopology API. For applications that require control only of the volume level of an exclusive-mode stream, the EndpointVolume API is simpler to use and works reliably with a wider range of audio hardware devices.

For code examples that use the interfaces in the EndpointVolume API, see the following topics:

-   [Endpoint Volume Controls](endpoint-volume-controls.md)
-   [Peak Meters](peak-meters.md)

To see a sample that uses the EndpointVolume API, see [EndpointVolume](endpointvolume.md) in the Windows SDK.

The EndpointVolume API implements the following interfaces.



| Interface                                                | Description                                                                             |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**IAudioEndpointVolume**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolume)     | Represents the volume controls on the audio stream to or from an audio endpoint device. |
| [**IAudioMeterInformation**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudiometerinformation) | Represents a peak meter on the audio stream to or from an audio endpoint device.        |



 

In addition, clients of the EndpointVolume API that require notification of volume and muting changes in audio endpoint devices should implement the following interface.



| Interface                                                            | Description                                                                                       |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**IAudioEndpointVolumeCallback**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback) | Provides notifications when the volume level or muting state of an audio endpoint device changes. |



 

## Related topics

<dl> <dt>

[Volume Controls](volume-controls.md)
</dt> <dt>

[**IMMDevice Interface**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice)
</dt> <dt>

[**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate)
</dt> <dt>

[**ISimpleAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-isimpleaudiovolume)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



