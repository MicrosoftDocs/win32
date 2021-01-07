---
description: Raised by a stream sink when the rate has changed.
ms.assetid: c61c71de-fd3c-429b-a29f-f9d2bbfcb531
title: MEStreamSinkRateChanged event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEStreamSinkRateChanged event

Raised by a stream sink when the rate has changed.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

If a stream sink supports rate changes, it sends this event after the rate change is complete. The event is sent once for each call to the sink's [**IMFClockStateSink::OnClockSetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfclockstatesink-onclocksetrate) method. If the rate change is not successful, the event status value is an error code.

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
</dt> </dl>

 

 




