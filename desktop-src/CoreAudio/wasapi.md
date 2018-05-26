---
Description: About WASAPI
ms.assetid: 452b9725-b0b9-4888-bbb5-a23e0067e840
title: About WASAPI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About WASAPI

The Windows Audio Session API (WASAPI) enables client applications to manage the flow of audio data between the application and an [audio endpoint device](audio-endpoint-devices.md).

Header files Audioclient.h and Audiopolicy.h define the WASAPI interfaces.

Every audio stream is a member of an [audio session](audio-sessions.md). Through the session abstraction, a WASAPI client can identify an audio stream as a member of a group of related audio streams. The system can manage all of the streams in the session as a single unit.

The audio engine is the [user-mode audio component](user-mode-audio-components.md) through which applications share access to an audio endpoint device. The audio engine transports audio data between an endpoint buffer and an endpoint device. To play an audio stream through a rendering endpoint device, an application periodically writes audio data to a rendering endpoint buffer. The audio engine mixes the streams from the various applications. To record an audio stream from a capture endpoint device, an application periodically reads audio data from a capture endpoint buffer.

WASAPI consists of several interfaces. The first of these is the [**IAudioClient**](/windows/win32/Audioclient/nn-audioclient-iaudioclient?branch=master) interface. To access the WASAPI interfaces, a client first obtains a reference to the **IAudioClient** interface of an audio endpoint device by calling the [**IMMDevice::Activate**](/windows/win32/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate?branch=master) method with parameter *iid* set to **REFIID** IID\_IAudioClient. The client calls the [**IAudioClient::Initialize**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-initialize?branch=master) method to initialize a stream on an endpoint device. After initializing a stream, the client can obtain references to the other WASAPI interfaces by calling the [**IAudioClient::GetService**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getservice?branch=master) method.

Many of the methods in WASAPI return error code AUDCLNT\_E\_DEVICE\_INVALIDATED if the audio endpoint device that a client application is using becomes invalid. Frequently, the application can recover from this error. For more information, see [Recovering from an Invalid-Device Error](recovering-from-an-invalid-device-error.md).

WASAPI implements the following interfaces.



| Interface                                            | Description                                                                                                                                                     |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioCaptureClient**](/windows/win32/Audioclient/nn-audioclient-iaudiocaptureclient?branch=master)   | Enables a client to read input data from a capture endpoint buffer.                                                                                             |
| [**IAudioClient**](/windows/win32/Audioclient/nn-audioclient-iaudioclient?branch=master)                 | Enables a client to create and initialize an audio stream between an audio application and the audio engine or the hardware buffer of an audio endpoint device. |
| [**IAudioClock**](/windows/win32/Audioclient/nn-audioclient-iaudioclock?branch=master)                   | Enables a client to monitor a stream's data rate and the current position in the stream.                                                                        |
| [**IAudioRenderClient**](/windows/win32/Audioclient/nn-audioclient-iaudiorenderclient?branch=master)     | Enables a client to write output data to a rendering endpoint buffer.                                                                                           |
| [**IAudioSessionControl**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol?branch=master) | Enables a client to configure the control parameters for an audio session and to monitor events in the session.                                                 |
| [**IAudioSessionManager**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionmanager?branch=master) | Enables a client to access the session controls and volume controls for both cross-process and process-specific audio sessions.                                 |
| [**IAudioStreamVolume**](/windows/win32/Audioclient/nn-audioclient-iaudiostreamvolume?branch=master)     | Enables a client to control and monitor the volume levels for all of the channels in an audio stream.                                                           |
| [**IChannelAudioVolume**](/windows/win32/Audioclient/nn-audioclient-ichannelaudiovolume?branch=master)   | Enables a client to control the volume levels for all of the channels in the audio session that the stream belongs to.                                          |
| [**ISimpleAudioVolume**](/windows/win32/Audioclient/nn-audioclient-isimpleaudiovolume?branch=master)     | Enables a client to control the master volume level of an audio session.                                                                                        |



 

WASAPI clients that require notification of session-related events should implement the following interface.



| Interface                                          | Description                                                                                                            |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master) | Provides notifications of session-related events such as changes in the volume level, display name, and session state. |



 

## Related topics

<dl> <dt>

[Stream Management](stream-management.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



