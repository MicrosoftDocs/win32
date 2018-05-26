---
Description: Raised when the IMFMediaSessionStop method completes asynchronously.
ms.assetid: 9cac9040-f652-4509-bbab-f2a41959d836
title: MESessionStopped event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MESessionStopped event

Raised when the [**IMFMediaSession::Stop**](/windows/win32/mfidl/nf-mfidl-imfmediasession-stop?branch=master) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




