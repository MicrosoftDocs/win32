---
description: Media Stream uses this event to send protection system specific metadata to the decoder.
ms.assetid: 249446CA-AEF7-41A1-98EB-0B9392AE4AD8
title: MEContentProtectionMetadata event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEContentProtectionMetadata event

Media Stream uses this event to send protection system specific metadata to the decoder.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                                              | Description                                                                                         |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [MF\_EVENT\_STREAM\_METADATA\_KEYDATA](mf-event-stream-metadata-keydata.md)<br/>                | This is an optional attribute. Protection system specific data.<br/> <br/>              |
| [MF\_EVENT\_STREAM\_METADATA\_CONTENT\_KEYIDS](mf-event-stream-metadata-content-keyids.md)<br/> | Content key IDs which the event is associated with.<br/> <br/>                          |
| [MF\_EVENT\_STREAM\_METADATA\_SYSTEMID](mf-event-stream-metadata-systemid.md)<br/>              | This is an optional attribute. System ID for which the key data is intended.<br/> <br/> |



## Remarks

This event is used, for example, for communicating key rotation event. In this case it should be sent as early as possible to give the decoder time to prepare itself before samples encrypted with the new key ID start arriving.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




