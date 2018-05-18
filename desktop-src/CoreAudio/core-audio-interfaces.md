---
Description: 'This programming reference for the Core Audio SDK includes the following interfaces:'
ms.assetid: 'b18e2094-e974-4c23-b70b-ace5a168132d'
title: Core Audio Interfaces
---

# Core Audio Interfaces

This programming reference for the Core Audio SDK includes the following interfaces:

## MMDevice API

The Windows Multimedia Device (MMDevice) API enables audio clients to discover [audio endpoint devices](audio-endpoint-devices.md), determine their capabilities, and create driver instances for those devices.Header file Mmdeviceapi.h defines the interfaces in the MMDevice API. For more information, see [About MMDevice API](mmdevice-api.md).

The following table lists the MMDevice interfaces available with the Core Audio SDK for Windows Vista.



| Interface                                              | Description                                                                                                                                                                                    |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMMDevice**](immdevice.md)                         | Represents an audio device.                                                                                                                                                                    |
| [**IMMDeviceCollection**](immdevicecollection.md)     | Represents a collection of audio devices.                                                                                                                                                      |
| [**IMMDeviceEnumerator**](immdeviceenumerator.md)     | Provides methods for enumerating audio devices.                                                                                                                                                |
| [**IMMEndpoint**](immendpoint.md)                     | Represents an audio endpoint device.                                                                                                                                                           |
| [**IMMNotificationClient**](immnotificationclient.md) | Provides notifications when an audio endpoint device is added or removed, when the state or properties of a device change, or when there is a change in the default role assigned to a device. |



 

## WASAPI

The Windows Audio Session API (WASAPI) enables client applications to manage the flow of audio data between the application and an [audio endpoint device](audio-endpoint-devices.md). Header files Audioclient.h and Audiopolicy.h define the WASAPI interfaces. For more information, see [About WASAPI](wasapi.md).

The following table lists the WASAPI interfaces available with the Core Audio SDK for Windows Vista and later.



| Interface                                                                                    | Description                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IActivateAudioInterfaceAsyncOperation**](iactivateaudiointerfaceasyncoperation.md)       | Represents an asynchronous operation activating a [WASAPI](wasapi.md) interface and provides a method to retrieve the results of the activation.<br/> Applies beginning with Windows 8.<br/> |
| [**IActivateAudioInterfaceCompletionHandler**](iactivateaudiointerfacecompletionhandler.md) | Provides a callback to indicate that activation of a [WASAPI](wasapi.md) interface is complete.<br/> Applies beginning with Windows 8.<br/>                                                  |
| [**IAudioCaptureClient**](iaudiocaptureclient.md)                                           | Enables a client to read input data from a capture endpoint buffer.                                                                                                                                       |
| [**IAudioClient**](iaudioclient.md)                                                         | Enables a client to create and initialize an audio stream between an audio application and the audio engine or the hardware buffer of an audio endpoint device.                                           |
| [**IAudioClock**](iaudioclock.md)                                                           | Enables a client to monitor a stream's data rate and the current position in the stream.                                                                                                                  |
| [**IAudioClock2**](iaudioclock2.md)<br/>                                              | Enables a client to get the current device position.<br/>                                                                                                                                           |
| [**IAudioClockAdjustment**](iaudioclockadjustment.md)<br/>                            | Enables a client to set the sample rate of a stream.<br/>                                                                                                                                           |
| [**IAudioRenderClient**](iaudiorenderclient.md)                                             | Enables a client to write output data to a rendering endpoint buffer.                                                                                                                                     |
| [**IAudioSessionControl**](iaudiosessioncontrol.md)                                         | Enables a client to configure the control parameters for an audio session and to monitor events in the session.                                                                                           |
| [**IAudioSessionControl2**](iaudiosessioncontrol2.md)<br/>                            | Enables a client to get information about the audio session.<br/>                                                                                                                                   |
| [**IAudioSessionManager**](iaudiosessionmanager.md)                                         | Enables a client to access the session controls and volume controls for both cross-process and process-specific audio sessions.                                                                           |
| [**IAudioSessionManager2**](iaudiosessionmanager2.md)<br/>                            | Manages all submixes including enumeration and notification of submixes. It also provides support for ducking notifications.<br/>                                                                   |
| [**IAudioSessionEnumerator**](iaudiosessionenumerator.md)<br/>                        | Enables a client to enumerate audio sessions.<br/>                                                                                                                                                  |
| [**IAudioStreamVolume**](iaudiostreamvolume.md)                                             | Enables a client to control and monitor the volume levels for all of the channels in an audio stream.                                                                                                     |
| [**IChannelAudioVolume**](ichannelaudiovolume.md)                                           | Enables a client to control the volume levels for all of the channels in the audio session that the stream belongs to.                                                                                    |
| [**ISimpleAudioVolume**](isimpleaudiovolume.md)                                             | Enables a client to control the master volume level of an audio session.                                                                                                                                  |
| [**IAudioSessionEvents**](iaudiosessionevents.md)                                           | Provides notifications of session-related events such as changes in the volume level, display name, and session state.                                                                                    |
| [**IAudioSessionNotification**](iaudiosessionnotification.md)<br/>                    | Sends notifications when session changes occur. <br/>                                                                                                                                               |
| [**IAudioVolumeDuckNotification**](iaudiovolumeducknotification.md)<br/>              | Sends notifications about pending system ducking changes.<br/>                                                                                                                                      |



 

## DeviceTopology API

The DeviceTopology API provides client applications with the ability to traverse the functional hardware topologies of audio rendering and capture devices. Header file Devicetopology.h defines the interfaces in the DeviceTopology API. For more information, see [Device Topologies](device-topologies.md) and [**DeviceTopology API**](idevicetopology.md).

The following table lists the DeviceTopology interfaces available with the Core Audio SDK for Windows Vista and later.



| Interface                                                           | Description                                                                                                                                                                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioAutoGainControl**](iaudioautogaincontrol.md)              | Provides access to a hardware automatic gain control (AGC).                                                                                                                                                               |
| [**IAudioBass**](iaudiobass.md)                                    | Provides access to a hardware bass-level control.                                                                                                                                                                         |
| [**IAudioChannelConfig**](iaudiochannelconfig.md)                  | Provides access to a hardware channel-configuration control.                                                                                                                                                              |
| [**IAudioInputSelector**](iaudioinputselector.md)                  | Provides access to a hardware multiplexer control (input selector).                                                                                                                                                       |
| [**IAudioLoudness**](iaudioloudness.md)                            | Provides access to a "loudness" compensation control.                                                                                                                                                                     |
| [**IAudioMidrange**](iaudiomidrange.md)                            | Provides access to a hardware midrange-level control.                                                                                                                                                                     |
| [**IAudioMute**](iaudiomute.md)                                    | Provides access to a hardware mute control.                                                                                                                                                                               |
| [**IAudioOutputSelector**](iaudiooutputselector.md)                | Provides access to a hardware demultiplexer control (output selector).                                                                                                                                                    |
| [**IAudioPeakMeter**](iaudiopeakmeter.md)                          | Provides access to a hardware peak-meter control.                                                                                                                                                                         |
| [**IAudioTreble**](iaudiotreble.md)                                | Provides access to a hardware treble-level control.                                                                                                                                                                       |
| [**IAudioVolumeLevel**](iaudiovolumelevel.md)                      | Provides access to a hardware volume control.                                                                                                                                                                             |
| [**IConnector**](iconnector.md)                                    | Represents a point of connection between components.                                                                                                                                                                      |
| [**IControlInterface**](icontrolinterface.md)                      | Represents a control interface on a part (subunit or connector).                                                                                                                                                          |
| [**IDeviceSpecificProperty**](idevicespecificproperty.md)          | Represents a device-specific property of a connector or subunit.                                                                                                                                                          |
| [**IDeviceTopology**](idevicetopology.md)                          | Provides access to the topology of an audio device.                                                                                                                                                                       |
| [**IKsFormatSupport**](iksformatsupport.md)                        | Provides information about the audio data formats that are supported by a software-configured I/O connection (typically a DMA channel) between the audio device and system memory.                                        |
| [**IKsJackDescription**](iksjackdescription.md)                    | Provides information about the jacks or internal connectors that provide a physical connection between a device on an audio adapter and an external or internal endpoint device (for example, a microphone or CD player). |
| [**IKsJackDescription2**](iksjackdescription2.md)<br/>       | Provides convenient access to the **KSPROPERTY\_JACK\_DESCRIPTION2** property of a connector to an endpoint device.<br/>                                                                                            |
| [**IKsJackSinkInformation**](iksjacksinkinformation.md)<br/> | Provides information about the jack sink if the jack is supported by the hardware.<br/>                                                                                                                             |
| [**IPart**](ipart.md)                                              | Represents a part (connector or subunit) of a device topology.                                                                                                                                                            |
| [**IPartsList**](ipartslist.md)                                    | Represents a list of parts (connectors and subunits).                                                                                                                                                                     |
| [**IPerChannelDbLevel**](iperchanneldblevel.md)                    | Represents a generic subunit control interface that provides per-channel control over the volume level, in decibels, of an audio stream or of a frequency band in an audio stream.                                        |
| [**ISubunit**](isubunit.md)                                        | Represents a hardware subunit (for example, a volume-level control) that lies in the data path between a client and an audio endpoint device.                                                                             |
| [**IControlChangeNotify**](icontrolchangenotify.md)                | Provides notifications when the status of a part (connector or subunit) changes.                                                                                                                                          |



 

## EndpointVolume API

The EndpointVolume API enables specialized clients to control and monitor the volume levels of [audio endpoint devices](audio-endpoint-devices.md). Header file Endpointvolume.h defines the interfaces in the EndpointVolume API. For more information, see [**EndpointVolume API**](iaudioendpointvolume.md) .

The following table lists the EndpointVolume interfaces available with the Core Audio SDK for Windows Vista.



| **Interface**                                                        | **Description**                                                                                   |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**IAudioEndpointVolume**](iaudioendpointvolume.md)                 | Represents the volume controls on the audio stream to or from an audio endpoint device.           |
| [**IAudioEndpointVolumeEx**](iaudioendpointvolumeex.md)<br/>  | Provides volume controls on the audio stream to or from a device endpoint.<br/>             |
| [**IAudioMeterInformation**](iaudiometerinformation.md)             | Represents a peak meter on the audio stream to or from an audio endpoint device.                  |
| [**IAudioEndpointVolumeCallback**](iaudioendpointvolumecallback.md) | Provides notifications when the volume level or muting state of an audio endpoint device changes. |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> </dl>

 

 




