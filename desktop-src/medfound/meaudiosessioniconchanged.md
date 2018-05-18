---
Description: 'Raised by the audio renderer when the audio session icon changes.'
ms.assetid: '72aae901-e5fe-481d-babb-459038abd629'
title: MEAudioSessionIconChanged event
---

# MEAudioSessionIconChanged event

Raised by the audio renderer when the audio session icon changes.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/>   | No event data.<br/> <br/>                                                     |
| VT\_UNKNOWN<br/> | Pointer to the [**IMFAudioPolicy**](imfaudiopolicy.md) interface.<br/> <br/> |



## Remarks

This event is sent by the audio renderer's stream sink. The event is triggered when the audio renderer receives an [**IAudioSessionEvents::OnIconPathChanged**](coreaudio.iaudiosessionevents_oniconpathchanged) event from the audio session.

To get the new icon, call [**IMFAudioPolicy::GetIconPath**](imfaudiopolicy-geticonpath.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFAudioPolicy::GetIconPath**](imfaudiopolicy-geticonpath.md)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




