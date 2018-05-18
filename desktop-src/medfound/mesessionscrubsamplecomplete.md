---
Description: 'Raised by the Media Session when it completes a scrubbing request.'
ms.assetid: '1ae97022-3fb2-4c5e-9262-d5bdc2a62bee'
title: MESessionScrubSampleComplete event
---

# MESessionScrubSampleComplete event

Raised by the Media Session when it completes a scrubbing request.

Scrubbing occurs when the playback rate is zero and the application calls [**IMFMediaSession::Start**](imfmediasession-start.md). This event is raised after every stream sink has completed the scrubbing request.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[MEStreamSinkScrubSampleComplete](mestreamsinkscrubsamplecomplete.md)
</dt> </dl>

 

 




