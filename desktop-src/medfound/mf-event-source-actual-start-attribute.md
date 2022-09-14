---
description: Contains the start time at which a media source restarts from its current position.
ms.assetid: b598b4d1-40e1-4282-b312-5aa6ca3a6733
title: MF_EVENT_SOURCE_ACTUAL_START attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_SOURCE\_ACTUAL\_START attribute

Contains the start time at which a media source restarts from its current position.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

This attribute is used with the [MESourceStarted](mesourcestarted.md) event. The attribute is relevant when the event data is empty (**VT\_EMPTY**), which indicates that the media source started from the current playback position. In that case, the **MF\_EVENT\_SOURCE\_ACTUAL\_START** attribute specifies the actual starting time. If the event data is **VT\_EMPTY** and this attribute is not set, the starting time is assumed to be zero.

When the [MESourceStarted](mesourcestarted.md) event data contains the start time (**VT\_I8**), this attribute should not be set.

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

 

 




