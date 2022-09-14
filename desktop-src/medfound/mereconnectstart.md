---
description: Signals that a media source is attempting to reconnect to the server.
ms.assetid: c5975279-c710-4046-9152-d1e1c62eb785
title: MEReconnectStart event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEReconnectStart event

Signals that a media source is attempting to reconnect to the server.

Raised by a media source at the start of a reconnection attempt. The network source raises this event if it attempts to reconnect to the server. The Media Session forwards this event to the application.

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

 

 




