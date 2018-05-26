---
Description: Stream Management
ms.assetid: 936d8d69-e86c-418b-b5b0-c4fbbfa1dd49
title: Stream Management
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Stream Management

After enumerating the [audio endpoint devices](audio-endpoint-devices.md) in the system and identifying a suitable rendering or capture device, the next task for an audio client application is to open a connection with the endpoint device and to manage the flow of audio data over that connection. [WASAPI](wasapi.md) enables clients to create and manage audio streams.

WASAPI implements several interfaces to provide stream-management services to audio clients. The primary interface is [**IAudioClient**](/windows/win32/Audioclient/nn-audioclient-iaudioclient?branch=master). A client obtains the **IAudioClient** interface for an audio endpoint device by calling the [**IMMDevice::Activate**](/windows/win32/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate?branch=master) method (with parameter *iid* set to **REFIID** IID\_IAudioClient) on the endpoint object.

The client calls the methods in the [**IAudioClient**](/windows/win32/Audioclient/nn-audioclient-iaudioclient?branch=master) interface to do the following:

-   Discover which audio formats the endpoint device supports.
-   Get the endpoint buffer size.
-   Get the stream format and latency.
-   Start, stop, and reset the stream that flows through the endpoint device.
-   Access additional audio services.

To create a stream, a client calls the [**IAudioClient::Initialize**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-initialize?branch=master) method. Through this method, the client specifies the data format for the stream, the size of the endpoint buffer, and whether the stream operates in shared or exclusive mode.

The remaining methods in the [**IAudioClient**](/windows/win32/Audioclient/nn-audioclient-iaudioclient?branch=master) interface fall into two groups:

-   Methods that can be called only after the stream has been opened by [**IAudioClient::Initialize**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-initialize?branch=master).
-   Methods that can be called at any time before or after the [**Initialize**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-initialize?branch=master) call.

The following methods can be called only after the call to [**IAudioClient::Initialize**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-initialize?branch=master):

-   [**IAudioClient::GetBufferSize**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getbuffersize?branch=master)
-   [**IAudioClient::GetCurrentPadding**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getcurrentpadding?branch=master)
-   [**IAudioClient::GetService**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getservice?branch=master)
-   [**IAudioClient::GetStreamLatency**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getstreamlatency?branch=master)
-   [**IAudioClient::Reset**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-reset?branch=master)
-   [**IAudioClient::Start**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-start?branch=master)
-   [**IAudioClient::Stop**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-stop?branch=master)

The following methods can be called before or after the [**IAudioClient::Initialize**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-initialize?branch=master) call:

-   [**IAudioClient::GetDevicePeriod**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getdeviceperiod?branch=master)
-   [**IAudioClient::GetMixFormat**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getmixformat?branch=master)
-   [**IAudioClient::IsFormatSupported**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-isformatsupported?branch=master)

To access the additional audio client services, the client calls the [**IAudioClient::GetService**](/windows/win32/Audioclient/nf-audioclient-iaudioclient-getservice?branch=master) method. Through this method, the client can obtain references to the following interfaces:

-   [**IAudioRenderClient**](/windows/win32/Audioclient/nn-audioclient-iaudiorenderclient?branch=master)

    Writes rendering data to an audio-rendering endpoint buffer.

-   [**IAudioCaptureClient**](/windows/win32/Audioclient/nn-audioclient-iaudiocaptureclient?branch=master)

    Reads captured data from an audio-capture endpoint buffer.

-   [**IAudioSessionControl**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol?branch=master)

    Communicates with the audio session manager to configure and manage the audio session that is associated with the stream.

-   [**ISimpleAudioVolume**](/windows/win32/Audioclient/nn-audioclient-isimpleaudiovolume?branch=master)

    Controls the volume level of the audio session that is associated with the stream.

-   [**IChannelAudioVolume**](/windows/win32/Audioclient/nn-audioclient-ichannelaudiovolume?branch=master)

    Controls the volume levels of the individual channels in the audio session that is associated with the stream.

-   [**IAudioClock**](/windows/win32/Audioclient/nn-audioclient-iaudioclock?branch=master)

    Monitors the stream data rate and stream position.

In addition, WASAPI clients that require notification of session-related events should implement the following interface:

-   [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master)

    To receive event notifications, the client passes a pointer to its [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master) interface to the [**IAudioSessionControl::RegisterAudioSessionNotification**](/windows/win32/Audiopolicy/nf-audiopolicy-iaudiosessioncontrol-registeraudiosessionnotification?branch=master) method as a call parameter.

Finally, a client might use a higher-level API to create an audio stream, but also require access to the session controls and volume controls for the session that contains the stream. A higher-level API typically does not provide this access. The client can obtain the controls for a particular session through the [**IAudioSessionManager**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionmanager?branch=master) interface. This interface enables the client to obtain the [**IAudioSessionControl**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol?branch=master) and [**ISimpleAudioVolume**](/windows/win32/Audioclient/nn-audioclient-isimpleaudiovolume?branch=master) interfaces for a session without requiring the client to use the [**IAudioClient**](/windows/win32/Audioclient/nn-audioclient-iaudioclient?branch=master) interface to create a stream and to assign the stream to the session. A client obtains the **IAudioSessionManager** interface for an audio endpoint device by calling the [**IMMDevice::Activate**](/windows/win32/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate?branch=master) method (with parameter *iid* set to **REFIID** IID\_IAudioSessionManager) on the endpoint object.

The [**IAudioSessionControl**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol?branch=master), [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master), and [**IAudioSessionManager**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionmanager?branch=master) interfaces are defined in header file Audiopolicy.h. All other WASAPI interfaces are defined in header file Audioclient.h.

The following sections describe how to use WASAPI to manage audio streams:

-   [About WASAPI](wasapi.md)
-   [Rendering a Stream](rendering-a-stream.md)
-   [Capturing a Stream](capturing-a-stream.md)
-   [Loopback Recording](loopback-recording.md)
-   [Exclusive-Mode Streams](exclusive-mode-streams.md)
-   [Recovering from an Invalid-Device Error](recovering-from-an-invalid-device-error.md)
-   [Using a Communication Device](using-the-communication-device.md)
-   [Stream Routing](stream-routing.md)

## Related topics

<dl> <dt>

[Programming Guide](programming-guide.md)
</dt> </dl>

 

 



