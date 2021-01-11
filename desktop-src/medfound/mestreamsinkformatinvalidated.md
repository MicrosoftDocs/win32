---
description: Sent by a stream sink when the downstream format has become invalidated and it needs to be renegotiated.
ms.assetid: 732B3BDD-F394-430F-B895-AF18ED61114D
title: MEStreamSinkFormatInvalidated event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEStreamSinkFormatInvalidated event

Sent by a stream sink when the downstream format has become invalidated and it needs to be renegotiated.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

Data that was queued to the sink, past the current playback position, should be resent.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                                           |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




