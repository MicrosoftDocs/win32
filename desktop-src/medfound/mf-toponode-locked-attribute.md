---
Description: 'Specifies whether the media types can be changed on this topology node.'
ms.assetid: '8805ed63-1408-40bc-bb82-f3c51576dfa4'
title: 'MF\_TOPONODE\_LOCKED attribute'
---

# MF\_TOPONODE\_LOCKED attribute

Specifies whether the media types can be changed on this topology node.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to all node types.

If value of this attribute is nonzero, the topology loader will not change the media types. This attribute is set to **TRUE** when the node is in use.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFTopologyNode**](imftopologynode.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




