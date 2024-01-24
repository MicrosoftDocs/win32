---
description: Signals that a media source has completed an attempt to reconnect to the server.
ms.assetid: 228e069a-a26b-472e-915e-ff9aec5ee9c1
title: MEReconnectEnd event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEReconnectEnd event

Signals that a media source has completed an attempt to reconnect to the server.

Raised by a media source at the end of a reconnection attempt. The network source raises this event if it reconnects to the server. The Media Session forwards this event to the application.

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

 

 




