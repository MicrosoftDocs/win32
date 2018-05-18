---
Description: About WASAPI
ms.assetid: '452b9725-b0b9-4888-bbb5-a23e0067e840'
title: About WASAPI
---

# About WASAPI

The Windows Audio Session API (WASAPI) enables client applications to manage the flow of audio data between the application and an [audio endpoint device](audio-endpoint-devices.md).

Header files Audioclient.h and Audiopolicy.h define the WASAPI interfaces.

Every audio stream is a member of an [audio session](audio-sessions.md). Through the session abstraction, a WASAPI client can identify an audio stream as a member of a group of related audio streams. The system can manage all of the streams in the session as a single unit.

The audio engine is the [user-mode audio component](user-mode-audio-components.md) through which applications share access to an audio endpoint device. The audio engine transports audio data between an endpoint buffer and an endpoint device. To play an audio stream through a rendering endpoint device, an application periodically writes audio data to a rendering endpoint buffer. The audio engine mixes the streams from the various applications. To record an audio stream from a capture endpoint device, an application periodically reads audio data from a capture endpoint buffer.

WASAPI consists of several interfaces. The first of these is the [**IAudioClient**](iaudioclient.md) interface. To access the WASAPI interfaces, a client first obtains a reference to the **IAudioClient** interface of an audio endpoint device by calling the [**IMMDevice::Activate**](immdevice-activate.md) method with parameter *iid* set to **REFIID** IID\_IAudioClient. The client calls the [**IAudioClient::Initialize**](iaudioclient-initialize.md) method to initialize a stream on an endpoint device. After initializing a stream, the client can obtain references to the other WASAPI interfaces by calling the [**IAudioClient::GetService**](iaudioclient-getservice.md) method.

Many of the methods in WASAPI return error code AUDCLNT\_E\_DEVICE\_INVALIDATED if the audio endpoint device that a client application is using becomes invalid. Frequently, the application can recover from this error. For more information, see [Recovering from an Invalid-Device Error](recovering-from-an-invalid-device-error.md).

WASAPI implements the following interfaces.



| Interface                                            | Description                                                                                                                                                     |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioCaptureClient**](iaudiocaptureclient.md)   | Enables a client to read input data from a capture endpoint buffer.                                                                                             |
| [**IAudioClient**](iaudioclient.md)                 | Enables a client to create and initialize an audio stream between an audio application and the audio engine or the hardware buffer of an audio endpoint device. |
| [**IAudioClock**](iaudioclock.md)                   | Enables a client to monitor a stream's data rate and the current position in the stream.                                                                        |
| [**IAudioRenderClient**](iaudiorenderclient.md)     | Enables a client to write output data to a rendering endpoint buffer.                                                                                           |
| [**IAudioSessionControl**](iaudiosessioncontrol.md) | Enables a client to configure the control parameters for an audio session and to monitor events in the session.                                                 |
| [**IAudioSessionManager**](iaudiosessionmanager.md) | Enables a client to access the session controls and volume controls for both cross-process and process-specific audio sessions.                                 |
| [**IAudioStreamVolume**](iaudiostreamvolume.md)     | Enables a client to control and monitor the volume levels for all of the channels in an audio stream.                                                           |
| [**IChannelAudioVolume**](ichannelaudiovolume.md)   | Enables a client to control the volume levels for all of the channels in the audio session that the stream belongs to.                                          |
| [**ISimpleAudioVolume**](isimpleaudiovolume.md)     | Enables a client to control the master volume level of an audio session.                                                                                        |



 

WASAPI clients that require notification of session-related events should implement the following interface.



| Interface                                          | Description                                                                                                            |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**IAudioSessionEvents**](iaudiosessionevents.md) | Provides notifications of session-related events such as changes in the volume level, display name, and session state. |



 

## Related topics

<dl> <dt>

[Stream Management](stream-management.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



