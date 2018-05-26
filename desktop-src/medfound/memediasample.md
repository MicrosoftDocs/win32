---
Description: Sent when a media stream delivers a new sample in response to a call to IMFMediaStreamRequestSample.
ms.assetid: 01610053-786f-44b5-90d6-2cb2668cd632
title: MEMediaSample event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEMediaSample event

Sent when a media stream delivers a new sample in response to a call to [**IMFMediaStream::RequestSample**](/windows/win32/mfidl/nf-mfidl-imfmediastream-requestsample?branch=master).

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE                | Description                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master) interface of the sample.<br/> <br/> |



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

[Media Sources](media-sources.md)
</dt> </dl>

 

 




