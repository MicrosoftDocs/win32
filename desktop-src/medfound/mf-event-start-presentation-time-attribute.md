---
description: The starting time for the presentation, in 100-nanosecond units, as measured by the presentation clock.
ms.assetid: d19d851c-ab4a-4a9d-bcc4-8dd4e993fa2c
title: MF_EVENT_START_PRESENTATION_TIME attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_START\_PRESENTATION\_TIME attribute

The starting time for the presentation, in 100-nanosecond units, as measured by the presentation clock.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

This attribute is used with the [MESessionNotifyPresentationTime](mesessionnotifypresentationtime.md) event.

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

 

 




