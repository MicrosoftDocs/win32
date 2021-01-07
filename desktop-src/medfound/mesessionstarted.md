---
description: Raised when the IMFMediaSession::Start method completes asynchronously.
ms.assetid: 28ed32f0-9b23-4da1-9587-15f490da7bf9
title: MESessionStarted event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESessionStarted event

Raised when the [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                                               | Description                                                                                     |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**MF\_EVENT\_PRESENTATION\_TIME\_OFFSET**](mf-event-presentation-time-offset-attribute.md)<br/> | Offset between the presentation time and the media source's time stamps.<br/> <br/> |



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

 

 




