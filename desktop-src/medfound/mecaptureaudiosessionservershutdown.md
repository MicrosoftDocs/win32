---
Description: Sent by an audio capture source when the capture audio session is disconnected due to the audio server being shutdown.
ms.assetid: 43284B3E-3018-44F3-8D6C-8C3041DCCD3E
title: MECaptureAudioSessionServerShutdown event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MECaptureAudioSessionServerShutdown event

Sent by an audio capture source when the capture audio session is disconnected due to the audio server being shutdown.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



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

 

 




