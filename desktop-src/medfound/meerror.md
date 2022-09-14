---
description: Signals a serious error. Any Media Foundation component can send this event at any time. Call IMFMediaEvent::GetStatus to get the error code of the operation that failed.
ms.assetid: bff80041-77d8-43b1-a410-9cefaf45eb2c
title: MEError event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEError event

Signals a serious error. Any Media Foundation component can send this event at any time. Call [**IMFMediaEvent::GetStatus**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getstatus) to get the error code of the operation that failed.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

This event should be used only for unexpected errors. Do not send this event to signal that an asynchronous method failed. If an asynchronous method fails, the error code is returned in the normal event for that method.

If a recoverable error occurs during streaming, send the [MENonFatalError](menonfatalerror.md) event.

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

 

 




