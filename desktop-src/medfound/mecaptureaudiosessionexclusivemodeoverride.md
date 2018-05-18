---
Description: 'Sent by an audio capture source when another program opens the audio device in exclusive mode.'
ms.assetid: 'E9CC8507-38AB-4049-8DAC-767EC0ECE270'
title: MECaptureAudioSessionExclusiveModeOverride event
---

# MECaptureAudioSessionExclusiveModeOverride event

Sent by an audio capture source when another program opens the audio device in exclusive mode.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



## Remarks

This event is sent by the media stream of the audio capture source.

The capture source sends this event when it receives an [**IAudioSessionEvents::OnSessionDisconnected**](coreaudio.iaudiosessionevents_onsessiondisconnected) event from the audio session with the disconnection reason equal to **DisconnectReasonExclusiveModeOverride**.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




