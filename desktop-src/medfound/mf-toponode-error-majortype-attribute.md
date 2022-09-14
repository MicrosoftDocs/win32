---
description: Contains the major media type for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found.
ms.assetid: eb837fe6-12c9-479c-a0be-63b24093e6fd
title: MF_TOPONODE_ERROR_MAJORTYPE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_ERROR\_MAJORTYPE attribute

Contains the major media type for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found.

## Data type

**GUID**

## Remarks

This attribute applies to all node types.

The topology loader might set the attribute. Applications typically read this attribute but do not set it.

For a list of possible values, see [Major Media Types](media-type-guids.md).

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

[**IMFAttributes::GetGUID**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getguid)
</dt> <dt>

[**IMFAttributes::SetGUID**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setguid)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




