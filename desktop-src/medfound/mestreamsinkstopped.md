---
Description: 'Raised by a stream sink when it completes the transition to the stopped state. The transition to stopped occurs when the IMFPresentationClock::Stop method is called on the sink''s presentation clock.'
ms.assetid: '1a8c7faa-4d4a-4458-ad08-a760a15dc347'
title: MEStreamSinkStopped event
---

# MEStreamSinkStopped event

Raised by a stream sink when it completes the transition to the stopped state. The transition to stopped occurs when the [**IMFPresentationClock::Stop**](imfpresentationclock-stop.md) method is called on the sink's presentation clock.

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

 

 




