---
description: About WASAPI
ms.assetid: 452b9725-b0b9-4888-bbb5-a23e0067e840
title: About WASAPI
ms.topic: concept-article
ms.date: 05/31/2018
---

# About WASAPI

The Windows Audio Session API (WASAPI) enables client applications to manage the flow of audio data between the application and an [audio endpoint device](audio-endpoint-devices.md).

The WASAPI interfaces are defined in the header files, Audioclient.h and Audiopolicy.h.

Every audio stream is a member of an [audio session](audio-sessions.md). Through the session abstraction, a WASAPI client can identify an audio stream as a member of a group of related audio streams. The system can manage all of the streams in the session as a single unit.

The audio engine is the [user-mode audio component](user-mode-audio-components.md) through which applications share access to an audio endpoint device. The audio engine transports audio data between an endpoint buffer and an endpoint device. To play an audio stream through a rendering endpoint device, an application periodically writes audio data to a rendering endpoint buffer. The audio engine mixes the streams from the various applications. To record an audio stream from a capture endpoint device, an application periodically reads audio data from a capture endpoint buffer.

WASAPI consists of several interfaces. The first of these is the [**IAudioClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient) interface. To access the WASAPI interfaces, a client first obtains a reference to the **IAudioClient** interface of an audio endpoint device by calling the [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate) method with parameter *iid* set to **REFIID** IID\_IAudioClient. The client calls the [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) method to initialize a stream on an endpoint device. After initializing a stream, the client can obtain references to the other WASAPI interfaces by calling the [**IAudioClient::GetService**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getservice) method.

Many of the methods in WASAPI return error code AUDCLNT\_E\_DEVICE\_INVALIDATED if the audio endpoint device that a client application is using becomes invalid. Frequently, the application can recover from this error. For more information, see [Recovering from an Invalid-Device Error](recovering-from-an-invalid-device-error.md).

WASAPI implements the following interfaces.



| Interface                                            | Description                                                                                                                                                     |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAcousticEchoCancellationControl**](/windows/desktop/api/Audioclient/nn-audioclient-iacousticechocancellationcontrol) | Provides a mechanism for determining if an audio capture endpoint supports acoustic echo cancellation (AEC) and, if so, allows the client to set the audio render endpoint that should be used as the reference stream. |
| [**IAudioCaptureClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiocaptureclient)   | Enables a client to read input data from a capture endpoint buffer.                                                                                             |
| [**IAudioClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient)                 | Enables a client to create and initialize an audio stream between an audio application and the audio engine or the hardware buffer of an audio endpoint device. |
| [**IAudioClient2**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient2)               | Enables a client to opt in for offloading, query stream properties, and get information from the hardware that handles offloading.                             |
| [**IAudioClient3**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient3)               | Enables a client to query for the audio engine's supported periodicities and current periodicity as well as request initialization of a shared audio stream with a specified periodicity. |
| [**IAudioClientDuckingControl**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclientduckingcontrol) | Provides a method that allows an app to specify that the system shouldn't duck the audio of other streams when the app's audio render stream is active.      |
| [**IAudioClock**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclock)                   | Enables a client to monitor a stream's data rate and the current position in the stream.                                                                        |
| [**IAudioClock2**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclock2)                 | Enables a client to get the current device position.                                                                                                            |
| [**IAudioClockAdjustment**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclockadjustment) | Enables a client to adjust the sample rate of a stream.                                                                                                       |
| [**IAudioEffectsManager**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioeffectsmanager) | Provides management functionality for the audio effects pipeline.                                                                                               |
| [**IAudioRenderClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiorenderclient)     | Enables a client to write output data to a rendering endpoint buffer.                                                                                           |
| [**IAudioSessionControl**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol) | Enables a client to configure the control parameters for an audio session and to monitor events in the session.                                                 |
| [**IAudioSessionManager**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionmanager) | Enables a client to access the session controls and volume controls for both cross-process and process-specific audio sessions.                                 |
| [**IAudioStreamVolume**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiostreamvolume)     | Enables a client to control and monitor the volume levels for all of the channels in an audio stream.                                                           |
| [**IAudioViewManagerService**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioviewmanagerservice) | Provides APIs for associating an HWND with an audio stream.                                                                                                   |
| [**IChannelAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-ichannelaudiovolume)   | Enables a client to control the volume levels for all of the channels in the audio session that the stream belongs to.                                          |
| [**ISimpleAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-isimpleaudiovolume)     | Enables a client to control the master volume level of an audio session.                                                                                        |

WASAPI clients that require notification of session-related events should implement the following interface.

| Interface                                          | Description                                                                                                            |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**IAudioEffectsChangedNotificationClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioeffectschangednotificationclient) | A callback interface that allows applications to receive notifications when the list of audio effects changes or the resources needed to enable an effect changes. |
| [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) | Provides notifications of session-related events such as changes in the volume level, display name, and session state. |

## Related topics

[Stream Management](stream-management.md)

[**Programming Reference**](programming-reference.md)

 

 



