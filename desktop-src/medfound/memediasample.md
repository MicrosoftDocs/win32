---
Description: 'Sent when a media stream delivers a new sample in response to a call to IMFMediaStream::RequestSample.'
ms.assetid: '01610053-786f-44b5-90d6-2cb2668cd632'
title: MEMediaSample event
---

# MEMediaSample event

Sent when a media stream delivers a new sample in response to a call to [**IMFMediaStream::RequestSample**](imfmediastream-requestsample.md).

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFSample**](imfsample.md) interface of the sample.<br/> <br/> |



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

 

 




