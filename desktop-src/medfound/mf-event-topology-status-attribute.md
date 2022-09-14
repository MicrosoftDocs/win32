---
description: Specifies the status of a topology during playback.
ms.assetid: f7c93bad-1a64-45b0-ab5c-6edea4a1c0d1
title: MF_EVENT_TOPOLOGY_STATUS attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_TOPOLOGY\_STATUS attribute

Specifies the status of a topology during playback.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MF\_TOPOSTATUS**](/windows/desktop/api/mfapi/ne-mfapi-mf_topostatus) enumeration.

This attribute is used with the [MESessionTopologyStatus](mesessiontopologystatus.md) event.

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

 

 




