---
description: Sent when a media stream delivers a new sample in response to a call to IMFMediaStream::RequestSample.
ms.assetid: 01610053-786f-44b5-90d6-2cb2668cd632
title: MEMediaSample event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEMediaSample event

Sent when a media stream delivers a new sample in response to a call to [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample).

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE                | Description                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface of the sample.<br/> <br/> |



## Requirements



| Requirement | Value |
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

 

 




