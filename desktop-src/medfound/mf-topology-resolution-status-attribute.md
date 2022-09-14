---
description: Specifies the status of an attempt to resolve a topology.
ms.assetid: 7c2410ce-e70b-4303-9dbc-caff4a355d6b
title: MF_TOPOLOGY_RESOLUTION_STATUS attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPOLOGY\_RESOLUTION\_STATUS attribute

Specifies the status of an attempt to resolve a topology.

## Data type

**UINT32**

## Remarks

The topology loader or the Media Session might set this attribute on a topology. The value of this attribute is a bitwise **OR** of flags from the [**MF\_TOPOLOGY\_RESOLUTION\_STATUS\_FLAGS**](/windows/desktop/api/mfidl/ne-mfidl-mf_topology_resolution_status_flags) enumeration.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 




