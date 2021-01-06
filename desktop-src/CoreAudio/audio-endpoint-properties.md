---
description: Audio Endpoint Properties
ms.assetid: db85ff3b-dbb1-4ed0-b663-21ca9eb66352
title: Audio Endpoint Properties
ms.topic: article
ms.date: 05/31/2018
---

# Audio Endpoint Properties

Header file Mmdeviceapi.h defines several properties of [audio endpoint devices](audio-endpoint-devices.md) in Windows Vista and later. The Windows audio service sets the values of these properties. Clients can read these properties, but should not set them. Property values are stored as **PROPVARIANT** structures.

The recommended way of reading the properties of an audio input device is to use the APIs in the [**Windows.Devices.Enumeration**](/uwp/api/Windows.Devices.Enumeration) namespace. These APIs are supported for Windows Store apps and desktop apps. For existing desktop apps that read device properties using the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface, see [Device Properties](device-properties.md). **IMMDevice** is not supported for Windows Store apps.

For code examples that show how to access the properties of an audio endpoint device, see the following topics:

-   [Device Events](device-events.md)
-   [Device Roles for DirectSound Applications](device-roles-for-directsound-applications.md)

For information about **PROPVARIANT**, see the Windows SDK documentation.

The following properties are specific to audio endpoint devices.



| Property                                                                                                            | Description                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PKEY\_AudioEndpoint\_Association**](pkey-audioendpoint-association.md)                                          | Associates a kernel-streaming (KS) pin category with an audio endpoint device.                                                                                |
| [**PKEY\_AudioEndpoint\_ControlPanelPageProvider**](pkey-audioendpoint-controlpanelpageprovider.md)                | Specifies the CLSID of the registered provider of the device-properties extension for the audio endpoint device.                                              |
| [**PKEY\_AudioEndpoint\_Disable\_SysFx**](pkey-audioendpoint-disable-sysfx.md)                                     | Indicates whether system effects are enabled in the shared-mode stream that flows to or from the audio endpoint device.                                       |
| [**PKEY\_AudioEndpoint\_FormFactor**](pkey-audioendpoint-formfactor.md)                                            | Indicates the physical attributes of the audio endpoint device.                                                                                               |
| [**PKEY\_AudioEndpoint\_FullRangeSpeakers**](pkey-audioendpoint-fullrangespeakers.md)                              | Specifies the channel-configuration mask for the full-range speakers that are connected to the audio endpoint device.                                         |
| [**PKEY\_AudioEndpoint\_GUID**](pkey-audioendpoint-guid.md)                                                        | Supplies the DirectSound device identifier that corresponds to the audio endpoint device.                                                                     |
| [**PKEY\_AudioEndpoint\_PhysicalSpeakers**](pkey-audioendpoint-physicalspeakers.md)                                | Defines the physical speaker configuration for the audio endpoint device.                                                                                     |
| [**PKEY\_AudioEngine\_DeviceFormat**](pkey-audioengine-deviceformat.md)                                            | Specifies the device format, which is the format that the audio engine uses for the shared-mode stream that flows to or from the audio endpoint device.       |
| [**PKEY\_AudioEngine\_OEMFormat**](pkey-audioengine-oemformat.md)<br/>                                       | Specifies the default format of the device that is used for rendering or capturing a stream. The values are populated by the OEM in an .inf file. <br/> |
| [**PKEY\_AudioEndpoint\_Supports\_EventDriven\_Mode**](pkey-audioendpoint-supports-eventdriven-mode.md)<br/> | Indicates whether the endpoint supports the event-driven mode. The values are populated by the OEM in an .inf file.<br/>                                |



 

The core audio APIs support additional properties that do not apply exclusively to audio endpoint devices. For more information about these additional properties, see [Device Properties](device-properties.md).

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

