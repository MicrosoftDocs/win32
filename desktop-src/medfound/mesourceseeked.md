---
Description: 'Raised when a media source seeks to a new position. A media source raises this event if the source is running or paused and the application calls IMFMediaSource::Start with a start time that does not equal the current position.'
ms.assetid: '51ce770e-ddc7-41c1-8e31-59481cafe2b0'
title: MESourceSeeked event
---

# MESourceSeeked event

Raised when a media source seeks to a new position. A media source raises this event if the source is running or paused and the application calls [**IMFMediaSource::Start**](imfmediasource-start.md) with a start time that does not equal the current position.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE           | Description                                                                |
|-------------------|----------------------------------------------------------------------------|
| VT\_I8<br/> | The new starting position, in 100-nanosecond units.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




