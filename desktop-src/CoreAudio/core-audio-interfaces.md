---
Description: This programming reference for the Core Audio SDK includes the following interfaces
ms.assetid: b18e2094-e974-4c23-b70b-ace5a168132d
title: Core Audio Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Core Audio Interfaces

This programming reference for the Core Audio SDK includes the following interfaces:

## MMDevice API

The Windows Multimedia Device (MMDevice) API enables audio clients to discover [audio endpoint devices](audio-endpoint-devices.md), determine their capabilities, and create driver instances for those devices.Header file Mmdeviceapi.h defines the interfaces in the MMDevice API. For more information, see [About MMDevice API](mmdevice-api.md).

The following table lists the MMDevice interfaces available with the Core Audio SDK for Windows Vista.



| Interface                                              | Description                                                                                                                                                                                    |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMMDevice**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immdevice?branch=master)                         | Represents an audio device.                                                                                                                                                                    |
| [**IMMDeviceCollection**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immdevicecollection?branch=master)     | Represents a collection of audio devices.                                                                                                                                                      |
| [**IMMDeviceEnumerator**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator?branch=master)     | Provides methods for enumerating audio devices.                                                                                                                                                |
| [**IMMEndpoint**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immendpoint?branch=master)                     | Represents an audio endpoint device.                                                                                                                                                           |
| [**IMMNotificationClient**](/windows/win32/Mmdeviceapi/nn-mmdeviceapi-immnotificationclient?branch=master) | Provides notifications when an audio endpoint device is added or removed, when the state or properties of a device change, or when there is a change in the default role assigned to a device. |



 

## WASAPI

The Windows Audio Session API (WASAPI) enables client applications to manage the flow of audio data between the application and an [audio endpoint device](audio-endpoint-devices.md). Header files Audioclient.h and Audiopolicy.h define the WASAPI interfaces. For more information, see [About WASAPI](wasapi.md).

The following table lists the WASAPI interfaces available with the Core Audio SDK for Windows Vista and later.



| Interface                                                                                    | Description                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IActivateAudioInterfaceAsyncOperation**](/windows/win32/mmdeviceapi/nn-mmdeviceapi-iactivateaudiointerfaceasyncoperation?branch=master)       | Represents an asynchronous operation activating a [WASAPI](wasapi.md) interface and provides a method to retrieve the results of the activation.<br/> Applies beginning with Windows 8.<br/> |
| [**IActivateAudioInterfaceCompletionHandler**](/windows/win32/mmdeviceapi/nn-mmdeviceapi-iactivateaudiointerfacecompletionhandler?branch=master) | Provides a callback to indicate that activation of a [WASAPI](wasapi.md) interface is complete.<br/> Applies beginning with Windows 8.<br/>                                                  |
| [**IAudioCaptureClient**](/windows/win32/Audioclient/nn-audioclient-iaudiocaptureclient?branch=master)                                           | Enables a client to read input data from a capture endpoint buffer.                                                                                                                                       |
| [**IAudioClient**](/windows/win32/Audioclient/nn-audioclient-iaudioclient?branch=master)                                                         | Enables a client to create and initialize an audio stream between an audio application and the audio engine or the hardware buffer of an audio endpoint device.                                           |
| [**IAudioClock**](/windows/win32/Audioclient/nn-audioclient-iaudioclock?branch=master)                                                           | Enables a client to monitor a stream's data rate and the current position in the stream.                                                                                                                  |
| [**IAudioClock2**](/windows/win32/audioclient/nn-audioclient-iaudioclock2?branch=master)<br/>                                              | Enables a client to get the current device position.<br/>                                                                                                                                           |
| [**IAudioClockAdjustment**](/windows/win32/audioclient/nn-audioclient-iaudioclockadjustment?branch=master)<br/>                            | Enables a client to set the sample rate of a stream.<br/>                                                                                                                                           |
| [**IAudioRenderClient**](/windows/win32/Audioclient/nn-audioclient-iaudiorenderclient?branch=master)                                             | Enables a client to write output data to a rendering endpoint buffer.                                                                                                                                     |
| [**IAudioSessionControl**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol?branch=master)                                         | Enables a client to configure the control parameters for an audio session and to monitor events in the session.                                                                                           |
| [**IAudioSessionControl2**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessioncontrol2?branch=master)<br/>                            | Enables a client to get information about the audio session.<br/>                                                                                                                                   |
| [**IAudioSessionManager**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionmanager?branch=master)                                         | Enables a client to access the session controls and volume controls for both cross-process and process-specific audio sessions.                                                                           |
| [**IAudioSessionManager2**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessionmanager2?branch=master)<br/>                            | Manages all submixes including enumeration and notification of submixes. It also provides support for ducking notifications.<br/>                                                                   |
| [**IAudioSessionEnumerator**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessionenumerator?branch=master)<br/>                        | Enables a client to enumerate audio sessions.<br/>                                                                                                                                                  |
| [**IAudioStreamVolume**](/windows/win32/Audioclient/nn-audioclient-iaudiostreamvolume?branch=master)                                             | Enables a client to control and monitor the volume levels for all of the channels in an audio stream.                                                                                                     |
| [**IChannelAudioVolume**](/windows/win32/Audioclient/nn-audioclient-ichannelaudiovolume?branch=master)                                           | Enables a client to control the volume levels for all of the channels in the audio session that the stream belongs to.                                                                                    |
| [**ISimpleAudioVolume**](/windows/win32/Audioclient/nn-audioclient-isimpleaudiovolume?branch=master)                                             | Enables a client to control the master volume level of an audio session.                                                                                                                                  |
| [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master)                                           | Provides notifications of session-related events such as changes in the volume level, display name, and session state.                                                                                    |
| [**IAudioSessionNotification**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessionnotification?branch=master)<br/>                    | Sends notifications when session changes occur. <br/>                                                                                                                                               |
| [**IAudioVolumeDuckNotification**](/windows/win32/AudioPolicy/nn-audiopolicy-iaudiovolumeducknotification?branch=master)<br/>              | Sends notifications about pending system ducking changes.<br/>                                                                                                                                      |



 

## DeviceTopology API

The DeviceTopology API provides client applications with the ability to traverse the functional hardware topologies of audio rendering and capture devices. Header file Devicetopology.h defines the interfaces in the DeviceTopology API. For more information, see [Device Topologies](device-topologies.md) and [**DeviceTopology API**](/windows/win32/Devicetopology/nn-devicetopology-idevicetopology?branch=master).

The following table lists the DeviceTopology interfaces available with the Core Audio SDK for Windows Vista and later.



| Interface                                                           | Description                                                                                                                                                                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioAutoGainControl**](/windows/win32/Devicetopology/nn-devicetopology-iaudioautogaincontrol?branch=master)              | Provides access to a hardware automatic gain control (AGC).                                                                                                                                                               |
| [**IAudioBass**](/windows/win32/Devicetopology/?branch=master)                                    | Provides access to a hardware bass-level control.                                                                                                                                                                         |
| [**IAudioChannelConfig**](/windows/win32/Devicetopology/nn-devicetopology-iaudiochannelconfig?branch=master)                  | Provides access to a hardware channel-configuration control.                                                                                                                                                              |
| [**IAudioInputSelector**](/windows/win32/Devicetopology/nn-devicetopology-iaudioinputselector?branch=master)                  | Provides access to a hardware multiplexer control (input selector).                                                                                                                                                       |
| [**IAudioLoudness**](/windows/win32/Devicetopology/nn-devicetopology-iaudioloudness?branch=master)                            | Provides access to a "loudness" compensation control.                                                                                                                                                                     |
| [**IAudioMidrange**](/windows/win32/Devicetopology/?branch=master)                            | Provides access to a hardware midrange-level control.                                                                                                                                                                     |
| [**IAudioMute**](/windows/win32/Devicetopology/nn-devicetopology-iaudiomute?branch=master)                                    | Provides access to a hardware mute control.                                                                                                                                                                               |
| [**IAudioOutputSelector**](/windows/win32/Devicetopology/nn-devicetopology-iaudiooutputselector?branch=master)                | Provides access to a hardware demultiplexer control (output selector).                                                                                                                                                    |
| [**IAudioPeakMeter**](/windows/win32/Devicetopology/nn-devicetopology-iaudiopeakmeter?branch=master)                          | Provides access to a hardware peak-meter control.                                                                                                                                                                         |
| [**IAudioTreble**](/windows/win32/Devicetopology/?branch=master)                                | Provides access to a hardware treble-level control.                                                                                                                                                                       |
| [**IAudioVolumeLevel**](/windows/win32/Devicetopology/?branch=master)                      | Provides access to a hardware volume control.                                                                                                                                                                             |
| [**IConnector**](/windows/win32/Devicetopology/nn-devicetopology-iconnector?branch=master)                                    | Represents a point of connection between components.                                                                                                                                                                      |
| [**IControlInterface**](/windows/win32/Devicetopology/nn-devicetopology-icontrolinterface?branch=master)                      | Represents a control interface on a part (subunit or connector).                                                                                                                                                          |
| [**IDeviceSpecificProperty**](/windows/win32/Devicetopology/nn-devicetopology-idevicespecificproperty?branch=master)          | Represents a device-specific property of a connector or subunit.                                                                                                                                                          |
| [**IDeviceTopology**](/windows/win32/Devicetopology/nn-devicetopology-idevicetopology?branch=master)                          | Provides access to the topology of an audio device.                                                                                                                                                                       |
| [**IKsFormatSupport**](/windows/win32/Devicetopology/nn-devicetopology-iksformatsupport?branch=master)                        | Provides information about the audio data formats that are supported by a software-configured I/O connection (typically a DMA channel) between the audio device and system memory.                                        |
| [**IKsJackDescription**](/windows/win32/Devicetopology/nn-devicetopology-iksjackdescription?branch=master)                    | Provides information about the jacks or internal connectors that provide a physical connection between a device on an audio adapter and an external or internal endpoint device (for example, a microphone or CD player). |
| [**IKsJackDescription2**](/windows/win32/Devicetopology/nn-devicetopology-iksjackdescription2?branch=master)<br/>       | Provides convenient access to the **KSPROPERTY\_JACK\_DESCRIPTION2** property of a connector to an endpoint device.<br/>                                                                                            |
| [**IKsJackSinkInformation**](/windows/win32/Devicetopology/nn-devicetopology-iksjacksinkinformation?branch=master)<br/> | Provides information about the jack sink if the jack is supported by the hardware.<br/>                                                                                                                             |
| [**IPart**](/windows/win32/Devicetopology/nn-devicetopology-ipart?branch=master)                                              | Represents a part (connector or subunit) of a device topology.                                                                                                                                                            |
| [**IPartsList**](/windows/win32/Devicetopology/nn-devicetopology-ipartslist?branch=master)                                    | Represents a list of parts (connectors and subunits).                                                                                                                                                                     |
| [**IPerChannelDbLevel**](/windows/win32/Devicetopology/nn-devicetopology-iperchanneldblevel?branch=master)                    | Represents a generic subunit control interface that provides per-channel control over the volume level, in decibels, of an audio stream or of a frequency band in an audio stream.                                        |
| [**ISubunit**](/windows/win32/Devicetopology/?branch=master)                                        | Represents a hardware subunit (for example, a volume-level control) that lies in the data path between a client and an audio endpoint device.                                                                             |
| [**IControlChangeNotify**](/windows/win32/Devicetopology/nn-devicetopology-icontrolchangenotify?branch=master)                | Provides notifications when the status of a part (connector or subunit) changes.                                                                                                                                          |



 

## EndpointVolume API

The EndpointVolume API enables specialized clients to control and monitor the volume levels of [audio endpoint devices](audio-endpoint-devices.md). Header file Endpointvolume.h defines the interfaces in the EndpointVolume API. For more information, see [**EndpointVolume API**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolume?branch=master) .

The following table lists the EndpointVolume interfaces available with the Core Audio SDK for Windows Vista.



| **Interface**                                                        | **Description**                                                                                   |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**IAudioEndpointVolume**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolume?branch=master)                 | Represents the volume controls on the audio stream to or from an audio endpoint device.           |
| [**IAudioEndpointVolumeEx**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolumeex?branch=master)<br/>  | Provides volume controls on the audio stream to or from a device endpoint.<br/>             |
| [**IAudioMeterInformation**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudiometerinformation?branch=master)             | Represents a peak meter on the audio stream to or from an audio endpoint device.                  |
| [**IAudioEndpointVolumeCallback**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback?branch=master) | Provides notifications when the volume level or muting state of an audio endpoint device changes. |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> </dl>

 

 




