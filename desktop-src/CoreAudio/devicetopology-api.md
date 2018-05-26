---
Description: DeviceTopology API
ms.assetid: 051311ef-dd29-4014-bb9c-4cdccf7ce7de
title: DeviceTopology API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DeviceTopology API

The DeviceTopology API provides client applications with the ability to traverse the functional hardware topologies of audio rendering and capture devices. Through the interfaces and methods in the DeviceTopology API, clients can discover the functional subunits (for example, volume control) that lie along the data paths that lead to and from [audio endpoint devices](audio-endpoint-devices.md). Clients can traverse the internal topologies of both audio adapter devices and audio endpoint devices and step across the connections that link one device to another. For more information, see [Device Topologies](device-topologies.md).

Header file Devicetopology.h defines the interfaces in the DeviceTopology API.

To access the DeviceTopology API interfaces, a client first obtains a reference to the [**IDeviceTopology**](/windows/win32/Devicetopology/nn-devicetopology-idevicetopology?branch=master) interface for an audio endpoint device by following these steps:

1.  By using one of the techniques described in [**IMMDevice Interface**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immdevice?branch=master), obtain a reference to the **IMMDevice** interface for an audio endpoint device.
2.  Call the [**IMMDevice::Activate**](/windows/win32/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate?branch=master) method with parameter *iid* set to **REFIID** IID\_IDeviceTopology.

The client can obtain references to the other interfaces in the DeviceTopology API by calling the methods in the [**IDeviceTopology**](/windows/win32/Devicetopology/nn-devicetopology-idevicetopology?branch=master) interface.

The DeviceTopology API implements the following interfaces.



| Interface                                                  | Description                                                                                                                                                                                                               |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioAutoGainControl**](/windows/win32/Devicetopology/nn-devicetopology-iaudioautogaincontrol?branch=master)     | Provides access to a hardware automatic gain control (AGC).                                                                                                                                                               |
| [**IAudioBass**](/windows/win32/Devicetopology/?branch=master)                           | Provides access to a hardware bass-level control.                                                                                                                                                                         |
| [**IAudioChannelConfig**](/windows/win32/Devicetopology/nn-devicetopology-iaudiochannelconfig?branch=master)         | Provides access to a hardware channel-configuration control.                                                                                                                                                              |
| [**IAudioInputSelector**](/windows/win32/Devicetopology/nn-devicetopology-iaudioinputselector?branch=master)         | Provides access to a hardware multiplexer control (input selector).                                                                                                                                                       |
| [**IAudioLoudness**](/windows/win32/Devicetopology/nn-devicetopology-iaudioloudness?branch=master)                   | Provides access to a "loudness" compensation control.                                                                                                                                                                     |
| [**IAudioMidrange**](/windows/win32/Devicetopology/?branch=master)                   | Provides access to a hardware midrange-level control.                                                                                                                                                                     |
| [**IAudioMute**](/windows/win32/Devicetopology/nn-devicetopology-iaudiomute?branch=master)                           | Provides access to a hardware mute control.                                                                                                                                                                               |
| [**IAudioOutputSelector**](/windows/win32/Devicetopology/nn-devicetopology-iaudiooutputselector?branch=master)       | Provides access to a hardware demultiplexer control (output selector).                                                                                                                                                    |
| [**IAudioPeakMeter**](/windows/win32/Devicetopology/nn-devicetopology-iaudiopeakmeter?branch=master)                 | Provides access to a hardware peak-meter control.                                                                                                                                                                         |
| [**IAudioTreble**](/windows/win32/Devicetopology/?branch=master)                       | Provides access to a hardware treble-level control.                                                                                                                                                                       |
| [**IAudioVolumeLevel**](/windows/win32/Devicetopology/?branch=master)             | Provides access to a hardware volume control.                                                                                                                                                                             |
| [**IConnector**](/windows/win32/Devicetopology/nn-devicetopology-iconnector?branch=master)                           | Represents a point of connection between components.                                                                                                                                                                      |
| [**IControlInterface**](/windows/win32/Devicetopology/nn-devicetopology-icontrolinterface?branch=master)             | Represents a control interface on a part (subunit or connector).                                                                                                                                                          |
| [**IDeviceSpecificProperty**](/windows/win32/Devicetopology/nn-devicetopology-idevicespecificproperty?branch=master) | Represents a device-specific property of a connector or subunit.                                                                                                                                                          |
| [**IDeviceTopology**](/windows/win32/Devicetopology/nn-devicetopology-idevicetopology?branch=master)                 | Provides access to the topology of an audio device.                                                                                                                                                                       |
| [**IKsFormatSupport**](/windows/win32/Devicetopology/nn-devicetopology-iksformatsupport?branch=master)               | Provides information about the audio data formats that are supported by a software-configured I/O connection (typically a DMA channel) between the audio device and system memory.                                        |
| [**IKsJackDescription**](/windows/win32/Devicetopology/nn-devicetopology-iksjackdescription?branch=master)           | Provides information about the jacks or internal connectors that provide a physical connection between a device on an audio adapter and an external or internal endpoint device (for example, a microphone or CD player). |
| [**IPart**](/windows/win32/Devicetopology/nn-devicetopology-ipart?branch=master)                                     | Represents a part (connector or subunit) of a device topology.                                                                                                                                                            |
| [**IPartsList**](/windows/win32/Devicetopology/nn-devicetopology-ipartslist?branch=master)                           | Represents a list of parts (connectors and subunits).                                                                                                                                                                     |
| [**IPerChannelDbLevel**](/windows/win32/Devicetopology/nn-devicetopology-iperchanneldblevel?branch=master)           | Represents a generic subunit control interface that provides per-channel control over the volume level, in decibels, of an audio stream or of a frequency band in an audio stream.                                        |
| [**ISubunit**](/windows/win32/Devicetopology/?branch=master)                               | Represents a hardware subunit (for example, a volume-level control) that lies in the data path between a client and an audio endpoint device.                                                                             |



 

DeviceTopology API clients that require notification of control-change events in connectors and subunits should implement the following interface.



| Interface                                            | Description                                                                      |
|------------------------------------------------------|----------------------------------------------------------------------------------|
| [**IControlChangeNotify**](/windows/win32/Devicetopology/nn-devicetopology-icontrolchangenotify?branch=master) | Provides notifications when the status of a part (connector or subunit) changes. |



 

## Related topics

<dl> <dt>

[Device Topologies](device-topologies.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



