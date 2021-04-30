---
description: Raised when a media source seeks to a new position. A media source raises this event if the source is running or paused and the application calls IMFMediaSource::Start with a start time that does not equal the current position.
ms.assetid: 51ce770e-ddc7-41c1-8e31-59481cafe2b0
title: MESourceSeeked event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESourceSeeked event

Raised when a media source seeks to a new position. A media source raises this event if the source is running or paused and the application calls [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) with a start time that does not equal the current position.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE           | Description                                                                |
|-------------------|----------------------------------------------------------------------------|
| VT\_I8<br/> | The new starting position, in 100-nanosecond units.<br/> <br/> |



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

 

 




