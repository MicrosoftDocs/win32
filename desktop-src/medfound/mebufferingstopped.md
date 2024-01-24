---
description: Signals that a media source has stopped buffering data.
ms.assetid: 11b1290d-d462-4aa0-a358-b3f6447c99d8
title: MEBufferingStopped event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEBufferingStopped event

Signals that a media source has stopped buffering data.

A media source sends this when it stops buffering data after sending the [MEBufferingStarted](mebufferingstarted.md) event.

Byte streams that implement the [**IMFByteStreamBuffering**](/windows/desktop/api/mfidl/nn-mfidl-imfbytestreambuffering) interface also send this event.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

When the Media Session receives this event, it restarts the presentation clock. The Media Session also forwards the event to the application.

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

 

 




