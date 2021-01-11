---
description: Sent by an audio capture source when the audio dession is disconnected because the user logged off from a Windows Terminal Services (WTS) session.
ms.assetid: 88B24E79-FEB8-46AF-9A6C-3FB426089584
title: MECaptureAudioSessionDisconnected event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MECaptureAudioSessionDisconnected event

Sent by an audio capture source when the audio dession is disconnected because the user logged off from a Windows Terminal Services (WTS) session.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



## Remarks

This event is sent by the media stream of the audio capture source.

The capture source sends this event when it receives an [**IAudioSessionEvents::OnSessionDisconnected**](/windows/win32/api/audiopolicy/nf-audiopolicy-iaudiosessionevents-onsessiondisconnected) event from the audio session with the disconnection reason equal to **DisconnectReasonSessionDisconnected**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 
