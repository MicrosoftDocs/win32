---
description: Specifies whether the pipeline can drop samples from a topology node.
ms.assetid: 8be20446-4876-4d6f-b0db-2eb1ffaef9aa
title: MF_TOPONODE_DISCARDABLE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_DISCARDABLE attribute

Specifies whether the pipeline can drop samples from a topology node.

## Data type

Byte array

## Remarks

This attribute applies to all node types. Typically you would set this attribute on tee nodes, to indicate that the secondary outputs are not essential.

The value of the attribute is an array of indexes to output streams on the node.

If this attribute is set, the pipeline might drop samples from the specified output streams, if the stream is falling behind.

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

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




