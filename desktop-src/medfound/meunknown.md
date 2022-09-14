---
description: Unknown event type. You can use this value to initialize variables of type MediaEventType, but a component should never raise the MEUnknown event.
ms.assetid: 786b69f4-8713-41db-829a-c13512baa3f1
title: MEUnknown event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEUnknown event

Unknown event type. You can use this value to initialize variables of type **MediaEventType**, but a component should never raise the MEUnknown event

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



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

 

 




