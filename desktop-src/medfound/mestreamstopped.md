---
Description: 'Raised by a media stream when the IMFMediaSource::Stop method completes asynchronously.'
ms.assetid: '80280820-b618-43d9-881e-6119dfa36e22'
title: MEStreamStopped event
---

# MEStreamStopped event

Raised by a media stream when the [**IMFMediaSource::Stop**](imfmediasource-stop.md) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

Each active stream in the presentation sends this event.

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

 

 




