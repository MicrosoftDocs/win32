---
description: This programming reference for the Core Audio SDK includes the following properties.
ms.assetid: db7d68c3-5642-4238-a212-88d3479ce73d
title: Core Audio Properties
ms.topic: article
ms.date: 05/31/2018
---

# Core Audio Properties

This programming reference for the Core Audio SDK includes the following properties.

## Audio Endpoint Properties

Core Audio SDK includes several properties of [audio endpoint devices](audio-endpoint-devices.md). For more information, see [Audio Endpoint Properties](audio-endpoint-properties.md).

The following properties are defined in Mmdeviceapi.h in Windows Vista and later.



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
| [**PKEY\_AudioEndpoint\_JackSubType**](pkey-audioendpoint-jacksubtype.md)<br/>                               | Contains an output category GUID for an audio endpoint device. <br/>                                                                                    |



 

## Device Properties

Core Audio SDK includes several device properties of [audio endpoint devices](audio-endpoint-devices.md). For more information, see [Device Properties](device-properties.md).

The following properties are defined in Functiondiscoverykeys\_devpkey.h in Windows Vista and later.



| Property                                                                         | Description                                                                                                                                                                                       |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PKEY\_DeviceInterface\_FriendlyName**](pkey-deviceinterface-friendlyname.md) | The friendly name of the audio adapter to which the endpoint device is attached (for example, "XYZ Audio Adapter").                                                                               |
| [**PKEY\_Device\_DeviceDesc**](pkey-device-devicedesc.md)                       | The device description of the endpoint device (for example, "Speakers").                                                                                                                          |
| [**PKEY\_Device\_FriendlyName**](pkey-device-friendlyname.md)                   | The friendly name of the endpoint device (for example, "Speakers (XYZ Audio Adapter)").                                                                                                           |
| **PKEY\_Device\_ContainerId**                                                    | Stores the container identifier of the PnP device that implements the audio endpoint. For more information about this property, see "Device Property Reference" in the Windows WDK documentation. |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> </dl>

 

 




