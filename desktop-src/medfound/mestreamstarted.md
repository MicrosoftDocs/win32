---
description: Raised by a media stream when the source starts without seeking. A media stream raises this event when the media source raises the MESourceStarted event.
ms.assetid: 6652e440-5de9-4767-b7a6-9d919ceece38
title: MEStreamStarted event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEStreamStarted event

Raised by a media stream when the source starts without seeking. A media stream raises this event when the media source raises the [MESourceStarted](mesourcestarted.md) event.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/>                                                                          |
| VT\_I8<br/>    | The starting time, in 100-nanosecond units, relative to the time stamps on the samples.<br/> <br/> |



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

 

 




