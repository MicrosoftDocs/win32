---
description: Raised by a stream sink when it completes a scrubbing request.
ms.assetid: 451c7e09-868e-4c05-b970-d222b97223f2
title: MEStreamSinkScrubSampleComplete event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEStreamSinkScrubSampleComplete event

Raised by a stream sink when it completes a scrubbing request.

Scrubbing occurs when the playback rate is zero and the presentation clock is started with a specified srubbing time. If a media sink supports scrubbing, every stream on the sink raises this event whenever the [**IMFClockStateSink::OnClockStart**](/windows/desktop/api/mfidl/nf-mfidl-imfclockstatesink-onclockstart) method is called while the playback rate is zero.

If the stream renders data while scrubbing, it sends the event as soon as the data is rendered. If the stream does not render data, it sends the event immediately after [**OnClockStart**](/windows/desktop/api/mfidl/nf-mfidl-imfclockstatesink-onclockstart) is called.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                              | Description                                                                                                                                                   |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_EVENT\_SCRUBSAMPLE\_TIME**](mf-event-scrubsample-time-attribute.md)<br/> | Presentation time for which data was rendered. If the media sink does not render data while scrubbing, it does not set this attribute.<br/> <br/> |



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

[Media Sinks](media-sinks.md)
</dt> <dt>

[MESessionScrubSampleComplete](mesessionscrubsamplecomplete.md)
</dt> </dl>

 

 




