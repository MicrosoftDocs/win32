---
Description: 'Raised by the audio renderer when the grouping parameters change for the audio session.'
ms.assetid: 'd6f7757c-fd91-40bd-b2b5-a3e808445250'
title: MEAudioSessionGroupingParamChanged event
---

# MEAudioSessionGroupingParamChanged event

Raised by the audio renderer when the grouping parameters change for the audio session.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFAudioPolicy**](imfaudiopolicy.md) interface.<br/> <br/> |



## Remarks

This event is sent by the audio renderer's stream sink. The event is triggered when the audio renderer receives an [**IAudioSessionEvents::OnGroupingParamChanged**](coreaudio.iaudiosessionevents_ongroupingparamchanged) event from the audio session.

To get the new grouping parameters, call [**IMFAudioPolicy::GetGroupingParam**](imfaudiopolicy-getgroupingparam.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[**IMFAudioPolicy::GetGroupingParam**](imfaudiopolicy-getgroupingparam.md)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




