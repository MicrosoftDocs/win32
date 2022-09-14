---
description: Raised by a media source when a presentation ends. This event signals that all streams in the presentation are complete. The Media Session forwards this event to the application.
ms.assetid: 259b00ae-a91b-461b-a12f-f7291ecc04ff
title: MEEndOfPresentation event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEEndOfPresentation event

Raised by a media source when a presentation ends. This event signals that all streams in the presentation are complete. The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                                               | Description                                                                               |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**MF\_EVENT\_SOURCE\_TOPOLOGY\_CANCELED**](mf-event-source-topology-canceled-attribute.md)<br/> | Specifies whether the sequencer source canceled this presentation.<br/> <br/> |



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

 

 




