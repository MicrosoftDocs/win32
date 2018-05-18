---
Description: Stream Management
ms.assetid: '936d8d69-e86c-418b-b5b0-c4fbbfa1dd49'
title: Stream Management
---

# Stream Management

After enumerating the [audio endpoint devices](audio-endpoint-devices.md) in the system and identifying a suitable rendering or capture device, the next task for an audio client application is to open a connection with the endpoint device and to manage the flow of audio data over that connection. [WASAPI](wasapi.md) enables clients to create and manage audio streams.

WASAPI implements several interfaces to provide stream-management services to audio clients. The primary interface is [**IAudioClient**](iaudioclient.md). A client obtains the **IAudioClient** interface for an audio endpoint device by calling the [**IMMDevice::Activate**](immdevice-activate.md) method (with parameter *iid* set to **REFIID** IID\_IAudioClient) on the endpoint object.

The client calls the methods in the [**IAudioClient**](iaudioclient.md) interface to do the following:

-   Discover which audio formats the endpoint device supports.
-   Get the endpoint buffer size.
-   Get the stream format and latency.
-   Start, stop, and reset the stream that flows through the endpoint device.
-   Access additional audio services.

To create a stream, a client calls the [**IAudioClient::Initialize**](iaudioclient-initialize.md) method. Through this method, the client specifies the data format for the stream, the size of the endpoint buffer, and whether the stream operates in shared or exclusive mode.

The remaining methods in the [**IAudioClient**](iaudioclient.md) interface fall into two groups:

-   Methods that can be called only after the stream has been opened by [**IAudioClient::Initialize**](iaudioclient-initialize.md).
-   Methods that can be called at any time before or after the [**Initialize**](iaudioclient-initialize.md) call.

The following methods can be called only after the call to [**IAudioClient::Initialize**](iaudioclient-initialize.md):

-   [**IAudioClient::GetBufferSize**](iaudioclient-getbuffersize.md)
-   [**IAudioClient::GetCurrentPadding**](iaudioclient-getcurrentpadding.md)
-   [**IAudioClient::GetService**](iaudioclient-getservice.md)
-   [**IAudioClient::GetStreamLatency**](iaudioclient-getstreamlatency.md)
-   [**IAudioClient::Reset**](iaudioclient-reset.md)
-   [**IAudioClient::Start**](iaudioclient-start.md)
-   [**IAudioClient::Stop**](iaudioclient-stop.md)

The following methods can be called before or after the [**IAudioClient::Initialize**](iaudioclient-initialize.md) call:

-   [**IAudioClient::GetDevicePeriod**](iaudioclient-getdeviceperiod.md)
-   [**IAudioClient::GetMixFormat**](iaudioclient-getmixformat.md)
-   [**IAudioClient::IsFormatSupported**](iaudioclient-isformatsupported.md)

To access the additional audio client services, the client calls the [**IAudioClient::GetService**](iaudioclient-getservice.md) method. Through this method, the client can obtain references to the following interfaces:

-   [**IAudioRenderClient**](iaudiorenderclient.md)

    Writes rendering data to an audio-rendering endpoint buffer.

-   [**IAudioCaptureClient**](iaudiocaptureclient.md)

    Reads captured data from an audio-capture endpoint buffer.

-   [**IAudioSessionControl**](iaudiosessioncontrol.md)

    Communicates with the audio session manager to configure and manage the audio session that is associated with the stream.

-   [**ISimpleAudioVolume**](isimpleaudiovolume.md)

    Controls the volume level of the audio session that is associated with the stream.

-   [**IChannelAudioVolume**](ichannelaudiovolume.md)

    Controls the volume levels of the individual channels in the audio session that is associated with the stream.

-   [**IAudioClock**](iaudioclock.md)

    Monitors the stream data rate and stream position.

In addition, WASAPI clients that require notification of session-related events should implement the following interface:

-   [**IAudioSessionEvents**](iaudiosessionevents.md)

    To receive event notifications, the client passes a pointer to its [**IAudioSessionEvents**](iaudiosessionevents.md) interface to the [**IAudioSessionControl::RegisterAudioSessionNotification**](iaudiosessioncontrol-registeraudiosessionnotification.md) method as a call parameter.

Finally, a client might use a higher-level API to create an audio stream, but also require access to the session controls and volume controls for the session that contains the stream. A higher-level API typically does not provide this access. The client can obtain the controls for a particular session through the [**IAudioSessionManager**](iaudiosessionmanager.md) interface. This interface enables the client to obtain the [**IAudioSessionControl**](iaudiosessioncontrol.md) and [**ISimpleAudioVolume**](isimpleaudiovolume.md) interfaces for a session without requiring the client to use the [**IAudioClient**](iaudioclient.md) interface to create a stream and to assign the stream to the session. A client obtains the **IAudioSessionManager** interface for an audio endpoint device by calling the [**IMMDevice::Activate**](immdevice-activate.md) method (with parameter *iid* set to **REFIID** IID\_IAudioSessionManager) on the endpoint object.

The [**IAudioSessionControl**](iaudiosessioncontrol.md), [**IAudioSessionEvents**](iaudiosessionevents.md), and [**IAudioSessionManager**](iaudiosessionmanager.md) interfaces are defined in header file Audiopolicy.h. All other WASAPI interfaces are defined in header file Audioclient.h.

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

 

 



