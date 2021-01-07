---
description: Specifies whether the current segment topology is empty.
ms.assetid: efd497dc-affc-4453-975c-09c5dca06374
title: MF_EVENT_SOURCE_FAKE_START attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_SOURCE\_FAKE\_START attribute

Specifies whether the current segment topology is empty.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute is used with the [MESourceStarted](mesourcestarted.md) event.

The sequencer source sets this attribute to **TRUE** if the current segment topology is empty. If this attribute is **TRUE**, playback has not started yet. The default value of this attribute is **FALSE**.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> </dl>

 

 




