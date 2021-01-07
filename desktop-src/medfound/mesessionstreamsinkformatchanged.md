---
description: Raised by the Media Session when the format changes on a media sink.
ms.assetid: f56419f8-7f50-4eda-bf4a-fcdbbe46e180
title: MESessionStreamSinkFormatChanged event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESessionStreamSinkFormatChanged event

Raised by the Media Session when the format changes on a media sink.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                    | Description                                                                                  |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**MF\_EVENT\_OUTPUT\_NODE**](mf-event-output-node-attribute.md)<br/> | Identifies the topology node for the media sink whose format changed.<br/> <br/> |



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

 

 




