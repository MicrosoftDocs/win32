---
description: Raised by a media source when the sources characteristics change.
ms.assetid: df7bb9a3-5949-4a4a-8835-c5b1d01b5cb3
title: MESourceCharacteristicsChanged event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESourceCharacteristicsChanged event

Raised by a media source when the source's characteristics change.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                                                   | Description                                                          |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**MF\_EVENT\_SOURCE\_CHARACTERISTICS**](mf-event-source-characteristics-attribute.md)<br/>          | New characteristics of the media source.<br/> <br/>      |
| [**MF\_EVENT\_SOURCE\_CHARACTERISTICS\_OLD**](mf-event-source-characteristics-old-attribute.md)<br/> | Previous characteristics of the media source.<br/> <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




