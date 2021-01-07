---
description: Raised by a media stream when the stream ends.
ms.assetid: e793131a-f737-411f-a9fc-03b5b3d09aea
title: MEEndOfStream event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEEndOfStream event

Raised by a media stream when the stream ends.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

When the [Media Session](media-session.md) receives the MEEndOfStream event, it calls [**IMFStreamSink::PlaceMarker**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamsink-placemarker) on the corresponding media sink, with the **MFSTREAMSINK\_MARKER\_ENDOFSEGMENT** marker type.

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

 

 




