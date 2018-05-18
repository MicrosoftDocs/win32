---
Description: 'Raised by a stream sink when it completes the transition to the paused state.'
ms.assetid: '84ab62fc-1525-433c-8af5-70659122703c'
title: MEStreamSinkPaused event
---

# MEStreamSinkPaused event

Raised by a stream sink when it completes the transition to the paused state. The transition to paused occurs when the [**IMFPresentationClock::Pause**](imfpresentationclock-pause.md) method is called on the sink's presentation clock.

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

 

 




