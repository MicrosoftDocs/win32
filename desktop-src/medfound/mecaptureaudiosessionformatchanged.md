---
Description: Sent by an audio capture source when the audio format changes.
ms.assetid: 8197BBAD-8102-43C3-BA61-8DC3BC13B7D6
title: MECaptureAudioSessionFormatChanged event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MECaptureAudioSessionFormatChanged event

Sent by an audio capture source when the audio format changes.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



## Remarks

This event is sent by the media stream of the audio capture source.

The capture source sends this event when it receives an [**IAudioSessionEvents::OnSessionDisconnected**](coreaudio.iaudiosessionevents_onsessiondisconnected) event from the audio session with the disconnection reason equal to **DisconnectReasonFormatChanged**.

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

 

 




