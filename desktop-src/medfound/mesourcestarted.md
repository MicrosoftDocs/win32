---
description: Raised when a media source starts without seeking.
ms.assetid: a52d8ee1-cb46-487d-a744-fca6db7c2353
title: MESourceStarted event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESourceStarted event

Raised when a media source starts without seeking.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/> | No event data. The start time was from the current position.<br/> <br/>                            |
| VT\_I8<br/>    | The starting time, in 100-nanosecond units, relative to the time stamps on the samples.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                                     | Description                                                                                                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_EVENT\_SOURCE\_ACTUAL\_START**](mf-event-source-actual-start-attribute.md)<br/> | Start time. The media source sets this attribute if it restarts from its current position.<br/> <br/>                     |
| [**MF\_EVENT\_SOURCE\_FAKE\_START**](mf-event-source-fake-start-attribute.md)<br/>     | Specifies whether the current segment topology is empty. The sequencer source sets this attribute.<br/> <br/>             |
| [**MF\_EVENT\_SOURCE\_PROJECTSTART**](mf-event-source-projectstart-attribute.md)<br/>  | Start time for a segment, relative to the start of the presentation. The sequencer source sets this attribute.<br/> <br/> |



## Remarks

A media source raises this event when it starts from a stopped state, or starts from a paused state at the same position in the source. The event is raised if the [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method returns S\_OK.

If the media source starts from the current position and the source's previous state was running or paused, the event data can empty (VT\_EMPTY). If the event data is VT\_EMPTY, the media source might set the [**MF\_EVENT\_SOURCE\_ACTUAL\_START**](mf-event-source-actual-start-attribute.md) attribute with the actual starting time.

If the media source starts from a new position, or the source's previous state was stopped, the event data must be the starting time (VT\_I8).

If the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method causes a seek, the media source sends the [MESourceSeeked](mesourceseeked.md) event instead of MESourceStarted.

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

 

 




