---
description: Raised by a media source when it updates its metadata.
ms.assetid: 6818b0c9-9628-41e6-8dc6-dff26f4fcfd2
title: MESourceMetadataChanged event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESourceMetadataChanged event

Raised by a media source when it updates its metadata.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

If the media source cannot provide all of the metadata when the source is first created, it should raise this event after the metadata is available.

The media source should create a new presentation descriptor and copy all of the attributes from the presentation descriptor (PD) to the event object. The application can use the event object to enumerate the new PD attributes. In particular, the values for [MF\_PD\_DURATION](mf-pd-duration-attribute.md) and [MF\_PD\_TOTAL\_FILE\_SIZE](mf-pd-total-file-size-attribute.md) might be unknown until the file is completely downloaded.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




