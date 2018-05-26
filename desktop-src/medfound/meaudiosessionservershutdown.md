---
Description: Raised by the audio renderer when the Windows audio server system is shut down. The audio renderer is now invalid.
ms.assetid: 8e80903c-d6ce-4fa2-87db-552c7fba3c6a
title: MEAudioSessionServerShutdown event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEAudioSessionServerShutdown event

Raised by the audio renderer when the Windows audio server system is shut down. The audio renderer is now invalid.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE                | Description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/>   | No event data.<br/> <br/>                                                     |
| VT\_UNKNOWN<br/> | Pointer to the [**IMFAudioPolicy**](/windows/win32/mfidl/nn-mfidl-imfaudiopolicy?branch=master) interface.<br/> <br/> |



## Remarks

This event is sent by the audio renderer's stream sink. The event is triggered when the audio renderer receives an [**IAudioSessionEvents::OnSessionDisconnected**](coreaudio.iaudiosessionevents_onsessiondisconnected) event from the audio session with the disconnection reason equal to **DisconnectReasonServerShutdown**.

The [**IMFAudioPolicy**](/windows/win32/mfidl/nn-mfidl-imfaudiopolicy?branch=master) pointer, if set, is not useful, because the audio stream is no longer valid.

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

 

 




