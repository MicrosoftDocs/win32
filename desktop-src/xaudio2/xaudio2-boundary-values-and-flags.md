---
description: XAudio2 constants that specify default parameters, maximum values, and flags.
ms.assetid: 074ac40e-a17e-7366-1954-6699407b82f7
title: XAudio2 Boundary Values and Flags (Xaudio2.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XAudio2 Boundary Values and Flags

XAudio2 constants that specify default parameters, maximum values, and flags.

**XAudio2 boundary values**



| Constant                                                                                                                                                                                                     | Description                                                                                                                                     |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="XAUDIO2_MAX_BUFFER_BYTES"></span><span id="xaudio2_max_buffer_bytes"></span><dl> <dt>**XAUDIO2\_MAX\_BUFFER\_BYTES**</dt> </dl>             | Maximum value allowed for [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer).AudioBytes.<br/>                                                      |
| <span id="XAUDIO2_MAX_QUEUED_BUFFERS"></span><span id="xaudio2_max_queued_buffers"></span><dl> <dt>**XAUDIO2\_MAX\_QUEUED\_BUFFERS**</dt> </dl>       | Maximum buffers allowed in a voice queue.<br/>                                                                                            |
| <span id="XAUDIO2_MAX_BUFFERS_SYSTEM"></span><span id="xaudio2_max_buffers_system"></span><dl> <dt>**XAUDIO2\_MAX\_BUFFERS\_SYSTEM**</dt> </dl>       | Maximum buffers allowed for system threads (Xbox 360 only).<br/>                                                                          |
| <span id="XAUDIO2_MAX_AUDIO_CHANNELS"></span><span id="xaudio2_max_audio_channels"></span><dl> <dt>**XAUDIO2\_MAX\_AUDIO\_CHANNELS**</dt> </dl>       | Maximum value allowed for **WAVEFORMATEX.nChannels**.<br/>                                                                                |
| <span id="XAUDIO2_MIN_SAMPLE_RATE"></span><span id="xaudio2_min_sample_rate"></span><dl> <dt>**XAUDIO2\_MIN\_SAMPLE\_RATE**</dt> </dl>                | Minimum audio sample rate supported.<br/>                                                                                                 |
| <span id="XAUDIO2_MAX_SAMPLE_RATE"></span><span id="xaudio2_max_sample_rate"></span><dl> <dt>**XAUDIO2\_MAX\_SAMPLE\_RATE**</dt> </dl>                | Maximum audio sample rate supported.<br/>                                                                                                 |
| <span id="XAUDIO2_MAX_VOLUME_LEVEL"></span><span id="xaudio2_max_volume_level"></span><dl> <dt>**XAUDIO2\_MAX\_VOLUME\_LEVEL**</dt> </dl>             | Maximum allowed volume level.<br/>                                                                                                        |
| <span id="XAUDIO2_MIN_FREQ_RATIO"></span><span id="xaudio2_min_freq_ratio"></span><dl> <dt>**XAUDIO2\_MIN\_FREQ\_RATIO**</dt> </dl>                   | Minimum frequency ratio allowed in a source voice.<br/>                                                                                   |
| <span id="XAUDIO2_MAX_FREQ_RATIO"></span><span id="xaudio2_max_freq_ratio"></span><dl> <dt>**XAUDIO2\_MAX\_FREQ\_RATIO**</dt> </dl>                   | Maximum frequency ratio allowed in a source voice.<br/>                                                                                   |
| <span id="XAUDIO2_DEFAULT_FREQ_RATIO"></span><span id="xaudio2_default_freq_ratio"></span><dl> <dt>**XAUDIO2\_DEFAULT\_FREQ\_RATIO**</dt> </dl>       | Default value for the **MaxFrequencyRatio** argument of [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice).<br/> |
| <span id="XAUDIO2_MAX_FILTER_ONEOVERQ"></span><span id="xaudio2_max_filter_oneoverq"></span><dl> <dt>**XAUDIO2\_MAX\_FILTER\_ONEOVERQ**</dt> </dl>    | Maximum value for [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_filter_parameters).**OneOverQ**.<br/>                                     |
| <span id="XAUDIO2_MAX_FILTER_FREQUENCY"></span><span id="xaudio2_max_filter_frequency"></span><dl> <dt>**XAUDIO2\_MAX\_FILTER\_FREQUENCY**</dt> </dl> | Maximum value for [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_filter_parameters).**Frequency**.<br/>                                    |
| <span id="XAUDIO2_MAX_LOOP_COUNT"></span><span id="xaudio2_max_loop_count"></span><dl> <dt>**XAUDIO2\_MAX\_LOOP\_COUNT**</dt> </dl>                   | Maximum value that will not be treated as infinite looping for [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer).**LoopCount**.<br/>              |
| <span id="XAUDIO2_MAX_INSTANCES"></span><span id="xaudio2_max_instances"></span><dl> <dt>**XAUDIO2\_MAX\_INSTANCES**</dt> </dl>                       | Maximum simultaneous instances of XAudio2 allowed on Xbox 360.<br/>                                                                       |



**XAudio2 values with special meaning**



| Constant                                                                                                                                                                                              | Description                                                                                                                                                              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="XAUDIO2_COMMIT_NOW"></span><span id="xaudio2_commit_now"></span><dl> <dt>**XAUDIO2\_COMMIT\_NOW**</dt> </dl>                         | Used as a parameter to methods with an OperationSet argument. See [XAudio2 Operation Sets](xaudio2-operation-sets.md) for more information.<br/>                  |
| <span id="XAUDIO2_COMMIT_ALL"></span><span id="xaudio2_commit_all"></span><dl> <dt>**XAUDIO2\_COMMIT\_ALL**</dt> </dl>                         | Used as a parameter in [**IXAudio2::CommitChanges**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-commitchanges).<br/>                                                                   |
| <span id="XAUDIO2_INVALID_OPSET"></span><span id="xaudio2_invalid_opset"></span><dl> <dt>**XAUDIO2\_INVALID\_OPSET**</dt> </dl>                | Specifies an invalid value for OperationSet arguments. See [XAudio2 Operation Sets](xaudio2-operation-sets.md) for more information.<br/>                         |
| <span id="XAUDIO2_NO_LOOP_REGION"></span><span id="xaudio2_no_loop_region"></span><dl> <dt>**XAUDIO2\_NO\_LOOP\_REGION**</dt> </dl>            | Specifies no loop region, used in [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer).**LoopCount**.<br/>                                                                    |
| <span id="XAUDIO2_LOOP_INFINITE"></span><span id="xaudio2_loop_infinite"></span><dl> <dt>**XAUDIO2\_LOOP\_INFINITE**</dt> </dl>                | Specifies infinite looping, used in [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer).**LoopCount**.<br/>                                                                  |
| <span id="XAUDIO2_DEFAULT_CHANNELS"></span><span id="xaudio2_default_channels"></span><dl> <dt>**XAUDIO2\_DEFAULT\_CHANNELS**</dt> </dl>       | Specifies the default number of channels for the current platform, used in [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice).<br/> |
| <span id="XAUDIO2_DEFAULT_SAMPLERATE"></span><span id="xaudio2_default_samplerate"></span><dl> <dt>**XAUDIO2\_DEFAULT\_SAMPLERATE**</dt> </dl> | Specifies the default sample rate for the current platform, used in [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice).<br/>        |



**XAudio2 Flags**




| Constant | Description | 
|----------|-------------|
| <span id="XAUDIO2_DEBUG_ENGINE"></span><span id="xaudio2_debug_engine"></span><dl><dt><strong>XAUDIO2_DEBUG_ENGINE</strong></dt></dl> | Specifies that the debug/checked version of the audio engine should be used instead of the release version. See <a href="/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create"><strong>XAudio2Create</strong></a>.<br /><blockquote>[!Note]<br />This flag is not supported on Windows 8 or Windows 10.</blockquote><br /> | 
| <span id="XAUDIO2_VOICE_NOPITCH"></span><span id="xaudio2_voice_nopitch"></span><dl><dt><strong>XAUDIO2_VOICE_NOPITCH</strong></dt></dl> | Specifies that a source voice will not use pitch shifting, see <a href="/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice"><strong>IXAudio2::CreateSourceVoice</strong></a>.<br /> | 
| <span id="XAUDIO2_VOICE_NOSRC"></span><span id="xaudio2_voice_nosrc"></span><dl><dt><strong>XAUDIO2_VOICE_NOSRC</strong></dt></dl> | Specifies that no sample rate conversion is available on a source voice, the voice's outputs must have the same sample rate. See <a href="/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice"><strong>IXAudio2::CreateSourceVoice</strong></a>.<br /> | 
| <span id="XAUDIO2_VOICE_USEFILTER"></span><span id="xaudio2_voice_usefilter"></span><dl><dt><strong>XAUDIO2_VOICE_USEFILTER</strong></dt></dl> | Specifies that the filter effect should be available on a voice. See <a href="/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice"><strong>IXAudio2::CreateSourceVoice</strong></a> and <a href="/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2-createsubmixvoice"><strong>IXAudio2::CreateSubmixVoice</strong></a>.<br /> | 
| <span id="XAUDIO2_PLAY_TAILS"></span><span id="xaudio2_play_tails"></span><dl><dt><strong>XAUDIO2_PLAY_TAILS</strong></dt></dl> | Specifies that a voice should continue emitting effect output after it is stopped. See <a href="/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-stop"><strong>IXAudio2SourceVoice::Stop</strong></a>.<br /> | 
| <span id="XAUDIO2_END_OF_STREAM"></span><span id="xaudio2_end_of_stream"></span><dl><dt><strong>XAUDIO2_END_OF_STREAM</strong></dt></dl> | Indicates the last buffer in a stream. See <a href="/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer"><strong>XAUDIO2_BUFFER</strong></a>.<strong>Flags</strong>.<br /> | 
| <span id="XAUDIO2_STOP_ENGINE_WHEN_IDLE"></span><span id="xaudio2_stop_engine_when_idle"></span><dl><dt><strong>XAUDIO2_STOP_ENGINE_WHEN_IDLE</strong></dt></dl> | Specifies that the audio engine should stop when no source voices are started and start when a voice is started. See <a href="/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create"><strong>XAudio2Create</strong></a>.<br /> | 
| <span id="XAUDIO2_SEND_USEFILTER"></span><span id="xaudio2_send_usefilter"></span><dl><dt><strong>XAUDIO2_SEND_USEFILTER</strong></dt></dl> | Indicates a filter should be used on a voice send. See <a href="/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_send_descriptor"><strong>XAUDIO2_SEND_DESCRIPTOR</strong></a>.<strong>Flags</strong>.<br /> | 
| <span id="XAUDIO2_1024_QUANTUM"></span><span id="xaudio2_1024_quantum"></span><dl><dt><strong>XAUDIO2_1024_QUANTUM</strong></dt></dl> | Specifies a non-default processing quantum of 21.33 ms (1024 samples at 48KHz). See <a href="/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create"><strong>XAudio2Create</strong></a>.<br /> | 
| <span id="XAUDIO2_NO_VIRTUAL_AUDIO_CLIENT"></span><span id="xaudio2_no_virtual_audio_client"></span><dl><dt><strong>XAUDIO2_NO_VIRTUAL_AUDIO_CLIENT</strong></dt></dl> | Specifies that a virtual audio client should not be used. See <a href="/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice"><strong>IXAudio2::CreateMasteringVoice</strong></a>.<br /><blockquote>[!Note]<br />On devices in the Mobile device family, a virtual audio client is always used, regardless of whether this flag is used.</blockquote><br /> | 




**XAudio2 Default Parameters for the Built-in Voice Filter**



| Constant                                                                                                                                                                                                                 | Description                                                                                   |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| <span id="XAUDIO2_DEFAULT_FILTER_TYPE"></span><span id="xaudio2_default_filter_type"></span><dl> <dt>**XAUDIO2\_DEFAULT\_FILTER\_TYPE**</dt> </dl>                | Specifies the default filter type to be used with voices and voice sends.<br/>          |
| <span id="XAUDIO2_DEFAULT_FILTER_FREQUENCY"></span><span id="xaudio2_default_filter_frequency"></span><dl> <dt>**XAUDIO2\_DEFAULT\_FILTER\_FREQUENCY**</dt> </dl> | Specifies the default filter frequency to be used with voices and voice sends.<br/>     |
| <span id="XAUDIO2_DEFAULT_FILTER_ONEOVERQ"></span><span id="xaudio2_default_filter_oneoverq"></span><dl> <dt>**XAUDIO2\_DEFAULT\_FILTER\_ONEOVERQ**</dt> </dl>    | Specifies the default filter rate of decay to be used with voices and voice sends.<br/> |



## Remarks

### Platform Requirements

Windows 10 (XAudio2.9); Windows 8, Windows Phone 8 (XAudio 2.8); DirectX SDK (XAudio 2.7)

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Xaudio2.h</dt> </dl> |



## See also

<dl> <dt>

[XAudio2::Constants](constants.md)
</dt> </dl>

 

 
