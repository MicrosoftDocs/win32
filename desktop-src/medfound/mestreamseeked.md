---
description: Raised by a media stream after a call to IMFMediaSource::Start causes a seek in the stream. A media stream raises this event when the media source raises the MESourceSeeked event.
ms.assetid: df06df16-711d-4262-b049-fb29f25934de
title: MEStreamSeeked event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEStreamSeeked event

Raised by a media stream after a call to [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) causes a seek in the stream. A media stream raises this event when the media source raises the [MESourceSeeked](mesourceseeked.md) event.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE           | Description                                                        |
|-------------------|--------------------------------------------------------------------|
| VT\_I8<br/> | New starting time, in 100-nanosecond units.<br/> <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




