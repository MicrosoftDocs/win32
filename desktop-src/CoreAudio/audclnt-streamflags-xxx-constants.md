---
description: Specifies characteristics that a client can assign to an audio stream during the initialization of the stream.
ms.assetid: 7b2267c3-79f5-4ada-a7ce-78dd514f8487
title: AUDCLNT_STREAMFLAGS_XXX Constants (Audiosessiontypes.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AUDCLNT\_STREAMFLAGS\_XXX Constants

Specifies characteristics that a client can assign to an audio stream during the initialization of the stream.



| Constant/value                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                        |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="AUDCLNT_STREAMFLAGS_CROSSPROCESS"></span><span id="audclnt_streamflags_crossprocess"></span><dl> <dt>**AUDCLNT\_STREAMFLAGS\_CROSSPROCESS**</dt> <dt>0x00010000</dt> </dl>                                       | The audio stream will be a member of a cross-process audio session. For more information, see Remarks.<br/>                                                                                                                                                                                                                                  |
| <span id="AUDCLNT_STREAMFLAGS_LOOPBACK"></span><span id="audclnt_streamflags_loopback"></span><dl> <dt>**AUDCLNT\_STREAMFLAGS\_LOOPBACK**</dt> <dt>0x00020000</dt> </dl>                                                   | The audio stream will operate in loopback mode. For more information, see Remarks.<br/>                                                                                                                                                                                                                                                      |
| <span id="AUDCLNT_STREAMFLAGS_EVENTCALLBACK"></span><span id="audclnt_streamflags_eventcallback"></span><dl> <dt>**AUDCLNT\_STREAMFLAGS\_EVENTCALLBACK**</dt> <dt>0x00040000</dt> </dl>                                    | Processing of the audio buffer by the client will be event driven. For more information, see Remarks. <br/>                                                                                                                                                                                                                                  |
| <span id="AUDCLNT_STREAMFLAGS_NOPERSIST"></span><span id="audclnt_streamflags_nopersist"></span><dl> <dt>**AUDCLNT\_STREAMFLAGS\_NOPERSIST**</dt> <dt>0x00080000</dt> </dl>                                                | The volume and mute settings for an audio session will not persist across application restarts. For more information, see Remarks.<br/>                                                                                                                                                                                                           |
| <span id="AUDCLNT_STREAMFLAGS_RATEADJUST"></span><span id="audclnt_streamflags_rateadjust"></span><dl> <dt>**AUDCLNT\_STREAMFLAGS\_RATEADJUST**</dt> <dt>0x00100000</dt> </dl>                                             | This constant is new in Windows 7. The sample rate of the stream is adjusted to a rate specified by an application. For more information, see Remarks. <br/>                                                                                                                                                                                 |
| <span id="AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM"></span><span id="audclnt_streamflags_autoconvertpcm"></span><dl> <dt>**AUDCLNT\_STREAMFLAGS\_AUTOCONVERTPCM**</dt> <dt>0x80000000</dt> </dl>                                 | A channel matrixer and a sample rate converter are inserted as necessary to convert between the uncompressed format supplied to [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) and the audio engine mix format.<br/>                                                                                                            |
| <span id="AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY"></span><span id="audclnt_streamflags_src_default_quality"></span><dl> <dt>**AUDCLNT\_STREAMFLAGS\_SRC\_DEFAULT\_QUALITY**</dt> <dt>0x08000000</dt> </dl>                | When used with **AUDCLNT\_STREAMFLAGS\_AUTOCONVERTPCM**, a sample rate converter with better quality than the default conversion but with a higher performance cost is used. This should be used if the audio is ultimately intended to be heard by humans as opposed to other scenarios such as pumping silence or populating a meter.<br/> |



## Remarks

The [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) method and the [**DIRECTX\_AUDIO\_ACTIVATION\_PARAMS**](/windows/win32/api/mmdeviceapi/ns-mmdeviceapi-directx_audio_activation_params) structure use the AUDCLNT\_STREAMFLAGS\_XXX constants.

The AUDCLNT\_STREAMFLAGS\_CROSSPROCESS flag indicates that the audio session for the stream is a cross-process session. A cross-process session can accept streams from more than one process. If two applications in two separate processes call **IAudioClient::Initialize** with identical session GUIDs, and both applications set the AUDCLNT\_SHAREMODE\_CROSSPROCESS flag, then the audio engine assigns their streams to the same cross-process session. This flag overrides the default behavior, which is to assign the stream to a process-specific session rather than a cross-process session. The AUDCLNT\_STREAMFLAGS\_CROSSPROCESS flag bit is incompatible with exclusive mode. For more information about cross-process sessions, see [Audio Sessions](audio-sessions.md).

The AUDCLNT\_STREAMFLAGS\_LOOPBACK flag enables loopback recording. In loopback recording, the audio engine copies the audio stream that is being played by a rendering endpoint device into an audio endpoint buffer so that a [WASAPI](wasapi.md) client can capture the stream. If this flag is set, the **IAudioClient::Initialize** method attempts to open a capture buffer on the rendering device. This flag is valid only for a rendering device and only if the **Initialize** call sets the *ShareMode* parameter to AUDCLNT\_SHAREMODE\_SHARED. Otherwise the **Initialize** call will fail. If the call succeeds, the client can call the [**IAudioClient::GetService**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getservice) method to obtain an [**IAudioCaptureClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiocaptureclient) interface on the rendering device. For more information, see [Loopback Recording](loopback-recording.md).

The AUDCLNT\_STREAMFLAGS\_EVENTCALLBACK flag enables event-driven buffering. If a client sets this flag in the call to **IAudioClient::Initialize** that initializes a stream, the client must subsequently call the [**IAudioClient::SetEventHandle**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-seteventhandle) method to supply an event handle for the stream. After the stream starts, the audio engine will signal the event handle to notify the client each time a buffer becomes ready for the client to process. WASAPI supports event-driven buffering for both rendering and capture buffers. Both shared-mode and exclusive-mode streams can use event-driven buffering. For a code example that uses the AUDCLNT\_STREAMFLAGS\_EVENTCALLBACK flag, see [Exclusive-Mode Streams](exclusive-mode-streams.md).

The AUDCLNT\_STREAMFLAGS\_NOPERSIST flag disables persistence of the volume and mute settings for a session that contains rendering streams. By default, the volume level and muting state for a rendering session are persistent across application restarts. The volume level and muting state for a capture session are never persistent. For more information about the persistence of session volume and mute settings, see [Audio Sessions](audio-sessions.md).

The AUDCLNT\_STREAMFLAGS\_RATEADJUST flag enables an application to get a reference to the [**IAudioClockAdjustment**](/windows/desktop/api/audioclient/nn-audioclient-iaudioclockadjustment) interface that is used to set the sample rate for the stream. To get a pointer to this interace, an application must initialize the audio client with this flag and then call [**IAudioClient::GetService**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getservice) by specifying the **IID\_IAudioClockAdjustment** identifier. To set the new sample rate, call [**IAudioClockAdjustment::SetSampleRate**](/windows/desktop/api/audioclient/nf-audioclient-iaudioclockadjustment-setsamplerate). This flag is valid only for a rendering device. Otherwise the **GetService** call fails with the error code AUDCLNT\_E\_WRONG\_ENDPOINT\_TYPE. The application must also set the *ShareMode* parameter to AUDCLNT\_SHAREMODE\_SHARED during the [**Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) call. **SetSampleRate** fails if the audio client is not in shared mode.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Audiosessiontypes.h</dt> </dl> |



## See also

<dl> <dt>

[Core Audio Constants](core-audio-constants.md)
</dt> <dt>

[**IAudioCaptureClient Interface**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiocaptureclient)
</dt> <dt>

[**IAudioClient::GetService**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getservice)
</dt> <dt>

[**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize)
</dt> <dt>

[**IAudioClient::SetEventHandle**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-seteventhandle)
</dt> </dl>

 

 




