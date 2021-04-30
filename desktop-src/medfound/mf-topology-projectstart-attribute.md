---
description: Specifies the stop time for a topology, relative to the start of the first topology in the sequence.
ms.assetid: 7669f97e-87ad-4a64-a2a5-62b8ce450d80
title: MF_TOPOLOGY_PROJECTSTART attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPOLOGY\_PROJECTSTART attribute

Specifies the stop time for a topology, relative to the start of the first topology in the sequence.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

The value is given in units of 100 nanoseconds.

If the Media Session was created with the [**MF\_SESSION\_GLOBAL\_TIME**](mf-session-global-time-attribute.md) attribute equal to **TRUE**, all topologies must contain the **MF\_TOPOLOGY\_PROJECTSTART** attribute. Otherwise, topologies must not contain the **MF\_TOPOLOGY\_PROJECTSTART** attribute. For more information, see [Sequence Presentation Times](sequence-presentation-times.md).

This attribute is a signed value, although it is stored as a **UINT64**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sequence Presentation Times](sequence-presentation-times.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64)
</dt> <dt>

[**MF\_TOPOLOGY\_PROJECTSTOP**](mf-topology-projectstop-attribute.md)
</dt> </dl>

 

 




