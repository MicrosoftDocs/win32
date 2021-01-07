---
description: A non-fatal error occurred during streaming.
ms.assetid: 04afcca5-34d9-4c99-86bc-b37c19232ec1
title: MENonFatalError event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MENonFatalError event

A non-fatal error occurred during streaming. Any Media Foundation component can send this event at any time.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE            | Description                                                        |
|--------------------|--------------------------------------------------------------------|
| VT\_UI4<br/> | **HRESULT** value that describes the error.<br/> <br/> |



## Attributes

No attributes are defined for this event.

## Remarks

This event signals an unexpected but recoverable error during streaming. For example, a media source might send this event if it drops a packet.

Do not send this event to signal that an asynchronous method failed. If an asynchronous method fails, the error code is returned in the normal event for that method.

If a non-recoverable streaming error occurs, send the [MEError](meerror.md) event.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




