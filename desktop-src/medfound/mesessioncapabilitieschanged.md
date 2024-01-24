---
description: Raised by the Media Session when the session capabilities change.
ms.assetid: d59fd3a0-29db-434c-b6ba-d9beb33bd965
title: MESessionCapabilitiesChanged event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESessionCapabilitiesChanged event

Raised by the Media Session when the session capabilities change.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

The event contains the following attributes.



| Attribute                                                                     | Description                                      |
|-------------------------------------------------------------------------------|--------------------------------------------------|
| [**MF\_EVENT\_SESSIONCAPS**](mf-event-sessioncaps-attribute.md)              | New session capabilities flags.                  |
| [**MF\_EVENT\_SESSIONCAPS\_DELTA**](mf-event-sessioncaps-delta-attribute.md) | Indicates which capabilities flags have changed. |



 

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

 

 




