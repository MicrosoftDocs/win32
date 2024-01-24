---
description: DeviceTopology API
ms.assetid: 051311ef-dd29-4014-bb9c-4cdccf7ce7de
title: DeviceTopology API
ms.topic: article
ms.date: 05/31/2018
ms.custom: project-verbatim
---

# DeviceTopology API

See the [Microsoft high quality voice capture DMO sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/audio/aecmicarray).

The DeviceTopology API provides client applications with the ability to traverse the functional hardware topologies of audio rendering and capture devices. Through the interfaces and methods in the DeviceTopology API, clients can discover the functional subunits (for example, volume control) that lie along the data paths that lead to and from [audio endpoint devices](audio-endpoint-devices.md). Clients can traverse the internal topologies of both audio adapter devices and audio endpoint devices and step across the connections that link one device to another. For more information, see [Device Topologies](device-topologies.md).

Header file Devicetopology.h defines the interfaces in the DeviceTopology API.

To access the DeviceTopology API interfaces, a client first obtains a reference to the [**IDeviceTopology**](/windows/desktop/api/Devicetopology/nn-devicetopology-idevicetopology) interface for an audio endpoint device by following these steps:

1.  By using one of the techniques described in [**IMMDevice Interface**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice), obtain a reference to the **IMMDevice** interface for an audio endpoint device.
2.  Call the [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate) method with parameter *iid* set to **REFIID** IID\_IDeviceTopology.

The client can obtain references to the other interfaces in the DeviceTopology API by calling the methods in the [**IDeviceTopology**](/windows/desktop/api/Devicetopology/nn-devicetopology-idevicetopology) interface.

The DeviceTopology API implements the following interfaces.



| Interface                                                  | Description                                                                                                                                                                                                               |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioAutoGainControl**](/windows/desktop/api/Devicetopology/nn-devicetopology-iaudioautogaincontrol)     | Provides access to a hardware automatic gain control (AGC).                                                                                                                                                               |
| [**IAudioBass**](/windows/win32/api/devicetopology/nn-devicetopology-iaudiobass)                           | Provides access to a hardware bass-level control.                                                                                                                                                                         |
| [**IAudioChannelConfig**](/windows/desktop/api/Devicetopology/nn-devicetopology-iaudiochannelconfig)         | Provides access to a hardware channel-configuration control.                                                                                                                                                              |
| [**IAudioInputSelector**](/windows/desktop/api/Devicetopology/nn-devicetopology-iaudioinputselector)         | Provides access to a hardware multiplexer control (input selector).                                                                                                                                                       |
| [**IAudioLoudness**](/windows/desktop/api/Devicetopology/nn-devicetopology-iaudioloudness)                   | Provides access to a "loudness" compensation control.                                                                                                                                                                     |
| [**IAudioMidrange**](/windows/win32/api/devicetopology/nn-devicetopology-iaudiomidrange)                   | Provides access to a hardware midrange-level control.                                                                                                                                                                     |
| [**IAudioMute**](/windows/desktop/api/Devicetopology/nn-devicetopology-iaudiomute)                           | Provides access to a hardware mute control.                                                                                                                                                                               |
| [**IAudioOutputSelector**](/windows/desktop/api/Devicetopology/nn-devicetopology-iaudiooutputselector)       | Provides access to a hardware demultiplexer control (output selector).                                                                                                                                                    |
| [**IAudioPeakMeter**](/windows/desktop/api/Devicetopology/nn-devicetopology-iaudiopeakmeter)                 | Provides access to a hardware peak-meter control.                                                                                                                                                                         |
| [**IAudioTreble**](/windows/win32/api/devicetopology/nn-devicetopology-iaudiotreble)                       | Provides access to a hardware treble-level control.                                                                                                                                                                       |
| [**IAudioVolumeLevel**](/windows/win32/api/devicetopology/nn-devicetopology-iaudiovolumelevel)             | Provides access to a hardware volume control.                                                                                                                                                                             |
| [**IConnector**](/windows/desktop/api/Devicetopology/nn-devicetopology-iconnector)                           | Represents a point of connection between components.                                                                                                                                                                      |
| [**IControlInterface**](/windows/desktop/api/Devicetopology/nn-devicetopology-icontrolinterface)             | Represents a control interface on a part (subunit or connector).                                                                                                                                                          |
| [**IDeviceSpecificProperty**](/windows/desktop/api/Devicetopology/nn-devicetopology-idevicespecificproperty) | Represents a device-specific property of a connector or subunit.                                                                                                                                                          |
| [**IDeviceTopology**](/windows/desktop/api/Devicetopology/nn-devicetopology-idevicetopology)                 | Provides access to the topology of an audio device.                                                                                                                                                                       |
| [**IKsFormatSupport**](/windows/desktop/api/Devicetopology/nn-devicetopology-iksformatsupport)               | Provides information about the audio data formats that are supported by a software-configured I/O connection (typically a DMA channel) between the audio device and system memory.                                        |
| [**IKsJackDescription**](/windows/desktop/api/Devicetopology/nn-devicetopology-iksjackdescription)           | Provides information about the jacks or internal connectors that provide a physical connection between a device on an audio adapter and an external or internal endpoint device (for example, a microphone or CD player). |
| [**IPart**](/windows/desktop/api/Devicetopology/nn-devicetopology-ipart)                                     | Represents a part (connector or subunit) of a device topology.                                                                                                                                                            |
| [**IPartsList**](/windows/desktop/api/Devicetopology/nn-devicetopology-ipartslist)                           | Represents a list of parts (connectors and subunits).                                                                                                                                                                     |
| [**IPerChannelDbLevel**](/windows/desktop/api/Devicetopology/nn-devicetopology-iperchanneldblevel)           | Represents a generic subunit control interface that provides per-channel control over the volume level, in decibels, of an audio stream or of a frequency band in an audio stream.                                        |
| [**ISubunit**](/windows/win32/api/devicetopology/nn-devicetopology-isubunit)                               | Represents a hardware subunit (for example, a volume-level control) that lies in the data path between a client and an audio endpoint device.                                                                             |



 

DeviceTopology API clients that require notification of control-change events in connectors and subunits should implement the following interface.



| Interface                                            | Description                                                                      |
|------------------------------------------------------|----------------------------------------------------------------------------------|
| [**IControlChangeNotify**](/windows/desktop/api/Devicetopology/nn-devicetopology-icontrolchangenotify) | Provides notifications when the status of a part (connector or subunit) changes. |



 

## Related topics

<dl> <dt>

[Device Topologies](device-topologies.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 
