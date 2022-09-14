---
description: Raised by the sequencer source when a segment is completed and is followed by another segment. When the final segment is completed, the sequencer source raises an MEEndOfPresentation event.
ms.assetid: 1be13c9a-d454-4642-b26b-556f2461b705
title: MEEndOfPresentationSegment event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEEndOfPresentationSegment event

Raised by the sequencer source when a segment is completed and is followed by another segment. When the final segment is completed, the sequencer source raises an [MEEndOfPresentation](meendofpresentation.md) event.

The Media Session forwards this event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                                               | Description                                                                          |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**MF\_EVENT\_SOURCE\_TOPOLOGY\_CANCELED**](mf-event-source-topology-canceled-attribute.md)<br/> | Specifies whether the sequencer source canceled this segment.<br/> <br/> |



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

[About the Sequencer Source](about-the-sequencer-source.md)
</dt> <dt>

[Sequencer Source Events](sequencer-source-events.md)
</dt> </dl>

 

 




