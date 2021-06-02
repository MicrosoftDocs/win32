---
description: Indicates which output is the primary output on a tee node.
ms.assetid: f7d98837-75da-48cc-8307-091be2d95392
title: MF_TOPONODE_PRIMARYOUTPUT attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_PRIMARYOUTPUT attribute

Indicates which output is the primary output on a tee node.

## Data type

**UINT32**

## Remarks

This attribute applies to tee nodes (**MF\_TOPOLOGY\_TEE\_NODE**).

The value of this attribute is the zero-based index of an output connection on this tee node. This value indicates which output is the primary output stream. The pipeline waits for a request from the primary output before processing requests from the other outputs.

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

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




