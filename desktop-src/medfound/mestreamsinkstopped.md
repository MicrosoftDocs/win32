---
Description: Raised by a stream sink when it completes the transition to the stopped state. The transition to stopped occurs when the IMFPresentationClockStop method is called on the sinks presentation clock.
ms.assetid: 1a8c7faa-4d4a-4458-ad08-a760a15dc347
title: MEStreamSinkStopped event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEStreamSinkStopped event

Raised by a stream sink when it completes the transition to the stopped state. The transition to stopped occurs when the [**IMFPresentationClock::Stop**](/windows/win32/mfidl/nf-mfidl-imfpresentationclock-stop?branch=master) method is called on the sink's presentation clock.

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

 

 




