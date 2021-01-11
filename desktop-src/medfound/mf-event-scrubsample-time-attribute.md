---
description: Presentation time for a sample that was rendered while scrubbing.
ms.assetid: 6ce52cf5-014b-49a2-abf7-2c9cc5340a42
title: MF_EVENT_SCRUBSAMPLE_TIME attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_SCRUBSAMPLE\_TIME attribute

Presentation time for a sample that was rendered while scrubbing.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

This attribute is used with the [MEStreamSinkScrubSampleComplete](mestreamsinkscrubsamplecomplete.md) event.

This attribute is a signed value, although it is stored as a **UINT64**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Event Attributes](event-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64)
</dt> </dl>

 

 




