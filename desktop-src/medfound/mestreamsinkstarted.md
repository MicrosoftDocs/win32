---
Description: Raised by a stream sink when it completes the transition to the running state.
ms.assetid: 95ac658b-bec0-442d-85ef-61966b40a2f2
title: MEStreamSinkStarted event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEStreamSinkStarted event

Raised by a stream sink when it completes the transition to the running state. The transition to running occurs when the [**IMFPresentationClock::Start**](/windows/win32/mfidl/nf-mfidl-imfpresentationclock-start?branch=master) method is called on the sink's presentation clock. The media sink receives the notification through its [**IMFClockStateSink::OnClockStart**](/windows/win32/mfidl/nf-mfidl-imfclockstatesink-onclockstart?branch=master) or [**IMFClockStateSink::OnClockRestart**](/windows/win32/mfidl/nf-mfidl-imfclockstatesink-onclockrestart?branch=master) method.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



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

 

 




