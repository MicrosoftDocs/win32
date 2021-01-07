---
description: Specifies the start time for a segment topology.
ms.assetid: d8902fb6-c758-4d3d-9230-e918948bda19
title: MF_EVENT_SOURCE_PROJECTSTART attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_SOURCE\_PROJECTSTART attribute

Specifies the start time for a segment topology.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

This attribute is used with the [MESourceStarted](mesourcestarted.md) event. The sequencer source sets this attribute when the current segment topology has the [**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md) attribute. The two attributes have the same value.

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

 

 




