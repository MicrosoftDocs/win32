---
Description: 'Raised by the audio renderer when the audio session display name changes.'
ms.assetid: 'd180b145-88e1-4f85-b001-b76140ca39d8'
title: MEAudioSessionNameChanged event
---

# MEAudioSessionNameChanged event

Raised by the audio renderer when the audio session display name changes.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFAudioPolicy**](imfaudiopolicy.md) interface.<br/> <br/> |



## Remarks

This event is sent by the audio renderer's stream sink. The event is triggered when the audio renderer receives an [**IAudioSessionEvents::OnDisplayNameChanged**](coreaudio.iaudiosessionevents_ondisplaynamechanged) event from the audio session.

To get the new display name, call [**IMFAudioPolicy::GetDisplayName**](imfaudiopolicy-getdisplayname.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFAudioPolicy::GetDisplayName**](imfaudiopolicy-getdisplayname.md)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




