---
Description: Sent by the streaming audio renderer (SAR) when the volume or mute state of the audio session changes.
ms.assetid: 63c37bd2-0289-407a-92f1-169eb5d2e02e
title: MEAudioSessionVolumeChanged event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEAudioSessionVolumeChanged event

Sent by the streaming audio renderer (SAR) when the volume or mute state of the audio session changes.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE                | Description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/>   | No event data.<br/> <br/>                                                     |
| VT\_UNKNOWN<br/> | Pointer to the [**IMFAudioPolicy**](/windows/win32/mfidl/nn-mfidl-imfaudiopolicy?branch=master) interface.<br/> <br/> |



## Remarks

This event is raised by the stream sink of the SAR. The event is triggered when the SAR receives an [**IAudioSessionEvents::OnSimpleVolumeChanged**](coreaudio.iaudiosessionevents_onsimplevolumechanged) event from the audio session. To get the new volume level and mute state, call [**IMFSimpleAudioVolume::GetMasterVolume**](/windows/win32/mfidl/nf-mfidl-imfsimpleaudiovolume-getmastervolume?branch=master) and [**IMFSimpleAudioVolume::GetMute**](/windows/win32/mfidl/nf-mfidl-imfsimpleaudiovolume-getmute?branch=master).

The SAR sends this event if an external action changes the volume—for example, if the user changes the volume through the system volume-control program (SndVol). The SAR does not send the event if the application changes the volume directly on the SAR.

Also, the SAR does not send this event when the channel volume changes ([**IAudioSessionEvents::OnChannelVolumeChanged**](coreaudio.iaudiosessionevents_onchannelvolumechanged)).

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

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




