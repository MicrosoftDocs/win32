---
description: Specifies whether the pipeline applies mark-out at this node. Mark-out is the point where a presentation ends. If pipeline components generate data past the mark-out point, the data is not rendered.
ms.assetid: adf2361a-90c7-4650-a486-5c450a41ab54
title: MF_TOPONODE_MARKOUT_HERE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_MARKOUT\_HERE attribute

Specifies whether the pipeline applies mark-out at this node. Mark-out is the point where a presentation ends. If pipeline components generate data past the mark-out point, the data is not rendered.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to all node types.

If this attribute is **TRUE**, the Media Foundation pipeline trims the output samples from this node to match the stop time for the presentation. The topology loader sets this attribute when it resolves a topology. Most applications do not need to set or retrieve this attribute.

It is recommended that exactly one node in every branch of the topology should have this attribute set to **TRUE**. A topology branch is defined as the path from a source node to an output node. Within a branch, the MF\_TOPONODE\_MARKOUT\_HERE and [MF\_TOPONODE\_MARKIN\_HERE](mf-toponode-markin-here-attribute.md) attributes must be set on the same node in the branch. They cannot be set on different nodes within the same branch.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[**MF\_TOPONODE\_MARKIN\_HERE**](mf-toponode-markin-here-attribute.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




