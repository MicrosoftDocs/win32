---
Description: Raised by the audio renderer when the grouping parameters change for the audio session.
ms.assetid: d6f7757c-fd91-40bd-b2b5-a3e808445250
title: MEAudioSessionGroupingParamChanged event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEAudioSessionGroupingParamChanged event

Raised by the audio renderer when the grouping parameters change for the audio session.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE                | Description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFAudioPolicy**](/windows/win32/mfidl/nn-mfidl-imfaudiopolicy?branch=master) interface.<br/> <br/> |



## Remarks

This event is sent by the audio renderer's stream sink. The event is triggered when the audio renderer receives an [**IAudioSessionEvents::OnGroupingParamChanged**](coreaudio.iaudiosessionevents_ongroupingparamchanged) event from the audio session.

To get the new grouping parameters, call [**IMFAudioPolicy::GetGroupingParam**](/windows/win32/mfidl/nf-mfidl-imfaudiopolicy-getgroupingparam?branch=master).

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

[**IMFAudioPolicy::GetGroupingParam**](/windows/win32/mfidl/nf-mfidl-imfaudiopolicy-getgroupingparam?branch=master)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




