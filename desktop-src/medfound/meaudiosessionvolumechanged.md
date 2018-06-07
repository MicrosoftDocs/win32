---
Description: Sent by the streaming audio renderer (SAR) when the volume or mute state of the audio session changes.
ms.assetid: 63c37bd2-0289-407a-92f1-169eb5d2e02e
title: MEAudioSessionVolumeChanged event
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MEAudioSessionVolumeChanged event

Sent by the streaming audio renderer (SAR) when the volume or mute state of the audio session changes.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE                | Description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/>   | No event data.<br/> <br/>                                                     |
| VT\_UNKNOWN<br/> | Pointer to the [**IMFAudioPolicy**](/windows/desktop/api/mfidl/nn-mfidl-imfaudiopolicy) interface.<br/> <br/> |



## Remarks

This event is raised by the stream sink of the SAR. The event is triggered when the SAR receives an [**IAudioSessionEvents::OnSimpleVolumeChanged**](https://msdn.microsoft.com/e60e8996-3c01-4458-88f2-cd6cb118bd76) event from the audio session. To get the new volume level and mute state, call [**IMFSimpleAudioVolume::GetMasterVolume**](/windows/desktop/api/mfidl/nf-mfidl-imfsimpleaudiovolume-getmastervolume) and [**IMFSimpleAudioVolume::GetMute**](/windows/desktop/api/mfidl/nf-mfidl-imfsimpleaudiovolume-getmute).

The SAR sends this event if an external action changes the volume—for example, if the user changes the volume through the system volume-control program (SndVol). The SAR does not send the event if the application changes the volume directly on the SAR.

Also, the SAR does not send this event when the channel volume changes ([**IAudioSessionEvents::OnChannelVolumeChanged**](https://msdn.microsoft.com/cdd3ec9b-cf72-4c2e-b874-60370d41447d)).

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

 

 




