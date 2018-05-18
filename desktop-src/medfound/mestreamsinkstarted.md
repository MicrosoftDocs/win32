---
Description: 'Raised by a stream sink when it completes the transition to the running state.'
ms.assetid: '95ac658b-bec0-442d-85ef-61966b40a2f2'
title: MEStreamSinkStarted event
---

# MEStreamSinkStarted event

Raised by a stream sink when it completes the transition to the running state. The transition to running occurs when the [**IMFPresentationClock::Start**](imfpresentationclock-start.md) method is called on the sink's presentation clock. The media sink receives the notification through its [**IMFClockStateSink::OnClockStart**](imfclockstatesink-onclockstart.md) or [**IMFClockStateSink::OnClockRestart**](imfclockstatesink-onclockrestart.md) method.

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

[Media Sinks](media-sinks.md)
</dt> </dl>

 

 




